from datetime import datetime
import requests
import telebot
from telebot.apihelper import send_message
import dados_bot
import conexao_bot as conect

token = dados_bot.btoken

bot = telebot.TeleBot(token, threaded=True)


class Alunos():
    def __init__(self):
        self.para_si = None #para solicitação
        self.data = None #para solicitação
        self.hora_inicio = None #para solicitação
        self.hora_fim = None #para solicitação
        self.nome = None #para solicitação
        self.telefone = None #para solicitação

        self.campus = None
        self.cpf = None #criar token e achar id usuario
        self.matricula= None #usado para achar nome e id aluno
        self.recurso = None #para solicitação
        self.id_discente = None #para solicitação
        self.id_usuario = None #para solicitação
        self.id_recurso = None
        
        

aluno = Alunos()

@bot.message_handler(commands=['start'])
def inicio(message):
    chat_id = message.chat.id
    bot.reply_to(message, "Olá, sou o Bot de agendamento da UFOPA, para fazer uma socitação de acesso,"
                          " basta enviar os seguintes dados NA ORDEM PEDIDA:\n\n"
                          "A solicitação de agendamento é para você?\n"
                          "CPF\n"
                          "Nº da Matricula\n"
                          "data que quer agendar\n"
                          "Horario requerido\n"
                          "Local desejado\n"
                          "Nº do seu telefone")
    #pegar campus

    e = bot.send_message(chat_id, "Ex:\nSim\n03051107032\n2019004525\n24/08/2022\n08:00 as 10:00\nBiblioteca\n"
                                  "(93)992991452560")

    bot.register_next_step_handler(e, check_dados)


def check_dados(message):
    chat_id = message.chat.id
    mensagem = str(message.text)
    bot.send_message(chat_id, "Certo, aguarde um momento enquanto eu confiro os dados...")

    try:
        para_si, cpf, matricula, data, hora, recurso, telefone = mensagem.split('\n')

        if para_si is not None and cpf is not None and matricula is not None and \
            data is not None and hora is not None and telefone is not None and recurso is not None: #saber se não há dados vazios
            
            data =str(data)
            para_si = str(para_si)
            cpf = str(cpf) 
            matricula = str(matricula) 
            hora = str(hora) 
            recurso = str(recurso) 
            telefone = str(telefone)

            data_verific = data_valida(data, chat_id) #verificação data valida
            if data_verific:
                try:
                    resp, nome, id_discente, campus, id_recurso, id_usuario, token = conect.login(cpf, matricula, recurso)

                    if resp:
                        prepara_agendar(para_si, campus, cpf, matricula, data, hora, recurso,\
                                telefone,nome, id_discente, id_usuario,id_recurso, token, chat_id)
                        
                    else:
                        bot.send_message(chat_id, "Houve algum erro no servidor, verifique se você enviou o cpf ou matricula certos pois eu preciso que você envie tudo corretamente, igual ao "
                                                    "indicado, Digite SIM para tentar novamente, ou NÂO para encerrar o acesso.")
                except Exception:
                    bot.send_message(chat_id, "Houve um erro no servidor digite /start e tente novamente")
            else:
                bot,send_message(chat_id, "Parece que a data que você passou não é valida, tente "
                                          "novamente com uma data valida. Basta clicar em /start para tentar de novo")
        
        else:
            bot.send_message(chat_id, "Olha parece que faltaram alguns dados, envie /start e tente de novo")

    except Exception:
        print("ERRO")
        bot.send_message(chat_id, "Houve algum erro, eu preciso que você envie todos os dados corretamente, igual ao "
                                      "indicado, digite /start e envie os dados novamente")



