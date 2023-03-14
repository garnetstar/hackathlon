import logging

import azure.functions as func

#def get_ratings(ratings: func.DocumentList) -> object:
#    if not ratings:
#        logging.warning("Rating items not found")
#    else:
#        logging.info("Found rating items %s", len(ratings))
#    return ratings


def main(req: func.HttpRequest, ratings: func.DocumentList) -> func.HttpResponse:
    logging.info('Python HTTP trigger function processed a request.')
    userId = req.params.get('userid')
   
    rating_list = []

    for rating in ratings:
        raiting_dict = {"id": rating['id'],"userId": rating['userId'],"productId": rating['productId'],"timestamp": rating['timestamp'],"locationName": rating['locationName'],"rating": rating['rating'],"userNotes": rating['userNotes'] }
        rating_list.append(raiting_dict)

    return rating_list



#    if not userId:
#        try:
#            req_body = req.get_json()
#        except ValueError:
#            pass
#        else:
#            userId = req_body.get('userid')

#    if userId:
#       return func.HttpResponse(
#             status_code=200
#        )
#    else:
#        return func.HttpResponse(
#             status_code=404
#        )
    
