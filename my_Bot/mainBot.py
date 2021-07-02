from datetime import datetime
import telebot  # API do Telegram
import os
from bot_conexao import login
from dados_Bot import btoken

token = btoken
bot = telebot.TeleBot(token)


class Aluno:
    def __init__(self):
        self.nome = None
        self.para_si = None
        self.data = None
        self.hora_inicio = None
        self.hora_fim = None
        self.espaco = None
        self.telefone = None
        self.matricula = None


class Pessoa:
    def __init__(self):
        self.pessoa_telegram = None


aluno = Aluno()
tele_user = Pessoa()


@bot.message_handler(commands=['start'])  # comando start
def send_welcome(message):
    msg = bot.reply_to(message, f"Olá, eu sou o bot de agendamento da UFOPA! Antes de mais nada eu preciso saber se "
                                f"você está tentando agendar um espaço para você mesmo ou para terceiros então, "
                                f"esse atendimento é para você "
                                f"mesmo?\n Responda com Sim ou Não")
    bot.register_next_step_handler(msg, step_for_you)


def step_for_you(message):
    try:
        chat_id = message.chat.id
        msg = message.text
        msg = str(msg).lower()
        if msg == "sim":
            setattr(aluno, 'para_si', 1)
            bot.send_message(chat_id, "Certo, vou precisar do seu CPF. "
                                      "Basta digitar /agendar + CPF\n"
                                      "Ex: /agendar 03022504472")
        elif msg == "não":
            setattr(aluno, 'para_si', -1)
            bot.send_message(chat_id, "Ok, vou precisar do CPF da pessoa para quem devo registrar."
                                      "Basta digitar /agendar + CPF\n"
                                      "Ex: /agendar 03022504472")
        else:
            new_msg = bot.send_message(chat_id, "Desculpe, não entendi o que você disse,"
                                                " este atendimento é para você mesmo? responda com Sim ou Não esse")
            bot.register_next_step_handler(new_msg, step_for_you)

    except EOFError:
        new_msg = bot.send_message(message.chat.id, "Desculpe, não entendi o que você disse,"
                                                    "este atendimento é para você mesmo? responda "
                                                    "com Sim ou Não esse 2")
        bot.register_next_step_handler(new_msg, step_for_you)


# tarefa de agendamento de espaço
@bot.message_handler(commands=['agendar'])  # comando agendar
def schedule(message):
    para_quem = aluno.para_si
    chat_id = message.chat.id
    if para_quem is not None:  # teste para saber se apessoa fez a etapa de dizer para quem é o acesso
        try:
            bot.reply_to(message, "certo aguarde um momento...")
            mensagem = message.text
            comando, matricula = map(str, mensagem.split(' '))

            #nome_aluno, id_discente = conetct.login(matricula)  # como eu acho que vai ficar
            
            if login(matricula): #Teste para saber se o CPF está no bd
                try:
                    setattr(aluno, 'matricula', matricula)
                    # salvando informações da pessoa que está reservando
                    tele_User = f"id = {message.from_user.id} nome = {message.from_user.first_name} " \
                        f"{message.from_user.last_name} "
                    setattr(tele_user, 'pessoa_telegram', tele_User)
                    # indice = Lista_pessoas.index(cpf)  # pegando o nome da pessoa para quem vou reservar
                    # bot.reply_to(message, f"Muito bem vou agendar um horario para o(a) {Lista_pessoas[indice - 1]}")
                    bot.send_message(chat_id, "Agora eu preciso que me diga a data que quer agendar, basta digitar "
                                              "/data dd/mm/yyyy")
                except EOFError:
                    bot.send_message(chat_id, f"Opa, parece que você digitou algo errado,"
                                              f" tente de novo, siga o exemplo{os.linesep} "
                                              f"/agendar 2019002548")
            else:
                bot.send_message(chat_id,
                                 "Olha, eu não achei essa pessoa no banco de dados, "
                                 "verifique se você digitou certo e tente de novo")
        except EOFError:
            bot.send_message(chat_id, f"Opa, parece que você digitou algo errado,"
                                      f" tente de novo, siga o exemplo{os.linesep}"
                                      f"/agendar 03022504472")
    else:
        bot.send_message(chat_id, "Desculpe estão faltando alguns dados, envie /start para iniciar o atendimento")

