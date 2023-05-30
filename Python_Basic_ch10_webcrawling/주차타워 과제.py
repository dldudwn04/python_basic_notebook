
slot = 5
tower = [None] * slot

print("■" * 50)
print("■■ == 주차타워 ==")
print("■" * 50)
print("■ 메인 기능")
while True:
    print("1. 차량 입고")
    print("2. 차량 출고")
    print("3. 차량 입고 정보")
    print("4. 프로그램 종료")

    choice = int(input("메인 기능을 선택하세요 (1~4): "))

    if choice == 1:
        num = input("입고 차량 번호를 입력하세요: ")
        if None in tower:
            tower[tower.index(None)] = num
            print("차량이 주차되었습니다.")
        else:
            print(f"최대: {slot}대, 현재: {slot}대 / 더 이상 차량을 입고할 수 없습니다.")

    elif choice == 2:
        num = input("출고 차량 번호를 입력하세요: ")
        if num in tower:
            tower[tower.index(num)] = None
            print("차량이 출고되었습니다.")
        else:
            print("차량이 존재하지 않습니다.")

    elif choice == 3:
        for i, num in enumerate(tower):
            if num:
                print(f"{i + 1}층: {num}")
            else:
                print(f"{i + 1}층: 빈 공간")

    elif choice == 4:
        print("프로그램을 종료합니다.")
        break

    else:
        print("잘못된 입력입니다. 다시 입력해주세요.")

