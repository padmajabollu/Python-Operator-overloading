class currency(object):

    cv = {"Rs":1,"$":60,"#":90,"E":70}

    def __init__(self, value, unit):
        self.value = value
        self.unit = unit

    def __str__(self):
        return str(self.value) + " " + self.unit

    def __add__(self,other):
        if isinstance(other, currency):
            v = (self.value*currency.cv[self.unit] + other.value*currency.cv[other.unit])*1.0
            return currency(v,"Rs")
        else:
            return other + self

    def __radd__(self,other):
        v = (self.value*currency.cv[self.unit]) + other
        return currency(v, "Rs")

    def __sub__(self,other):
        if isinstance(other, currency):
            v = (self.value*currency.cv[self.unit] - other.value*currency.cv[other.unit])
            if v<0:
                v=-(v)
            return currency(v, "Rs")
        else:
            v = self.value - other
            return currency(v, self.unit)

    def __rsub__(self,other):
        v = (self.value*currency.cv[self.unit]) - other
        if v<0:
            v=-(v)
        return currency(v, "Rs")

    def __mul__(self,other):
        if isinstance(other, currency):
            v = (self.value*currency.cv[self.unit] * other.value*currency.cv[other.unit])
            return currency(v,"Rs")
        else:
            return other * self

    def __rmul__(self,other):
        v = (self.value*currency.cv[self.unit]) * other
        return currency(v, "Rs")

while True:
    try:
        print()
        print("***"*20)
        print("\nEnter Value for Currency object 1 :")
        value1=int(input())
        print("\nEnter Unit for Currency object 1 :")
        unit1=(input())
        print("\nEnter Value for Currency object 2 :")
        value2=int(input())
        print("\nEnter Unit for Currency object 2 :")
        unit2=(input())
        break
    except:
        print("\nEnter Valid Data.........")
        continue

c1=currency(value1,unit1)
c2=currency(value2,unit2)


while True:
    print()
    print("***"*20)
    print("1.Addition of money")
    print("2.Substraction of money")
    print("3.Multiplication of money")
    print("4.Exit\n")
    ch=int(input())
    if ch==1:
        while True:
            print()
            print("***"*20)    
            print("1.Result want in Rs(Rupees)")
            print("2.Result want in $(Doller)")
            print("3.Result want in #(Pond)")
            print("4.Result want in E(Euro)")
            print("5.Exit\n")
            ch1=int(input())
            if ch1==1:
                Result=c1+c2
                print(c1," + ",c2," = ",Result)

            elif ch1==2:
                Result=c1+c2
                Result.value=Result.value/currency.cv["$"]
                Result.unit="$"
                print(c1," + ",c2," = ",Result)
            elif ch1==3:
                Result=c1+c2
                Result.value=Result.value/currency.cv["#"]
                Result.unit="#"
                print(c1," + ",c2," = ",Result)

            elif ch1==4:
                Result=c1+c2
                Result.value=Result.value/currency.cv["E"]
                Result.unit="E"
                print(c1," + ",c2," = ",Result)

            elif ch1==5:
                break
            
            else:
                print("\nWrong Choice.......")

    elif ch==2:
        while True:
            print()
            print("***"*20)    
            print("1.Result want in Rs(Rupees)")
            print("2.Result want in $(Doller)")
            print("3.Result want in #(Pond)")
            print("4.Result want in E(Euro)")
            print("5.Exit\n")
            ch1=int(input())
            if ch1==1:
                Result=c1-c2
                print(c1," - ",c2," = ",Result)

            elif ch1==2:
                Result=c1-c2
                Result.value=Result.value/currency.cv["$"]
                Result.unit="$"
                print(c1," - ",c2," = ",Result)
            elif ch1==3:
                Result=c1-c2
                Result.value=Result.value/currency.cv["#"]
                Result.unit="#"
                print(c1," - ",c2," = ",Result)

            elif ch1==4:
                Result=c1-c2
                Result.value=Result.value/currency.cv["E"]
                Result.unit="E"
                print(c1," - ",c2," = ",Result)

            elif ch1==5:
                break
            
            else:
                print("\nWrong Choice.......")

    elif ch==3:
        while True:
            print()
            print("***"*20)    
            print("1.Result want in Rs(Rupees)")
            print("2.Result want in $(Doller)")
            print("3.Result want in #(Pond)")
            print("4.Result want in E(Euro)")
            print("5.Exit\n")
            ch1=int(input())
            if ch1==1:
                Result=c1*c2
                print(c1," * ",c2," = ",Result)

            elif ch1==2:
                Result=c1*c2
                Result.value=Result.value/currency.cv["$"]
                Result.unit="$"
                print(c1," * ",c2," = ",Result)
            elif ch1==3:
                Result=c1*c2
                Result.value=Result.value/currency.cv["#"]
                Result.unit="#"
                print(c1," * ",c2," = ",Result)

            elif ch1==4:
                Result=c1*c2
                Result.value=Result.value/currency.cv["E"]
                Result.unit="E"
                print(c1," * ",c2," = ",Result)

            elif ch1==5:
                break
            
            else:
                print("\nWrong Choice.......")

    elif ch==4:
        break

    else:
        print("\nWrong Choice.......")


Currency1=currency(6,"$")

Currency2=currency(50,"Rs")

Currency3=currency(3,"E")

Currency4=currency(100,"Rs")

Currency5=currency(5,"E")

Currency6=currency(1,"$")

Result=Currency1+Currency2
Result.value=Result.value/currency.cv["$"]
Result.unit="$"
print(Currency1," + ",Currency2," = ",Result)

Result= Currency3+Currency6-Currency4
Result.value=Result.value/currency.cv["E"]
Result.unit="E"
print(Currency3," + ",Currency6," - ", Currency4 ," = ",Result)
Result=20+Currency5
Result.value=Result.value/currency.cv["E"]
Result.unit="E"
print("20 + ",Currency5," = ",Result)
