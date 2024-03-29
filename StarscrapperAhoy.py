import time
import random
def skip_engine(x):
    while x>0:
        x-=1
        time.sleep(0.5)
class Characters:
    def __init__(self, name, stats, skills, lvlsystem):
        self._name=name
        self._health=stats[0]
        self._maxhealth=stats[0]
        self._attack=stats[1]
        self._ogattack=stats[1]
        self._hitratio=stats[2]
        self._oghitratio=stats[2]
        self._defence=stats[3]
        self._ogdefence=stats[3]
        self._magic=stats[4]
        self._maxmagic=stats[4]
        self._skillist=skills
        self._level=lvlsystem[0]
        self._exp=lvlsystem[1]
        self._party = 0
        self._partymp = 0
        self._ogpartymp = 0
        self._partyskills1 = ["range mode", "full blast", "self strike"]
        self._partyskills2 = ["regen wave", "artist block", "call of the dead"]
        self._partyskills3 = ["sprint", "sharpen", "blitz"]
        self._gold = 0
        self._speedlv = 0
        self._hitratiolv = 4
        self._defencelv = 5
        self._speed = stats[5]
        self._ogspeed = stats[5]
    def replace_skills(self, skills):
        self._skillist = skills
    def new_party(self, num):
        self._party = num
    def spend(self, num):
        self._gold+=num
    def get_health(self):
        return self._health
    def get_party(self):
        return self._party
    def get_gold(self):
        return self._gold
    def get_skills(self):
        return self._skillist
    def get_hitratio(self):
        return self._hitratio
    def get_attack(self):
        return self._attack
    def get_defence(self):
        return self._defence
    def get_magic(self):
        return self._magic
    def get_name(self):
        return self._name
    def get_level(self):
        return self._level
    def get_speed(self):
        return self._speed
    def get_exp(self):
        return self._exp
    def get_test(self):
        print("HP ", self._health)
        print("LV ", self._level)
        print("Attack ",self._attack,"Hitratio ", self._hitratio,"Defence ", self._defence)
    def reset(self):
        self._health = self._maxhealth
        self._magic = self._maxmagic
        self._hitratio = self._oghitratio
        self._defence = self._ogdefence
        self._attack = self._ogattack
        self._partymp = self._ogpartymp
        self._speed = self._ogspeed
    def damage(self, damage, hitratio):
        roll = random.randint(0, hitratio)
        if roll == hitratio:
            self._health-=damage * 1.5
            print("CRIT")
        elif roll >= self._defence or self._defence > hitratio:
            self._health-=damage
            print("Hit")
        else:
            print("Miss")
    def levelup(self, exp):
        self._exp += exp
        if self._exp > self._level*10:
            print("level up")
            self._exp -= self._level*10
            self._level += 1
            self._maxhealth+=20
            self._maxmagic+=10
            self._ogpartymp+=10
            self._speedlv += 1
            self._hitratiolv += 1
            self._defencelv += 1
            if self._speedlv >= 8:
                self._ogspeed += 1
                self._maxhealth += 5
                self._maxmagic += 5
                self._ogpartymp += 5
                self._speedlv = 0
            if self._hitratiolv >= 3:
                self._oghitratio += 2
                self._hitratiolv = 0
            if self._defencelv >= 4:
                self._ogattack += 3
                self._ogdefence += 2
                self._defencelv = 0
            if self._level == 15:
                print("<You feel something change inside of you>")
                time.sleep(0.8)
                print("<Your mind grows stronger>")
                self._skillist = ["Charge Strike", "Ahoy!", "Cannon Fire"]
            elif self._level == 20:
                print("<You feel something change inside of you>")
                time.sleep(0.8)
                print("<Your body grows stronger>")
                self._skillist = ["Revol Shot", "Ahoy!", "Cannon Fire"]
            elif self._level == 35:
                print("<You feel something change inside of you>")
                time.sleep(0.8)
                print("<You can see the truth>")
                self._skillist = ["Revol Shot", "Ahoy!", "Big Bang Punch"]
            elif self._level == 45:
                print("<You feel something change inside of you>")
                time.sleep(0.8)
                print("<Your body is liberated>")
                self._skillist = ["Soul Liberate", "Ahoy!", "Big Bang Punch"]
            elif self._level == 50:
                print("<You feel something change inside of you>")
                time.sleep(0.8)
                print("<Your mind is liberated>")
                self._skillist = ["Soul Liberate", "Rebel Wishes", "Big Bang Punch"]
            elif self._level == 60:
                print("<You feel something change inside of you>")
                time.sleep(0.8)
                print("<The truth has been liberated>")
                self._skillist = ["Soul Liberate", "Rebel Wishes", "Revolt Beam"]
    def slevelup(self, exp):
        self._exp += exp
        if self._exp > self._level*10:
            self._exp -= self._level*10
            self._level += 1
            self._maxhealth+=20
            self._maxmagic+=10
            self._ogpartymp+=5*self._party
            self._speedlv += 1
            self._hitratiolv += 1
            self._defencelv += 1
            if self._speedlv >= 8:
                self._ogspeed += 1
                self._maxhealth += 5
                self._maxmagic += 5
                self._ogpartymp += 5
                self._speedlv = 0
            if self._hitratiolv >= 3:
                self._oghitratio += 2
                self._hitratiolv = 0
            if self._defencelv >= 4:
                self._ogattack += 3
                self._ogdefence += 2
                self._defencelv = 0
        if self._level == 15:
            self._skillist = ["Charge Strike", "Ahoy!", "Cannon Fire"]
        elif self._level == 20:
            self._skillist = ["Revol Shot", "Ahoy!", "Cannon Fire"]
        elif self._level == 35:
            self._skillist = ["Revol Shot", "Ahoy!", "Big Bang Punch"]
        elif self._level == 45:
            self._skillist = ["Soul Liberate", "Ahoy!", "Big Bang Punch"]
        elif self._level == 50:
            self._skillist = ["Soul Liberate", "Rebel Wishes", "Big Bang Punch"]
        elif self._level == 60:
            self._skillist = ["Soul Liberate", "Rebel Wishes", "Revolt Beam"]
    def battle(self, enemy):
        skillet = 0
        while self._health>0 and enemy.get_health()>0:
            if self._magic < 0:
                    self._magic = 0
            if self._magic > 9999:
                self._magic = 9999
            if self._health > 9999:
                self._health = 9999
            time.sleep(0.8)
            if skillet == 0:
                skillet = 1
            else:
                skillet = 0
            roll = random.randint(1, 10)
            if roll == 5:
                skillet = 2
            enemyskillet = random.randint(0, 2)
            skillskillet = random.randint(0, 2)
            skillskillet2 = random.randint(0, 2)
            skillskillet3 = random.randint(0, 2)
            if self._speed >= enemy.get_speed():
                if self._party >= 1 and self._party != 4:
                    if self._partyskills1[skillskillet] == "range mode" and self._partymp>=10:
                        print("[Shelly] ranged mode")
                        enemy.damage(self._attack+20 , self._hitratio)
                        enemy.damage(self._attack, self._hitratio+10)
                        enemy.damage(self._attack-10, self._hitratio+20)
                        self._partymp -= 10
                    elif self._partyskills1[skillskillet] == "full blast" and self._partymp>=10:
                        print("[Shelly] full blast")
                        enemy.damage(self._attack*self._hitratio, 9223372036854775807)
                        self._partymp -= 10
                    elif self._partyskills1[skillskillet] == "self strike" and self._health>=self._speed+enemy.get_attack():
                        print("[Shelly] self strike")
                        self._health -= self._speed
                        self._partymp += 30
                        self._magic += 20
                    else:
                        print("[Shelly] attack")
                        enemy.damage(self._attack - 4, self._hitratio + 5)
                if self._party >= 2:
                    if self._partyskills2[skillskillet2] == "regen wave" and self._partymp>=5:
                        print("[Drake] regen wave")
                        self._health += 40
                        self._partymp -= 5
                    elif self._partyskills2[skillskillet2] == "artist block" and self._partymp>=5:
                        print("[Drake] artist block")
                        self._speed += 1
                        self._hitratio += 2
                        self._partymp -= 5
                    elif self._partyskills2[skillskillet2] == "call of the dead" and self._partymp>=5:
                        print("[Drake] call of the dead")
                        self._hitratio += 4
                        enemy.damage(self._attack, self._hitratio)
                        self._partymp -= 5
                    else:
                        print("[Drake] attack")
                        enemy.damage(self._attack - 2, self._hitratio - 2)
                if self._party >= 3:
                    if self._partyskills3[skillskillet3] == "sprint" and self._partymp>=10:
                        print("[Neo] sprint")
                        self._speed += 3
                        self._partymp -= 10
                    elif self._partyskills3[skillskillet3] == "sharpen" and self._partymp>=5:
                        print("[Neo] sharpen")
                        self._attack += 3
                        self._hitratio += 1
                        self._partymp -= 5
                    elif self._partyskills3[skillskillet3] == "blitz" and self._partymp>=5:
                        print("[Neo] blitz")
                        self._attack += 2
                        enemy.damage(self._attack, self._hitratio)
                        self._partymp -= 5
                    else:
                        print("[Neo] attack")
                        enemy.damage(self._attack + 2, self._hitratio + 2)
                time.sleep(0.9)
                print("["+self._name+"]", "HP:", self._health, "MP:", self._magic, "skill:", self._skillist[skillet])
                if enemy.get_health() >= 0:
                    print("Enemy: "+ enemy.get_name() + " Enemy HP: "+ str(enemy.get_health()))
                else:
                    print("Enemy: "+ enemy.get_name() + " Enemy HP: "+ "0")
                print("Option 1: Attack")
                print("Option 2: Skill")
                print("Option 3: Search")
                print("Option 4: Escape")
                action = input("Number of action you would like to take: ")
                while action!="1" and action!="2" and action!="3" and action!="4" and action!="7":
                    print("try again")
                    print("["+self._name+"]", "HP:", self._health, "MP:", self._magic, "skill:", self._skillist[skillet])
                    if enemy.get_health() >= 0:
                        print("Enemy: "+ enemy.get_name() + " Enemy HP: "+ str(enemy.get_health()))
                    else:
                        print("Enemy: "+ enemy.get_name() + " Enemy HP: "+ "0")
                    print("Option 1: Attack")
                    print("Option 2: Skill")
                    print("Option 3: Search")
                    print("Option 4: Escape")
                    action = input("Number of action you would like to take: ")
                if action == "1":
                    enemy.damage(self._attack, self._hitratio)
                elif action == "2":
                    if skillet == 0:
                        self._health -= 2
                    elif skillet == 1:
                        if self._magic > 0:
                            self._magic -= 2
                        else:
                            self._health -= 4
                    if self._skillist[skillet] == "Ahoy!":
                        self._attack += 3
                        self._defence -= 1
                        self._health += self._magic
                        if self._defence < 1:
                            self._defence = 1
                        if self._health >self._maxhealth:
                            self._health = self._maxhealth
                    elif self._skillist[skillet] == "Cannon Fire":
                        self._attack += 10
                        enemy.damage(self._attack, self._hitratio*10)
                    elif self._skillist[skillet] == "Pain Remover":
                        self._attack -= 1
                        self._health += 10
                        if self._attack < 1:
                            self._attack = 1
                    elif self._skillist[skillet] == "Charge Strike":
                        self._attack += 5
                        self._hitratio += 5
                    elif self._skillist[skillet] == "Revol Shot":
                        self._attack += 10
                        enemy.damage(self._attack, self._hitratio)
                        self._attack -= 10
                    elif self._skillist[skillet] == "Big Bang Punch":
                        self._partymp += 20
                        self._magic += 10
                        enemy.damage(self._attack*5, self._hitratio*10)
                    elif self._skillist[skillet] == "Revolt Beam":
                        self._speed = 1
                        enemy.damage(self._attack, 999999)
                        enemy.damage(self._attack, 999999)
                        enemy.damage(self._attack, 999999)
                    elif self._skillist[skillet] == "Rebel Wishes":
                        self._attack += 5
                        self._speed -= 2
                        self._health += self._magic + self._attack
                        if self._health >self._maxhealth:
                            self._health = self._maxhealth
                    elif self._skillist[skillet] == "Soul Liberate":
                        self._attack += 10
                        self._hitratio += 10
                        self._partymp += 10
                elif action == "4":
                    print("[???] you are a silly fool")
                    time.sleep(0.9)
                    print("[???] there is no escape")
                    time.sleep(0.9)
                    print("[???] don't even try")
                    time.sleep(0.9)
                elif action == "7":
                    enemy.damage(999999, 999999)
                else:
                    print("ThErE iS nO eScApE sIlLy MoRtAl")
                    print("Attack:", self._attack, "Hit Chance:", self._hitratio, "Defence:", self._defence)
                    print("Enemy HP:", enemy.get_health())
                time.sleep(0.8)
                if enemy.get_skills()[enemyskillet] == "void":
                    print("[Enemy]: Attack")
                    roll = random.randint(0, enemy.get_hitratio())
                    if roll>self._defence:
                        print("Hit")
                        self._health-=enemy.get_attack()
                    else:
                        print("Miss")
                elif enemy.get_skills()[enemyskillet] == "Slow":
                    print("[Enemy]: Slow")
                    self._speed -= 2
                elif enemy.get_skills()[enemyskillet] == "Aura Force":
                    print("[Enemy]: Aura Force")
                    print("<enemy gains health>")
                    enemy.damage(-3, 999999)
                elif enemy.get_skills()[enemyskillet] == "God Scape":
                    print("[Enemy]: God Scape")
                    print("<the ground distorts bellow you>")
                    self._defence = 1
                    if self._magic > 10:
                        self._magic -= 10
                    else:
                        self._health -= 5
                elif enemy.get_skills()[enemyskillet] == "Starscrapper":
                    print("[Enemy]: Starscrapper")
                    print("<time seems to speed up>")
                    self._defence = 1
                    self._hitratio = 1
                    enemy.damage(self._attack*-1, 999999)
                elif enemy.get_skills()[enemyskillet] == "Purify":
                    print("[Enemy]: Attack")
                    print("<your stats reset>")
                    roll = random.randint(0, enemy.get_hitratio())
                    if roll>self._defence:
                        print("Hit")
                        self._health-=enemy.get_attack()
                    else:
                        print("Miss")
                    self._defence = self._ogdefence
                    self._hitratio = self._oghitratio
                elif enemy.get_skills()[enemyskillet] == "Time Roar":
                    print("[Enemy]: Time Roar")
                    self._health -= 20
                    enemy.damage(-20, 999999)
                elif enemy.get_skills()[enemyskillet] == "Time Roar2":
                    print("[Enemy]: #%&$#$^%")
                    self._health -= 777
                    enemy.damage(-777, 999999)
                elif enemy.get_skills()[enemyskillet] == "Vamp Bite":
                    print("[Enemy]: Bite")
                    self._health -= 25
                    enemy.damage(-50, 999999)
                elif enemy.get_skills()[enemyskillet] == "Wrap":
                    print("[Enemy]: Wrap")
                    self._health -= 5
                    enemy.damage(-10, 999999)
                    self._magic -= 5
                    self._speed -= 1
                    if self._magic < 0:
                        self._magic = 0
                elif enemy.get_skills()[enemyskillet] == "Wrap2":
                    print("[Enemy]: #%&$#$^%")
                    roll = random.randint(0, enemy.get_hitratio())
                    if roll>self._defence:
                        print("Hit")
                        self._health-=enemy.get_attack()
                    else:
                        print("Miss")
                    print("<you feel yourself weaken>")
                    self._magic -= 5
                    self._attack -=5
                    self._speed -= 2
                    if self._magic < 0:
                        self._magic = 0
                    if self._attack < 1:
                        self._attack = 1
                elif enemy.get_skills()[enemyskillet] == "Tears":
                    print("[Enemy]: Heavy Tears")
                    self._health -= 5
                    self._attack -= 1
                    self._speed -= 1
                    if self._attack <= 1:
                        self._attack = 2
                time.sleep(0.9)
            if self._speed < enemy.get_speed() and enemy.get_health() > 0 and self._health > 0:
                enemyskillet = random.randint(0, 2)
                skillskillet = random.randint(0, 2)
                skillskillet2 = random.randint(0, 2)
                skillskillet3 = random.randint(0, 2)
                if enemy.get_skills()[enemyskillet] == "void":
                    print("[Enemy]: Attack")
                    roll = random.randint(0, enemy.get_hitratio())
                    if roll>self._defence:
                        print("Hit")
                        self._health-=enemy.get_attack()
                    else:
                        print("Miss")
                elif enemy.get_skills()[enemyskillet] == "Slow":
                    print("[Enemy]: Slow")
                    self._speed -= 1
                elif enemy.get_skills()[enemyskillet] == "Aura Force":
                    print("[Enemy]: Aura Force")
                    print("<enemy gains health>")
                    enemy.damage(-3, 999999)
                elif enemy.get_skills()[enemyskillet] == "God Scape":
                    print("[Enemy]: God Scape")
                    print("<the ground distorts bellow you>")
                    self._defence = 1
                    if self._magic > 10:
                        self._magic -= 10
                    else:
                        self._health -= 5
                elif enemy.get_skills()[enemyskillet] == "Starscrapper":
                    print("[Enemy]: Starscrapper")
                    print("<time seems to speed up>")
                    self._defence = 1
                    self._hitratio = 1
                    enemy.damage(self._attack*-1, 999999)
                elif enemy.get_skills()[enemyskillet] == "Purify":
                    print("[Enemy]: Attack")
                    print("<your stats reset>")
                    roll = random.randint(0, enemy.get_hitratio())
                    if roll>self._defence:
                        print("Hit")
                        self._health-=enemy.get_attack()
                    else:
                        print("Miss")
                    self._defence = self._ogdefence
                    self._hitratio = self._oghitratio
                elif enemy.get_skills()[enemyskillet] == "Time Roar":
                    print("[Enemy]: Time Roar")
                    self._health -= 20
                    enemy.damage(-20, 999999)
                elif enemy.get_skills()[enemyskillet] == "Wrap":
                    print("[Enemy]: Wrap")
                    self._health -= 10
                    enemy.damage(-10, 999999)
                    self._magic -= 10
                    if self._magic < 0:
                        self._magic = 0
                elif enemy.get_skills()[enemyskillet] == "Wrap2":
                    print("[Enemy]: #%&$#$^%")
                    roll = random.randint(0, enemy.get_hitratio())
                    if roll>self._defence:
                        print("Hit")
                        self._health-=enemy.get_attack()
                    else:
                        print("Miss")
                    print("<you feel yourself weaken>")
                    self._magic -= 10
                    self._attack -=10
                    if self._magic < 0:
                        self._magic = 0
                    if self._attack < 1:
                        self._attack = 1
                elif enemy.get_skills()[enemyskillet] == "Time Roar2":
                    print("[Enemy]: #%&$#$^%")
                    self._health -= 777
                    enemy.damage(-777, 999999)
                elif enemy.get_skills()[enemyskillet] == "Vamp Bite":
                    print("[Enemy]: Bite")
                    self._health -= 25
                    enemy.damage(-50, 999999)
                elif enemy.get_skills()[enemyskillet] == "Tears":
                    print("[Enemy]: Heavy Tears")
                    self._health -= 1
                    self._defence -= 1
                    self._speed += 3
                    if self._defence <= 0:
                        self._defence = 1
                time.sleep(0.9)
                print("["+self._name+"]", "HP:", self._health, "MP:", self._magic, "skill:", self._skillist[skillet])
                if enemy.get_health() >= 0:
                    print("Enemy: "+ enemy.get_name() + " Enemy HP: "+ str(enemy.get_health()))
                else:
                    print("Enemy: "+ enemy.get_name() + " Enemy HP: "+ "0")
                print("Option 1: Attack")
                print("Option 2: Skill")
                print("Option 3: Search")
                print("Option 4: Escape")
                action = input("Number of action you would like to take: ")
                while action!="1" and action!="2" and action!="3" and action!="4" and action!="7":
                    print("try again")
                    print("["+self._name+"]", "HP:", self._health, "MP:", self._magic, "skill:", self._skillist[skillet])
                    if enemy.get_health() >= 0:
                        print("Enemy: "+ enemy.get_name() + " Enemy HP: "+ str(enemy.get_health()))
                    else:
                        print("Enemy: "+ enemy.get_name() + " Enemy HP: "+ "0")
                    print("Option 1: Attack")
                    print("Option 2: Skill")
                    print("Option 3: Search")
                    print("Option 4: Escape")
                    action = input("Number of action you would like to take: ")
                if action == "1":
                    enemy.damage(self._attack, self._hitratio)
                elif action == "2":
                    if skillet == 0:
                        self._health -= 2
                    elif skillet == 1:
                        if self._magic > 0:
                            self._magic -= 2
                        else:
                            self._health -= 4
                    if self._skillist[skillet] == "Ahoy!":
                        self._attack += 3
                        self._defence -= 1
                        self._health += self._magic
                        if self._defence < 1:
                            self._defence = 1
                        if self._health >self._maxhealth:
                            self._health = self._maxhealth
                    elif self._skillist[skillet] == "Cannon Fire":
                        self._attack += 5
                        enemy.damage(self._attack, self._hitratio*5)
                    elif self._skillist[skillet] == "Pain Remover":
                        self._attack -= 2
                        self._speed += 1
                        self._health += 10
                        if self._attack < 1:
                            self._attack = 1
                    elif self._skillist[skillet] == "Charge Strike":
                        self._attack += 5
                        self._speed += 2
                    elif self._skillist[skillet] == "Revol Shot":
                        self._attack += 10
                        enemy.damage(self._attack, self._hitratio)
                        self._attack -= 10
                    elif self._skillist[skillet] == "Big Bang Punch":
                        self._partymp += 10
                        self._magic += 5
                        self._speed += 2
                        enemy.damage(self._attack, self._hitratio*5)
                    elif self._skillist[skillet] == "Revolt Beam":
                        self._speed += 20
                        self._attack += 5
                        self._hitratio += 5
                        self._defence += 1
                    elif self._skillist[skillet] == "Rebel Wishes":
                        self._attack += 2
                        self._speed += 3
                        self._health += self._attack
                        if self._health >self._maxhealth:
                            self._health = self._maxhealth
                    elif self._skillist[skillet] == "Soul Liberate":
                        self._attack += 5
                        self._hitratio += 5
                        self._speed += 2
                if self._party >= 1 and self._party != 4:
                    if self._partyskills1[skillskillet] == "range mode" and self._partymp>=10:
                        print("[Shelly] ranged mode")
                        enemy.damage(self._attack+10 , self._hitratio-10)
                        enemy.damage(self._attack, self._hitratio-10)
                        enemy.damage(self._attack-10, self._hitratio-10)
                        self._partymp -= 10
                    elif self._partyskills1[skillskillet] == "full blast" and self._partymp>=10:
                        print("[Shelly] full blast")
                        enemy.damage(self._attack*self._speed, 9223372036854775807)
                        self._speed += 1
                        self._partymp -= 10
                    elif self._partyskills1[skillskillet] == "self strike" and self._health>=self._speed+enemy.get_attack():
                        print("[Shelly] self strike")
                        self._health -= self._speed
                        self._partymp += 15
                        self._magic += 15
                    else:
                        print("[Shelly] attack")
                        enemy.damage(self._attack + 4, self._hitratio - 2)
                if self._party >= 2:
                    if self._partyskills2[skillskillet2] == "regen wave" and self._partymp>=10:
                        print("[Drake] regen wave")
                        self._health += 30
                        self._partymp -= 10
                    elif self._partyskills2[skillskillet2] == "artist block" and self._partymp>=5:
                        print("[Drake] artist block")
                        self._speed += 3
                        self._partymp -= 5
                    elif self._partyskills2[skillskillet2] == "call of the dead" and self._partymp>=5:
                        print("[Drake] call of the dead")
                        self._hitratio += 1
                        self._speed += 1
                        enemy.damage(self._attack, self._hitratio)
                        self._partymp -= 5
                    else:
                        print("[Drake] attack")
                        enemy.damage(self._attack + 3, self._hitratio + 3)
                if self._party >= 3:
                    if self._partyskills3[skillskillet3] == "sprint" and self._partymp>=5:
                        print("[Neo] sprint")
                        self._speed += 3
                        self._partymp -= 5
                    elif self._partyskills3[skillskillet3] == "sharpen" and self._partymp>=5:
                        print("[Neo] sharpen")
                        self._attack += 7
                        self._partymp -= 5
                    elif self._partyskills3[skillskillet3] == "blitz" and self._partymp>=5:
                        print("[Neo] blitz")
                        self._attack += 5
                        self._speed += 2
                        self._partymp -= 5
                    else:
                        print("[Neo] attack")
                        enemy.damage(self._attack - 2, self._hitratio + 3)
                time.sleep(0.9)
            if self._party > 0 and self._party != 4:
                roll = random.randint(1, 9-self._party)
                if roll == 5:
                    print("[Party]: FULL ASSAULT!")
                    enemy.damage(self._attack*self._party, self._hitratio*self._party)
                elif roll == 1:
                    print("[Party]: Magic Break!")
                    self._partymp += self._party*2
                elif roll == 2 and self._party == 1:
                    print("[Shelly]: cheering!")
                    self._magic += 3
                    self._attack += 3
            elif self._party == 4:
                roll = random.randint(1, 5)
                if roll == 1:
                    print("[Party]: Party Assault?")
                    enemy.damage(self._attack, self._hitratio)
                elif roll == 2:
                    print("[Party]: Magic Break?")
                    self._partymp += self._party
                elif roll == 3:
                    print("[Shelly]: Shelly's tears")
                    self._magic += 3
                    self._partymp += 6
            if self._magic < 0:
                self._magic = 0
            if self._magic > 9999:
                self._magic = 9999
            if self._health > 9999:
                self._health = 9999
        print("Battle End")
        self._attack = self._ogattack
        self._hitratio = self._oghitratio
        self._defence = self._ogdefence
        self._partymp = self._ogpartymp
        self._speed = self._ogspeed
