import os
from dotenv import load_dotenv

def get_csv_file():
    load_dotenv()
    __location__ = os.path.realpath(os.path.join(os.getcwd(), os.path.dirname(__file__)))
    file_location=os.path.join(__location__, os.getenv('DATA_FILE'))
    return(file_location)