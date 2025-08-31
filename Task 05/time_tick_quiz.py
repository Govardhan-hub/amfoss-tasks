# time_tick_quiz.py

import requests
import html
import random
import threading
import time

CATEGORY_URL = "https://opentdb.com/api_category.php"
QUESTION_URL = "https://opentdb.com/api.php"
TIME_LIMIT = 15  # seconds per question

# ------------------ api functionss ------------------

def fetch_categories():
    """
    fetches trivia categories from the API.
    """
    response=requests.get(CATEGORY_URL)
    data=response.json()
    categories=data["trivia_categories"]
    return categories

def fetch_questions(category=None , difficulty=None , q_type=None , amount=10):
    """
    fetches the questions based on given filters.
    """
    params={
        "amount":amount
    }
    if category:
        params["category"] = category
    if difficulty:
        params["difficulty"] = difficulty
    if q_type:
        params["type"] = q_type

    response=requests.get(QUESTION_URL,params=params)
    data=response.json()
    questions=data["results"]
    return questions
# ------------------ user input selection ------------------

def select_category(categories):
    """
    prompts user to select a category from the list.
    """
    for cat in categories:
        print(cat["id"],"-",cat["name"])
    cat_id=int(input("Enter the category id :"))
    return cat_id

def select_difficulty():
    """
    prompst user to select question difficulty.
    """
    difficulty=input("Enter the difficulty :").lower()
    return difficulty
def select_question_type():
    """
    prompts the user to select type of questions (multiple/boolean).
    """
    q_type = input("Enter the question type(multiple/boolean): ").lower()
    return q_type 

# ------------------ quiz logicc ------------------

def ask_question(questions):
    """
    presents a question to the user with a countdown timer.
    """
    score=0
    question_number = 1
    for q in questions:
        print(f"\nQuestion{question_number} : {q['question']}")
    
        options = q["incorrect_answers"] + [q["correct_answer"]]
        random.shuffle(options)

        for i in range(len(options)):
            print(f"{i+1}.{options[i]}")

        def time_up():
            print("Your time has completed!. Moving to the next question.Please click ENTER ")
        timer = threading.Timer(TIME_LIMIT,time_up)
        timer.start()

        try:
            choice = int(input("Enter your choice : "))
            timer.cancel()

            if options[choice-1] == q["correct_answer"]:
                print("Yes your answer is correct! ")
                score+=1
            else:
                print("Oh! Your answer is wrong")
        except Exception:
            print("Invalid input or no answer is given")

        question_number+=1
        
    print(f"\nQuiz over! your final score is: {score}/{len(questions)}")
    
def select_quiz_options(categories):
    """
    gathers all the quiz options and fetch questions accordingly.
    """
    cat_id = select_category(categories)
    difficulty = select_difficulty()    
    q_type = select_question_type()
    amount = int(input("How many questions do you want? "))

    questions = fetch_questions(
        category=cat_id,
        difficulty=difficulty,
        q_type=q_type,
        amount=amount
    )
    return questions

# ------------------ main fucntion ------------------

def main():

    """
    Entry point for the TimeTickQuiz game.
    """
    categories = fetch_categories()
    questions = select_quiz_options(categories)
    ask_question(questions)
if __name__ == "__main__":
    main()
