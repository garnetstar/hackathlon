import logging
import requests
import uuid
import json
from datetime import datetime
import azure.functions as func


# {
#   "userId": "cc20a6fb-a91f-4192-874d-132493685376",
#   "productId": "4c25613a-a3c2-4ef3-8e02-9c335eb23204",
#   "locationName": "Sample ice cream shop",
#   "rating": 5,
#   "userNotes": "I love the subtle notes of orange in this ice cream!"
# }

# def main(req: func.HttpRequest, doc: func.Out[func.Document]) -> func.HttpResponse:
#     request_body = req.get_body()
#     doc.set(func.Document.from_json(request_body))
#     return 'OK'


def validate_item(item_type, id):
    r = requests.get(url="https://serverlessohapi.azurewebsites.net/api/Get{0}?{1}Id={2}".format(item_type.capitalize(), item_type, id), timeout=5)
    logging.info("Validate item response code: %s", r.status_code)
    return r.status_code == 200

def validate_rating(rating):
    try:
        id_int = isinstance(rating["rating"], int)
        logging.warning("ID: %s", id_int)
        product = validate_item("product", rating["productId"])
        logging.warning("Product: %s", product)
        user = validate_item("user", rating["userId"])
        logging.warning("User: %s", user)
        return all([id_int, product, user])
    except KeyError:
        logging.error("Check if rating is an integer and if productId and userId exists.")
        return False

def main(req: func.HttpRequest, doc: func.Out[func.Document]) -> func.HttpResponse:
    logging.info('Python HTTP trigger function processed a request.')

    try:
        rating = req.get_json()
    except ValueError:
        return func.HttpResponse("Invalid input", status_code=400)

    if validate_rating(rating):
        rating["id"] = f"{uuid.uuid4()}"
        rating["timestamp"] = f"{datetime.utcnow()}"
        logging.warn("req body2: %s", rating)
        try:
            doc.set(func.Document.from_json(json.dumps(rating)))
        except Exception as ex:
            return func.HttpResponse(f"Could not insert data into database. Error: {ex}", status_code=500)        
    else:
        return func.HttpResponse("Input data not complete.", status_code=400)

    return func.HttpResponse("Done processing", status_code=200)
