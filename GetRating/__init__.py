import logging
import azure.functions as func

def main(req: func.HttpRequest, documents: func.DocumentList) -> str:
    if not documents:
        logging.warning("Rating id not found")
    else:
        logging.info("Found rating ID, full rating=%s",
                     documents[0])
        document = documents[0]
    return document