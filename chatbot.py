import random
import datetime

def chatbot():
    print("🤖 Smart AI Chatbot (type 'bye' to exit)\n")

    # Get user name
    name = input("Bot: What's your name? ")
    print(f"Bot: Nice to meet you, {name}! 😊")

    # Data
    greetings = ["Hello!", "Hi there!", "Hey!", "Nice to see you!"]
    jokes = [
        "Why do programmers prefer dark mode? Because light attracts bugs 😄",
        "Why did Python go to school? To improve its class 😂",
        "Why do Java developers wear glasses? Because they don’t see sharp 🤓"
    ]

    while True:
        user_input = input(f"{name}: ").lower()

        if user_input == "bye":
            print(f"Bot: Goodbye {name}! 👋")
            break

        elif "hi" in user_input or "hello" in user_input:
            print("Bot:", random.choice(greetings))

        elif "how are you" in user_input:
            print("Bot: I'm doing great! How about you? 😄")

        # Mood detection
        elif "sad" in user_input or "upset" in user_input:
            print("Bot: I'm here for you 💙 Things will get better!")

        elif "happy" in user_input or "good" in user_input:
            print("Bot: That's awesome! Keep smiling 😄✨")

        elif "stress" in user_input:
            print("Bot: Take a deep breath 😌 You got this!")

        # Time feature
        elif "time" in user_input:
            current_time = datetime.datetime.now().strftime("%H:%M:%S")
            print("Bot: Current time is", current_time)

        # Joke feature
        elif "joke" in user_input:
            print("Bot:", random.choice(jokes))

        elif "your name" in user_input:
            print("Bot: I'm your Smart AI Chatbot 🤖")

        elif "python" in user_input:
            print("Bot: Python is powerful for AI and ML 🚀")

        else:
            print("Bot: Hmm... I didn't understand that. Tell me more 🤔")


# Run chatbot
chatbot()