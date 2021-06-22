
from ..controller import DocenteController, UsuarioController
from ..util.authorization import Authorization

from flask_restful import Resource, reqparse, request
class DocenteResource(Resource):
    ENDPOINT = 'docente'
    ROUTE = '/docentes/docente'

    @Authorization.token_required()    
    def get(self):
        parse = reqparse.RequestParser()
        parse.add_argument("id_docente", required=True, type=int, help="Query string id_discente must be integer")
        args = parse.parse_args(strict=True)
        id_docente = args.get("id_docente")
        
        return DocenteController.get(id_docente)
    
    @Authorization.token_required()
    def post(self):
        body = request.json
        docente_body = body.get("docente")
        usuario_body = body.get("usuario")
        usuario = UsuarioController.create_usuario(usuario_body)

        return DocenteController.post(docente_body, usuario=usuario)

    @Authorization.token_required()
    def put(self):
        body = request.json
        return DocenteController.put(body)
    
    @Authorization.token_required()
    def delete(self):
        parse = reqparse.RequestParser()
        parse.add_argument("id_docente", required=True, type=int, help="Query string id_discente must be integer")
        args = parse.parse_args(strict=True)
        id_docente = args.get("id_docente")

        return DocenteController.delete(id_docente)

class ListaDocenteResource(Resource):
    
    ENDPOINT = 'docentes'
    ROUTE = '/docentes'

    @Authorization.token_required()
    def get(self):
        return DocenteController.get_all_names()    
