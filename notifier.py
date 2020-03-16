from getArticleData import getArticleData

import yaml

data = []
with open('articles.yaml') as f:
    data = yaml.load(f, Loader=yaml.FullLoader)

for articleNr in data:
    articleNr = str(articleNr)
    try:
        article = getArticleData(articleNr)
    except ValueError as e:
        print('Error: cannot find article #' + articleNr + ': ' + str(e))
        continue
    try:
        amountIncl = article['product']['pricing']['price']['amountIncl']
    except BaseException as e:
        print('Error: cannot get price of article #' + articleNr + ': ' + str(e))
        continue

    amountBefore = amountIncl
    try:
        amountBefore = article['product']['pricing']['insteadOfPrice']['price']['amountIncl']
    except TypeError:
        amountBefore = amountIncl

    discount = amountBefore - amountIncl
    if discount == 0:
        print('Article #' + articleNr + ' has no discount')
        continue

    print('Article #' + articleNr + ' has a discount of ' + str(discount) + ' CHF (' + str(round(discount/amountBefore, 2)*100) + '%)')
