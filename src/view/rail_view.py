from flask import request,json,Response,Blueprint
from ..controller.rail_controller import RailController
import logging 

logger=logging.getLogger(__name__+".rail_view")
rail_api=Blueprint('rail',__name__)

@rail_api.route('/getall',methods=['GET'])
def get_all():
    return RailController.get_all()


@rail_api.route('/search',methods=['GET'])
def get_search_result():
    search_name=request.args.get('station')
    return RailController.get_all_by_station_name_pattern(search_name)


@rail_api.route('/distance',methods=['GET'])
def get_distance_between_station():
    
    from_station_code=request.args.get('from')
    to_station_code=request.args.get('to')

    return RailController.get_distance(from_station_code,to_station_code)
