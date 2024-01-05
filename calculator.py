def addition(num1,num2):
    return num1 + num2

def subtraction(num1,num2):
    return num1 - num2

def multiplication(num1,num2):
    return num1 * num2

def division(num1,num2):
    return num1 / num2

def selectNumber():
    print("Yapmak istediğiniz işlemi girin= ")
    try:
        num1 = int(input("1.sayıyı girin="))
        num2 = int(input("2.sayıyı girin="))
        return num1,num2
    except ValueError:
        print("Tip uyuşmazlığı: Sayı girin.")
        return selectNumber()
    except:
        print("Bir hata oluştu.Tekrar dene")
        return selectNumber()

def selectOperator():       
    operators = ["+","-","*","/"]

    opt = input("Bir operator seçiniz\n+\n-\n*\n/\nopt:")
    print("**********************************")
    if opt in operators:
        return opt
    else:
        print("Geçerli bir operatör seçilemedi.Tekrar dene")
        return selectOperator()         
    
        
num1,num2 = selectNumber()

opt = selectOperator()


if opt == "+":
    print("Sonuc=" + str(addition(num1, num2)))
elif opt == "-":
    print("Sonuc=" + str(subtraction(num1, num2)))
elif opt == "*":
    print("Sonuc=" + str(multiplication(num1, num2)))
elif opt == "/":
    print("Sonuc=" + str(division(num1, num2)))
else:
    print("Geçerli bir operator seçilemedi.")

