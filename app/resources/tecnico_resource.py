from ..controller import TecnicoController
from flask_restful import Resource, reqparse, request

class TecnicoResource(Resource):
    
    ENDPOINT = 'tecnico'
    ROUTE = '/tecnicos/tecnico'

    def get(self):
        parser = reqparse.RequestParser()
        parser.add_argument('id_tecnico', type=int, required=True, help="Required query string id_tecnico.")

        args = parser.parse_args(strict=True)
        id_tecnico = args.get('id_tecnico')

        return TecnicoController.get(id_tecnico)
    
    def post(self):
        body = request.json
        return TecnicoController.post(body)
    
    def put(self):
        body = request.json
        return TecnicoController.put(body)
    
    def delete(self):
        
        parser = reqparse.RequestParser()
        parser.add_argument('id_tecnico', type=int, required=True, help="Required query string id_tecnico")
        
        args = parser.parse_args()
        id_tecnico = args.get('id_tecnico')

        return TecnicoController.delete(id_tecnico)

class ListaTecnicoResource(Resource):
    
    ENDPOINT = 'tenicos'
    ROUTE = '/tecnicos'
    
    def get(self):
        return TecnicoController.get_list()
