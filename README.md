# Mental Health Support Chatbot: Serenity

## Overview

Serenity is a mental health support chatbot designed to provide guided advice and support for users experiencing emotional distress or seeking mental well-being tips. This chatbot utilizes the BARD API by TextBase to generate empathetic and supportive responses based on user interactions.

## Features

- Empathetic Responses: Serenity is designed to respond empathetically, acknowledging the user's feelings and experiences in a supportive manner.

- Prompt Engineering: The chatbot sets a supportive and compassionate context to create a safe space for users to share their feelings.

- Guardrails Against Harmful Responses: Serenity filters out messages containing banned words or phrases to ensure the chatbot does not provide harmful content.

- Dynamic Responses: The chatbot dynamically generates responses based on user input, tailoring advice to specific emotions or mental health concerns.

## Setup

1. **BARD API Key**: Obtain your BARD API key from TextBase. Replace `<YOUR_API_KEY>` in `main.py` with your actual API key.

2. **TextBase Installation**: Ensure that TextBase is installed in your Python environment. You can install it using pip:

```bash
pip install textbase
