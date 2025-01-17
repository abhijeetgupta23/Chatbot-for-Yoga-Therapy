<h1>Yoga Therapy Chatbot</h1> 

The goal of this project is to integrate AI-based features into a yoga treatment website to improve its functioning and user experience. 

Initially, LLM was OpenAI's GPT-4.0, whose responses were enhanced with Retrieval-Augmented Generation (RAG) using Vector Database (Marqo) to generate real and context-appropriate responses. 
However, we chose Perplexity's approach because of its improved capacity to provide more detailed and contextually rich information. 
Perplexity provides better contextual comprehension and more comprehensive reactions, making it an excellent choice for our specialist yoga treatment assistance.

To increase the accuracy and relevance of these responses, the bot searches a huge database of yoga-related content on PubMed and Google Scholar. Chainlit is used to deploy the bot and improve its usability. It also prompts users with follow-up questions, allowing them to refine their queries and receive more effective solutions. This interaction paradigm ensures that users obtain complete and accurate yoga treatment information that is personalized to their own needs.

Results :

1) Ailment help

![image](https://github.com/abhijeetgupta23/Chatbot-for-Yoga-Therapy/assets/16919762/fef3843e-0f68-49d5-bea4-c95f3bfa9713)

2) Therapist Search

![image](https://github.com/abhijeetgupta23/Chatbot-for-Yoga-Therapy/assets/16919762/eb845410-f032-4717-8f74-6e5c729fc50c)

3) Therapist Profile Creation

![image](https://github.com/abhijeetgupta23/Chatbot-for-Yoga-Therapy/assets/16919762/893cb8f8-29f6-48a7-8024-951357de7020)

4) Message Chaining Ability

![image](https://github.com/abhijeetgupta23/Chatbot-for-Yoga-Therapy/assets/16919762/cb449613-9dfd-4787-b509-8827b043cd52)

![image](https://github.com/abhijeetgupta23/Chatbot-for-Yoga-Therapy/assets/16919762/221f5e64-8af2-4457-990b-14b8d06a7e8e)

Chatbot Demo :

[![Watch the video](https://img.youtube.com/vi/Ye-XBZnbD3w/maxresdefault.jpg)](https://youtu.be/Ye-XBZnbD3w)

Steps to install the Chatbot:

1.	Set Up Environment: Make sure Python is installed, and then create a virtual environment. This establishes an isolated environment for managing dependencies.
2.	Install Dependencies: Install the required libraries using the following command:
bash
Copy code
pip install openai chainlit
3.  Download: Yoga_Chatbot_FinalVersion.py from this repository 
4.	API Key: Replace YOUR_API_KEY with your actual Perplexity API key.
5.	Powershell : Open it and change directory to where Yoga_Chatbot_FinalVersion.py is saved using cd command
6.	Run the Script: Execute the script to start the Chainlit application:
   
    ```Chainlit run Yoga_Chatbot_FinalVersion.py```

7.	Interact with the Bot: Launch the application in your browser and begin engaging with the Yoga Therapy Assistant Bot. Enter your questions about yoga therapy and get detailed answers.

