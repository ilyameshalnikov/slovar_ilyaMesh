print ("Привет,я словарик ,давай учить язык вместе :)\n")
def loe_fail(f):
    fail=open(f,'r',encoding="utf-8-sig")
    mas=[]
    for rida in fail:
        mas.append(rida.strip())
    fail.close()
    return mas

def list_faili(f,list):
    fail=open(f,'w',encoding="utf-8-sig")
    for k in list:
        fail.write(k+"\n")
    fail.close()
    return list

def save_fail(f,text):
    fail=open(f,'a',encoding="utf-8-sig")
    fail.write(text+"\n")
    fail.close()
    mas=[]
    mas=loe_fail(f)
    return mas



def uued_words():
        rus_sona=input("Введи слово на русском:\n")
        ing_sona=input("Введи слово на английском:\n")
        rus_list=save_fail("rus.txt",rus_sona)
        ing_list=save_fail("ing.txt",ing_sona)
        print(rus_list)
        print(ing_list)
        return rus_list,ing_list

def tolkimine(rus_list,ing_list):
    slovo=input("Введи слово для перевода:\n")
    if slovo in rus_list:
         ind=rus_list.index(slovo)
         print(f"{slovo}-{ing_list[ind]}")
    elif slovo in ing_list:
         ind=ing_list.index(slovo)
         print(f"{slovo}-{rus_list[ind]}")
    else:
         print(f"{slovo.upper()} отсутствует в словаре")
         v=input("Хотите добавить это слово в словарь?\n")
         if v.lower()=="да": uued_words()
def corrector(rus_list,ing_list):
    viga=input("Введите слово с ошибкой\n")
    if viga in rus_list:
        ind=rus_list.index(viga)#index
        print(f"Будет исправлена пара слов {viga}-{ing_list[ind]}")
        rus_list.pop(ind)
        ing_list.pop(ind)
        rus_list=list_faili("rus.txt",rus_list)
        ing_list=list_faili("ing.txt",ing_list)
        uued_words

      
    elif viga in ing_list:
         ind=ing_list.index(viga)
         print(f"Будет исправлена пара слов {viga}-{rus_list[ind]}")
         rus_list.pop(ind)
         ing_list.pop(ind)
         uued_words()
    else:
         print(f"{viga.upper()} отсутствует в словаре")
         rus_list=loe_fail("rus.txt")
         ing_list=loe_fail("ing.txt")
    return rus_list,ing_list


rus_list=loe_fail("rus.txt")
ing_list=loe_fail("ing.txt")
print(rus_list)
print(ing_list)

print("Я тут создал пару функций,выбери то что тебе больше нравится \n Нажми ")
while True:
    otv=input("1-Перевод слов\n2-Добавить слово\n3-Исправить ошибку\n4-Проверка знаний\nВыбери цифру:\n")
    if otv=="1":
         tolkimine(rus_list,ing_list)
    elif otv=="2":
        rus_list,ing_list=uued_words()
    elif otv=="3":
        print(rus_list,ing_list)
        rus_list,ing_list=corrector(rus_list,ing_list)
        print(rus_list,ing_list)
   #