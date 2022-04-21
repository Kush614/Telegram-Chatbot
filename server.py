from bot import telegram_chatbot
from chatterbot import ChatBot
from chatterbot.trainers import ChatterBotCorpusTrainer

bot = telegram_chatbot("config.cfg")

chatbot = ChatBot("Kush_chatbot")
trainer = ChatterBotCorpusTrainer(chatbot)
trainer.train("chatterbot.corpus.english")

def make_reply(msg):
    reply = None
    if msg is not None:
        reply = chatbot.get_response(msg)
    return reply

print("Server started, Now the bot can respond to messages")

update_id = None
while True:
    updates = bot.get_updates(offset=update_id)
    updates = updates["result"]
    if updates:
        for item in updates:
            update_id = item["update_id"]
            try:
                message = str(item["message"]["text"])
            except:
                message = None
            from_ = item["message"]["from"]["id"]
            reply = make_reply(message)
            bot.send_message(reply, from_)
