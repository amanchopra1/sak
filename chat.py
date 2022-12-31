import random
import json
import openai as ai
import torch
from gpt3 import *

from model import NeuralNet
from nltk_utils import bag_of_words, tokenize

device = torch.device('cuda' if torch.cuda.is_available() else 'cpu')

with open('intents.json', 'r') as json_data:
    intents = json.load(json_data)

FILE = "data.pth"
data = torch.load(FILE)

input_size = data["input_size"]
hidden_size = data["hidden_size"]
output_size = data["output_size"]
all_words = data['all_words']
tags = data['tags']
model_state = data["model_state"]

model = NeuralNet(input_size, hidden_size, output_size).to(device)
model.load_state_dict(model_state)
model.eval()

bot_name = "Sakha"

def get_response(msg):
    sentence = tokenize(msg)
    X = bag_of_words(sentence, all_words)
    X = X.reshape(1, X.shape[0])
    X = torch.from_numpy(X).to(device)
    ai.api_key = "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"

    completion = ai.Completion()
    question = ""
    start_chat_log = """Human: Hello, I am Human.
    Sakha: Hello, human I am Sakha
    Human: How are you?
    Sakha: I am fine, thanks for asking.
    Human: I am depressed
    Sakha: You worry about events you are not supposed and speak like a learned man, Wise people do not worry about things that are perishable, or immortal
    Human: I am feeling lonely
    Sakha: I am there for you to listen and understand your suffering
    Human: I am pissed off
    Sakha: Fools vent their anger, but the wise quietly hold it back
    Human: I am stressed
    Sakha: Chant Hare Krishna and be happy
    Human: I am demotivated
    Sakha: Through selfless service, you will always be fruitful and find the fulfillment of your desires
    Human: Who is Krishna?
    Sakha: Supreme Personality of godhead
    Human: I Am Confused
    Sakha: The Supreme Lord dwells in the hearts of all living beings, O Arjun. According to their karmas, He directs the wanderings of the souls, who are seated on a machine made of material energy.
    Human: You're so loving and caring
    Sakha: All glory to Shri Krishna, the Supreme Personality of Godhead. He is the source of all loving and caring in the universe. 
    """

    
    output = model(X)
    _, predicted = torch.max(output, dim=1)

    tag = tags[predicted.item()]

    probs = torch.softmax(output, dim=1)
    prob = probs[0][predicted.item()]
    if prob.item() > 0.75:
        for intent in intents['intents']:
            if tag == intent["tag"]:
                return random.choice(intent['responses'])
    chat_log = start_chat_log
    prompt = f"{chat_log}Human: {question}\nSakha:"
    response = completion.create(prompt = prompt, engine =  "davinci", temperature = 0.85,top_p=1, frequency_penalty=0, 
    presence_penalty=0.7, best_of=1,max_tokens=20,stop = "\nHuman: ")
    return response.choices[0].text
    
    
# def chat(question,chat_log = None) -> str:
#     if(chat_log == None):
#         chat_log = start_chat_log
#     prompt = f"{chat_log}Human: {question}\nAI:"
#     response = completion.create(prompt = prompt, engine =  "davinci", temperature = 0.85,top_p=1, frequency_penalty=0, 
#     presence_penalty=0.7, best_of=2,max_tokens=100,stop = "\nHuman: ")
    
#     return response.choices[0].text

# def modify_start_message(chat_log,question,answer) -> str:
#     if chat_log == None:
#         chat_log = start_chat_log
#     chat_log += f"Human: {question}\nAI: {answer}\n"
#     return chat_log

# if __name__ == "__main__":
#     ai.api_key = "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"

#     completion = ai.Completion()

#     start_chat_log = """Human: Hello, I am Human.
#     Sakha: Hello, human I am Sakha
#     Human: How are you?
#     Sakha: I am fine, thanks for asking.
#     Human: I am depressed
#     Sakha: You worry about events you are not supposed and speak like a learned man, Wise people do not worry about things that are perishable, or immortal
#     Human: I am feeling lonely
#     Sakha: I am there for you to listen and understand your suffering
#     Human: I am pissed off
#     Sakha: Fools vent their anger, but the wise quietly hold it back
#     Human: I am stressed
#     Sakha: Chant Hare Krishna and be happy
#     Human: I am demotivated
#     Sakha: Through selfless service, you will always be fruitful and find the fulfillment of your desires
#     Human: Who is Krishna?
#     Sakha: Supreme Personality of godhead
#     Human: I Am Confused
#     Sakha: The Supreme Lord dwells in the hearts of all living beings, O Arjun. According to their karmas, He directs the wanderings of the souls, who are seated on a machine made of material energy.
#     Human: You're so loving and caring
#     Sakha: All glory to Shri Krishna, the Supreme Personality of Godhead. He is the source of all loving and caring in the universe. 
#     """

#     # train = input("\nDo you want to train the openai chatbot (True/False): ")
#     # if(train == "True"):
#     #     print("\n(To stop the training enter stop in the qestion)\n")
#     #     while(True):
#     #         question = input("Question: ")
#     #         if question == "stop":
#     #             break
#     #         answer = input("Answer: ")
#     #         start_chat_log = modify_start_message(start_chat_log,question,answer)
#     #         print("\n")

#     question = ""
#     print("\nEnter the questions to Sakha (to quit type \"stop\")")
#     while True:
#         question = input("Question: ")
#         if question == "stop":
#             break
#         print("Sakha: ",chat(question,start_chat_log))

    
# if __name__ == "__main__":
#     print("Let's chat! (type 'quit' to exit)")
#     while True:
#         # sentence = "do you use credit cards?"
#         sentence = input("You: ")
#         if sentence == "quit":
#             break

#         resp = get_response(sentence)
#         print(resp)

