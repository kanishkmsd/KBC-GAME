def questions():
    questions_list = ["The Rath Yatra at Puri is celebrated in honour of which Hindu diety?",
                      "The Indian National Calendar is based on:",
                      "Which of the following is a folk dance of India?",
                      "Who is the only Vice President of India to have worked under three different Presidents?",
                      "Who wrote the Saraswati Vandana 'Var de Veenavaadini var de'?",
                      "Who became the first Indian to score a century before lunch in the opening session of a Test Match in June 2018?",
                      "In which of these sports would you normally see the referee running on the field?",
                      "Madhuri Dixit's 'Bucket List' is her film in which language?",
                      "What characteristics of a leopard is used by scientists to identify them individually?",
                      "Which of these national flags has the most number of stars on them?",
                      "Which of these food items has different varieties such as ‘Suji ka _______’. ‘Aate ka _______’, ‘Moong dal ka __________’ and ‘Gajar ka _______________’?",
                      "Which of these is the name of a type of women's clothing?",
                      "Which of these actresses became known as the 'Hawa-Hawai' girl?",
                      "Samukha, Vighnaharta and Ekadanta are other names for which Hindu god?",
                      "Which of these foods would complete the name of these three common dishes: Kadhai _______, Shahi _______, and Matar ______?",
                      "Which animal is known as the ‘Ship of the Desert?",
                      "How many letters are there in the English alphabet?",
                      "What do you call the person who brings a letter to your home from post office?",
                      "How many consonants are there in the English alphabet?", "Which country is Delhi located in?"]
    option1 = ["Ram", "Cristian era", "Kathakkali", "S Radhakrishnan ", "Jaishankar Prasad", "Lokesh Rahul", "Cricket", "English", "Pugmarks", "USA", "Sharbat ", "Padmini  ", "Sridevi", "Brahma", "Dahi", "cat","22","postman","27","USA"]
    option2 = ["Vishnu", "Saka era", "Bihu", "Bhairo Singh Shekhawat ", "Sumitranandan Pant", "Shikhar Dhawan ", "Football", "Hindi  ", "Spot patterns ", "Brazil", "Halwa   ", "Man Bai  ", "Hema Malini  ", "Krishna", "Ghee", "camel","28","police","29","India"]
    option3 = ["Shiva", "Vikram era", "Garba", "B D Jatti", "Ramdhari Singh 'Dinkar' ", "Ajinkya Rahane ", "Badminton  ", "Marathi", "Tail", "Australia  ", "Pakora  ", "Jodha    ", "Rekha", "Rama ","Paneer ", "cow","26","doctor","32","Switzerland"]
    option4 = ["Jagganath", "Hijii era", "Mannipuri", "Hamid Ansari ", "Suryakant Tripathi 'Nirala'", "Rohit Sharma", "Tennis ", "Telugu ", "Whiskers", "New Zealand", "Chaat", "Anarkali ", "Madhuri Dixit", "Ganesha", "Khoya", "bull","29","teacher","21","England"]
    answer_list = ["D", "B", "C", 'D', 'D', 'B', 'B', 'C', 'B', 'A', 'B', 'D', 'A', 'D', 'C', 'B', 'C', 'A', 'D', 'B']
    prize = [1000, 2000, 3000, 5000, 10000, 20000, 40000, 80000, 160000, 320000, 640000, 1250000, 2500000, 5000000, 10000000]
    lifelines=["flip", "expert", "phone"]
    guarantee_point1 = 10000
    guarantee_point2 = 320000
    guarantee_point3 = 10000000
    import random
    m = -1
    amt=0
    while range(0, 16):
     i = random.randrange(0, len(questions_list))
     playsound("4. Next Question.mp3", False)
     print(questions_list[i])
     print(f'''
A- {option1[i]}                    
B- {option2[i]}
C- {option3[i]}                    
D- {option4[i]}''')
     while True:
      answer = input("Enter your choice: ").upper()
      playsound("9. Lock (mp3cut.net).mp3")
      if answer == answer_list[i]:
            print("You're answer is correct!")
            for j in range(m+1,15):
             print(f"\nYou've won {prize[j]}\n")
             m=m+1
             if prize[j] == guarantee_point1:
                print("\nCongrats! You have passed the first Guarantee point!\n")
                amt = guarantee_point1
             elif prize[j] == guarantee_point2:
                print("\nCongrats! You have passed the Second Guarantee point!\n")
                amt = guarantee_point2
             elif prize[j] == guarantee_point3:
                print("\nCongrats! You have won 1 Crore!")
                quit()
             playsound("2-1-10001 (mp3cut.net).mp3")
             break
            break
      elif answer == "PHONE":
         if lifelines.__contains__("phone"):
             print("Your time starts now!!")
             playsound("12. Phone A Friend.mp3", False)
             from threading import Timer
             def timeout():
                 print("Time over")
             # duration is in seconds
             t = Timer(19, timeout)
             t.start()
             # wait for time completion
             t.join()
             lifelines.remove("phone")
             continue
         else:
             print("You've used this lifeline!!")
             continue
      elif answer == "FLIP":
         if lifelines.__contains__("flip"):
             print("Your flipped question is:\n")
             lifelines.remove("flip")
             break
         else:
             print("You've used this lifeline!!")
             continue
      elif answer == "EXPERT":
          if lifelines.__contains__("expert"):
              print(f"Expert says: {answer_list[i]}")
              lifelines.remove("expert")
              continue
          else:
              print("You've used this lifeline!!")
              continue

      elif answer == "QUIT":
            playsound("2-1-10001 (mp3cut.net).mp3", False)
            print(f"\nYou've won Rs. {prize[j]} ")
            delay = input("Press enter to finish")
            quit()
      elif answer != answer_list[i]:
            playsound("10. Wrong Answer.mp3", False)
            print("\nSorry, you have failed!")
            if amt >= 10000:
                print(f"\nYou've won Rs. {amt}")
                delay = input("Press enter to finish")
                quit()
            else:
                print("\nYou have won nothing!")
                delay = input("Press enter to finish")
                quit()
      else:
            print("I don't understand!!")
            continue
     questions_list.pop(i)
     option1.pop(i)
     option2.pop(i)
     option3.pop(i)
     option4.pop(i)
     answer_list.pop(i)
# Main Program
from playsound import playsound
playsound("kbc_break.mp3", False)
print("Welcome to KBC! :)")
user_name = input("Please enter your name: ")

print('''
Instructions:
1. You will get 4 options for each question.
2. There will be two Gaurantee points, each at Rs.10,000 and Rs. 3,20,000
3. You will get three lifelines: Flip the question, phone a friend and expert advice.
   To use them:
   Flip the question = Type flip 
   Phone a friend = Type phone
   Expert advice = Type expert
4. There will be 15 Questions. Each will win you a certain amount of money.
5. You can quit whenever you want to keep your earnings. 
6. To quit : Type quit in the answers place.
''')

print(f'''Good luck {user_name}!!
To start press enter!''')
inp = input("")
if inp == "":
    questions()
