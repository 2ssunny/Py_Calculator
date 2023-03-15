# 평행이동, 대칭이동- input: 방향별로 얼마나. output: 평행이동(방향별로 얼마나 이동-> (x,y)), 대칭이동(x축, y축, 원점, y=x 대한 대칭이동 각각 (x,y))
TOF=False
a=False

def parallel():
    x_move, y_move=input("\nx방향으로 이동한 정도와 y방향으로 이동할 정도를 띄어쓰기로 구분해 입력하세요.\n----> ").split()
    x_move, y_move=int(x_move),int(y_move)
    print("\n\nx축으로",x_move,"만큼, y축으로",y_move,"만큼 평행이동한 결과:\n(",x+x_move,",",y+y_move,")")


def symmetric():
    print("\n\nx축에 대해 평행이동한 결과: (",x,",",y*-1,")")
    print("\ny축에 대해 평행이동한 결과: (",x*-1,",",y,")")
    print("\n원점에 대해 평행이동한 결과: (",x*-1,",",y*-1,")")
    print("\ny=x에 대해 평행이동한 결과: (",y,",",x,")")

def run():
    global TOF
    while TOF==False:
        try:
            global x, y
            x,y = input("\n점의 x좌표와 y좌표를 띄어쓰기로 구분해 입력하세요. 종료하려면 exit를 2번 입력해 주세요.\n----> ").split()
            if x=="exit" and y=="exit":
                TOF=True
            else:
                x,y=int(x),int(y)

            choice=int(input("\n대칭이동은 1, 평행이동은 2를, 종료하려면 9를 입력하세요.\n----> "))
            if choice==1:
                parallel()
            elif choice==2:
                symmetric()
            elif choice==9:
                TOF=True
            else:
                print("\n잘못된 입력입니다.")
        except :
            print("\n잘못된 입력입니다.")
    TOF=False
