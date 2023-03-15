#순열, 계승, 조합- input: 선택. P, C, ! 각각 필요요소 입력. output: 결과값 출력

TOF=False

def permutation():
    result=0
    out=0
    a,b=map(int, input("\n순열(aPb)의 a와 b를 입력하세요. ex) 5P3:5 3\n----> ").split())
    list=[]
    for i in (a, -1, -1):
        try:
            for j in (1, b+1):
                list[j]=i
                j+=1
        except:
            print("오류가 발생했거나 계산이 불가능합니다.")
            pass
            
    for h in (1, b+1):
        result+=list[h]
        h+=1

    for k in (1, a+1) :
        out+=k
        k+=1

    result=result/out
    print("\n\n순열(aPb)의 결과는",result,"입니다.")


def combination():
    result=0
    a,b=input("\n조합(aCb)의 a와 b를 입력하세요. ex) 5C3:5 3\n----> ").split()
    a=float(a)
    b=float(b)
    list=[]
    for i in (a, 0, -1):
        list[i]=i
    for j in range(1, b+1) :
        result+=list[j]
        j+=1
    print("\n\n조합(aCb)의 결과는",result,"입니다.")


def factorial():
    result=0
    a=input("\n계승(a!)의 a를 입력하세요. ex) 5!:5\n----> ")
    a=float(a)
    list=[]
    for i in (a, 0, -1):
        list[i]=i
    for k in (1, a+1) :
        result+=list[k]
        k+=1
    print("\n\n계승(a!)의 결과는",result,"입니다.")


def run():
    global TOF
    while not TOF:
        try:
            choice = int(input("\n순열(aPb)은 1, 계승(a!)은 2, 조합(aCb)은 3, 종료는 9를 입력하세요.\n----> "))
            if choice == 1:
                permutation()
            elif choice == 2:
                factorial()
            elif choice == 3:
                combination()
            elif choice == 9:
                TOF = True
            else:
                print("\n잘못된 입력입니다. 다시 입력해 주세요.")
        except:
            print("\n잘못된 입력입니다. 다시 입력해 주세요.")
    TOF=False