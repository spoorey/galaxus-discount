from getArticleData import getArticleData


article = getArticleData('10401355')

print(float(article['price']) - float(article['insteadOfPrice']))