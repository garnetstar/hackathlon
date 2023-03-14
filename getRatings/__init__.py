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
        raiting_dict = {"id": rating[0]['id'],"userId": rating[0]['userId'],"productId": rating[0]['productId'],"timestamp": rating[0]['timestamp'],"locationName": rating[0]['locationName'],"rating": rating[0]['rating'],"userNotes": rating[0]['userNotes'] }
        rating_list.append(raiting_dict)

    return func.HttpResponse(
 #       rating_list,
        status_code=200
    )



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
    
