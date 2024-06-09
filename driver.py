from user import User

if __name__ == "__main__":
    user1 = User("강영훈", "younghoon@codeit.xyz", "123456")
    user2 = User("이윤수", "yoonsoo@codeit.xyz", "abcdef")
    
    User.print_number_of_users()
    print(user1.name, user1.email, user1.password)
    print(user2.name, user2.email, user2.password)