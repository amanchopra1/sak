import openai as ai

def chat(question,chat_log = None) -> str:
    if(chat_log == None):
        chat_log = start_chat_log
    prompt = f"{chat_log}Human: {question}\nAI:"
    response = completion.create(prompt = prompt, engine =  "davinci", temperature = 0.85,top_p=1, frequency_penalty=0, 
    presence_penalty=0.7, best_of=2,max_tokens=100,stop = "\nHuman: ")
    return response.choices[0].text

def modify_start_message(chat_log,question,answer) -> str:
    if chat_log == None:
        chat_log = start_chat_log
    chat_log += f"Human: {question}\nAI: {answer}\n"
    return chat_log

if __name__ == "__main__":
    ai.api_key = "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"

    completion = ai.Completion()

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

    # train = input("\nDo you want to train the openai chatbot (True/False): ")
    # if(train == "True"):
    #     print("\n(To stop the training enter stop in the qestion)\n")
    #     while(True):
    #         question = input("Question: ")
    #         if question == "stop":
    #             break
    #         answer = input("Answer: ")
    #         start_chat_log = modify_start_message(start_chat_log,question,answer)
    #         print("\n")

    question = ""
    print("\nEnter the questions to Sakha (to quit type \"stop\")")
    while True:
        question = input("Question: ")
        if question == "stop":
            break
        print("Sakha: ",chat(question,start_chat_log))
