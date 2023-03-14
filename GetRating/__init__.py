import logging
import azure.functions as func

def main(req: func.HttpRequest, rating: func.DocumentList) -> str:
    if not rating:
        logging.warning("Rating id not found")
    else:
        logging.info("Found rating ID, full rating=%s",
                     rating[0])
    return 'OK'