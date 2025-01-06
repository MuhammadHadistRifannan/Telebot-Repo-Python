import telebot
import google.generativeai as gemini
from spread_sheet import init_spreadsheet , get_spreadsheet
from apikey import GEMINI_API , TELE_API , IDENTITY_BOT , CREDENTIAL_FILE

client = gemini.GenerativeModel('gemini-1.5-flash-002')
gemini.configure(api_key=GEMINI_API)

botTele = telebot.TeleBot(token=TELE_API)

@botTele.message_handler(func=lambda msg : True)
def sendMessage(message):
    identity = IDENTITY_BOT #add identity
    response = client.generate_content(identity + message.text) #generate output for gemini
    result = response.text.removeprefix("*")


def main():
    botTele.polling()
    


if __name__ == '__main__':
    main()