def voice(person, speach):
    print("["+person+"]", end=" ", flush=True)
    for i in speach:
        print(i, end="", flush=True)
        time.sleep(0.07)
    print("")
def pa(text):
    print("<", end="", flush=True)
    for i in text:
        print(i, end="", flush=True)
        time.sleep(0.07)
    print(">")
def re_burst(mc, enemy):
    mc.reset()
    enemy.reset()
def saver(chapter):
    mc.reset()
    output_file = open("AhoySave.txt", "w")
    output_file.write(str(chapter))
    output_file.close()
    output_file = open("Name.txt", "w")
    output_file.write(str(name))
    output_file.close()
    output_file = open("AhoyLV.txt", "w")
    output_file.write(str(mc.get_level()))
    output_file.close()
    output_file = open("AhoyParty.txt", "w")
    output_file.write(str(mc.get_party()))
    output_file.close()
def ship(enemies):
    action = "0"
    while action != "3":
        print("Infront of you are the great seas")
        print("Option 1: Set sail")
        print("Option 2: Take a rest")
        print("Option 3: head towards land")
        print("Option 4: talk to the crew")
        action = input("What now? ")
        if action == "1":
            roll = random.randint(1, 5)
            if roll == 1:
                pa("You quickly ran into trouble")
            elif roll == 2:
                pa("A beast rises from the water to attack you")
            elif roll == 3:
                pa("You see a small monster in the distance")
                pa("You decide to approach it")
                pa("You quickly find out it isn't very small")
            elif roll == 4:
                pa("Something hits your ship at high speeds")
            elif roll == 5:
                pa("Something feels off about this...")
                mc.spend(5)
                pa("You found some gold coins")
            if roll != 5:
                roll = random.randint(1, 70)
            else:
                roll = random.randint(30, 70)
            if roll == 1:
                enemy = enemies[2]
            elif roll >= 30:
                enemy = enemies[1]
            else:
                enemy = enemies[0]
            mc.battle(enemy)
            if mc.get_health() > 0:
                mc.levelup(enemy.get_exp())
                mc.spend(5)
                if enemy.get_name == enemies[0].get_name:
                    mc.levelup(enemy.get_exp())
                    mc.spend(5)
            re_burst(mc, enemy)
        elif action == "2":
            voice("Shelly", "Wait, you still sleep?")
            roll = random.randint(1, 10)
            if roll == 1:
                pa("You feel slightly offended")
            elif roll == 2:
                pa("Wait? She doesn't sleep?")
            pa("You decided to rest")
            mc.reset()
            mc.get_test()
        elif action == "4" and mc.get_party() < 2:
            voice("Shelly", "Wait, you want to spend time together?")
            roll = random.randint(1, 5)
            if roll == 1:
                pa("You played some games together")
            elif roll == 2:
                pa("You couldn't find anything fun to do")
            elif roll == 3:
                pa("You got sea sick and had to rest")
            elif roll == 4:
                pa("You had a nice conversation with Shelly")
            else:
                pa("Is time moving slower suddenly?")
        if action != "3":
            action = "0"
