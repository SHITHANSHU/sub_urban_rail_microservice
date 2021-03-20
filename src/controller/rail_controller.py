from flask import request,json,Response,Blueprint
from ..model.rail_model import RailModel,RailSchema
from ..utils.data_reader import DataReader
from ..utils.shared_response import SharedResponse
import traceback
import logging

logger=logging.getLogger(__name__+".rail_controller")
data_reader=DataReader()
rail_schema=RailSchema()
class RailController:

    def get_all():

        try:
            rail_data_frame=data_reader.get_all()
            rail_list=[]
            size=rail_data_frame.shape[0]

            for i in range(0,size):
                rail_model=RailModel(rail_data_frame.iloc[i])
                rail_list.append(rail_model)
            
            serialize_rail_model=rail_schema.dump(rail_list,many=True)
            

            return SharedResponse.success_response(serialize_rail_model)
        
        except Exception as err:
            logger.error(err)
            traceback.print_exc()
            return SharedResponse.server_error_response()
        

    
    def get_all_by_station_name_pattern(station_name):

        try:
            if station_name is None :
                return SharedResponse.validation_error_response()
            rail_data_frame=data_reader.get_all_by_station_name_pattern(station_name)
            rail_list=[]
            size=rail_data_frame.shape[0]
            for i in range(0,size):
                rail_model=RailModel(rail_data_frame.iloc[i])
                rail_list.append(rail_model)
            
            serialize_rail_model=rail_schema.dump(rail_list,many=True)
            

            return SharedResponse.success_response(serialize_rail_model)

        except Exception as err:
            logger.error(err)
            traceback.print_exc()
            return SharedResponse.server_error_response()

    def get_distance(from_station_code,to_station_code):

        try:
            
            if from_station_code is None or to_station_code is None:
                return SharedResponse.validation_error_response()

            from_rail_data_frame=data_reader.get_by_station_code(from_station_code)
            to_rail_data_frame=data_reader.get_by_station_code(to_station_code)

            from_rail_data_frame_size=from_rail_data_frame.shape[0]
            to_rail_data_frame_size=to_rail_data_frame.shape[0]

            if from_rail_data_frame_size==0 or to_rail_data_frame_size==0 :
                return SharedResponse.id_not_found_error_response()
            
            response_message_list=[]
            for i in range(from_rail_data_frame_size):
                for j in range(to_rail_data_frame_size):
                    if from_rail_data_frame.iloc[i]['Connection']==to_rail_data_frame.iloc[j]['Connection']:
                        distance=abs(from_rail_data_frame.iloc[i]['Distance in Kms']-to_rail_data_frame.iloc[j]['Distance in Kms'])
                        response_message={"from":from_station_code,"to":to_station_code,"Distance in Kms":round(distance,2),"Connection":to_rail_data_frame.iloc[j]['Connection']}
                        response_message_list.append(response_message)
            

            if len(response_message_list)==0:
                return SharedResponse.common_line_not_found_error_response()
            
            return SharedResponse.success_response(response_message)
            

        except Exception as err:
            logger.error(err)
            traceback.print_exc()
            return SharedResponse.server_error_response()
        
