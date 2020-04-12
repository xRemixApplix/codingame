n = int(input())
temp_list = []
for i in input().split():
    t = int(i)
    temp_list.append(t)
    
temp = 99999999
if len(temp_list) > 0 :
    for element in temp_list :
        if abs(element) < abs(temp) or (abs(element) == abs(temp) and (element-0)>0): temp = element
else :
    temp = 0

print(temp)