import pandas as pd 
from dotenv import load_dotenv
import os
from ..assets.asset import get_csv_file


class DataReader:
    


    def __init__(self):
        load_dotenv()
        __location__ = os.path.realpath(os.path.join(os.getcwd(), os.path.dirname(__file__)))
        self.file_name=os.path.join(__location__, os.getenv('DATA_FILE'))
        self.file_name= get_csv_file()
        self.data_frame=pd.read_csv(self.file_name)
        
    
    def get_all(self):
        return self.data_frame
    
    def get_all_by_station_name_pattern(self,name):
        return self.data_frame[self.data_frame['Station'].str.contains(name,case=False)]
    
    def get_by_station_code(self,station_code):
        return self.data_frame[self.data_frame['Station Code']==station_code]

