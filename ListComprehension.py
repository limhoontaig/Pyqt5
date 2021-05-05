a = [1,-5, -62,3,4,-45,6,7,8,9,10]
b = [2*x for x in a]
print(b)
c=[2*x for x in a if x <0]
print(c)


stocks = [
    {'name':'a','price':50,'stock':20},
    {'name':'abc','price':700,'stock':25},
    {'name':'ba','price':50,'stock':20},
    {'name':'cba','price':50,'stock':20}
]
stocknames = [s['name'] for s in stocks]
cost = sum([s['price']*s['stock'] for s in stocks])
print(stocknames)
print(cost)