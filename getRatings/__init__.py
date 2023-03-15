import logging
import json
import azure.functions as func

def main(req: func.HttpRequest, ratings: func.DocumentList) -> func.HttpResponse:
    logging.info('Python HTTP trigger function processed a request.')
    userId = req.params.get('userId')
   
    rating_list = []

    for rating in ratings:
        raiting_dict = {"id": rating['id'],"userId": rating['userId'],"productId": rating['productId'],"timestamp": rating['timestamp'],"locationName": rating['locationName'],"rating": rating['rating'],"userNotes": rating['userNotes'] }
        rating_list.append(raiting_dict)

    if len(rating_list) > 0:
        return json.dumps(rating_list)
    else:
        return func.HttpResponse(
             "",
             status_code=404
        )