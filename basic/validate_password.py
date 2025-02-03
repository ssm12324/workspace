import re

def validate_password(password):
    # 정규 표현식 패턴: 최소 하나의 소문자, 대문자, 숫자, 특수 문자 포함
    pattern = r'^(?=.*[a-z])(?=.*[A-Z])(?=.*\d)(?=.*[\W_]).{4,}$'
    
    if re.match(pattern, password):
        return "유효한 비밀번호입니다."
    else:
        return "비밀번호는 최소 하나의 소문자, 대문자, 숫자, 특수 문자를 포함해야 합니다."

# 테스트
a = input("password?: ")
passwords = ["Password123!", "weakpass", "NOLOWERCASE123!", "NoSpecial1", "Strong@Pass1","qQ1!"]
passwords.append(a)
for pw in passwords:
    print(f"{pw}: {validate_password(pw)}")
