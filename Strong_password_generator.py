#CODE BY YUVRAJ JWALA
import random  
import string 
chracter=['!','@','#','$','%','&'] 
def generatePassword(letter_count):  
    str1 = ''.join((random.choice(string.ascii_uppercase) for x in range(random.randint(1,letter_count-5))))
    str1 += ''.join((random.choice(string.ascii_lowercase) for x in range(random.randint(1,letter_count-5))))
    str1 += ''.join((random.choice(string.digits) for x in range(random.randint(1,letter_count-5))))  
  
    paswordList = list(str1)   
   #  random.shuffle(paswordList)   
    password = ''.join(paswordList)  
    return password  
print("\nPassword must contains atleast one uppercase and one lowercase letter \nand atleast 1 digit and special chracter\nPassword length should be more than 8 digits.\n")
question=input("Do you want Auto generated Strong Password : YES or NO : ")

if question=="YES"or question=="yes" or question=="Yes":
   letter_count=12
   password=generatePassword(letter_count) 
   length=len(password)
   for i in range(1-(length-letter_count)):
      password+=random.choice(chracter)
   password=list(password)
   random.shuffle(password)
   print("Your strong password : ",end="")
   for i in password:
      print(i.strip(),end='')

else:
   print("You can create your own one.")