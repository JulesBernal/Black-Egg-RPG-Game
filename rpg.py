# Jules
# Egg - Auto moves?
# Taking severe damage ->


# Notes:
# Shield, Battle Axe, Tome, Dagger
# SB - 2X HP, Zerk - 1.5X HP, Book - 1.2X HP, Dagger- 1X HP
# SB - 1X ATK, Zerk- 1.5/2X ATK, Book - 1.4X ATK, Dagger - 3X ATK
# SB - 5X BLOCK, Zerk - 2X Block (OR NO BLOCK AND MORE DEF?),
#  Book - 1.5X DEF + 5X DEF (Once), Dagger - .8 BLOCK
# Ultimates: SB Copy Cat - ultimate eyes. 
# SB - Can no longer be hit, deal critical damage.
# Zerk - Survive Deadly Blow, friends with egg, -stun?
# Book - Restrict movement.
# Dagger - 6x atk, if friends with egg. - 12x atk.
# Shield Bearer, Berseker, Mage, Thief/Assassin
# Class: Primary Attack, block, dodge?, Ultimate (once)
import random
def gameStart():


    def choiceFnc(question,flag=False,ultFlag=False):
        inputCorrect=False
        while inputCorrect==False:
            choice = (input(f"{question} >"))
            if choice.lower()=='yes' and len(choice)>1 or choice.lower()=='no' and len(choice)>1:
                if choice.lower()=='yes':
                    return True
                elif choice.lower()=='no':
                    return False
                break
            elif len(choice)>1 and isinstance(choice,str) and flag==False: #is string
                break
            elif len(choice)==1 and isinstance(choice,str) and flag==False:
                if choice =='1' or choice =='2' or choice=='3' or choice=='4':
                    break
                print('Not a choice')
            # battle input sanitation
            elif len(choice)>1 and isinstance(choice,str) and flag==True:
                if choice.lower()=='attack':
                    choice=3.5
                    break
                elif choice.lower()=='block' or choice.lower()=='parry':
                    choice=7
                    break
                elif choice.lower()=='ultimate':
                    choice=10
                    break
                print('Not a choice')
            elif len(choice)==1 and isinstance(choice,str) and flag==True:
                if choice =='1' or choice =='2':
                    choice=int(choice)*3.5
                    break
                elif choice=='3' and ultFlag==False:
                    print('Ultimate not Ready.')
                elif choice=='3' and ultFlag==True:
                    choice=int(choice)*3.5
                    break
                print('Not a choice')
            else: 
                print('Not a choice')
        return choice

    monsters=["skeleton","sleepDemon","mothMan"]
    thisPlayer={
            "Name": "",
            "HP": 20,
            "Max HP": 20,
            "Atk": 5,
            "Block": 5,
            "Job": "",
            "AtkTxt": "",
            "BlockTxt": "",
            "ParryTxt": "",
            "Ultimate": False,
            "Ult Points": 0
        }
    thisEnemy={
            "Name": "",
            "HP": 25,
            "Max HP": 25,
            "Atk": 4,
            "Block": 4,
            "Job": "Enemy"
        }
    pClasses={
            "shield":(2,1,2,'slapped with their shield','blocked with their shield',"parries the opponent's attack back"),
            "axe":(1.5,1.8,1.2,'strikes hard with their axe','uses their axe to block',''),
            "book":(1.2,1.4,1.1,'conjures black magic with their tome',"blocks using the tome's magic",''),
            "dagger":(1,3,.8,'stabs with the deadly dagger','painfully blocks with the dagger','')
        }
    pEnemies={ #enemies seed, Name, HP,attack, block
        "skeleton":("Skeleton",1,1.5,0.8,'swings a giant femur down','raises a boney hand to block'),
        "sleepDemon":("Sleep Paralysis Demon",1,2,0,'attacks you with dreams of taxes','is unable to block'),
        "mothMan":("Moth Man",2,2,2,'swings their claws','shields themselves with their wings'),
        "dagger":("Chupacabra",2.2,2.2,2.2,'bites','throws a goat to shield themselves.')
    }
    enemies={ #enemies dictionary
        "skeleton":"",
        "sleepDemon":"",
        "mothMan":"",
        "dagger":""
    }
    def monsterSet(list):
        for item in list:
            enemies[item] = thisEnemy.copy()
            enemies[item]["Name"]=pEnemies[item][0]
            enemies[item]["HP"]*=pEnemies[item][1]
            enemies[item]["Max HP"]*=pEnemies[item][1]
            enemies[item]["Atk"]*=pEnemies[item][2]
            enemies[item]["Block"]*=pEnemies[item][3]
            enemies[item]["AtkTxt"]=pEnemies[item][4]
            enemies[item]["BlockTxt"]=pEnemies[item][5]
        return print('You feel a great rumbling all around you as deafening noises echoes through the door.')



    def playerInfo(input,flag='none'):
        if input=='player':
            return thisPlayer
        if input=='enemy':
            return thisEnemy
        if input =='intro':
            thisPlayer["Name"]=flag
        if input =='rest':
            print(f"Your Health has been restored.\t{thisPlayer['HP']} -> {thisPlayer['Max HP']}")
            thisPlayer["HP"]=thisPlayer["Max HP"]

        if input=='start':
            if len(flag)==1:
                pickedClass=list(pClasses)[int(flag)-1]
            else:
                pickedClass=flag.lower()
            thisPlayer["Job"]=pickedClass
            thisPlayer["HP"]*=pClasses[pickedClass][0]
            thisPlayer["Max HP"]*=pClasses[pickedClass][0]
            thisPlayer["Atk"]*=pClasses[pickedClass][1]
            thisPlayer["Block"]*=pClasses[pickedClass][2]
            thisPlayer["AtkTxt"]=pClasses[pickedClass][3]
            thisPlayer["BlockTxt"]=pClasses[pickedClass][4]
            thisPlayer["ParryTxt"]=pClasses[pickedClass][4]


    def restAction():
        rest=choiceFnc('Do you wish to take a short rest?')
        if rest==True:
            playerInfo('rest')
            return
        if rest==False:
            return print(f'You have chosen to not rest.')


    def fight(monster):
        battleStatus = battle(thisPlayer,enemies[monster])
        if battleStatus==False:
            return [False,choiceFnc('Do you wish to retry?')]
        restAction()
        return True

    # def battle(player,enemy,egg):
    def battle(player,enemy,egg=False):
        def attack(attacker,defender,atkInput,defInput):
            tempHP=defender["HP"]
            tempAHP=attacker["HP"]
            if defInput<6.5 and atkInput<10.5: #Defender does not block.
                defender["HP"] -= attacker["Atk"]
                print(f"{attacker['Name']} {attacker['AtkTxt']}.\n{defender['Name']} is hit.")
                print(f"{defender['Name']}'s HP: {tempHP}\t->\t{defender['HP']}")
            elif defInput>=6.5 and atkInput<10.5 and defender["Job"]!="Shield": # Defender blocks
                if (attacker["Atk"] - defender["Block"])<=0:
                    defender["HP"]-=0
                elif (attacker["Atk"] - defender["Block"])>0:
                    defender["HP"] -= attacker["Atk"] - defender["Block"]
                print(f"{attacker['Name']} {attacker['AtkTxt']}.\n{defender['Name']} {defender['BlockTxt']}.")
                print(f"{defender['Name']}'s HP: {tempHP}\t->\t{defender['HP']}")
            
            elif defInput>=6.5 and atkInput<10.5 and defender["Job"]=="Shield": #shield parries
                attacker["HP"]-=abs(attacker["Atk"] - defender["Block"])
                print(f"{attacker['Name']} {attacker['AtkTxt']}.\n{defender['Name']} {defender['ParryTxt']}.")
                print(f"{attacker['Name']}'s HP: {tempAHP}\t->\t{attacker['HP']}")
            elif atkInput>6.5 and attacker["Job"]!='Shield':  #both parties block. 
                print(f"{attacker['Name']} and {enemy['Name']} both blocked.")

            elif atkInput==10.5 and attacker['Ultimate']==True: #Ultimate battle
                print(f"ULTIMATEEEEEEEEEEE")
                print(f"{attacker['Name']} {attacker['AtkTxt']}.\n{defender['Name']} is hit.")
                print(f"{defender['Name']}'s HP: {tempHP}\t->\t{defender['HP']}")
            elif atkInput==10.5 and attacker['Ultimate']==False:
                print("Ultimate not ready yet,")
            
            

        while not (enemy["HP"]<0 or player["HP"]<0):
            print(f"\n{enemy['Name']}\t\t{enemy['HP']} / {enemy['Max HP']}")
            print(f"1. ATTACK\n2.BLOCK\n3.ULTIMATE\t\t({player['Ult Points']}/10)")
            print(f"{player['Name']}\t\t{player['HP']} / {player['Max HP']}")

            enemyChoice =   random.randint(1,10)
            if player["Job"]=="shield" and enemyChoice>6:
                print(f"{enemy['Name']} is going to block.")
            elif player["Job"]=="shield" and enemyChoice <=6:
                print(f"{enemy['Name']} is going to attack.")
            attackerChoice=   choiceFnc('Command?',True)
            if attackerChoice<7:
                attack(player,enemy,attackerChoice,enemyChoice)
                player["Ult Points"]+=1
            if enemyChoice<=6.5 and enemy["HP"]>0:
                attack(enemy,player,enemyChoice,attackerChoice)
                player["Ult Points"]+=1
        player["Ult Points"]=0
        player["Ultimate"]=False
        if player["HP"]<0:
            print('You have been defeated.')
            return False
        print(f"{enemy['Name']} has been defeated")
        return [True]
        
    
    def loopChoice(flagChoice,flagInitQ,flagRepeatQ):
        pChoice = choiceFnc(flagInitQ)
        while pChoice.lower()!=flagChoice.lower():
            pChoice=choiceFnc(flagRepeatQ)
    
    def consoleColor(code):
        return f'\033[{code}m'

    print('You wake up with a headache in a dimly lit room.')
    playerInfo('intro',choiceFnc('What is your name?\t'))
    print(f"Your name is \033[31;1;4m{playerInfo('player')['Name'].upper()}\033[0m")

    # print("The table beckons you forth, drawing your attention to it.")
    # loopChoice('yes','Do you go to the table?','You try to pull away from the table. Your hand now rests, pulling you to make a decision.')

    # print('Before you lay four weapons, each of different schools.')
    # print('First, a shield with a crest of the hare. Second, an axe.\nThird, a mysterious tome. Lastly, a pair of ominous daggers.')
    print('Pick your weapon.    Pick your class.')
    option = (choiceFnc('What do you choose? '))

    playerInfo('start',option)
    monsterSet(monsters)
    

    print(thisPlayer)
    print(enemies[monsters[0]]) #
    # print(f"{thisPlayer['Name']} the {thisPlayer['Job']}")
    # print('get ready to fight')
    # battle(thisPlayer,enemies[monsters[0]]) # Skeleton fight
    
    fSeg=fight(monsters[0])
    if fSeg[0]==False:
        print(fSeg)
        return fSeg[1]

gameStatus=True
while gameStatus==True:
    gameStatus=gameStart()


print('The End\nThank you for playing!')