def saved():
    print("The Game Has Been Saved")
"""/////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////"""
"""HP ATK HR DEF MP SP"""
wolf=Characters("Wolf", [10,5,15,1,5,2], ["void", "void", "void"], (1,2))
shark=Characters("Shark", [15,3,10,1,5,1], ["void", "void", "void"], (1,2))
drake=Characters("Drake", [30,7,15,4,5,5], ["void", "void", "void"], (1,6))
drakek=Characters("Drake King", [140,20,20,10,70,10], ["void", "void", "void"], (1,7))
beast=Characters("Berserker", [500,2,30,10,20,5], ["void", "Slow", "Purify"], (1,2))
narator1=Characters("Beast?", [300,2,2,2,200,7], ["void", "Slow", "Tears"], (1,14))
kraken=Characters("Kraken", [300,35,15,10,150,100], ["Slow", "Purify", "Wrap"], (1,6))
Starscrapper=Characters("Weird lookin' whale", [999999,99,999,999,999,1], ["Wrap2", "Purify", "Time Roar2"], (1,9999))
"""/////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////"""
chapter = 0
action = 0
with open("AhoySave.txt", "r") as read_file:
    content = read_file.read()
    if content.strip():
        chapter = int(content)
    else:
        print("File is empty.")
with open("difficulty.txt", "r") as read_file:
    content = read_file.read()
    if content.strip():
        action = int(content)
    else:
        print("File is empty.")
