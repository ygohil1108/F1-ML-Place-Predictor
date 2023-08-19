import pymongo
from gridfs import GridFS


def main():
    # Load the Joblib files
    rf_ADASYN_path = 'models/rf_model_ADASYN.joblib'
    rf_SMOTE_path = 'models/rf_model_SMOTE.joblib'
    rf_BSMOTE_path = 'models/rf_model_BSMOTE.joblib'
    rf_SVM_path = 'models/rf_model_SVM.joblib'

    with open(rf_ADASYN_path, 'rb') as rf_ADASYN_file:
        rf_ADASYN_data = rf_ADASYN_file.read()

    with open(rf_SMOTE_path, 'rb') as rf_SMOTE_file:
        rf_SMOTE_data = rf_SMOTE_file.read()

    with open(rf_BSMOTE_path, 'rb') as rf_BSMOTE_file:
        rf_BSMOTE_data = rf_BSMOTE_file.read()

    with open(rf_SVM_path, 'rb') as rf_SVM_file:
        rf_SVM_data = rf_SVM_file.read()

    # Connect to MongoDB
    client = pymongo.MongoClient("mongodb://localhost:27017")
    db = client["F1_ML_Data"]
    fs = GridFS(db, collection='ML-Models')

    # Store the Joblib data using GridFS
    rf_ADASYN_id = fs.put(rf_ADASYN_data, filename='model_ADASYN.joblib')
    rf_SMOTE_id = fs.put(rf_SMOTE_data, filename='model_SMOTE.joblib')
    rf_BSMOTE_id = fs.put(rf_BSMOTE_data, filename='model_BSMOTE.joblib')
    rf_SVM_id = fs.put(rf_SVM_data, filename='model_SVM.joblib')

    print("Joblib data uploaded to MongoDB using GridFS.")


if __name__ == "__main__":
    main()

