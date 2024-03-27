import math

def answer(a,b,c):
    D = b**2 - (4*a*c)

    # 근이 2개일 때
    if(D>0):
        x1 = (-b + math.sqrt(D)) / (2*a)
        x2 = (-b - math.sqrt(D)) / (2*a)

        print(x1)
        print(x2)

    # 중근을 가질 때
    elif(D == 0):
        x = - b / 2 * a
        
        print(x)
        print("중근을 갖습니다.")

    # 근이 없을 때
    else:
        print("근이 존재하지 않습니다.")
