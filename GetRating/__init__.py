import logging
import azure.functions as func
import json

def main(req: func.HttpRequest, documents: func.DocumentList) -> str:
    if not documents:
        logging.warning("Rating id not found")
    else:
        logging.info("Found rating ID, full rating=%s",
                     documents[0])
        raiting_dict = {"id": documents[0]['id'],"userId": documents[0]['userId'],"productId": documents[0]['productId'],"timestamp": documents[0]['timestamp'],"locationName": documents[0]['locationName'],"rating": documents[0]['rating'],"userNotes": documents[0]['userNotes'] }
        raiting_json = json.dumps(raiting_dict)
    return raiting_json