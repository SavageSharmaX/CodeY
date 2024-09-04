# Import the ChatterBot library
from chatterbot import ChatBot
from chatterbot.trainers import ChatterBotCorpusTrainer # Create a new chatbot instance
chatbot = ChatBot('MyBot')

# Create a trainer for the chatbot
trainer = ChatterBotCorpusTrainer(chatbot)

# Train the chatbot using the English language corpus
trainer.train("chatterbot.corpus.english")

# Now you can interact with the chatbot
while True:
    user_input = input("You: ")
    response = chatbot.get_response(user_input)
    print("Bot:", response)
