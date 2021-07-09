from datetime import datetime
import telebot  # API do Telegram
import os

from telebot.util import is_string

from dados_bot import btoken
import conexao_bot as conBot


token = btoken
bot = telebot.TeleBot(token)


"""
Significado dos comentarios

#/ -> coisas a fazer

# -> explicação do que faz

"""

link = "https://www.linkDoCristian.com"


class Aluno:
    #adicionar id
    def __init__(self):
        self.nome = None
        self.para_si = None
        self.data = None
        self.hora_inicio = None
        self.hora_fim = None
        self.espaco = None
        self.telefone = None
        self.cpf = None


class Pessoa:
    def __init__(self):
        self.pessoa_telegram = None


aluno = Aluno()
tele_user = Pessoa()


@bot.message_handler(commands=['start'])  # comando start
def send_welcome(message):
    msg = bot.reply_to(message, "Olá, eu sou o bot de agendamento da UFOPA! para continuar você precisar ter uma conta, você possui tal conta? Responda com Sim ou Não ")
    bot.register_next_step_handler(msg, acount_verifc)


def acount_verifc(message):
    try:
        chat_id = message.chat.id
        msg = str(message.text).lower()
        if msg == "sim":
            resp = bot.send_message(chat_id, "Certo, esse atendimento é para você mesmo?\n Responda com sim ou não")
            bot.register_next_step_handler(resp, step_for_you)
        elif msg == "não":
            bot.send_message(chat_id, "Ok, então, você precisa criar uma conta antes de tentar reservar um espaço na UFOPA, \
                                    vou te mandar um link pra você se cadastrar, aí depois você pode voltar aqui")
            bot.send_message(chat_id, link)
        else:
            resp = bot.send_message(chat_id, "Desculpe não entendi oque disse. Você já possui uma conta de usuario? Responda com Sim ou Não")
            bot.register_next_step_handler(resp, acount_verifc)
    except:
        resp = bot.send_message(chat_id, "Desculpe não entendi oque disse. Você já possui uma conta de usuario? Responda com Sim ou Não")
        bot.register_next_step_handler(resp, acount_verifc)
    

def step_for_you(message):#passo para a pessoa dizer se o atendimento vai ser pra ela
    try:
        chat_id = message.chat.id
        msg = str(message.text).lower()
        if msg == "sim":
            setattr(aluno, 'para_si', 1)
            msg = bot.send_message(chat_id, "Certo, vou precisar do seu CPF.")
            bot.register_next_step_handler(msg, schedule)
        elif msg == "não":
            setattr(aluno, 'para_si', 0)
            msg = bot.send_message(chat_id, "Ok, vou precisar do CPF da pessoa para quem devo registrar.")
            bot.register_next_step_handler(msg, schedule)
        else:
            new_msg = bot.send_message(chat_id, "Desculpe, não entendi o que você disse,\
                                                 este atendimento é para você mesmo? responda com Sim ou Não esse")
            bot.register_next_step_handler(new_msg, step_for_you)

    except EOFError:
        new_msg = bot.send_message(message.chat.id, "Desculpe, não entendi o que você disse, \
                                                    este atendimento é para você mesmo? responda com Sim ou Não esse 2")
        bot.register_next_step_handler(new_msg, step_for_you)


#@bot.message_handler(commands=['agendar'])  

