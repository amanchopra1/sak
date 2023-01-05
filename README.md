# Sakha || NLTK & GPT 3 Conversational Chatbot

 Development of a conversational Chatbot which provides to be a friend who listens and gives solutions to one's problems related to mental health, lifestyle, and goals of life concerning the ultimate guide Bhagavad Gita 
 
Deployed at Digital Ocean https://sakha.chat

In this project we have used NLTK, GPT3 and AI to give solution to every life problem's solution.

Read Design and Implementation of Sakha to understand the working of this project: https://drive.google.com/file/d/14ounQHekbmhJEz2P5bnFEi9PXZhH4f57/view?usp=sharing

This gives 2 deployment options:
- Deploy within Flask app with jinja2 template
- Serve only the Flask prediction API. The used html and javascript files can be included in any Frontend application (with only a slight modification) and can run completely separate from the Flask App then.

## Initial Setup:
This repo currently contains all the files and the basic dataset of (Bhagavad Gita) which provides the ultimate guidance for life

The below commands are for Unix/Linux System

Clone repo and create a virtual environment

Get your api key for gpt-3 (46th line chat.py)
https://beta.openai.com/account/api-keys

```
$ git clone https://github.com/amanchopra1/sak.git
$ cd sak
$ python3 -m venv venv
$ . venv/bin/activate
```
The below commands are for Windows
```
 pip install virtualenv
 virtualenv venv
 venvironment\Scripts\activate
 ```
 import nltk
  ```
 python
>>> import nltk
>>> nltk.download('punkt')
 ```

Install dependencies
```
$ (venv) pip install -r requirements.txt
```
```
Run
```
$ (venv) python train.py
```
This will dump data.pth file. And then run
the following command to test it in the console.

```

$ (venv) python chat.py
$ (venv) python app.py


---------------------------------------------------------------------------------
```
All Glories to Shri Krishna

All Glories to Shrimad Bhagavad Gita

All Glories to Shri Chaitanya Mahaprabhu

All Glories to Srila Prabhupaad

All Glories to all the Vaishnavas and enlightened souls of the universe

Hare Krishna Hare Krishna Krishna Krishna Hare Hare
Hare Raam Hare Raam Raam Raam Hare Hare
```
You can reach us at: 
Aastha Tripathi (https://www.linkedin.com/in/aastha-tripathi-6601641ba/)

Aman Chopra (https://www.linkedin.com/in/amanchopra9/)

Vaibhav Deep Jaiswal (https://www.linkedin.com/in/vaibhav-deep-jaiswal-12ba7b1a5/)

Abhishek Kumar Rai (https://www.linkedin.com/in/abhishek-rai-692397227/)

Yogendra Bhardwaj (https://www.linkedin.com/in/bh-yogendra/)


----------------------------------------------------------------------------------------
