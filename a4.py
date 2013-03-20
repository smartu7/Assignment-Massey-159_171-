#159.171 Assignment 1
#Student: Raymond Ji
#Student ID: 12198108
#Email: jizongshan@sina.com
#Tutorial Time: Friday, 09:00-11:00

def myInfo() :
    student = "Raymond Ji"
    studentID = "12198108"
    email = "jizongshan@sina.com"
    tutorialTime = "Friday, 09:00-11:00"
  
    printNow("*****************************")
    printNow( " Student: " + student)
    printNow( " Student ID: " + studentID)
    printNow( " Email: " + email)
    printNow( " Tutorial Time: " + tutorialTime)
    printNow("*****************************")

count =0
def x() :
# function to calculate this function is called how many times
    global count
    count +=1
    printNow("Called " +str(count) + " times")

def translate(word,language) :
# function to translate the 'cat' and 'dog' to different luanguage
    if (word == "cat") :
      if (language == "German") :
           printNow("The translation of cat into German is katze")
      elif language == "French") :
           printNow("The translation of cat into French is chat")                  
      elif language == "Spanish") :
           printNow("The translation of cat into Spanish is gato")
      else:
           printNow("No this language")
    elif (word == "dog") :
      if (language == "German") :
           printNow("The translation of dog into German is hund")
      elif language == "French") :
           printNow("The translation of dog into French is chien")
      elif language == "Spanish") :
           printNow("The translation of dog into Spanish is perro")
      else:
           printNow("No this language")
      
myInfo()
x()
x()
x()
translate("dog","German")
