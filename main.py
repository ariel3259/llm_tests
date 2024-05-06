from questions import (get_questions, make_question)
from datasets import Dataset
from dotenv import (load_dotenv, find_dotenv)
from metrics import make_metrics
from upload_metrics import upload_metrics


load_dotenv(find_dotenv(), override=True)

#Get Questions from solr
questions, ground_truth = get_questions()

#Check length
print(len(questions))

#Get the inference model results from those questions
res = [make_question(x) for x in questions]
#answers = [x[0] for x in res]
contexts = [x[1] for x in res]

#Check answers length
#print(len(answers))
#Check context length
print(len(contexts))
datasets = []

chunks = 5
for i in range(0, len(questions), chunks):
    data = {
        "question": questions[i:i+chunks],
        #"answer": answers[i:i+chunks],
        "contexts": contexts[i:i+chunks],
        "ground_truth": ground_truth[i:i+chunks]
    }
    dataset = Dataset.from_dict(data)
    datasets.append(dataset)

raw_metrics = make_metrics(datasets)
config_detail= {
        "dataset": "legislation-qa-01",
        "question_quantity":  len(raw_metrics),
        "name": "detail",
        "llm_model": "Mixtral-8x7B-Instruct-v0.1",
        "embedding_moddel": "text-embedding-3-large",
        "manual_metadata_on": True,
        "rag_on": False,
        "context_database": "chromadb"
    }
metrics = [{
        "answer_correctness": x["answer_correctness"],
        "context_utilization": x["context_utilization"],
        "answer_relevancy": x["answer_relevancy"],
        "faithfulness": x["faithfulness"],
        "context_precision": x["context_precision"],
        "context_recall": x["context_recall"],
        "answer_similarity": x["answer_similarity"]
    } for x in raw_metrics]
upload_metrics(metrics=metrics, config=config_detail)

avg = {
    "answer_correctness": 0,
    "context_utilization": 0,
    "answer_relevancy": 0,
    "faithfulness": 0,
    "context_precision": 0,
    "context_recall": 0,
    "answer_similarity": 0
}
for raw_metric in raw_metrics:
    avg["answer_correctness"] = avg["answer_correctness"] + raw_metric["answer_correctness"] if raw_metric["answer_correctness"] is not None else avg["answer_correctness"] + 0
    avg["answer_relevancy"] = avg["answer_relevancy"] + raw_metric["answer_relevancy"] if raw_metric["answer_relevancy"] is not None else avg["answer_relevancy"] + 0
    avg["answer_similarity"] = avg["answer_similarity"] + raw_metric["answer_similarity"] if raw_metric["answer_similarity"] is not None else avg["answer_similarity"] + 0
    avg["context_precision"] = avg["context_precision"] + raw_metric["context_precision"] if raw_metric["context_precision"] is not None else avg["context_precision"] + 0
    avg["context_recall"] = avg["context_recall"] + raw_metric["context_recall"] if raw_metric["context_recall"] is not None else avg["context_recall"] + 0
    avg["context_utilization"] = avg["context_utilization"] + raw_metric["context_utilization"] if raw_metric["context_utilization"] is not None else avg["context_utilization"] + 0
    avg["faithfulness"] = avg["faithfulness"] + raw_metric["faithfulness"] if raw_metric["faithfulness"] is not None else avg["faithfulness"] + 0

config_avg= {
        "dataset": "legislation-qa-01",
        "question_quantity":  1,
        "name": "avg",
        "llm_model": "Mixtral-8x7B-Instruct-v0.1",
        "embedding_moddel": "text-embedding-3-large",
        "manual_metadata_on": True,
        "rag_on": False,
        "context_database": "memorytext"
    }
upload_metrics(metrics=[avg], config=config_avg)