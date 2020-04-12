message = input()

answer = item = ""
i = 0

while i < len(message) :
    ascii_elt = format(ord(message[i]), "b")
    
    j = 0
    
    while len(ascii_elt) < 7 : ascii_elt = "0" + ascii_elt
        
    while j < len(ascii_elt) :
        if item == "" :
            answer += "0 0" if ascii_elt[j] == "1" else "00 0"
            item = ascii_elt[j]
        elif item != ascii_elt[j]:
            answer += " 0 0" if ascii_elt[j] == "1" else " 00 0"
            item = ascii_elt[j]
        else :
            answer += "0"

        item = ascii_elt[j]    
        j += 1
    i += 1

print(answer)