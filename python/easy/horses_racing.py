ecart = 10000000
tab_pi = []

n = int(input())
for i in range(n): tab_pi.append(int(input()))

tab_pi = sorted(tab_pi)

for i in range(len(tab_pi)-1): 
    if abs(tab_pi[i] - tab_pi[i+1]) < ecart: ecart = abs(tab_pi[i] - tab_pi[i+1])
    
print(ecart)