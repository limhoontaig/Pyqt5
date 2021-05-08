# E:\source\pyqt5\Bouncing_Ball.py
#height = 0.0
#i=0
height = float(input("input your initial height(meters): "))
for i in range(15):
    
    print (f'{i:>3d} {height:>8.2f}')
    #height = 0.6 * height
    height *= 0.6


