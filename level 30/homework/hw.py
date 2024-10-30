def odd_even():
   num = int(input("Enter ur number:" ))
   if num % 2 == 0:
      print("even")
   else:
      print("odd")   


def age():  
  age =int(input("enter your age: "))
  if age > 18:
     print("სრულწლოვანი ხარ")
  else:
    print("არასრულწლოვანი ხარ")    



def sum():
    sum = 0
    for i in range(1, 11):
        sum += i
        print("1 დან 10 ის ჩათვლით რიცხვების ჯამი არის: ", sum)


