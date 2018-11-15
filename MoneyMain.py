import Money

cash = Money.Money(0,46)
cash1 = Money.Money(5,97)
cash2 = Money.Money(13, 254)    #format() carries cents over 100 to dollars
print(cash)
print(cash1)
print(cash2)

total = cash + cash1            #the sum of two money objects creates a new object
total_sum = total + cash2       #object total, can be used in special method __add__
print(total)
print(total_sum)

canada = cash.getCanadian()
euro = total.getEuro()          #new objects can use getter modules
colombia = total_sum.getColoPeso()
print(canada)
print(euro)
print(colombia)