@bot.message_handler(commands=['data'])  # comando data
def date(message):
    para_quem = aluno.para_si
    chat_id = message.chat.id
    if para_quem is not None:  # teste para saber se apessoa fez a etapa de dizer para quem é o acesso
        try:
            mensagem = message.text
            chat_id = message.chat.id
            comando, data = map(str, mensagem.split(' '))
            test_data = data_valida(data, chat_id)
            if test_data:
                data = str(data).replace("/", "-")
                setattr(aluno, 'data', data)
                hora = bot.send_message(chat_id, f"Muito bem, para qual horario? {os.linesep}"
                                                 f"1- 8:00 às 10:00{os.linesep}2- 10:00 às 12:00{os.linesep}"
                                                 f"3- 14:00 às16:00{os.linesep}4- 16:00 às 18:00")
                bot.register_next_step_handler(hora, ask_phone_number)
            else:
                bot.send_message(chat_id, "Por favor digite uma data valida")
        except EOFError:
            bot.send_message(chat_id, f"Opa, digite a data conforme o exemplo indicado, sem encurtar o ano{os.linesep}"
                                      f"Ex: /data 25/06/2022")
    else:
        bot.send_message(chat_id, "Desculpe estão faltando alguns dados, envie /start para iniciar o atendimento")


def data_valida(data_user, chat_id):  # validando a data enviada
    try:
        data_recebida = datetime.strptime(data_user, '%d/%m/%Y')
        if data_recebida >= datetime.today():
            #  data_fim = data_recebida.split('')
            # __ADICIONAR__ Verificar se a data está disponivel no banco
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


def ask_phone_number(message):
    chat_id = message.chat.id
    msg = message.text
    msg = str(msg)
    horas = {"1": "08:00:00 10:00:00",
             "2": "10:00:00 12:00:00",
             "3": "14:00:00 16:00:00",
             "4": "16:00:00 18:00:00"}

    if msg in horas:
        h = horas[msg].split(' ')
        setattr(aluno, 'hora_inicio', h[0])
        setattr(aluno, 'hora_fim', h[1])
        phone = bot.send_message(chat_id, "Beleza, agora preciso do seu numero de telefone:\n "
                                          "Ex: (93)991302546")
        bot.register_next_step_handler(phone, verific_fim)

    else:
        new_msg = bot.send_message(chat_id, f"Opa deu algo errado, digite novamente para qual horario vai ser a "
                                            f"reserva: {os.linesep} 1- 8:00 às 10:00{os.linesep}"
                                            f"2- 10:00 às 12:00{os.linesep}"
                                            f"3- 14:00 às16:00{os.linesep}4- 16:00 às 18:00")
        bot.register_next_step_handler(new_msg, ask_phone_number)


# verificação final
def verific_fim(message):
    chat_id = message.chat.id
    if tele_user.pessoa_telegram is not None and aluno.matricula is not None and aluno.data is not None \
            and aluno.hora_inicio is not None and aluno.hora_fim is not None:
        bot.send_message(chat_id, "Certo, sua reserva ja foi agendada, obrigado por usar este serviço")
        # salvar no bd

    else:
        bot.send_message(chat_id, "Opa, parece que você não deu todos os dados, não tente pular etapas!\n"
                                  "digite /start e tente novamente")


# tratar mensagens aleatorias
@bot.message_handler(func=lambda m: True)
@bot.message_handler(content_types=['audio', 'sticker'])
def inesp(message):
    bot.reply_to(message, "Desculpe, não entendi o que disse. "
                          "Digite /start para iniciar o atendimento novamente")


bot.polling(none_stop=True, interval=3, timeout=20)
