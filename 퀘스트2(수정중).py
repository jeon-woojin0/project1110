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

class Monster(Character) : #상속받음
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
        if not mob.is_alive():
            break
        damage2=mob.attack_target()
        pl.take_damage(damage2) 
        print(f"{mob.name}이 {pl.name}에게 {damage2} 만큼 공격했다")
        print(f"{pl.name}의 체력: {pl.hp}")

    if pl.is_alive() :
        pl.gain_exp(mob.level*20) #gain_exp 안에 이미 레벨업 메소드 있음
        print("전투 승리!",end="\n")
        return True
    else :
        print("전투 패배..")
        return False
        
            
def main(pl,monster_dict):

    for m_name, m_level in monster_dict.items():
        mob = Monster(m_name, m_level)
        win = battle(pl, mob)
        if not win:
            print("게임 오버")
            return
#-------------------------------------------
#현재 문제 
#레벨업


pl = Player('전우진')
mob = {'슬라임': 1, '고블린': 2, '오크': 3}
main(pl,mob)

        
