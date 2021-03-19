import sys, os

name = sys.platform

for i in range (1,6):
    newPath = os.path.join(os.getcwd(),f'{name}_{i}')
    os.mkdir(newPath)