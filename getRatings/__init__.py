import logging

import azure.functions as func

def get_ratings(ratings: func.DocumentList) -> str:
    if not ratings:
        logging.warning("Rating items not found")
    else:
        logging.info("Found rating items %s", len(ratings))
    return ratings


def main(req: func.HttpRequest, ratings: func.DocumentList) -> func.HttpResponse:
    logging.info('Python HTTP trigger function processed a request.')
    userId = req.params.get('userid')
    if not userId:
        try:
            req_body = req.get_json()
        except ValueError:
            pass
        else:
            userId = req_body.get('userid')

    if userId:
       ratings = get_ratings(ratings)

       return func.HttpResponse(
             status_code=200
        )
    else:
        return func.HttpResponse(
             status_code=404
        )
    