def schedule(message):# tarefa de agendamento de espaço
    para_quem = aluno.para_si
    chat_id = message.chat.id    
    cpf = str(message.text)
    if para_quem is not None:# teste para saber se apessoa fez a etapa de dizer para quem é o acesso
        try:            
            "comando, cpf = map(str, mensagem.split(' '))"
            if cpf is not None: 
                bot.reply_to(message, "certo aguarde um momento...")

                resp = conBot.login(cpf)

                if resp: #Teste para saber se o CPF está no bd
                        setattr(aluno, 'cpf', cpf)
                        # salvando informações da pessoa que está reservando
                        tele_User = f"id = {message.from_user.id} nome = {message.from_user.first_name} {message.from_user.last_name}"
                        setattr(tele_user, 'pessoa_telegram', tele_User)

                        #/provavelmente vou precisar acessar a rota campus
                        campus = bot.send_message(chat_id, "Ok, para qual campus você quer fazer a reserva?")
                        bot.register_next_step_handler(campus, ask_campus)
                elif resp == "erro":
                    bot.send_message(chat_id, "Houve um erro de conexão, tente enviar o CPF novamente, caso o erro persista entre em contato conosco")
                else:
                    bot.send_message(chat_id, "Olha, eu não achei essa pessoa no banco de dados, verifique se você digitou certo e tente de novo") 
                    bot.send_message(chat_id, f"Ou então, caso você não tenha uma conta basta acessar o link e criar uma antes de poder prosseguir {link}" )

        except Exception:
            bot.send_message(chat_id, "Opa, parece que você digitou algo errado, digite novamente o CPF.")
    else:
        bot.send_message(chat_id, "Desculpe estão faltando alguns dados,\n envie /start para iniciar o atendimento")


def ask_campus(message):
    #/passar dados de forma dinamica para o usuario
    chat_id = message.chat.id
    campus = str(message.text)
    try:
        if campus is not None: #verificar de qual campus a pessoa é
            #/ pegar salas de fomra dinamica
            recurso = bot.send_message(chat_id, f"Certo qual sala você quer reservar? Digite o número da opção que deseja{os.linesep}"
                                                    "1- Laboratório de ensino em Biologia\n"
                                                    "2- Laboratório multidisciplinar de biologia II\n"
                                                    "3- Laboratório de Informática\n"
                                                    "4- Biblioteca\n"
                                                    "5- Area Comum de Convivência\n"
                                                    "6- Auditorio")
            bot.register_next_step_handler(recurso, agendar_recurso)
    except:
        camp = bot.send_message(chat_id, "Não entendi, para qual campus você quer fazer a reserva?")
        bot.register_next_step_handler(camp, ask_campus)

def agendar_recurso(message):
    try:
        chat_id = message.chat.id
        texto = str( message.text)
        recursos = {"1": "Laboratório de ensino em Biologia",
                    "2": "Laboratório multidisciplinar de biologia II",
                    "3": "Laboratório de Informática",
                    "4": "Biblioteca",
                    "5": "Area_Comum",
                    "6": "Auditorio"}
        #/verificar como eu vou resetar para liberar as vagas
        if texto in recursos:
                setattr(aluno, 'espaco', texto)
                data = bot.send_message(chat_id, "Agora eu preciso que me diga a data que quer agendar no seguinte formato dd/mm/yyyy")
                bot.register_next_step_handler(data, my_date)
        else:
            new_msg = bot.send_message(chat_id, "ERRO, digite um valor valido:\n"
                                                "1- Laboratório de ensino em Biologia\n"
                                                "2- Laboratório multidisciplinar de biologia II\n"
                                                "3- Laboratório de Informática\n"
                                                "4- Biblioteca\n"
                                                "5- Area Comum de Convivência\n"
                                                "6- Auditorio")
            bot.register_next_step_handler(new_msg, agendar_recurso)
    except:
        new_msg = bot.send_message(chat_id, "ERRO, digite um valor valido:\n"
                                            "1- Laboratório de ensino em Biologia\n"
                                            "2- Laboratório multidisciplinar de biologia II\n"
                                            "3- Laboratório de Informática\n"
                                            "4- Biblioteca\n"
                                            "5- Area Comum de Convivência\n"
                                            "6- Auditorio")
        bot.register_next_step_handler(new_msg, agendar_recurso)



