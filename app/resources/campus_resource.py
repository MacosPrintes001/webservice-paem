from ..controller import CampusController
from ..util.authorization import Authorization

from flask_restful import reqparse, request, Resource


class CampusResource(Resource):
    ENDPOINT = 'campi'
    ROUTE = '/campus/campi'

    @Authorization.token_required()
    def get(self):

        parser = reqparse.RequestParser()
        parser.add_argument('id_campus', type=str, required=True, help="You need to send query string id_campus.")

        args = parser.parse_args(strict=True)
        id_campus = args.get('id_campus')
        
        return CampusController.get(id_campus)

    @Authorization.token_required()
    def post(self):
        body = request.json
        return CampusController.post(body)
      
    @Authorization.token_required()
    def put(self):
        body = request.json
        return CampusController.put(body)

    @Authorization.token_required()
    def delete(self):

        parser = reqparse.RequestParser()
        parser.add_argument('id_campus', type=str, required=True, help="You need to send query string id_campus.")

        args = parser.parse_args(strict=True)
        id_campus = args.get('id_campus')

        return CampusController.delete(id_campus)

class ListaCampusResource(Resource):
    
    ENDPOINT = 'campus'
    ROUTE = '/campus'
    
    @Authorization.token_required()
    def get(self):
        return CampusController.get_all_names()
