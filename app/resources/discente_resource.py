from ..controller import DiscenteController, UsuarioController
from ..util.authorization import Authorization

from flask_restful import Resource, reqparse, request
class DiscenteResource(Resource):
    
    ENDPOINT = 'discente'
    ROUTE = '/discentes/discente'
    
    @Authorization.token_required()
    def get(self):

        parser = reqparse.RequestParser()
        parser.add_argument('matricula', type=str, required=False, help="You need to send query string maticula.")
        parser.add_argument('id_discente', type=int, required=False, help="Query string id_discente must be integer.")

        args = parser.parse_args(strict=True)

        matricula = args.get('matricula')
        id_discente = args.get('id_discente')

        if matricula:
            return DiscenteController.get_by_matricula(matricula)

        elif id_discente:
            return DiscenteController.get(id_discente)

        return {"massage":" query string matricula or id_discente não encontrado."}

    @Authorization.token_required()
    def post(self):

        discente_body  = request.json.get("discente")
        usuario_body = request.json.get("usuario")
        usuario = UsuarioController.create_usuario(usuario_body)
        
        return DiscenteController.post(discente_body, usuario)
      
    @Authorization.token_required()
    def put(self):
        discente = request.json
        return DiscenteController.put(discente)

    @Authorization.token_required()
    def delete(self):

        parser = reqparse.RequestParser()
        parser.add_argument("id_discente", type=int, required=True, help="query string id_discente não encontrada")

        args = parser.parse_args(strict=True)
        id_discente = args.get("id_discente")

        return DiscenteController.delete(id_discente)


class ListaDiscenteResource(Resource):
      
      ENDPOINT = 'discentes'
      ROUTE = '/discentes'

      @Authorization.token_required()
      def get(self):
          return DiscenteController.get_all_names()