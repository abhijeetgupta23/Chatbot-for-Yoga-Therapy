#!/usr/bin/env python
# coding: utf-8

# In[1]:


#!/usr/bin/env python

# Install libraries in Command Line using "pip install openai chainlit" before running below code

from openai import OpenAI
import chainlit as cl

# Change YOUR_API_KEY by creating one on https://www.perplexity.ai/settings/api. 
# Below is our API Key which will run out of credit in a few days

YOUR_API_KEY = "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"

messages = [
    {"role": "system", "content": "You are a helpful assistant."}
]

client = OpenAI(api_key=YOUR_API_KEY, base_url="https://api.perplexity.ai")

# Define the function to handle user queries
def handle_query(user_prompt):
    messages.append({"role": "user", "content":  (
            "You are an artificial intelligence assistant that specializes in providing Treatment solutions using Yoga Therapy and"
            "you need to engage in a helpful, detailed, polite conversation with a user."
            "Always provide 3 follow up questions that users might want to ask at the end before you are done."
            "Use  data from these given links' to answer questions regarding user ailments and diseases:"
            "1) https://drive.google.com/file/d/1IXQjpBgDOFnk43s5usF5cuxf8E2kB_DE/view?usp=sharing "
            "2) https://www.researchgate.net/publication/241276627_PRINCIPLES_AND_METHODS_OF_YOGA_THERAPY_Compilation "
            "3) https://drive.google.com/file/d/1C-Op_gwU1mqtz6xRGnizfKaNhL9cOWYH/view?usp=drivesdk "
            "4) https://pubmed.ncbi.nlm.nih.gov "
            "5) https://scholar.google.com "
            "If user asks for a yoga therapist recommendation based on a certain location, Contact details must be provided, including an IAYT URL."
            "They must be IAYT approved, users don't want to scroll the website themselves"    
 
            "User's question - " + user_prompt +"\nAnswer :"
        )})

    # Chat completion without streaming
    response = client.chat.completions.create(
        model="llama-3-sonar-large-32k-online",
        messages=messages,
    )

    assistant_response = response.choices[0].message.content
    messages.append({"role": "assistant", "content": assistant_response})

    return assistant_response

# Chainlit integration
@cl.on_chat_start
async def start():
    msg = cl.Message(content="Starting the Yoga Therapy Bot...")
    await msg.send()
    msg.content = "Hi, Welcome to the Yoga Therapy Assistant Bot. How can I help you today?\n\n(Note: Enter any questions related to yoga)"
    await msg.update()

@cl.on_message
async def main(message: cl.Message):
    user_prompt = message.content
    response = handle_query(user_prompt)
    await cl.Message(content=response).send()

  # This will start the Chainlit application when the script is run


# In[ ]:




