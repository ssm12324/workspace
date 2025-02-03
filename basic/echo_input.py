# 사용자가 문장을 반복적으로 입력할 수 있는 프로그램

while True:  # 무한 루프 시작
    user_input = input("문장을 입력하세요 (종료하려면 !quit을 입력하세요): ")
    
    if user_input == "!quit":  # 사용자가 !quit을 입력하면
        print("프로그램을 종료합니다. 안녕히 가세요!")
        break  # 반복문 종료
    else:
        print("1")
        print("입력한 문장:", user_input)  # 입력한 문장 출력