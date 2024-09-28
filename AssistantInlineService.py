from chatbot.BotFactory import BotFactory
from chatbot.ChatBot import ChatBot
from chatbot.CommandDTO import CommandDTO


class AssistantInlineService():
    def getAssistant(self) -> ChatBot:
        return BotFactory().getBot("Gemini")
    def defineAssistant(self, code: str) -> CommandDTO:
        return CommandDTO(role = "Inline Code Assistant", temperature= 0.1, prompt=f"Return the next line of code: {code}")
    def getInlineAssistance(self, code):
        bot = self.getAssistant()
        command = self.defineAssistant(code)
        try:
            return bot.generateText(command)
        except Exception as e:
            raise Exception("Internal server Error")


