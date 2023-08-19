import pandas as pd
from flask import Flask, request, jsonify, render_template
from io import BytesIO
import sklearn
from sklearn.impute import KNNImputer
import joblib
from gridfs import GridFS
from pymongo import MongoClient

app = Flask(__name__)

# Connect to MongoDB
client = MongoClient("{Your-LocalHost-Server}")
db = client["F1_ML_Data"]
collection_cat = db["Current_Season_Categorical"]
collection_num = db['Current_Season']
fs = GridFS(db, collection='ML-Models')

cursor_cat = collection_cat.find()
cursor_num = collection_num.find()

# Transform documents into a list of dictionaries
documents_cat = [doc for doc in cursor_cat]
documents_num = [doc for doc in cursor_num]

# DataFrame with categorical Data to match with user inputs
cat_df = pd.DataFrame(documents_cat).drop(columns='_id')
num_df = pd.DataFrame(documents_num).drop(columns='_id')

search_df = cat_df[['year', 'driver_name', 'driverId', 'grand_prix', 'raceId']]


def load_model_from_gridfs(db, fs, model_name):
    model_doc = db['ML-Models.files'].find_one({'filename': f'{model_name}.joblib'})

    if model_doc:
        # Retrieve the chunks associated with the model
        chunks = db['ML-Models.chunks'].find({'files_id': model_doc['_id']}).sort('n')

        # Read and concatenate the chunks to reconstruct the binary data
        model_binary = b''.join(chunk['data'] for chunk in chunks)

        # Load the model from the binary data using BytesIO
        with BytesIO(model_binary) as model_stream:
            loaded_model = joblib.load(model_stream)
        return loaded_model
    else:
        return None


@app.route('/')
def index():
    return render_template('index.html')


@app.route('/results')
def results():
    return render_template('results.html')


@app.route('/api/data', methods=['GET'])
def get_data():
    grand_prix_data = search_df['grand_prix'].unique().tolist()
    driver_data = search_df['driver_name'].unique().tolist()
    return jsonify({"drivers": driver_data, "grandPrix": grand_prix_data})


@app.route('/api/predict', methods=['POST'])
def predict():
    data = request.json
    grand_prix_query = data.get('grand_prix')
    driver_name_query = data.get('driver_name')

    X_df = num_df.drop(columns=['driver_pos', 'driver_points', 'milliseconds', 'constructor_position',
                                'constructor_points', 'finish_domain_encoded'])

    filtered_data = cat_df[(cat_df['driver_name'] == driver_name_query) & (cat_df['grand_prix'] == grand_prix_query)]

    # Extract driverId and raceId
    result = filtered_data[['driverId', 'raceId']]

    X = X_df.merge(result, on=['raceId', 'driverId'])

    imputer = KNNImputer(n_neighbors=5)

    if X.isna().any().any():
        X_imputed = imputer.fit_transform(X)
        X = pd.DataFrame(X_imputed, columns=X.columns)

    # Load in Model
    model = load_model_from_gridfs(db, fs, 'model_ADASYN')

    output = model.predict(X)

    if output == 0:
        output = "Podium"
    elif output == 1:
        output = "Points"
    else:
        output = "No Points"

    # Create the prediction dictionary
    prediction = {
        "race_year": grand_prix_query,
        "driver_name": driver_name_query,
        "status": output
    }

    return jsonify(prediction)


if __name__ == '__main__':
    app.run(debug=True)
