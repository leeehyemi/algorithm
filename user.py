class User:

    count = 0
    
    def __init__(self, name, email, password):
        self.name = name
        self.email = email
        self.password = password
        
        User.count += 1
        
    def say_hello(self):
        print(f"안녕하세요 저는 {self.name}입니다")
    
    def login(self, email, password):
        if self.email == email and self.password == password:
            print("로그인 성공, 환영합니다.")
            self.say_hello()
        else:
            print("로그인 실패, 없는 아이디거나 잘못된 비밀번호입니다.")

    def __str__(self):
        return f"사용자: {self.name}, 이메일:{self.email}"
    
    @classmethod
    def print_number_of_users(cls):
        print(f"총 유저수는: {cls.count}입니다.")
    
    @staticmethod
    def valid_email(email):
        return "@" in email
        
user1 = User("leehyemi", "hyemi@nam.com", "12345")
user2 = User("yushi", "yy@n.com", "abcdef")
user3 = User("juyen", "asf@code.com", "12345")

user1.say_hello() # User.say_hello(user1)
user1.login("ad@n.com", "12345")

print(user1) #str 함수를 직접 쓰지 않아도 str형태로 바뀌면서 출력
print(user2)

print(User.count) # 3
print(user1.count) # 3
print(user2.count) # 3

#user1.count = 5 로 설정하면 user1.count에서만 5로 출력됨 

User.print_number_of_users()
print(User.valid_email("abcdes"))
print(User.valid_email("abcdes@n.com"))