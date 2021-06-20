from ..controller import CursoController

from flask_restful import Resource, reqparse, request

class CursoResource(Resource):
    
    ENDPOINT = "curso"
    ROUTE =  "/cursos/curso"

    def get(self):
        
        parser = reqparse.RequestParser(bundle_errors=True)
        parser.add_argument("id_curso", required=True, type=int, help="query string id_curso não encontrado na requisição.")
        args = parser.parse_args(strict=True)
        id_curso = args.get("id_curso")

        return CursoController.get(id_curso)

    def post(self):
        body = request.json
        return CursoController.post(body)
    
    def put(self):
        body = request.json
        return CursoController.put(body)

    def delete(self):
        
        parser = reqparse.RequestParser(bundle_errors=True)
        parser.add_argument("id_curso", required=True, type=int, help="query string id_curso não encontrado na requisição.")
        args = parser.parse_args(strict=True)
        id_curso = args.get("id_curso")

        return CursoController.delete(id_curso)

class ListaCursoResource(Resource):
    
    ENDPOINT = "cursos"
    ROUTE = "/cursos"

    def get(self):
        return CursoController.get_all_names()

