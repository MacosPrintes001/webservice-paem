from ..controller import UsuarioController
from ..util.http_status_code import BAD_REQUEST, FORBIDDEN_REQUEST, NOT_FOUND_REQUEST, OK
from ..controller import UsuarioController

from flask_restful import Resource, reqparse, request


class UsuarioResource(Resource):
    ENDPOINT = 'usuario'
    ROUTE = '/usuarios/usuario'

    # @token_required
    def get(self):

        parser = reqparse.RequestParser()
        parser.add_argument('id_usuario', type=str, required=True, help="You need to send query string id_usuario.")

        args = parser.parse_args(strict=True)
        id_usuario = args.get('id_usuario')
        
        return UsuarioController.get(id_usuario)

    # @token_required
    def post(self):
        body = request.json
        return UsuarioController.post(body)
      
    # @token_required
    def put(self):
        body = request.json
        return UsuarioController.put(body)

    # @token_required
    def delete(self):

        parser = reqparse.RequestParser()
        parser.add_argument('id_usuario', type=str, required=True, help="You need to send query string id_usuario.")

        args = parser.parse_args(strict=True)
        id_usuario = args.get('id_usuario')

        return UsuarioController.delete(id_usuario)

class ListaUsuarioResource(Resource):

    ENDPOINT = 'users'
    ROUTE = '/usuarios'

    # @token_required
    def get(self):
        return UsuarioController.get_list()