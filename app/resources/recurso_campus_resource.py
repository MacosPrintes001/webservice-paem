from flask_restful import Resource, reqparse, request
from ..controller import RecursoCampusController


class RecursoCampusResource(Resource):

    ENDPOINT = 'recurso_campus'
    ROUTE = '/recursos_campus/recurso_campus'

    def get(self):
      parser = reqparse.RequestParser()
      parser.add_argument('id_recurso_campus', type=int, required=True, help='Required query string id_recurso.')
      
      args = parser.parse_args()
      id_recurso_campus = args.get('id_recurso_campus')
      return RecursoCampusController.get(id_recurso_campus)

    def post(self):
        body = request.json
        return RecursoCampusController.post(body)
      
    def put(self):
      body = request.json
      return RecursoCampusController.put(body)

    def delete(self):
      parser = reqparse.RequestParser()
      parser.add_argument('id_recurso_campus', type=int, required=True, help='Required query string id_recurso_campus.')

      args = parser.parse_args()
      id_recurso_campus = args.get('id_recurso_campus')

      return RecursoCampusController.delete(id_recurso_campus)


class ListaRecursoCampusResource(Resource):

    ENDPOINT = 'recursos_campus'
    ROUTE = '/recursos_campus'

    def get(self):
        return RecursoCampusController.get_list()