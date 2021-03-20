from marshmallow import fields, Schema 

class RailModel:
    # City,Zone,Division,Connection,Interchange,Station,Station Code,Distance in Kms,Layout,Parking Contract Available,Space Avaiable No Contract,Sapce Not Avaiable

    def __init__(self,data):
        temp_dataframe=data
        self.city=temp_dataframe["City"]
        self.zone=temp_dataframe["Zone"]
        self.division=temp_dataframe["Division"]
        self.connection=temp_dataframe["Connection"]
        self.interchange_list=temp_dataframe["Interchange"].split("; ")
        self.station_name=temp_dataframe["Station"]
        self.station_code=temp_dataframe["Station Code"]
        self.distance_in_kms=temp_dataframe["Distance in Kms"]
        self.layout=temp_dataframe["Layout"]
        self.parking_contract_available=temp_dataframe["Parking Contract Available"]
        self.space_available_no_contract=temp_dataframe["Space Avaiable No Contract"]
        self.sapce_not_avaiable=temp_dataframe["Sapce Not Avaiable"]
    

class RailSchema(Schema):
    city=fields.Str(required=True)
    zone=fields.Integer(required=True)
    division=fields.Integer(required=True)
    connection=fields.Str(required=True)
    interchange_list = fields.List(fields.Str(),required=True)
    station_name=fields.Str(required=True)
    station_code=fields.Str(required=True)
    distance_in_kms=fields.Float(required=True)
    layout=fields.Str(required=True)
    parking_contract_available=fields.Str(required=True)
    sapce_not_avaiable=fields.Str(required=True)
    space_available_no_contract=fields.Str(required=True)