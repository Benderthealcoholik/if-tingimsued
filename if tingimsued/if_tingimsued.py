'''
nimi = input("siseta nimi: ")
age = int(input("vanus:"))

if nimi == "juku":
    if age <=1 and age>6:  
        print("pilet on tasuta")
    elif age >=6 and age <=14:
        print("lastespilet")
    elif age >=15 and age <=65:
        print("täispilet")
    elif age>65:
        print("sooduspilet")
    elif age<0 and age >100:
        print("viga")
    print("Trer, juku! lähme kinno!")
else:
    print("only for juku")'''
    
'''
nimi1 = 'Vanya'
nimi2 = 'Vasya'
name1 = input("sisesta nimi: ").lower()
name2 = input("sisesta nimi: ").lower()

if(nimi1.lower() == name1 and nimi2.lower() == name2) or (nimi1.lower() == name2 and nimi2.lower() == name1):    
    print("oh its pinginaaber")
else:
    print("ure not my stepnaaber")   ''' 




'''
# запросить длины стен комнаты
pikkus = float(input("ruumi pikkus in m: "))
laius = float(input("ruumi laius in m:"))

# задаем вычисление площади
pindala = pikkus * laius

# we do if ask about remont
soov = input("do u want remont(y/n): ")
if soov.lower() == "y":
    pricekvadrat = float(input("price per kvadrat: "))
    priceremont = pricekvadrat * pindala
    
    print("total cost: ", priceremont, "$" )
else:
    print("no remont fo u")    '''
  

'''
#запросить цену
alghind = float(input("alghind palun: "))

#проверить, превышает ли исходная цена 700

if alghind > 700:
    soodus = alghind * 7
    print('cena so skidkoi 30%: ', soodus)
else:
    print('cena bez')  '''
    

'''

t = float(input("kusi temperatuur: "))
if t > 18:
    print('temperatura tu mach')
else:
    orint('temperatura gud')    '''
    


'''#kusi pikkus

pikkus = float(input('teie pikkus palun: '))
sugu = input("teie sugu(m/n): ")
#erinev pikkus

luhike_naine = 150
luhike_mees = 160
pikk_mees = 180
pikk_naine = 170

if sugu == "m":
    if pikkus < luhike_mees:
        print("short man")
    elif pikkus <= pikk_mees:
        print("middle man")
    else:
        print("sa oled pikk mees")
elif sugu == "n":
    if pikkus < luhike_naine:
        print("short woman")
    elif pikkus <= pikk_naine:
        print("middle naine")
    else: print("tall woman")
else:
    print("u must print m or n")'''






