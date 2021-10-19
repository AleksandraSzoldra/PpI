a=int(input("Podaj a: "))
b=int(input("Podaj b: "))
c=int(input("Podaj c: "))

p=(a+b+c)*0.5
P=(p*(p-a)*(p-b)*(p-c))**0.5
print ("Pole trójkąta wynosi: ",P) 