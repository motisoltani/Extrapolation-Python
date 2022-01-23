'''
Interpolation and Curve Fitting                                %
Extrapolation 
language: Python

Motahare Soltani
soltani.wse@gmail.com

'''

#Entering X and Y values
x = [0, 4, 8, 15]
y = [0, 9.1, 25, 31]

#xe = [0.25+i for i in range(5,7)]
xe = [-1.75]
ye = []

n = len(xe)

for i in range(n):
    if xe[i] < x[0]:
        f = y[0] + (xe[i] - x[0]) / (x[1] - x[0]) * (y[1] - y[0])
        ye.append(f)   
    else:
        f = y[-2] + (xe[i] - x[-2]) / (x[-1] - x[-2]) * (y[-1] - y[-2])
        ye.append(f)

print(ye)