with open("name.txt", "r") as read_file:
    name=str(read_file.read())
if action=="1":
    mc=Characters(name, [30,5,20,3,15,4], ["Charge Strike", "Pain Remover", "Revol Shot"], (1,2))
elif action=="2":
    mc=Characters(name, [20,3,10,2,5,1], ["Charge Strike", "Pain Remover", "Revol Shot"], (1,2))
else:
    mc=Characters(name, [15,2,8,2,5,0], ["Charge Strike", "Pain Remover", "Revol Shot"], (1,2))
with open("AhoyLV.txt", "r") as read_file:
    x=int(read_file.read())
    while(mc.get_level() < x):
        mc.slevelup(1)
with open("AhoyParty.txt", "r") as read_file:
    trys=int(read_file.read())
    mc.new_party(trys)
if chapter == 0:
    pa("You look around and see some weird building")
    pa("How did you get here?")
    voice("???", "Go! Quick! Run for the exit")
    skip_engine(5)
    pa("You start to run in a random direction")
    pa("You see an exit but see some beast in the way")
    pa("What is this feeling?")
    pa("Your body feels warm...")
    pa("Is this the truth?")
    mc=Characters("???", [999,10,50,15,0,5], ["Cannon Fire", "Ahoy!", "Big Bang Punch"], (1,2))
    mc.new_party(3)
    enemy = beast
    mc.battle(enemy)
    pa("You blacked out")
    #main story start
    pa("you wake up in a weird space")
    voice("???", "Welcome hero to a new world")
    skip_engine(4)
    voice("???", "I am the narator to your story")
    voice("Narator", "I will help you on your quest")
    voice("Narator", "So, what is your name?")
    name=input("Name: ")
    if name=="your mom" or name=="jayden" or name=="Your Mom" or name=="Your mom":
        voice("Narator", "You are not funny")
        name="loser"
    elif name=="jesus" or name=="Jesus" or name=="God":
        voice("Narator", "Those people don't exist here")
        name="false prophet"
    elif name=="Narator" or name=="narator":
        voice("Narator", "No it isn't")
        name="Copy Cat"
    elif name=="Bill" or name=="bill":
        voice("Bill", "May I borrow that?")
        name="Bill?"
    voice("Narator", "What a nice name")
    print("from now on you will only need the number pad and enter")
    mc=Characters(name, [20,5,10,2,10,1], ["Charge Strike", "Pain Remover", "Revol Shot"], (1,2))
    voice("Narator", "Is this your first time hero?")
    voice("Narator", "Do I need to teach you how to fight?")
    print("1=Yes")
    print("2=No")
    action=input("What will you do? ")
    if action=="1":
        print("Tutorial battle 1")
        enemy=Characters("Small Beast", [30,2,10,1,5,0], ["void", "void", "void"], (1,2))
        mc.battle(enemy)
        print("Tutorial battle 2")
        enemy=Characters("Small Beast", [20,2,10,1,5,1], ["void", "void", "void"], (1,2))
        mc.battle(enemy)
        re_burst(mc, enemy)
        print("Tutorial battle 3")
        enemy=Characters("Small Beast", [10,2,10,1,5,2], ["void", "void", "void"], (1,2))
        mc.battle(enemy)
    else:
        voice("Narator", "So, we have met before?")
    voice("Narator", "Now to choose dificulty")
    print("1=easy")
    print("2=normal")
    print("3=hard")
    action=input("what mode will you play? ")
    if action=="1":
        mc=Characters(name, [30,5,20,3,15,4], ["Charge Strike", "Pain Remover", "Revol Shot"], (1,2))
    elif action=="2":
        mc=Characters(name, [20,3,10,2,5,1], ["Charge Strike", "Pain Remover", "Revol Shot"], (1,2))
    else:
        mc=Characters(name, [15,2,8,2,5,0], ["Charge Strike", "Pain Remover", "Revol Shot"], (1,2))
    output_file = open("difficulty.txt", "w")
    output_file.write(str(action))
    output_file.close()
    chapter += 1
