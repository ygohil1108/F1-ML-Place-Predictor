import pymongo

from DataHandler import DataHandler

# Training Data / Web Predict Data Years
CURRENT_SEASON = 2022
MIN_YEAR_TRAIN = 2014
MAX_YEAR_TRAIN = CURRENT_SEASON - 1

# Data Handler Object for Model Training Purposes
train_test_dh = DataHandler()
train_test_dh.load_data()
train_test_dh.get_avg_lap_time()
train_test_dh.get_total_pit_stops()
train_test_dh.relevant_data(min_year=MIN_YEAR_TRAIN, max_year=MAX_YEAR_TRAIN)
train_test_dh.merge_data()
train_test_dh.manual_cleanup()
train_test_dh.map_data()
train_test_dh.transform_numerical()
train_test_dh.export_csv("train_test_f1_data")

# Data Handler Object for Current Season Prediction Purposes
current_season_dh = DataHandler()
current_season_dh.load_data()
current_season_dh.get_avg_lap_time()
current_season_dh.get_total_pit_stops()
current_season_dh.relevant_data(min_year=CURRENT_SEASON, max_year=CURRENT_SEASON)
current_season_dh.merge_data()
current_season_dh.manual_cleanup()
current_season_dh.map_data()
current_season_dh.transform_numerical()
current_season_dh.export_csv("current_season_f1_data")

# Categorical Dataset that will be used in backend
current_cat_dh = DataHandler()
current_cat_dh.load_data()
current_cat_dh.get_avg_lap_time()
current_cat_dh.get_total_pit_stops()
current_cat_dh.relevant_data(min_year=CURRENT_SEASON, max_year=CURRENT_SEASON)
current_cat_dh.merge_data()
current_cat_dh.manual_cleanup_categorical()

# Send to MongoDB Database
client = pymongo.MongoClient("mongodb://localhost:27017")
db = client["F1_ML_Data"]

train_test_data = train_test_dh.get_dataframe().to_dict(orient="records")
db.Train_Test.insert_many(train_test_data)

current_season_data = current_season_dh.get_dataframe().to_dict(orient="records")
db.Current_Season.insert_many(current_season_data)

current_cat_data = current_cat_dh.get_dataframe().to_dict(orient="records")
db.Current_Season_Categorical.insert_many(current_cat_data)

print("Success")
