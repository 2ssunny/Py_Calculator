#집합(교,합,여,차)- input: 집합 2개 입력, 선택. output: 각 집합 선택 따른 결과값 출력

TOF=False
a=False
b=False

def intersection(): #교집합
    set_result = set_A.intersection(set_B)
    print("\n\n집합 A와 집합 B의 교집합은",set_result)

def union(): #합집합
    set_result= set_A.union(set_B)
    print("\n\n집합 A와 집합 B의 합집합은", set_result)

def difference(): #차집합
    set_result_A=set()
    set_result_B=set()
    set_result_A=set(set_result_A)
    set_result_B=set(set_result_B)

    set_result_A= set_A.difference(set_B)
    set_result_B= set_B.difference(set_A)
    print("\n\n집합 A에서 집합 B을 뺀 차집합은", set_result_A)
    print("\n\n집합 B에서 집합 A을 뺀 차집합은", set_result_B)

def complement(): #여집합
    set_com_A = set()
    set_com_B = set()

    set_com_A=set_U.difference(set_A)
    set_com_B=set_U.difference(set_B)
    print("\n\n집합 A의 여집합은",set_com_A)
    print("\n\n집합 B의 여집합은",set_com_B)

def choice():
    global b
    b=True
    choice = int(input("\n교집합은 1, 합집합은 2, 차집합은 3, 여집합은 4를 입력하세요.\n----> "))
    if choice == 1:
        intersection()
    elif choice == 2:
        union()
    elif choice == 3:
        difference()
    elif choice == 4:
        complement()
    else:
        print("\n잘못된 입력입니다. 다시 입력해 주세요.")

def run():
    global set_U,set_B, set_A
    global TOF
    global a
    global b

    set_U = set()
    set_A = set()
    set_B = set()

    while TOF==False:
        try:
            if a == False:
                select=int(input("\n계산하려면 1, 종료하려면 9를 입력하세요."))
                if select == 1:
                    a = True
                    run()
                elif select == 9:
                    TOF=True

            if a==True:
                if b==True:
                    print("전체집합 U: ", set_U)
                    print("집합 A: ", set_A)
                    print("집합 B: ", set_B)

                    choice1=int(input("\n\n기존 집합을 재사용하려면 1, 새로운 집합을 입력하려면 2를, 종료하려면 9를 입력하세요.\n----> "))
                    if choice1==1:
                        choice()
                    elif choice1==2:
                        set_U = map(int,input("\n원소들을 띄어쓰기로 구분해 전체집합 U의 원소들을 입력하세요.\n----> ").split())
                        set_A = map(int,input("\n원소들을 띄어쓰기로 구분해 집합 A의 원소들을 입력하세요.\n----> ").split())
                        set_B = map(int,input("\n원소들을 띄어쓰기로 구분해 집합 B의 원소들을 입력하세요.\n----> ").split())

                        set_U=sorted(set_U)
                        set_A=sorted(set_A)
                        set_B=sorted(set_B)

                        set_U=set(set_U)
                        set_A= set(set_A)
                        set_B= set(set_B)
                        choice()
                    elif choice1==9:
                        TOF=True

                elif b==False:
                    set_U = map(int,input("\n원소들을 띄어쓰기로 구분해 전체집합 U의 원소들을 입력하세요.\n----> ").split())
                    set_A = map(int,input("\n원소들을 띄어쓰기로 구분해 집합 A의 원소들을 입력하세요.\n----> ").split())
                    set_B = map(int,input("\n원소들을 띄어쓰기로 구분해 집합 B의 원소들을 입력하세요.\n----> ").split())

                    set_U=sorted(set_U)
                    set_A=sorted(set_A)
                    set_B=sorted(set_B)

                    set_U=set(set_U)
                    set_A= set(set_A)
                    set_B= set(set_B)
                    choice()
        except :
            print("\n잘못된 입력입니다. 다시 입력해 주세요.")
    TOF = False