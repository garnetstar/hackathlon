import logging
import requests
import json
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
    logging.info("Validate item response code: {}".format(r.status_code))
    return r.status_code == 200

def validate_rating(rating):
    try:
        id_int = isinstance(rating["rating"], int)
        logging.warning("ID: {}".format(id_int))
        product = validate_item("product", rating["productId"])
        logging.warning("Product: {}".format(product))
        user = validate_item("user", rating["userId"])
        logging.warning("User: {}".format(user))
        return all([id_int, product, user])
    except KeyError:
        logging.error("Check if rating is an integer and if productId and userId exists.")
        return False

def main(req: func.HttpRequest) -> func.HttpResponse:
    logging.info('Python HTTP trigger function processed a request.')

    try:
        rating = req.get_json()
    except ValueError:
        return func.HttpResponse("Invalid input", status_code=400)

    if not validate_rating(rating):
        return func.HttpResponse("Input data not complete.", status_code=400)

    return func.HttpResponse("Done processing", status_code=200)
