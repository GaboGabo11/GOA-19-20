#1) კომენტარების საშუალებით ახსენით განსხვავება insert და append შორის


#insert-ფუნქციით შეგიძლია ჩასვა მნიშვნელობა რომელ ინდექსეც გინდა ხოლო append ფუნქციით შენ შეგიძლია დაამატო მნიშვნელობა მარტო ინდექსის ბოლოში მაგალითად:
#insert ფუნქცია:

movies = ["Avatar" , "bad boys"]
 
movies.insert(2, "Good Boys")

print(movies)



#append ფუნქცია:


movies = ["Avatar" , "bad boys"]
 
movies.append( "Good Boys")

print(movies)