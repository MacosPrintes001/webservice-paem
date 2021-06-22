from collections import namedtuple
from .http_status_code import BAD_REQUEST, UNAUTHORIZED_REQUEST
from ..controller import UsuarioController

from flask_restful import request, current_app
from functools import wraps
from datetime import datetime, timedelta
from jwt import encode, decode

class Authorization():

    @classmethod
    def token_required(cls, f):
        '''
        Decorator to lock rote and 
        just allow acces when send the valid token 
        as header like '{Authorization:Bearer Token}'.

        '''
        @wraps(f)
        def decorator(*args, **kwargs):
            
            isActive = False
            
            if isActive:
                Bearer_token = None
                
                auth_key = 'Authorization'
                if auth_key in request.headers:
                    Bearer_token = request.headers[auth_key]

                if not Bearer_token:
                    return {'message':'acesso não autorizado.'}, UNAUTHORIZED_REQUEST

                if not ("Bearer" in Bearer_token):
                    return {'message':'Token invalido'}, BAD_REQUEST

                try:

                    token = Bearer_token.split()[1]
            
                    data = decode(token, key=current_app.secret_key, algorithms='HS256')

                    id_usuario = data['id']
                    # current_user = UsuarioModel.find_by_id(id_usuario) IF NEED CURRENT USER

                except:
                    return {'message':'token invalido'}, BAD_REQUEST        
            
            return f(*args, **kwargs)
        
        return decorator
        
    @classmethod
    def get_token(cls, login):
        
        payload = {
            "login": login,
            "exp": datetime.utcnow()+timedelta(minutes=60)
        }

        token = encode(payload, current_app.secret_key, algorithm='HS256')

        return {'token':token}

    @classmethod
    def verify_user(cls, login_email, senha):

        if not (login_email and senha):
            return False
        
        usuario = UsuarioController.get_by_email(login_email)
        print("usuario email:", usuario)
        
        if not usuario:
            usuario = UsuarioController.get_by_login(login_email)
            print("usuario login:", usuario)

        if not usuario: 
            return False

        if not usuario.verify_password(senha):
            return False
        
        return True
    
    
    @classmethod
    def cpf_required(cls, f):
        '''
        Decorator to lock rote and 
        just allow acces when send the valid token 
        as header like '{Authorization:Bearer Token}'.

        '''
        @wraps(f)
        def decorator(*args, **kwargs):
                   
            auth_key = 'Authorization'
            if auth_key in request.headers:
                cpf_header = request.headers[auth_key]

            else:
                return {'message':'acesso não autorizado.'}, UNAUTHORIZED_REQUEST

            if not ("CPF" in cpf_header):
                return {'message':'CPF invalido'}, BAD_REQUEST
            
            cpf = cpf_header.split()[1]
            usuario = UsuarioController.get_by_cpf(cpf)
            
            if not usuario:
                return {'message':'Não existe usuário com este CPF'}, BAD_REQUEST
                
            return f(usuario=usuario, *args, **kwargs)
    
        return decorator