saver(chapter)
if chapter == 1:
    x=0
    while x<=4:
        x+=1
        pa("You wake up somewhere")
        pa("Looking around you see the ocean")
        pa("Water goes on for miles")
        print("1=walk across beach")
        print("2=try to swim")
        action=input("What will you do? ")
        b=0
        while action=="1" and b==0:
            pa("You walk across the beach")
            pa("You come across a small cave")
            pa("something comes out and looks at you")
            pa("It looks like a wolf")
            pa("It suddenly bolts at you")
            enemy=wolf
            mc.battle(enemy)
            if mc.get_health()>0:
                mc.levelup(enemy.get_exp())
                b=1
            re_burst(mc, enemy)
        if action=="1":
            pa("You walk into the cave")
            pa("It is too dark to see")
            pa("Soemthing feels off")
        i=0
        while action=="2" and i==0:
            pa("You jump into the water")
            pa("You keep going")
            pa("Looking back you already made it pretty far")
            pa("You might actual make it")
            pa("You see a boat in the distance")
            pa("Something bites your leg")
            skip_engine(3)
            pa("You get dragged under the water")
            skip_engine(4)
            pa("A shark attacks you")
            enemy=shark
            mc.battle(enemy)
            if mc.get_health()>0:
                mc.levelup(enemy.get_exp())
                i=1
                pa("You climb onto the boat")
            re_burst(mc, enemy)
        if action=="2":
            pa("The ship is old and rotted")
            pa("You still see no land in the distance")
            pa("Just a small island which you came")
            pa("Something feels off")
    pa("You wake up on the beach again")
    pa("You see a box of matches in the sand")
    pa("You go to explore the beach")
    pa("You come across a cave")
    pa("Nothing stands infront of it")
    pa("You light a match and enter the cave")
    pa("Some kind of scaled beast appears")
    pa("It roars at you then walks away")
    pa("You walk farther into the cave")
    pa("A box sits in the middle of the floor")
    pa("The box is covered in vines")
    pa("You walk upto the box")
    pa("It seems to be locked")
    skip_engine(4)
    voice("???", "OPEN THE BOX!!!")
    skip_engine(4)
    voice("???", "OPEN IT ALREADY!!!")
    skip_engine(4)
    pa("Something compells you to open the box")
    pa("You bang on the lock and it opens")
    pa("A girl in all white steps out")
    skip_engine(5)
    voice("???", "Thank you loser!")
    mc.new_party(1)
    skip_engine(5)
    pa("You feel breathing on your back")
    pa("Shelly joins the party!")
    skip_engine(4)
    pa("The beast attacks you")
    enemy=drake
    mc.battle(enemy)
    mc.levelup(enemy.get_exp())
    re_burst(mc, enemy)
    pa("You feel tired and pass out")
    chapter += 1
    saved()
