class Character:
    def __init__(self, hp, mp):
        self.hp = hp
        self.mp = mp

    def fireball(self):
        print("파이어볼을 발사합니다.")

lupi = Character(5,5333)  #인스턴스 선언

lupi.fireball()

print(lupi.hp)


class Book:
    def __init__(self, title, author, use):
        self.title = title
        self.author = author
        self.use = use

    def intro(self):
        print(f"이 책의 제목은 {self.title}이며 저자는 {self.author}이고 {self.use}로 쓰였습니다. ")


harry = Book("해리포터","롤링", "영어")
ring = Book("반지의 제왕","톨킨","영어")


harry.intro()
ring.intro()
    

