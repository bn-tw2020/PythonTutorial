class Character:
    def __init__(self, name, hp, ad):
        self.name = name
        self.strength = hp
        self.attack_damge = ad
        print('Character 클래스의 객체 생성 =>', self.name)

    def attack(self, target):
        print(target,'을/를 공격합니다.!')

    def information(self):
        print('이름 ->', self.name, ', 체력 =>', self.strength,
        ', 공격력 =>', self.attack_damge)

    def level_up(self):
        self.strength *= 1.2
        self.attack_damge += 5

swordsman = Character('검술사', 100, 10)
print(swordsman.name, swordsman.strength, swordsman.attack_damge)
print('변경 전 --------')
swordsman.information()

swordsman.level_up()
print('변경 후 --------')
swordsman.information()