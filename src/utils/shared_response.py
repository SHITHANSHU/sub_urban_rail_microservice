from flask import request,json,Response
class SharedResponse:
    
    def custom_response(response,status_code):
        return Response(
            mimetype="application/json",
            response=json.dumps(response),
            status=status_code
        )
    
    def validation_error_response():
        return SharedResponse.custom_response({"error":"Validation error Invalid input parameter"},400)

    def id_not_found_error_response():
        return SharedResponse.custom_response({'error':'Station code not found'},404)
    
    def data_not_found_error_response():
        return SharedResponse.custom_response({'error':'No data found'},401)
    
    def common_line_not_found_error_response():
        return SharedResponse.custom_response({'error':'No common line found between stations'},402)

    def server_error_response():
        return SharedResponse.custom_response({'error':'Server Error check logs'},500)
        
    def success_response(response_data):
        return SharedResponse.custom_response(response_data,200)