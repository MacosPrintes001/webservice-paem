







"""import telebot

tb = telebot.AsyncTeleBot("1882993234:AAHrEN2ENJnE22NnGkyBpTeVFttjR034SCM")
task = tb.get_me() # Execute an API call
# Do some other operations...
a = 0
for a in range(100):
    a += 10

result = task.wait() # Get the result of the execution
class Aluno:
    def __init__(self):
        self.id = None
        self.nome = None
        self.idade = None
        self.sexo = None


aluno = Aluno()


@bot.message_handler(commands=['start'])  # comando start
def send_welcome(message):
    global user
    user = message.from_user.id

    bot.    if aluno.id is None:
        setattr(aluno, 'id', user)
        bot.reply_to(message, "Olá, eu sou o bot de agendamento da UFOPA!")
        msg = bot.reply_to(message, "Qual seu nome?")
        bot.register_next_step_handler(msg, nome)
    else:
        lista = [user]
        #wen user is None send message for lista{user}
        #new aluno
        #creat new aluno
        bot.reply_to(message, "To ocupado, passa mais tarde")


def nome(message):
    nome = message.text
    setattr(aluno, 'nome', nome)
    idad = bot.reply_to(message, "Sua idade")
    bot.register_next_step_handler(idad, idade)


def idade(message):
    idad = message.text
    setattr(aluno, 'idade', idad)
    sex = bot.reply_to(message, "Qual seu sexo")
    bot.register_next_step_handler(sex, sexo)


def sexo(message):
    global user
    sex = message.text
    setattr(aluno, 'sexo', sex)
    alun = f"Nome:{aluno.nome}\nidade:{aluno.idade}\nsexo:{aluno.sexo}"

    bot.reply_to(message, "Fim atendimento")
    print(alun)

    aluno.id = None
    user = None"""


# def user_now(user):
#     u=user
#     return u
#
# user=''
#
#
# d=dict()
#
#
# @bot.message_handler(commands=['start'])  # comando start
# def send_welcome(message):
#     global user
#     user = message.from_user.id
#     d['id:'] = user
#     nome = f"{message.from_user.first_name}  {message.from_user.last_name}"
#
#     n = bot.reply_to(message, "Sua idade?")
#
#     bot.register_next_step_handler(n,idade)
#
#
# def idade(message):
#     print(user)
#     idade = message.text
#     #dick['idade'] = idade
#     d['dsfb']=idade
#     use=user_now(user)
#     if user!=use:
#         print('aqui')
#     final()
#
#
# def final():
#     print(d)

