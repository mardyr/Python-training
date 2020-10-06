int_var = 65
float_var = 3.1415926535897932384626433
formated_text = "%d %s %f %c %o %x %s"%(
    int_var,int_var,int_var,int_var,int_var,int_var,format(int_var,'b'))

print(formated_text)

formated_text = "{:o} {:x} {:b}".format(int_var,int_var,int_var)

print(formated_text)

#float_var = round(float_var,4)
print(float_var)

formated_text = f"Float ma wartosc {float_var:.5f}"
print(formated_text)

float_var *=1000
print(float_var)
formated_text = "Pomnożyłem razy 1000 i mam {:3.4f}".format(float_var)
print(formated_text)

formated_text = f"Formatuj {float_var:3.4f}"
print(formated_text)

width = 3
precision = 4
formated_text = f"TAKIE TANGO {float_var:{width}.{precision}f}"
print(formated_text)


width = 42
print("-"*width)
print("|  Czas  |      Zawodnik    |    Data    |")
print("*"*width)
print("| {:6.3f} | {:16s} | {:10s} |".format(9.58,"Usain Bolt","16.08.2009"))
print("| {:6.3f} | {:16s} | {:10s} |".format(9.69,"Tayson Gay","20.09.2009"))
print("| {:6.3f} | {:16s} | {:10s} |".format(9.69,"Yohan Blake","23.09.2012"))
print("| {:6.3f} | {:16s} | {:10s} |".format(9.74,"Asafa Powell","2.09.2008"))
print("-"*width)

width = 42
print("-"*width)
print("|  Czas  |      Zawodnik    |    Data    |")
print("*"*width)
print(f"| {9.58:6.3f} | {'Usain Bolt':16s} | {'16.08.2009':10s} |")
print(f"| {9.58:6.3f} | {'Tayson Gay':16s} | {'20.09.2009':10s} |")
print("| {:6.3f} | {:16s} | {:10s} |".format(9.69,"Yohan Blake","23.09.2012"))
print("| {:6.3f} | {:16s} | {:10s} |".format(9.74,"Asafa Powell","20.09.2008"))
print("-"*width)

