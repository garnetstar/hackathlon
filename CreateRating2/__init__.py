import logging
import requests
import json
import azure.functions as func


def main(req: func.HttpRequest, doc: func.Out[func.Document]) -> func.HttpResponse:
    logging.info('Python HTTP trigger function processed a request.')

    try:
        rating = req.get_json()
    except ValueError:
        return func.HttpResponse("Invalid input", status_code=400)

    request_body = req.get_body()
    doc.set(func.Document.from_json(request_body))

    return func.HttpResponse("Done processing", status_code=200)
