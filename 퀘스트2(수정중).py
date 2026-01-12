import random as r

class Character :
    def __init__(self, name,level,hp,offense,defense):
        self.name = name
        self.level = level
        self.hp = hp
        self.offense = offense
        self.defense = defense

    def __str__(self):
        return(f"이름:{self.name}, 레벨:{self.level}, 체력:{self.hp}, 공격력:{self.offense}, 방어력:{self.defense}")


    def is_alive(self) : #살아있는지 보는 매서드
        return bool(self.hp > 0 )

    def take_damage(self,damage) : #몬스터에게 데미지 받을 때
        if damage >= self.defense : #방어력이 더 작으면 감소
            self.hp -= (damage - self.defense)
    
    def attack_target(self) : #주는 데미지
        return r.randint(1,self.offense) #이 데미지를 상대에게 입혀야함


class Player(Character) :#상속받음
    def __init__(self,name) :
        super().__init__(name,1,100,25,5) #능력치 초기화
        self.exp = 0
        
    def gain_exp(self,amount):
        self.exp += amount
        self.level_up() #경험치 얻을때마다 레벨업 조건 확인
            
    def level_up(self) :
        up = self.exp // 50 #레벨업
        if up >= 1 :
            self.level += up
            self.offense += 10 * up # 10 * 올라간 레벨
            self.defense += 5 * up # 5 * 올라간 레벨
            self.exp %= 50 #50나누고 남은 경험치
            print(f"레벨업! 현재레벨:{self.level}")

class Monster(Character) : #Character 클래스에서 상속받음
    def __init__(self,name,level):
        hp = r.randint(10,30) * level 
        offense = r.randint(5,20) * level
        defense = r.randint(1,5) * level   
        super().__init__(name,level,hp,offense,defense)

        
def battle(pl,mob) :
    print(f"{mob.name}과의 전투를 시작합니다")
    while pl.is_alive() and mob.is_alive() : #둘다 살아있을 때까지 반복
        damage1=pl.attack_target()
        mob.take_damage(damage1)
        print(f"{pl.name}이 {mob.name}에게 {damage1}만큼 공격했다")
        print(f"{mob.name}의 체력: {mob.hp}")
        if not mob.is_alive(): #몹이 죽으면 끝
            break
        damage2=mob.attack_target()
        pl.take_damage(damage2) 
        print(f"{mob.name}이 {pl.name}에게 {damage2} 만큼 공격했다")
        print(f"{pl.name}의 체력: {pl.hp}")

    if pl.is_alive() : #플레이어가 살아있을 때 경험치 받고 승리
        pl.gain_exp(mob.level*20) #gain_exp 안에 이미 레벨업 메소드 있음

        print(f"'{mob.name}'와의 전투에서 승리!",end="\n")
        return True
    else : #플레이어가 죽으면..
        print("전투 패배..")
        return False
            
def main(pl,monster_dict):
    for m_name, m_level in monster_dict.items():
        mob = Monster(m_name, m_level)
        win = battle(pl, mob)
        if not win: #배틀에서 지면 게임오버
            print("게임 오버..")


pl = Player('전우진')
mob = {'슬라임': 1, '고블린': 2, '오크': 3}
main(pl,mob)

#out put
'''
슬라임과의 전투를 시작합니다
전우진이 슬라임에게 1만큼 공격했다
슬라임의 체력: 24
슬라임이 전우진에게 15 만큼 공격했다
전우진의 체력: 90
전우진이 슬라임에게 11만큼 공격했다
슬라임의 체력: 18
슬라임이 전우진에게 14 만큼 공격했다
전우진의 체력: 81
전우진이 슬라임에게 2만큼 공격했다
슬라임의 체력: 18
슬라임이 전우진에게 4 만큼 공격했다
전우진의 체력: 81
전우진이 슬라임에게 2만큼 공격했다
슬라임의 체력: 18
슬라임이 전우진에게 14 만큼 공격했다
전우진의 체력: 72
전우진이 슬라임에게 11만큼 공격했다
슬라임의 체력: 12
슬라임이 전우진에게 15 만큼 공격했다
전우진의 체력: 62
전우진이 슬라임에게 20만큼 공격했다
슬라임의 체력: -3
'슬라임'와의 전투에서 승리!
고블린과의 전투를 시작합니다
전우진이 고블린에게 17만큼 공격했다
고블린의 체력: 19
고블린이 전우진에게 7 만큼 공격했다
전우진의 체력: 60
전우진이 고블린에게 24만큼 공격했다
고블린의 체력: 5
고블린이 전우진에게 22 만큼 공격했다
전우진의 체력: 43
전우진이 고블린에게 18만큼 공격했다
고블린의 체력: -3
레벨업! 현재레벨:2
'고블린'와의 전투에서 승리!
오크과의 전투를 시작합니다
전우진이 오크에게 28만큼 공격했다
오크의 체력: 62
오크이 전우진에게 11 만큼 공격했다
전우진의 체력: 42
전우진이 오크에게 16만큼 공격했다
오크의 체력: 52
오크이 전우진에게 1 만큼 공격했다
전우진의 체력: 42
전우진이 오크에게 32만큼 공격했다
오크의 체력: 26
오크이 전우진에게 27 만큼 공격했다
전우진의 체력: 25
전우진이 오크에게 16만큼 공격했다
오크의 체력: 16
오크이 전우진에게 33 만큼 공격했다
전우진의 체력: 2
전우진이 오크에게 18만큼 공격했다
오크의 체력: 4
오크이 전우진에게 31 만큼 공격했다
전우진의 체력: -19
전투 패배..
게임 오버..
'''
