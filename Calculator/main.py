import circle
import move
import set
import function
import probability
choice = 0
TOF = False
while not TOF:
    choice = int(input("\n원과 직선의 관계는 1, 이동은 2, 집합은 3, 다양한 종류의 함수는 4, 경우의 수는 5, 종료는 9를 입력하세요.\n----> "))
    if choice == 1:
        circle.run()

    elif choice == 2:
        move.run()

    elif choice == 3:
        set.run()

    elif choice == 4:
        function.run()

    elif choice == 5:
        probability.run()

    elif choice == 9:
        TOF = True

    else:
        print("잘못된 입력입니다. 다시 입력해 주세요.")

print("프로그램을 종료합니다.")