#შექმენით სია, რომელშიც იქნება 10 ელემენტი. ამ სიის ბოლოში ჩაამატეთ რიცხვი - 1121. და ამოშალეთ
#მეორე ინდექსზე მდგომი  ელემენტი და გამოიტანეთ სია ტერმინალში (დაპრინტეთ)

lis = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 1121]
lis.remove(1121)
print(lis)


#შექმენით სია და ამ სიაში ჩაამატეთ ახალი სიიდან თითოეული ელემენტი. (თვითონ სია არ ჩაამატოთ)

lis = [1, 2, 3]
lis1 = [4,5,6]
lis.extend(lis1)
print(lis)

#შექმენით სია სადაც ჩაწერთ ციფრებს 1-დან 8-ის ჩათვლით. for loop-ის საშუალებით მიწვდით თითოეულ ელემენტს და გამოიტანეთ
#ტერმინალში რომელი ციფრია ლუწი და რომელი კენტი.

lis = [1, 2, 3, 4, 5, 6, 7, 8]
for i in lis:
    if i % 2 ==0:
        print(i, "Even")
    else:
        print(i, "Odd")