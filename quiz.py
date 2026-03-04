import random

questions = [
    {"question": "What is the capital of India? =", "answer": "delhi"},
    {"question": "What is 5 + 7? =", "answer": "12"},
    {"question": "Which programming language is this quiz written in? =", "answer": "Python"},
    {"question": "What is the largest planet in our solar system? =", "answer": "Jupiter"},
    {"question": "Which ocean is the largest? =", "answer": "Pacific"},
    {"question": "Who is known as the father of computers? =", "answer": "charles babbage"},
    {"question": "How many continents are there on Earth? =", "answer": "seven"},
    {"question": "What is the chemical symbol for water? =", "answer": "h2o"},
    {"question": "Which is the longest river in the world? =", "answer": "nile"},
    {"question": "Who painted the Mona Lisa? =", "answer": "leonardo da vinci"},
    {"question": "Which is the smallest country in the world? =", "answer": "vatican city"},
    {"question": "How many legs does a spider have? =", "answer": "eight"},
    {"question": "What is the currency of Japan? =", "answer": "yen"},
    {"question": "Which gas do plants absorb from the atmosphere? =", "answer": "co2"},
    {"question": "Who discovered gravity? =", "answer": "newton"}

]

def kabiquiz():
    score = 0

    random.shuffle(questions) #each time change the questions order

    for i in questions:
        user_answer = input(i["question"]).strip()
        if user_answer.lower() == i["answer"].lower():
            score = score +1
            print("Correct!")
        else:
            print("SORRY this is Wrong!, The correct answer is:",i["answer"])
    

    percentage = (score/len(questions)*100)
    print("\n PERCENTAGE", percentage)

    if(percentage >= 90):
        print("You are A+ grade")
    elif(percentage >= 80):
        print("You are A grade")
    elif(percentage >= 70):
        print("You are B+ grade")
    elif(percentage >= 60):   
        print("You are B grade")
    elif(percentage >= 50):
        print("You are C grade")
    else:
        print("RE")

while True:
    kabiquiz()
    choice = input("\n Do you want to play again?(yes/no): ").strip().lower()
    
    if choice == "no":
        print("Program ended.")
        break