saver(chapter)
if chapter == 2:
    pa("You slowly start to wake up")
    voice("???", "WAKE UP!!!")
    pa("You quickly bolt awake")
    skip_engine(3)
    pa("you look around a bit")
    skip_engine(3)
    pa("You seem to be on a boat")
    voice("???", "Finally, you are so annoying")
    skip_engine(5)
    voice("???", "I'm Shelly, thanks for saving me")
    voice("Shelly", "Welcome aboard my ship")
    voice("Shelly", "We call it the hour glass")
    voice("Shelly", "You might be wondering why")
    skip_engine(5)
    voice("Shelly", "Well that's a secret")
    pa("You decide to explore the ship")
    ship([drake, drake, drakek])
    pa("You finally reached land")
    chapter += 1
    saved()
saver(chapter)
if chapter == 3:
    voice("Shelly", "Well, we made it")
    pa("You head onto the land")
    pa("Heading towards the inn")
    pa("You hear a few men talking")
    voice("man1", "Did you hear about the mission?")
    voice("man2", "Yeah, when do they leave?")
    voice("man1", "The first crew leaves in 4 days")
    voice("man3", "You think they can finally find it?")
    voice("man2", "No way, it's been lost for years")
    voice("man1", "Yeah, the old man's chest")
    voice("man2", "They say it holds a powerful secret")
    pa("You wonder what could be in that chest")
    pa("You continue on to the inn")
    pa("Arriving at the inn you decide to stay the night")
    pa("In your dream you see a beast in white clothing")
    pa("Tears are rolling down it's eyes, is it crying?")
    pa("The beast roars and attacks you")
    enemy = narator1
    mc.battle(enemy)
    if mc.get_health() > 0:
        mc.levelup(enemy.get_exp())
    re_burst(mc, enemy)
    mc.levelup(enemy.get_exp())
    chapter += 1
    saved()
