import turtle as t
def plotN(Len, N):
    t.circle(-Len, 300,N)

t.rt(90)
t.color('black')
t.penup()
t.goto(150,0)
t.pendown()

for i in range(3,23):
    plotN(150,i)

t.color('green','green')
# for i in range(42,2,-1):
#     plotN(150,i)

# t.color('black','black')

plotN(150,100)

