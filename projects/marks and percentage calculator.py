name = input("Enter your Name : ")
clas = input("Enter your Class : ")
roll = input("Enter your Roll no. : ")
Maths = int(input("Enter marks of Maths :"))+20
Hindi = int(input("Enter marks of Hindi :"))+20
English = int(input("Enter marks of English :"))+20
Science = int(input("Enter marks of Science :"))+20
Computer = int(input("Enter marks of Computer :"))+20
Sanskrit = int(input("Enter marks of Sanskrit :"))+20
Socialstudies = int(input("Enter marks of Socialstudies :"))+20

marks = [Maths,Hindi,English,Science,Computer,Sanskrit,Socialstudies]
total = sum(marks)

p = (total*100)/700
# pe = str(p)
# per = pe[:5]
per = str(p)[:5]

xyz = p>33
result = "Pass" if xyz == True else "Fail"


print(" ________________________________________________________________ ")
print("| |                                                               ")
print("| |                    RESULT OF SESSION 2025-26                  ")
print("| |                                                               ")
print(f"| | NAME : {name}                                                ")            
print(f"| | CLASS : {clas}                                               ")
print(f"| | ROLL NO {roll}:                                              ")
print("| |                                                               ")
print(f"| | ~Marks obtained in Maths : {Maths}/100                       ")            
print(f"| | ~Marks obtained in Hindi : {Hindi}/100                       ")
print(f"| | ~Marks obtained in English : {English}/100                   ")
print(f"| | ~Marks obtained in Science : {Science}/100                   ")
print(f"| | ~Marks obtained in Computer : {Computer}/100                 ")
print(f"| | ~Marks obtained in Sanskrit : {Sanskrit}/100                 ")
print(f"| | ~Marks obtained in Social Studies : {Socialstudies}/100      ")
print("| |                                                               ")
print(f"| |  Percentage ={p}                                             ")
print(f"| |  Total marks obtained : {total}                              ")
print(f"| |  {result}                                                    ")
print("| |                                                               ")
print("| | Thank you                                                     ")
print("| |                                                               ")
print(" ________________________________________________________________ ")
 

# print(type(p))
# print (total)
# print (per)
# print(result)