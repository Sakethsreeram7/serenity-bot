import textbase
from textbase.message import Message
from textbase import models
import os
from typing import List

# Set the API key for the Bard model
models.Bard.api_key = "BARD_API key"

# This prompt is used to set the context for the chatbot.
MENTAL_HEALTH_PROMPT = """You are chatting with Serenity, a mental health support chatbot.
I am here to listen and provide guidance for your mental well-being.
"""

# These are filtered out to ensure the chatbot won't provide harmful responses.
BANNED_WORDS = ["suicidal", "harmful", "offensive", "inappropriate", "triggering"]

# This is the main function that is called when the chatbot receives a message.
def has_banned_words(text):
    
    text = text.lower()
    
    return any(word in text for word in BANNED_WORDS)

@textbase.chatbot("serenity-bot")
def on_message(message_history: List[Message], state: dict = None):
    """
    Mental Health Support Chatbot Logic:
    - The chatbot provides guided mental health support and advice to users.
    - It utilizes prompt engineering to set a supportive and empathetic context.
    - Guardrails are established to ensure harmful responses are filtered out.

    :param message_history: List of user messages in the conversation.
    :param state: A dictionary to store any relevant stateful information.

    :return: A string with the bot_response or a tuple of (bot_response: str, new_state: dict).
    """

    # Initialize the state if it is not provided
    if state is None:
        state = {}

    # Increment the counter in the state
    if "counter" not in state:
        state["counter"] = 0
    state["counter"] += 1

    # Generate a response from the chatbot
    bot_response = models.Bard.generate(
        system_prompt=MENTAL_HEALTH_PROMPT,
        message_history=message_history,
    )

    # Get the latest message from the user
    latest_user_message = message_history[-1].text.lower()

    # Filter out harmful responses
    if has_banned_words(latest_user_message):
        # If banned words are present, respond empathetically without triggering content.
        bot_response = "I'm really sorry to hear that you're feeling this way, but I can't provide a response to that. It's important to prioritize your safety and well-being. Please consider reaching out to a mental health professional or someone you trust for support."

    # Provide supportive responses for specific keywords
    if "feeling" in latest_user_message:
        if "sad" in latest_user_message or "down" in latest_user_message:
            # Provide support for sadness or depression.
            bot_response = "I'm sorry to hear that you're feeling sad. Remember that it's okay to experience a range of emotions. Try engaging in activities that bring you joy or talking to someone you trust about how you're feeling."

        elif "anxious" in latest_user_message or "nervous" in latest_user_message:
            # Provide support for anxiety.
            bot_response = "It's common to feel anxious or nervous at times. Consider practicing deep breathing or mindfulness exercises to help you feel more centered. Don't hesitate to reach out for support if you need it."

        elif "stressed" in latest_user_message:
            # Provide support for stress.
            bot_response = "Stress can be overwhelming, but there are strategies to manage it. Take breaks, practice self-care, and prioritize your well-being. If stress becomes too much, seek support from friends or professionals."

    # Additional dynamic responses based on specific keywords can be added here
    # For example, the chatbot can recognize other emotions or mental health concerns.

    return bot_response, state
