from chatbot.BotFactory import BotFactory
from chatbot.ChatBot import ChatBot
from chatbot.CommandDTO import CommandDTO

class ChatService():
    def getAssistant(self) -> ChatBot:
        return BotFactory().getBot("Gemini")

    def defineAssistant(self, prompt: str, historic: list = []) -> CommandDTO:
        TEMPERATURE = 0.5
        return CommandDTO(temperature=TEMPERATURE, prompt=prompt, history=historic)

    def getResponse(self, prompt, historic):
        bot = self.getAssistant()
        command = self.defineAssistant(prompt, historic)
        try:
            response = bot.chat(command)
            return response
        except Exception as e:
            raise e