#@bot.message_handler(commands=['data']) 
def my_date(message): # comando data
    para_quem = aluno.para_si
    chat_id = message.chat.id
    mensagem = str(message.text)
    if para_quem is not None:  # teste para saber se apessoa fez a etapa de dizer para quem é o acesso
            try:
                comando, data = map(str, mensagem.split(' '))
                test_data = data_valida(data, chat_id)
                if test_data:
                    data = str(data).replace("/", "-") #troco o separador da data antes de guardar ela
                    setattr(aluno, 'data', data)
                    hora = bot.send_message(chat_id,f"Muito bem, para qual horario? Responda com o número da opção \n"
                                                    "1- 08:00 às 09:00\n2- 09:01 às 10:00\n"
                                                    "3- 10:01 às 11:00\n4- 11:01 às 12:00\n"
                                                    "5- 14:00 às 15:00\n6- 15:01 às 16:00\n"
                                                    "7- 16:01 às 17:00\n8- 17:01 às 18:00")
                    bot.register_next_step_handler(hora, ask_phone_number)
                else:
                    bot.send_message(chat_id, "Por favor digite uma data valida")
            except:
                bot.send_message(chat_id, f"Opa, digite a data conforme o exemplo indicado, sem encurtar o ano{os.linesep}"
                                      f"Ex: /data 25/06/2022")           
    else:
        bot.send_message(chat_id, "Desculpe estão faltando alguns dados,\n envie /start para iniciar o atendimento")


def data_valida(data_user, chat_id):  # validando a data enviada
    try:
        data_recebida = datetime.strptime(data_user, "%d/%m/%Y")
        if data_recebida >= datetime.today():
            #  data_fim = data_recebida.split('')
            #/ Verificar se a data está disponivel no banco
            # if data_recebida is None in banco:
            #   return True
            # else:
            #     bot.send_message(chat_id, "Sinto muito esta data não está disponivel, tente com outra data")
            #        return False

            return True  # tirar esse cara na versão com conexão ao banco
        else:
            return False
    except ValueError:
        return False


def ask_phone_number(message): #perguntar qual o numero da pessoa
    chat_id = message.chat.id
    msg = str( message.text)
    horas = {"1": "08:00:00 09:00:00",
             "2": "09:01:00 10:00:00",
             "3": "10:01:00 11:00:00",
             "4": "11:01:00 12:00:00",
             "5": "14:00:00 15:00:00",
             "6": "15:01:00 16:00:00",
             "7": "16:01:00 17:00:00",
             "8": "17:01:00 18:00:00"}

    if msg in horas:
        h = horas[msg].split(' ')
        setattr(aluno, 'hora_inicio', h[0])
        setattr(aluno, 'hora_fim', h[1])
        phone = bot.send_message(chat_id, "Beleza, por motivos de segurança o telegram não me permite ver seu número então, você poderia digitar pra mim? Segue exemplo:\n "
                                          "Ex: (93)991302546")
        bot.register_next_step_handler(phone, verific_fim)

    else:
        new_msg = bot.send_message(chat_id, f"Opa deu algo errado, digite novamente para qual horario vai ser a sua reserva:(Digite o Numero da sua opção) \n"
                                            "1- 08:00 às 09:00\n2- 09:01 às 10:00\n"
                                            "3- 10:01 às 11:00\n4- 11:01 às 12:00\n"
                                            "5- 14:00 às 15:00\n6- 15:01 às 16:00\n"
                                            "7- 16:01 às 17:00\n8- 17:01 às 18:00")
        bot.register_next_step_handler(new_msg, ask_phone_number)


# verificação final
def verific_fim(message):
    chat_id = message.chat.id
    phone = str(message.text)
    if tele_user.pessoa_telegram is not None and aluno.cpf is not None and aluno.data is not None \
            and aluno.hora_inicio is not None and aluno.hora_fim is not None:
        setattr(aluno, 'telefone', phone)
        bot.send_message(chat_id, "Certo, sua reserva ja foi agendada, obrigado por usar este serviço")
        
        print(aluno.nome)
        print(aluno.cpf)
        print(aluno.data)
        print(aluno.espaco)
        print(aluno.para_si)
        print(aluno.telefone)
        print(aluno.hora_inicio)
        print(aluno.hora_fim)
        
        #/ salvar no bd

    else:
        bot.send_message(chat_id, "Desculpe estão faltando alguns dados,\n envie /start para iniciar o atendimento")


# tratar mensagens aleatorias
@bot.message_handler(func=lambda m: True)
@bot.message_handler(content_types=['audio', 'sticker'])
def inesp(message):
    bot.reply_to(message, "Desculpe, não entendi o que disse. Digite \n/start para iniciar o atendimento novamente")


bot.polling(none_stop=True, interval=3, timeout=20)
