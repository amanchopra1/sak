import random
import json
import openai as ai
import torch
from gpt3 import *
import os

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
def chat(question,chat_log = None) -> str:
    if(chat_log == None):
        chat_log = start_chat_log
    prompt = f"{chat_log} {question}\n"
    response = completion.create(prompt = prompt, engine =  "davinci", temperature = 0.85,top_p=1, frequency_penalty=0, 
    presence_penalty=0.7, best_of=2,max_tokens=64,stop = "\n ")
    return response.choices[0].text

def modify_start_message(chat_log,question,answer) -> str:
    if chat_log == None:
        chat_log = start_chat_log
    chat_log += f" {question}\n: {answer}\n"
    return chat_log


ai.api_key = os.environ['openai_api_key']

completion = ai.Completion()

start_chat_log = """ Hello, I am Human.
 Hello, human I am Sakha
 How are you?
 I am fine, thanks for asking.
 I am depressed
 You worry about events you are not supposed and speak like a learned man, Wise people do not worry about things that are perishable, or immortal
 I am feeling lonely
 I am there for you to listen and understand your suffering
 I am pissed off
 Fools vent their anger, but the wise quietly hold it back
  I am stressed
 Chant Hare Krishna and be happy
 I am demotivated
 Through selfless service, you will always be fruitful and find the fulfillment of your desires
Who is Krishna?
 Supreme Personality of godhead
 I Am Confused
 The Supreme Lord dwells in the hearts of all living beings, O Arjun. According to their karmas, He directs the wanderings of the souls, who are seated on a machine made of material energy.
 You're so loving and caring
 All glory to Shri Krishna, the Supreme Personality of Godhead. He is the source of all loving and caring in the universe. 
"""

def get_response(msg, chat_log = None):
    sentence = tokenize(msg)
    X = bag_of_words(sentence, all_words)
    X = X.reshape(1, X.shape[0])
    X = torch.from_numpy(X).to(device)
    
    output = model(X)
    _, predicted = torch.max(output, dim=1)

    tag = tags[predicted.item()]
    question = ""
    probs = torch.softmax(output, dim=1)
    prob = probs[0][predicted.item()]
    if prob.item() > 0.75:
        for intent in intents['intents']:
            if tag == intent["tag"]:
                return random.choice(intent['responses'])
  
    
    while True:
        question = msg
        if question == "stop":
            break
        return(chat(question,start_chat_log))
