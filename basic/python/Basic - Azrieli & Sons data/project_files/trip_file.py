import pandas as pd
import os


class TripFile():

    def __init__(self, trip_file_path):
        self.trip_file_path = trip_file_path
        self.trips_df = pd.read_csv(trip_file_path, index_col=0)
        self.file_name = os.path.basename(trip_file_path)
        self.month = self.file_name.split(' ')[0]
        self.year = self.file_name.split(' ')[1].split('_')[0]

        self.preprocess_trips_df(self.trips_df)

    def get_file_name(self):
        return self.file_name
    
    def preprocess_trips_df(self, trips_df):
        trips_df.start_time = pd.to_datetime(trips_df.start_time)
        trips_df.end_time = pd.to_datetime(trips_df.end_time)

    def get_data_frame(self):
        return self.trips_df

    def get_month(self):
        return self.month
    
    def get_year(self,):
        return self.year
