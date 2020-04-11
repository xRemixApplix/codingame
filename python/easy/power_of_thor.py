light_x, light_y, posX, posY = [int(i) for i in input().split()]

while True:
    remaining_turns = int(input())

    moveY = "N" if posY>light_y else "S" if posY<light_y else ""
    if posY > light_y :
        posY -= 1
    elif posY < light_y :
        posY += 1
        
    moveX = "W" if posX>light_x else "E" if posX<light_x else ""
    if posX > light_x :
        posX -= 1
    elif posX < light_x :
        posX += 1

    print(moveY + moveX)
    
    