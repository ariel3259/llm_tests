import wandb
import json
from incremental_id import get_incremental_name

def upload_metrics(metrics: list[dict], config: dict):
    raw_name = config["llm_model"] + "-" + config["context_database"] + config["embedding_moddel"] + "-" + config["name"] 
    name = get_incremental_name(raw_name)
    wandb.init(
        project="chatbot-legislación-metrics",
        name=name,
        config= config
    )
    for x in metrics:
        wandb.log(x)
    wandb.finish()