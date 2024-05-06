import requests
from base64 import b64encode
import os

def get_questions():
    user = os.environ.get("USER_SOLR")
    password = os.environ.get("PASSWORD_SOLR")
    url = "https://solr.errepar.com/solr/chatbotLegislacionTestingQA/select?_=1709232052365&indent=true&q=*:*&q.op=OR&rows=1000"
    headers = {
        "Authorization": 'Basic ' + b64encode(f'{user}:{password}'.encode()).decode('utf-8') 
    }
    response = requests.get(url, headers=headers)
    print(response.status_code)
    json = response.json()
    
    docs = json["response"]["docs"]
    ground_truth = [x["answer"] for x in docs]
    questions = [x["question"] for x in docs]
    return (questions, ground_truth)

def make_question(question):
    url = "http://localhost:5000/makeQuestion"
    body = {
    "historial": [
        {
            "role": "user",
            "content": question
        }
    ],
    "requireContext": True
    }
    response = requests.post(url, json=body)
    json = response.json()
    answer = json["message"]
    contexts: list[str] = []
    try:
        contexts = json["contexts"]
    except:
        contexts = []
    return (answer, contexts)