def prepara_agendar(para_si, campus, cpf, matricula, data, hora, 
recurso, telefone,nome, id_discente, id_usuario, id_recurso, token, chat_id):
    bot.send_message(chat_id, f"Falta pouco, tenha paciencia....") #Fazendo ultimas verificações e criando classe aluno
    erro = False
    try:
        try:
            hora_inicio, _ , hora_fim = str(hora).split()
            if hora_inicio is not None and hora_fim is not None:
                setattr(aluno, 'hora_inicio', hora_inicio)
                setattr(aluno, 'hora_fim', hora_fim)
        except Exception:
            erro = True
            bot.send_message(chat_id, "Deu erro no horario solicitado, clique em /start e tente novamente")
        try:
            data = str(data).replace("/", "-")
            setattr(aluno, 'data', data)
        except:
            erro = True            
            bot.send_message(chat_id, "Houve um erro com a data informada, a data deve ser enviada com a barra / como separador e o ano não deve ser encurtado digite /start e tente novamente")
        
        if str(para_si).lower() == "sim":
            setattr(aluno, 'para_si', 1)
        elif str(para_si).lower() == "não":
            setattr(aluno, 'para_si', -1)   
        else:
            erro = True

        if erro is False:
            setattr(aluno,'campus', campus)
            setattr(aluno, 'matricula', matricula)
            setattr(aluno, 'nome', nome)
            setattr(aluno, 'cpf', cpf)
            setattr(aluno, 'id_discente', id_discente)
            setattr(aluno, 'id_usuario', id_usuario)
            setattr(aluno, 'telefone', telefone)
            setattr(aluno, 'recurso', recurso)
            setattr(aluno, 'id_recurso', id_recurso)

            dados_aluno = {"para_si": aluno.para_si,
                        "data": aluno.data,
                        "hora_inicio": f"{aluno.hora_inicio}:00",
                        "hora_fim": f"{aluno.hora_fim}:00",
                        "status_acesso": 1,
                        "nome": aluno.nome,
                        "fone": aluno.telefone,
                        "cpf": aluno.cpf,
                        "visitante": "NULL",
                        "id_usuario": aluno.id_usuario,
                        "discente_id_discente": aluno.id_discente,
                        "recurso_campus_id_recurso_campus": aluno.id_recurso}
            print(dados_aluno)
            dados_aluno_test = {"para_si": 1,
                                "data":"2021-06-26",
                                "hora_inicio":"02:00:00",
                                "hora_final":"03:00:00",
                                "status_acesso": 1,
                                "nome":"Matheus Carvalho",
                                "fone":"NULL",
                                "cpf":"12345678910",
                                "visitante":"NULL",
                                "usuario_id_usuario":1,
                                "discente_id_discente":1,
                                "recurso_campus_id_recurso_campus":7}
            agendar(dados_aluno, token, chat_id)
            #print(dados_aluno)
            #bot.send_message(chat_id, "TUDO CERTO")
    except Exception:
        pass
      

def agendar(lista, token, chat_id):

    bearer_token = f"Bearer {token}"
    payload = {"Authorization": bearer_token}
    resp = requests.post(url=f"http://localhost:5000/api.paem/solicitacoes_acessos/solicitacao_acesso", headers=payload, data=lista)
    
    res = str(resp)[10:15]

    print(res)

    if res == "[201]":
        print(f"Para_si= {aluno.para_si}\nCampus= {aluno.campus}\nCPF= {aluno.cpf}\nMatricula= {aluno.matricula}\nData= {aluno.data}\nH_ini= {aluno.hora_inicio}"
            f"H_fim= {aluno.hora_fim}\nRecurso= {aluno.recurso}\nTelefone= {aluno.telefone}\nNome= {aluno.nome}\nID_DISCENTE= {aluno.id_discente}\nId_usuario= {aluno.id_usuario}\nId_recurso: {aluno.id_recurso}")

        bot.send_message(chat_id, f"Certo, a reserva de {aluno.nome} foi feita com sucesso")

    elif res == "[500]":
        bot.send_message(chat_id, "ESSE DISCENTE JÁ RESERVOU ESSA SALA!!")
    
    elif res == "[400]":
        bot.send_message(chat_id, "ERRO NO SERVIDOR")

    elif res == "[405]":
        bot.send_message(chat_id, "ERRO NO METODO")
    
#MENSAGEM PRA EU DO FUTURO# ENTRAR NA ROTA DE SOLICVITAÇÃO ACESSO E REGISTRAR A SOLICITAÇÃO



def data_valida(data_user, chat_id):  # validando a data enviada
    try:
        data_recebida = datetime.strptime(data_user, "%d/%m/%Y")
        if data_recebida >= datetime.today():
            return True 
        else:
            return False
    except ValueError:
        return False


@bot.message_handler(func=lambda m : True )
def indef(message):
    chat_id = message.chat.id
    bot.send_message(chat_id, "Desculpe não entendi o que disse, clique em /start para fazer uma solicitação de acesso")
        
bot.polling(none_stop=True, interval=5, timeout=20)
