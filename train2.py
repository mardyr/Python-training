
try :
    num = int("es2")
    print(n)
except :
    print("Wrong data type")

def dziel(a,b):
    if b==0 :
        raise Exception("Uwaga! Drugi argument dzielenie musi być różny od zera")
    else :
        return a/b

try:
    value = dziel(5,0)
    print(value)
except Exception as e:
    print(e)

'''
try:
    fine_numb = int({1,2,4,5})
except ValueError:
    print("Ten tekst to nie liczba")
    fine_numb = 0
except TypeError:
    print("Argument dla rzutowania int() powinien być napisem")
    fine_numb = 0
finally:
    print("ta sekcja wykona się zawsze")
    fine_numb +=1

print(fine_numb)
'''