saver(chapter)
if chapter == 4:
    pa("In the morning you decide to get going")
    pa("Should you ask Shelly if you can go to find the treasure?")
    print("1=Ask Shelly to go treasure hunting")
    print("2=See where the ocean brings you today")
    action = input("What do you do? ")
    if action == "1":
        voice("Shelly", "Treasure? Sounds like something a pirate would do")
        voice("Shelly", "So of course we can go treasure hunting!")
        pa("You and Shelly set sail on the great blue sea")
        chapter += 1
        saved()
    trip = 1
    while action == "2":
        if trip == 2:
            pa("When did we get back to land?")
        voice("Shelly", "Well, we should get going soon, prepare to set sail!")
        ship([drake, drake, drakek])
        pa("You see a small island in the distance")
        pa("After close inspection it looks like the island that you were at yesterday")
        pa("Should you head back there?")
        print("1=Go back to the island")
        print("2=Keep sailing and hopefully find new land")
        action = input("What do you do? ")
        if action == "1":
            chapter += 2
            saved()
saver(chapter)
if chapter == 5:
    pa("After sailing for a while you come across a small floating village")
    pa("It would probably be nice to check it out")
    pa("Stopping at the small village it looks fairly interesting")
    act = "0"
    while act != "3":
        pa("Where would you like to go?")
        print("1=Go fishing & make money")
        print("2=Stop at the inn to rest")
        print("3=Go back to the blue seas")
        act = input("What do you do? ")
        if act == "1":
            print("You go fishing in the shallow waters")
            roll = random.randint(1, 70)
            if roll <= 5:
                pa("You found some small fish, maybe you can sell them")
                mc.spend(3)
            elif roll <=40:
                pa("A beast pops out of the waters")
                enemy = drake
                mc.battle(enemy)
                if mc.get_health() > 0:
                    mc.levelup(enemy.get_exp())
                    mc.spend(6)
            elif roll <=65:
                pa("A monster attacks you from the water")
                enemy = drakek
                mc.battle(enemy)
                if mc.get_health() > 0:
                    mc.levelup(enemy.get_exp())
                    mc.spend(8)
            else:
                pa("Some kind of beast rises from the water")
                pa("The monster has giant tentacles")
                pa("It quickly attacks you")
                enemy = kraken
                mc.battle(enemy)
                if mc.get_health() > 0:
                    mc.levelup(enemy.get_exp())
                    mc.spend(10)
            enemy.reset()
        elif act == "2":
            pa("You stop at the inn for a short rest")
            voice("Inn Keeper", "Welcome to the east side inn")
            voice("Inn Keeper", "We have multiple different rooms")
            pa("You look at the different room options")
            pa("What room will you take?")
            print("1=normal room - 5 Gold")
            print("2=delux room - 12 Gold")
            print("3=Challenge room - 50 Gold")
            print("4=Leave the inn")
            print("Your Gold: ", mc.get_gold())
            action = input("What do you do? ")
            if action == "1" and mc.get_gold() >= 5:
                mc.spend(-5)
                mc.reset()
                mc.get_test()
                pa("You had a nice rest")
            elif action == "2" and mc.get_gold() >= 12:
                mc.spend(-12)
                mc.levelup(20)
                mc.reset()
                mc.get_test()
                pa("You feel refreshed after that")
            elif action == "3" and mc.get_gold() >= 50:
                voice("Inn Keeper", "Are you sure you want this?")
                print("1=No")
                print("2=Yes")
                choice = input("Are you sure? ")
                if choice == "2":
                    mc.spend(-50)
                    voice("Inn Keeper", "Your choice I guess")
                    mc.reset()
                    mc.get_test()
                    enemy = Starscrapper
                    pa("In your dreams some kind of monster attacks you")
                    mc.battle(enemy)
                    if mc.get_health() > 0:
                        mc.levelup(enemy.get_exp())
                        mc.spend(25)
            voice("Inn Keeper", "Come again soon")
    chapter += 1
    pa("You head back onto the great blue sea")
    saved()
saver(chapter)
if chapter == 6:
    pa("When you wake up you find that you've crashed onto shore")
    pa("There is sand all over your body")
    pa("It kind of hurts to walk but you have to find the ship")
    pa("Shelly has left the party")
    mc.new_party(0)
    pa("Walking across the beach you come across a large cave")
    pa("The cave looks to be made of some smooth stone")
    pa("Do you enter the cave?")
    print("1=Enter the cave")
    print("2=Keep walking")
    action = input("What do you do? ")
    if action == "2":
        pa("You keep walking across the beach side")
        pa("As time goes by it gets dark and you decide to rest")
        chapter += 2
        saved()
    else:
        pa("You slowly enter the cave")
        pa("After a while you get tired and decide to rest")
        chapter += 1
        saved()