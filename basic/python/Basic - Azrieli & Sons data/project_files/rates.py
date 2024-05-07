import pandas as pd

class Rates():

    def __init__(self, taarif_file):
        self.taarif_file = taarif_file
        self.df = pd.DataFrame(taarif_file)
        self.basic_fare = "basic_fare"
        self.weekend_bonus = "weekend_bonus"
        self.customer = "customer"


    def get_basic_fare(customer):
        return self.df[df[self.customer]][self.basic_fare]

    def preprocess_taarif(taarif_df: pd.DataFrame, copy=False) -> pd.DataFrame:
        df = drivers
        if copy:
            df = new_drivers.copy()

        return df
