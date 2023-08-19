import os

import kaggle
import numpy as np
import pandas as pd
from sklearn.preprocessing import OrdinalEncoder, OneHotEncoder


class DataHandler:
    data_filenames = []  # Instantiate File Names
    f1_data_dict = {}  # Instantiate Dictionary to hold F1 data frames
    df = pd.DataFrame()  # Actual dataframe used for model

    def __init__(self):
        # Set the dataset slug (the last part of the dataset URL)
        dataset_slug = "rohanrao/formula-1-world-championship-1950-2020"

        # Set the destination directory to save the files
        destination_dir = "csv_files"

        # Create the destination directory if it doesn't exist
        os.makedirs(destination_dir, exist_ok=True)

        # Download the dataset using the Kaggle API
        kaggle.api.authenticate()
        kaggle.api.dataset_download_files(dataset_slug, path=destination_dir, unzip=True)

        for dirname, _, filenames in os.walk('csv_files'):
            for filename in filenames:
                self.data_filenames.append((os.path.join(dirname, filename)))

    def load_data(self):
        for file_name in self.data_filenames:
            data_frame = pd.read_csv(file_name)
            base = os.path.basename(file_name)
            strip_ext = os.path.splitext(base)[0]
            self.f1_data_dict.update({strip_ext: data_frame})
            # print(f"Loaded DataFrame for {strip_ext}")

    def get_avg_lap_time(self):
        lap_times_df = self.f1_data_dict['lap_times']
        grouped = lap_times_df.groupby(['raceId', 'driverId']).agg(
            {'milliseconds': 'sum', 'lap': 'count'}).reset_index()

        # Calculate the average lap time in milliseconds
        grouped['avg_lap_time'] = grouped['milliseconds'] / grouped['lap']

        # Select the desired columns
        avg_lap_time_df = grouped[['raceId', 'driverId', 'avg_lap_time']]
        avg_lap_time_df.loc[:, 'avg_lap_time'] = avg_lap_time_df['avg_lap_time'].round(3)

        self.f1_data_dict.update({"avg_lap_times": avg_lap_time_df})

    def get_total_pit_stops(self):
        pit_info_df = self.f1_data_dict['pit_stops']
        pit_stops_df = pit_info_df.groupby(['raceId', 'driverId']).size().reset_index(name='num_pit_stops')

        self.f1_data_dict.update({"pit_stop_freq": pit_stops_df})

    def relevant_data(self, min_year, max_year):
        f1_data = self.f1_data_dict
        race_ids = f1_data['races'][(f1_data['races']['year'] >= min_year) & (f1_data['races']['year'] <= max_year)][
            'raceId']

        f1_data['circuits'] = f1_data['circuits'][f1_data['circuits']['circuitId'].isin(race_ids)]
        f1_data['constructor_results'] = f1_data['constructor_results'][
            f1_data['constructor_results']['raceId'].isin(race_ids)]
        f1_data['constructor_standings'] = f1_data['constructor_standings'][
            f1_data['constructor_standings']['raceId'].isin(race_ids)]
        #f1_data['lap_times'] = f1_data['lap_times'][f1_data['lap_times']['raceId'].isin(race_ids)]
        f1_data['avg_lap_times'] = f1_data['avg_lap_times'][f1_data['avg_lap_times']['raceId'].isin(race_ids)]
        f1_data['pit_stop_freq'] = f1_data['pit_stop_freq'][f1_data['pit_stop_freq']['raceId'].isin(race_ids)]
        f1_data['qualifying'] = f1_data['qualifying'][f1_data['qualifying']['raceId'].isin(race_ids)]
        f1_data['results'] = f1_data['results'][f1_data['results']['raceId'].isin(race_ids)]
        #f1_data['sprint_results'] = f1_data['sprint_results'][f1_data['sprint_results']['raceId'].isin(race_ids)]

    def merge_data(self):
        f1_data = self.f1_data_dict
        self.df = pd.merge(f1_data['results'], f1_data['races'][['raceId', 'year', 'name', 'round', 'circuitId']],
                           on='raceId',
                           how='left')
        self.df = pd.merge(self.df, f1_data['drivers'][['driverId', 'surname', 'nationality']], on='driverId',
                           how='left')
        self.df = pd.merge(self.df, f1_data['qualifying'][['raceId', 'driverId', 'position']],
                           on=['raceId', 'driverId'], how='left')
        self.df = pd.merge(self.df, f1_data['constructors'][['constructorId', 'name', 'nationality']],
                           on='constructorId',
                           how='left')
        self.df = pd.merge(self.df, f1_data['constructor_standings'][['raceId', 'constructorId', 'points']],
                           on=['raceId', 'constructorId'], how='left')
        self.df = pd.merge(self.df,
                           f1_data['pit_stop_freq'][['raceId', 'driverId', 'num_pit_stops']],
                           on=['raceId', 'driverId'], how='left')
        self.df = pd.merge(self.df, f1_data['status'][['statusId', 'status']], on='statusId', how='left')
        self.df = pd.merge(self.df, f1_data['avg_lap_times'][['raceId', 'driverId', 'avg_lap_time']],
                           on=['raceId', 'driverId'], how='left')

    def manual_cleanup(self):
        # Rename Columns
        self.df = self.df.rename(
            columns={'number': 'driver_number', 'grid': 'grid_start_pos', 'positionOrder': 'driver_pos',
                     'points_x': 'driver_points', 'time': 'finish_time', 'fastestLap': 'fastest_lap',
                     'rank': 'fast_lap_rank', 'fastestLapTime': 'fastest_lap_time',
                     'fastestLapSpeed': 'fastest_lap_speed',
                     'name_x': 'grand_prix', 'surname': 'driver_name', 'nationality_x': 'driver_nationality',
                     'position_y': 'constructor_position',
                     'name_y': 'constructor_name', 'nationality_y': 'constructor_nationality',
                     'points_y': 'constructor_points', 'milliseconds_x': 'completion_time_milli',
                     })
        # Drop Columns
        self.df = self.df.drop(
            ['positionText', 'position_x', 'finish_time', 'driver_number', 'resultId', 'grand_prix',
             'driver_name', 'driver_nationality', 'constructor_name', 'constructor_nationality', 'status',
             ], axis=1)
        # Add Missing Values
        self.df['constructor_points'].fillna(0, inplace=True)
        self.df.fillna("NaN", inplace=True)
        self.df['fastest_lap_time'] = self.df['fastest_lap_time'].apply(self.convert_time_milli)

    def manual_cleanup_categorical(self):
        # Rename Columns
        self.df = self.df.rename(
            columns={'number': 'driver_number', 'grid': 'grid_start_pos', 'positionOrder': 'driver_pos',
                     'points_x': 'driver_points', 'time': 'finish_time', 'fastestLap': 'fastest_lap',
                     'rank': 'fast_lap_rank', 'fastestLapTime': 'fastest_lap_time',
                     'fastestLapSpeed': 'fastest_lap_speed',
                     'name_x': 'grand_prix', 'surname': 'driver_name', 'nationality_x': 'driver_nationality',
                     'position_y': 'constructor_position',
                     'name_y': 'constructor_name', 'nationality_y': 'constructor_nationality',
                     'points_y': 'constructor_points', 'milliseconds_x': 'completion_time_milli',
                     })
        # Drop Columns
        self.df = self.df.drop(
            ['positionText', 'position_x', 'finish_time', 'resultId',
             'driver_nationality', 'constructor_nationality', 'status',
             ], axis=1)
        # Handle Categorical Missing Values
        self.df.fillna("NaN", inplace=True)
        # Na Value Cleanup
        for column in self.df:
            self.df[column] = [
                np.nan if value == r'\N' or value == 'NaN' or value == r'\\N' or pd.isna(value) else value for value in
                self.df[column].values]

    @staticmethod
    def convert_time_milli(time_string):
        if time_string != r"\N":
            minutes, seconds = time_string.split(':')
            seconds, milliseconds = seconds.split('.')
            milli = (int(minutes) * 60000) + (int(seconds) * 1000) + int(milliseconds)
            return milli

    # def export_data(self):
    #     scope = ['https://spreadsheets.google.com/feeds', 'https://www.googleapis.com/auth/drive']
    #     credentials = SAC.from_json_keyfile_name('credentials.json', scope)
    #     client = gspread.authorize(credentials)
    #     sheet = client.open('F1 Data V2').sheet1
    #     self.df = self.df.fillna('')
    #     # Get the column names as a list
    #     column_names = self.df.columns.tolist()
    #
    #     data = self.df.values.tolist()
    #     sheet.clear()
    #     sheet.insert_row(column_names, index=1)
    #     sheet.insert_rows(data, row=2)

    def map_data(self):
        conditions = [
            self.df['driver_pos'].between(1, 3),
            self.df['driver_pos'].between(4, 10),
            self.df['driver_pos'].between(11, 1000)
        ]
        values = ['Podium Finish', 'Points Finish', 'No Points Finish']
        self.df['finish_domain'] = np.select(conditions, values, default=0)

        # Encode
        order = ['Podium Finish', 'Points Finish', 'No Points Finish']

        ordinal_encoder = OrdinalEncoder(categories=[order])
        self.df['finish_domain_encoded'] = ordinal_encoder.fit_transform(self.df[['finish_domain']])

        onehot_encoder = OneHotEncoder(sparse_output=False)
        encoded_features = onehot_encoder.fit_transform(self.df[['finish_domain_encoded']])
        encoded_df = pd.DataFrame(encoded_features, columns=['Podium Finish', 'Points Finish', 'No Points Finish'])

        df_encoded = pd.concat([self.df[['finish_domain_encoded']], encoded_df], axis=1)
        self.df = self.df.drop('finish_domain', axis=1)

        # Na Value Cleanup
        for column in self.df:
            self.df[column] = [
                np.nan if value == r'\N' or value == 'NaN' or value == r'\\N' or pd.isna(value) else value for value in
                self.df[column].values]

    def transform_numerical(self):
        for col in self.df.columns:
            self.df[col] = pd.to_numeric(self.df[col], errors='coerce')

    def get_dataframe(self):
        return self.df

    def export_csv(self, filename):
        self.df.to_csv(filename)

    def print_data(self):
        print(self.df)
