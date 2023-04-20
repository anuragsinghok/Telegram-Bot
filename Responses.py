from datetime import datetime


def sample_responses(input_text):
    # lower because we don't want user will worry about capitalising any letter or word
    user_messages = str(input_text).lower()

    if user_messages in ("hello", "hi", "hey", "hey there", "hi there", "sup"):
        return "Hey there! How can I help you?"

    if user_messages in ("who are you", "what are you", "tell me about yourself"):
        return "I am a low-code bot created to assist you. You can ask me anything."

    if user_messages in ("time", "what's the time", "what is the time", "tell me the time","time?"):
        now = datetime.now()
        # for the current time with date
        date_time = now.strftime("%d/%m/%Y, %H:%M:%S")

        return f"The current date and time is {date_time}."

    if "add" in user_messages:
        # split the message by space and extract numbers
        numbers = [int(word) for word in user_messages.split() if word.isdigit()]
        if len(numbers) != 2:
            return "I'm sorry, I couldn't find two numbers to add. Could you please try again?"
        else:
            result = numbers[0] + numbers[1]
            return f"The result of adding {numbers[0]} and {numbers[1]} is {result}."

    if "subtract" in user_messages:
        # split the message by space and extract numbers
        numbers = [int(word) for word in user_messages.split() if word.isdigit()]
        if len(numbers) != 2:
            return "I'm sorry, I couldn't find two numbers to subtract. Could you please try again?"
        else:
            result = numbers[0] - numbers[1]
            return f"The result of subtracting {numbers[1]} from {numbers[0]} is {result}."

    if "multiply" in user_messages:
        # split the message by space and extract numbers
        numbers = [int(word) for word in user_messages.split() if word.isdigit()]
        if len(numbers) != 2:
            return "I'm sorry, I couldn't find two numbers to multiply. Could you please try again?"
        else:
            result = numbers[0] * numbers[1]
            return f"The result of multiplying {numbers[0]} and {numbers[1]} is {result}."

    return "I'm sorry, I don't understand what you mean. Could you please try again?"
