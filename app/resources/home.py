from flask_restful import Resource

class HomeResource(Resource):

    ENDPOINT = 'home'
    ROUTE = '/'

    # @token_required
    def get(self):
        return {"home": "Home Pege of PAEM Webservice"}