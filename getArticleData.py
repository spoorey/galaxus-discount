import http.client
import json

def getArticleData(articleNumber):
    articleNumber = str(articleNumber)
    conn = http.client.HTTPSConnection("www.galaxus.ch")
    payload = "[{\"operationName\":\"GET_PRODUCT_DETAILS_CRITICAL_DATA_REFETCH\",\"variables\":{\"productId\":" + articleNumber + "},\"extensions\":{\"persistedQuery\":{\"version\":1,\"sha256Hash\":\"515fb14830e389b7bb81a5027dd0b6d44f7d1366fa2ebd5192f2e106be0bb230\"}}}]"
    headers = {
        'content-type': ' application/json'
    }
    conn.request("POST", "/api/graphql", payload, headers)
    res = conn.getresponse()
    data = res.read()
    data = json.loads(data)

    notFoundError = ValueError('Article with number ' + articleNumber + ' not found.')

    try:
        data = data[0]['data']['productDetails']
    except TypeError:
            raise notFoundError
    return data
