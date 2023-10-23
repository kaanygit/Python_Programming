## calculator

def calculator(number1,number2,operation):
    if(operation=="+"):
        print("Toplama")
    elif(operation=="-"):
        print("Çıkarma")
    elif(operation=="/"):
        print("Bölme")
    elif(operation=="*"):
        print("Çarpma")

def main():
    number1=input(int())
    number2=input(int())
    operation=input(str("Operation : "))
    print(number1,number2,operation)
    if(not(operation=="+" or operation=="-" or operation=="/" or operation=="*")):
        print("Geçersiz işlem")
        main()
        
    
if __name__=="__main__":
    main()
