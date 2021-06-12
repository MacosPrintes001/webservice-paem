from ..controller import DiscenteController

from flask_restful import Resource, reqparse, request
class DiscenteResource(Resource):
    
    ENDPOINT = 'discente'
    ROUTE = '/discentes/discente'
    
    # @token_required
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

        return {"massage":"Required query string matricula or id_discente."}

    # @token_required
    def post(self):
        body = request.json
        return DiscenteController.post(body)
      
    # @token_required
    def put(self):
        body = request.json
        return DiscenteController.put(body)

    # @token_required
    def delete(self):

        parser = reqparse.RequestParser()
        parser.add_argument("id_discente", type=int, required=True, help="Not found query string id_discente")

        args = parser.parse_args(strict=True)
        id_discente = args.get("id_discente")

        return DiscenteController.delete(id_discente)


class ListaDiscenteResource(Resource):
      
      ENDPOINT = 'discentes'
      ROUTE = '/discentes'

      # @token_required
      def get(self):
          return DiscenteController.list()