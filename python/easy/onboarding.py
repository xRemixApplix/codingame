while 1:
    enemy_1, dist_1 = input(), int(input())
    enemy_2, dist_2 = input(), int(input())
    
    print(enemy_1 if dist_1<dist_2 else enemy_2)