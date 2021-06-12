from ..util.http_status_code import OK, CREATED, BAD_REQUEST, NOT_FOUND_REQUEST


class BaseController:
    
    @classmethod
    def get_by_id(cls, id, Model):

        model = Model.find_by_id(id)
        if not model:
            return {"message":"Not found this resource."}, NOT_FOUND_REQUEST
      
        return model.serialize(), OK
    
    @classmethod
    def post(cls, body, Model):

        if not body:
            return {"message":"Not found body data ."}, BAD_REQUEST
        
        print(body)
        new_model = Model(**body)
        new_model.save_to_db()

        return new_model.serialize(), CREATED

    @classmethod
    def put(cls, body, Model):

        if not body:
            return {"message":"Not found body data"}, BAD_REQUEST
        
        id_key = list(filter(lambda k:'id_' in k, body.keys()))[0]
        id = body.get(id_key)

        model = Model.find_by_id(id)
        if not model:
            return {"message":"It do not found this resource."}, BAD_REQUEST

        Model.update_by_id(id, body)
        
        return {"message":"Updated"}, OK

    @classmethod
    def delete(cls, id, Model):
        
        model = Model.find_by_id(id)
        
        if not model:
            return {"message":"Can't delete, not found this discente."}, BAD_REQUEST
        
        model.delete_from_db()

        return {"message":" Deleted"}, OK

    @classmethod
    def get_list(cls, Model):
        models = Model.query_all()
        return [model.serialize() for model in models]