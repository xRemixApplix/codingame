import sys
import math

lon = input().replace(",", ".")
lat = input().replace(",", ".")
n = int(input())

list_defib = []
dist = 6371

for i in range(n):
    defib = input()
    defib = defib.split(";")
    
    lonA = defib[4].replace(",", ".")
    latA = defib[5].replace(",", ".")
    
    x = math.radians(float(lon) - float(lonA)) * (math.cos(math.radians(float(lat)+float(latA))/2))
    y = math.radians(float(lat) - float(latA))
    
    d = math.sqrt(x**2 + y**2) * 6371
    
    if d < dist :
        nom = defib[1]
        dist = d

print(nom)