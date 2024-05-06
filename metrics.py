import pandas as pd
from datasets import Dataset
from ragas.metrics import (answer_correctness, context_utilization, answer_relevancy, answer_similarity, faithfulness, context_precision, context_recall)
from ragas import evaluate
from langchain_openai import ChatOpenAI
import time


def make_metrics(datasets: list[Dataset])-> pd.DataFrame:
    dataframe: pd.DataFrame = None
    #llm = ChatOpenAI(model_name="gpt-3.5-turbo-0125")
    for x in datasets:
        result = evaluate(
            #llm=llm,
            raise_exceptions=False,
            dataset=x,
            metrics=[
                answer_correctness,
                context_utilization,
                answer_relevancy,
                faithfulness,
                context_precision,
                context_recall,
                answer_similarity
            ]
        )       
        df = result.to_pandas()
        if dataframe is None:
            dataframe = df
        else:
            dataframe = pd.concat([dataframe, pd.DataFrame(df)], ignore_index=True)
        print("Sleeping for 30 seconds")
        time.sleep(50)
    return dataframe.to_dict('records')
