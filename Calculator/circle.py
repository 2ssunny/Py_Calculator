TOF=False
a=False

def stline(): # 직선의 방정식
    global a
    global liney, m
    while a==False:
        m=input("\n직선의 기울기를 입력하세요.\n----> ")
        m=int(m)
        lx, ly=map(int,input("직선이 지나가는 한 점의 x좌표와 y좌표를 띄어쓰기로 구분해 입력하세요. : ").split())
        liney = ly - (m * lx)

        circle()


def circle(): #원의 방정식
    global a
    global cx, cy, cr
    while a==False:
        cx, cy=map(int,input("원의 중심의 x좌표와 y좌표를 띄어쓰기로 구분해 입력하세요.\n----> ").split())
        cr=int(input("원의 반지름을 입력하세요. : "))
        calcD()


def calcD(): # 판별식D 계산
    global liney, m
    global cx, cy, cr
    global xa, xb, ya,yb
    global num

    lineycy = liney - cy
    A = m * m + 1
    B = m * lineycy - cx # x항 1/2=>2B로 계산해서 x항
    C = cx * cx + lineycy * lineycy - cr * cr
    D = 4 * B * B - 4 * A * C
    rootD = D**(1/2)

    xa = (-2 * B + rootD) / (2 * A)
    xb = (-2 * B - rootD) / (2 * A)
    ya = m * xa + liney
    yb = m * xb + liney

    if liney >= 0:
        print("\n\n직선의 방정식:\n y=",m,"+",liney)
    if liney < 0:
        print("\n\n직선의 방정식:\n y=",m,"+",liney)

    print("\n원의 방정식:\n(x-",cx,")²+(y-",cy,")²=",cr*cr)

    print("\n판별식 D=",D) # Output D

    if D == 0: # D=0 -> 교점이 1개
        num = 1

    if D > 0: # D>0 -> 교점이 2개
        num = 2

    if D < 0: # D<0 ->교점이 0개
        num = 0

    summary()


def summary(): # 결과 출력
    global a
    global xa, xb, ya,yb
    global num

    while a==False:
        print("\n교점이 ",num,"개 입니다.")
        if num == 1: # 교점 1개
            print("\n교점1 (",xa,",",ya,")")

        if num == 2: # 교점 2개

            print("\n교점1 (",xa,",",ya,")\n교점2 (",xb,",",yb,")\n")
        check=int(input("계속하려면 1을, 종료하려면 9를 입력하세요.\n----> "))
        if check==1:
            stline()
        if check==9:
            a=True


def run():
    global TOF
    global a
    while not TOF:
        try:
            choice=int(input("\n계산하려면 1, 종료하려면 9를 입력하세요.\n---->  "))
            if choice==1:
                a=False
                stline()
            elif choice==9:
                TOF=True
            else:
                print("잘못된 입력입니다.")
        except :
            print("잘못된 입력입니다.")
    TOF=False
