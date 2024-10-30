# დავალება: მომხმარებებელოს შემოატანინეთ range-ის დასაწყისი, საუნდა იდან დაიწყოს დიაპაზონის შექმნა, ასევე დასასრული, და სტეპი, (ანუ ნაბიჯი) , და ეს ჩასვით შემდეგ range-ში და გამოტანეთ რიცხვები.




Num1 = int(input("Enter Range Start:  "))
Num2 = int(input("Enter Range end:    "))
Num3 = int(input("Enter Range Step:   "))
for i in range(Num1, Num2, Num3):
    print(i)