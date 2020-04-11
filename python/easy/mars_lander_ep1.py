surface_n = int(input())

for i in range(surface_n): land_x, land_y = [int(j) for j in input().split()]


while True:
    x, y, h_speed, v_speed, fuel, rotate, power = [int(i) for i in input().split()]

    if v_speed > -40 and power > 0 : power -= 1
        
    if v_speed < - 40 and power < 4: power += 1
    
    print("0 {}".format(power))