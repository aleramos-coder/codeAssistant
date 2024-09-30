from chatbot.BotFactory import BotFactory
from chatbot.ChatBot import ChatBot
from chatbot.CommandDTO import CommandDTO


class AssistantInlineService():
    def getAssistant(self) -> ChatBot:
        return BotFactory().getBot("Gemini")
    def defineAssistant(self, code: str) -> CommandDTO:
        ROLE = "Code Assistant"
        TEMPERATURE = 0.5
        PROMPT = (f'Primary Task: return the next code snippets, complete scripts based ' +
                  f'on user input and comments.'+
                    'The response should always be concise, actionable, and executable.'
                  f' Code or user input: {code}')
        return CommandDTO(role = ROLE, temperature=TEMPERATURE , prompt=PROMPT)
    def getInlineAssistance(self, code):
        bot = self.getAssistant()
        command = self.defineAssistant(code)
        try:
            return bot.generateText(command)
        except Exception as e:
            raise Exception("Internal server Error")


