#create calculater function
def calculator():
    
            print ("//  FOR FINE Addition ENTER  Add  //")
            print ("//  FOR FINE Subtraction ENTER Sub  //")
            print ("//  FOR FINE Multiplication ENTER Mul  //")
            print ("//  FOR FINE Division ENTER Div  //")
            
            Operations = input("Enter your Operations : ")
            num1 =float( input("Enter Number One : "))
            num2 =float (input ("Enter Number Two : "))
            if Operations.lower() == "add":
               print(f"Result: {num1 + num2}")
            elif Operations.lower() == "sub":
              print(f"Result: {num1 - num2}")
            elif Operations.lower() == "mul":
              print(f"Result: {num1 * num2}")
            elif Operations.lower() == "div":
                if num2==0:
                    print("Answer is 0")
                
                else :
                    print(f"Answer : {num1 / num2}")
                
            else :
                return("Enter Ivaild Operations")
                
                
def chatbot_response(user_input):
    if user_input.lower() == "hello":
        return "Hello! How can i assist you today ?"

    elif user_input.lower() == "how are you":
        return "I'm doing great — thanks for asking! 😊 How about you? How's your day going so far?"
        
    elif user_input.lower() == "hi":
        return "Hi! How can i assist you today ?"
        
    elif user_input.lower() == "what is your name":
        return "My name is Oshi 1.0 , I'm a Chatbot"
        
    elif user_input.lower() == "thank you":
        return "Anytime 😄 — you’re doing awesome, keep that energy up!"
       
        if user_input.lower () == "im good" or user_input.lower () == "im fine" :
          print ("Glad to hear that! 😄 \n ")
          print ("What are you working on today — studies, coding, or just relaxing?")
    
    elif user_input.lower() == "open cal":
        print ("ONLY TWO NUMBERS FOR CALCULATION ! ")
        calculator() #call calculatod function
        
    else :
        return(" I'm Still learnig sorry for your truble ! , Is there any way to help you ?")
        
                
print("HELLO!, What are you working on? ")
                
while True:
    user_input = input("You: ")
    if user_input.lower().strip() == "exit":
        print("Bot: Goodbye!")
        break
    response = chatbot_response(user_input)
    print("Bot:", response)