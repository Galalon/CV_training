import pandas as pd

class Trip():

    def __init__(self, customer, driver_id, start_time, end_time, trip_km):
        self.customer = customer
        self.driver_id = driver_id
        self.start_time = start_time
        self.end_time = end_time
        self.trip_km = trip_km