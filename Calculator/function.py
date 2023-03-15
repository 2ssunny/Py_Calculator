#합성함수, 역함수, 유리함수, 무리함수
# input: 선택, 합성(함수 2개 입력. 각각 필요 요소), 역(함수 1개 입력. 필요 요소),
# 유리(함수 1개 입력. 필요 요소), 무리(함수 1개 입력. 필요 요소)

TOF=False

def composition_select(): #합성함수 선택
    choice1=int(input("\n1차함수+1차함수는 1, 1차함수+2차함수는 2, 2차함수+2차함수는 3를 입력하세요.\n----> "))
    if choice1 == 1:
        composition_1()
    elif choice1 == 2:
        composition_2()
    # elif choice1 == 3:
    #     composition_3()
    else:
        print("\n잘못된 입력입니다. 다시 입력해 주세요.")

def composition_1(): #1차함수+1차함수
    #f(x)= ax+b g(x)= cx+d
    a,b = map(int, input("\n1차함수 f(x)=ax+b의 기울기와 y절편을 띄어쓰기로 구분해 입력하세요.\n----> ").split())
    c,d = map(int, input("\n1차함수 g(x)=cx+d의 기울기와 y절편을 띄어쓰기로 구분해 입력하세요.\n----> ").split())
    fog_x= a*c
    fog_int=a*d+b
    gof_x= c*a
    gof_int= c*b+d
    print("\n\nfog(x)=",fog_x,'x+',fog_int)
    print("\ngof(x)=",gof_x,'x+',gof_int)

def composition_2(): # 1차함수+2차함수
    # f(x)= ax+b g(x)= cx^2+dx+e
    a,b = map(int, input("\n1차함수 f(x)=ax+b의 기울기와 y절편을 띄어쓰기로 구분해 입력하세요.\n----> ").split())
    c,d,e = map(int, input("\n2차함수 g(x)=cx^2+dx+e의 x^2의 계수와 x의 계수와 상수항을 띄어쓰기로 구분해 입력하세요.\n----> ").split())
    
    fog_2x= a*c
    fog_x=a*d
    fog_int=a*e+b

    gof_2x= c*a
    gof_x=c*b*d
    gof_int=c*b*e
    print("\n\nfog(x)=",fog_2x,'x^2+',fog_x,'x+',fog_int)
    print("\ngof(x)=",gof_2x,'x^2+',gof_x,'x+',gof_int)

def composition_3(): # 2차함수+2차함수
    # f(x)= ax^2+bx+c g(x)= dx^2+ex+f
    a,b,c = map(int, input("\n2차함수 f(x)=ax^2+bx+c의 x^2의 계수와 x의 계수와 상수항을 띄어쓰기로 구분해 입력하세요.\n----> ").split())
    d,e,f = map(int, input("\n2차함수 g(x)=dx^2+ex+f의 x^2의 계수와 x의 계수와 상수항을 띄어쓰기로 구분해 입력하세요.\n----> ").split())
    
    fog_4x = a * d
    fog_3x=(a * e + b * d)
    fog_2x=(a * f + b * e + c * d)
    fog_x=( b * f+c * e)
    fog=c*f
    
    gof_4x= d*a
    gof_3x=d*b+e*a
    gof_2x=d*c+e*b+f*a
    gof_x=e*c+f*b
    gof=f*c
    
    print("\n\nfog(x)=",fog_4x,'x^4+',fog_3x,'x^3+',fog_2x,'x^2+',fog_x,'x+',fog)
    print("\ngof(x)=",gof_4x,'x^4+',gof_3x,'x^3+',gof_2x,'x^2+',gof_x,'x+',gof)


def inverse(): #1차함수의 역함수
    a,b = map(int, input("\n1차함수 f(x)=ax+b의 기울기와 y절편을 띄어쓰기로 구분해 입력하세요.\n----> ").split())
    inverse_1 = 1/a
    inverse_2 =-1*b/a
    print("\n\nf^-1(x)=",inverse_1,'x+',inverse_2)


def rational(): #유리함수
    a,b,c,d = map(int, input("\n유리함수 f(x)=ax+b/cx+d의 분자의 x의 계수와 상수항, 분모의 x의 계수와 상수항을 띄어쓰기로 구분해 입력하세요.\n----> ").split())
    x_lim=-1*c/d
    y_lim=a/c
    y_intercept=b/d
    print("\n\n유리함수의 점근선은 x=",x_lim,",",y_lim,"이며 x=0일때 y=",y_intercept,"입니다.")

def irrational(): #무리함수
    a,b,c,d = map(int, input("\n무리함수 f(x)=)a√(bx+c)+d의 a, b, c, d 값을 띄어쓰기로 구분해 입력하세요.\n----> ").split())
    point_x= -1*c/b
    point_y= d
    way=["오른쪽 위", "오른쪽 아래", "왼쪽 위", "왼쪽 아래"]
    if a>0:
        if b>0:
            way_print=way[0]
        else:
            way_print=way[2]
    else:
        if b>0:
            way_print=way[1]
        else:
            way_print=way[3]
    print("\n\n무리함수의 꼭짓점은 (",point_x,",",point_y,")이며, 방향은", way_print,"입니다.")

def run():
    global TOF
    while TOF==False:
        try:
            choice=int(input("\n합성함수는 1, 역함수는 2, 유리함수는 3, 무리함수는 4를, 종료하려면 9를 입력하세요.\n----> "))
            if choice == 1:
                composition_select()
            elif choice == 2:
                inverse()
            elif choice == 3:
                rational()
            elif choice == 4:
                irrational()
            elif choice == 9:
                TOF = True
            else:
                print("\n잘못된 입력입니다. 다시 입력해 주세요.")
        except :
            print("\n잘못된 입력입니다. 다시 입력해 주세요.")
    TOF= False