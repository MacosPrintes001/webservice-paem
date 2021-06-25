from ..controller import TecnicoController, UsuarioController
from ..util.authorization import Authorization

from flask_restful import Resource, reqparse, request

class TecnicoResource(Resource):
    
    ENDPOINT = 'tecnico'
    ROUTE = '/tecnicos/tecnico'

    @Authorization.token_required()
    def get(self):
        parser = reqparse.RequestParser()
        parser.add_argument('id_tecnico', type=int, required=True, help="Required query string id_tecnico.")

        args = parser.parse_args(strict=True)
        id_tecnico = args.get('id_tecnico')

        return TecnicoController.get(id_tecnico)
    
    # @Authorization.token_required()
    def post(self):

        tecnico_body = request.json.get("tecnico")
        usuario_body = request.json.get("usuario")
        usuario = UsuarioController.create_usuario(usuario_body)

        return TecnicoController.post(tecnico_body, usuario)

    @Authorization.token_required()
    def put(self):
        body = request.json
        return TecnicoController.put(body)

    @Authorization.token_required()
    def delete(self):
        
        parser = reqparse.RequestParser()
        parser.add_argument('id_tecnico', type=int, required=True, help="Required query string id_tecnico")
        
        args = parser.parse_args()
        id_tecnico = args.get('id_tecnico')

        return TecnicoController.delete(id_tecnico)


class ListaTecnicoResource(Resource):
    
    ENDPOINT = 'tenicos'
    ROUTE = '/tecnicos'
    
    @Authorization.token_required()
    def get(self):
        return TecnicoController.get_all_names()
