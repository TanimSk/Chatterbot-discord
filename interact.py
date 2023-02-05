from chatterbot import ChatBot
from chatterbot.trainers import ChatterBotCorpusTrainer


class Interact:
    def __init__(self) -> None:

        self.chatbot = ChatBot('Diana Burnwood')

        # Create a new trainer for the chatbot
        trainer = ChatterBotCorpusTrainer(self.chatbot)

        # Now let us train our bot with multiple corpus
        trainer.train("chatterbot.corpus.english.greetings",
                    "chatterbot.corpus.english.conversations")

    def talk(self, msg) -> str:
        return self.chatbot.get_response(msg)
