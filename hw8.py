import random
class Basket:
    def __init__(self):
        self.__barrels = []
        for i in range(1,91): #for циклы
            self.__barrels.append(i)

    def getBarrel(self):
        if not self.isEmpty():
            barrel = random.choice(self.__barrels)
            self.__barrels.remove(barrel)
            return barrel
        else:
            print("My basket is empty")
            return False

    def isEmpty(self):
        if len(self.__barrels) > 0:
            return False 
        else:
            return True

class LotoPlayer:
    def __init__(self):
        self.__numbers = random.sample(range(1,91),15)
    def print(self):
        print("ВАША КАРТОЧКА")
        print("_______________________")
        for i in range(len(self.__numbers)):
            if i%5==0:
                print()
            print(self.__numbers[i],end=' ')
        print("\n_______________________")

    def ifNumInCard(self,num):
        if num in self.__numbers:
            return True
        else:
            return False
    def removeNum(self, num):
        if self.ifNumInCard(num):
            self.__numbers.remove(num)
            return True
        else:
            print("ТЫ ПРОИГРАЛ! Числа нет в твоей карточке")
            return False

    def next(self, num):
        if self.ifNumInCard(num):
            print("ТЫ ПРОИГРАЛ! Число имелось в твоей карточке")
            return False
        else:
            return True
    def ifWin(self):
        if len(self.__numbers)==0:
            return True
        else:
            return False

class LotoPlayerPC(LotoPlayer):
    def print(self):
        print("Карточка компьютера")
        LotoPlayer.print(self)
    def decision(self,num):
        if self.ifNumInCard(num):
            print("Комп решил зачернкуть")
            self.removeNum(num)
        else:
            print("Комп решил продолжить")
            self.next(num)
                    




myBasket = Basket()
player1 = LotoPlayer()
player2 = LotoPlayerPC()
rounds = 0 
# while(not player2.ifWin()):
#     player2.print()
#     barrel = myBasket.getBarrel()
#     print("Ваш бочонок: ",barrel)
#     player2.decision(barrel)
#     rounds+=1

print("Комп закончил игру за ",rounds," ходов")
lose = False
while (not player1.ifWin() and not lose and not player2.ifWin()):
    player1.print()
    print()
    player2.print()
    print()
    barrel = myBasket.getBarrel()
    rounds+=1
    player2.decision(barrel)

    print("Число бочонка: ",barrel)
    print("Зачеркиваем? y/n")
    answ = ""
    while (answ not  in ['y','n','Y','N']):
        answ = input()
        if answ in ["y","Y"]:
            print("Вы вычеркиваете")

            if (player1.removeNum(barrel)==False):
                lose = True
        elif answ in ["n","N"]:
            if (player1.next(barrel)==False):
                lose = True
        else:
            print("Некорректный ввод")

            
if player1.ifWin():
    print("Ура! Победа!")
else:
    print("В следующий раз повезет :-(")



