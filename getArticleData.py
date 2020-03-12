import http.client
import mimetypes
import json

def getArticleData(articleNumber):
    articleNumber = str(articleNumber)
    conn = http.client.HTTPSConnection("www.galaxus.ch")
    payload = "{\"query\":\"query GET_INCREMENTAL_SEARCH_RESULT($query: String!) { incrementalSearch(query: $query) { searchResults { Suggestion { total results { name id } } ProductType { total results { id name } } Product { total results { name currency price insteadOfPrice id imageSource } } } } }\",\"variables\":{\"query\":\"" + articleNumber + "\"}}"
    headers = {
    'Content-Type': 'application/json'
    }
    conn.request("POST", "/api/graphql", payload, headers)
    res = conn.getresponse()
    data = res.read()
    data = json.loads(data)

    data = data['data']['incrementalSearch']['searchResults']['Product']
    if (type(data) is not dict or len(data) != 2):
        raise ValueError('Article with number ' + articleNumber + ' not found.')
    data = data['results']
    if (len(data) != 1):
        raise ValueError('No unique article with number ' + articleNumber + ' not found.')
    return data[0]