money = input ("How much money you have: ")
divisor = money/50000
need = 50000-money
over= money%50000
overer= 50000-over
print ("Your money is", money)
print ("You can buy", divisor,"iphone")

if money <50000:
    print ("you need", need ," pesos to buy an iphone")
if money > 50000:
    print("You just need to have", overer, "pesos to buy another phone")
    
