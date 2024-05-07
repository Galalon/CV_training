import pandas as pd


class Drivers()

    def __init__(self, new_drivers, drivers_with_kviut):
        self.drivers_with_kviut = pd.read_csv(drivers_with_kviut)
        self.new_drivers = pd.read_csv(new_drivers)
        