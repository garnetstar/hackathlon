import logging
import azure.functions as func
import json

def main(req: func.HttpRequest, documents: func.DocumentList) -> str:
    if not documents:
        logging.warning("Rating id not found")
    else:
        logging.info("Found rating ID, full rating=%s",
                     documents[0])
        raiting_dict = {"id": documents[0]['id'],"userId": documents[0]['userId'] }
        raiting_json = json.dumps(raiting_dict)
    return raiting_json