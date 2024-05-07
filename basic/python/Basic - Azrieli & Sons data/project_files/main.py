import pandas as pd
import numpy as np
import seaborn as sns
import datetime as datetime
import os
from constants import *
from trip_file import TripFile
from trip import Trip
from tqdm import tqdm





def preprocess_drivers(drivers: pd.DataFrame, copy=False) -> pd.DataFrame:
    df = drivers
    if copy:
        df = drivers.copy()

    gender_mapping = {"F": FEMALE,
                    "M":MALE,
                    "m":MALE,
                    "male":MALE,
                    "boy":MALE,
                    "unknown":MALE,
                    'woman':FEMALE,
                    'girl':FEMALE,
                    'none':MALE,
                    'female':FEMALE}

    # Make preprocess
    df.gender.fillna(MALE, inplace=True)
    df.gender = df.gender.apply(lambda x: gender_mapping[x])
    df.birthdate = pd.to_datetime(df.birthdate, format="mixed")
    drivers.birthdate.fillna(datetime.datetime.now(),inplace=True)

    return df

def preprocess_taarif(taarif_df: pd.DataFrame, copy=False) -> pd.DataFrame:
        df = taarif_df
        if copy:
            df = df.copy()

        return df


# Concat the two tables of drivers with and without kviut
def concat_drivers_tables(new_drivers, drivers_with_kviut):
    drivers_with_kviut["kviut"] = 1
    drivers = pd.concat([new_drivers, drivers_with_kviut])
    drivers["kviut"].fillna(0, inplace=True)
    return drivers


def get_trip_files(folder, limit=100):
    files = np.array(list(os.listdir(folder)))
    if limit:
        files = files[:limit]
    files = np.array([name if not name[-5] == ")" else name[:-7]+".csv" for name in files])
    print("Processing files....")
    return np.array([TripFile(os.path.join(folder,file)) for file in tqdm(files)])
    


def calculate_trip_salary(taarif, drivers, customer, trip_km, trip_start, trip_end):
    info = ""
    
    basic_rate = taarif[taarif.customer == "blalbalbla"]["basic_taarif"]
    if basic_rate.empty:
        info = "Company not found"
        return -1
    
    if not trip_start or not trip_end:
        info = "possible weekend bonus\n"
    
    

def main():
    taarif = pd.read_csv("../files/taarif.csv")
    new_drivers = pd.read_csv("../files/new_drivers.csv", index_col=0)
    drivers_with_kviut = pd.read_csv("../files/drivers_with_kviut.csv",index_col=0)

    drivers = concat_drivers_tables(new_drivers, drivers_with_kviut)
    drivers = preprocess_drivers(drivers, copy=True)




if __name__ == "__main__":
    main()
    