# შევქმნათ პროგრამა რომელსაც გადავცემთ მოსწავლეების სახელებს შემდეგ კი ეს პროგრამა ამ სახელებიდან რენდომულად ამოარჩევს თითოეულს და გაანაწილებს ჯგუფებში.

# list
    # append - ლისტის ბოლოს ამატებს ახალ ელემენტს
    # extend
    # remove - სიიდან შლის ნებისმიერ ელემენტს
    

# if else
# loop
# random 


import random 


group19_students = ["ანდრია ჯღამაძე", "ილიკო რაჯებაშვილი", "ლუკა გოგოხია", "მათე ფირანიშვილი",
 "ნიკა სოსელია", "ნიკოლოზ კოტრიკიძე", "ირაკლი დუდაშვილი", "ირაკლი გელაძე", "გიორგი ჭყონიძე", "გიორგი წიბლიაშვილი"]


all_group = []
group = []

while group19_students != []:
        random_student = (random.choice(group19_students))
        group.append(random_student)
        group19_students.remove(random_student)

        if len(group) == 3:
            all_group.append(group)
            group = []


random_group = random.choice(all_group)
random_group.append(group[0])


for i in range(3):
    print(all_group[i])



