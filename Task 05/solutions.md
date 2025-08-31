## Task 05
## TimeTickQuiz

 For this task, I had to build a Python quiz game that fetches questions from the Open Trivia API and also runs with a timer for each question. I’ll explain how I did it step by step:
### Step 1: Setting up the Environment

 The first thing I did was create a virtual environment (venv) for the project so that all dependencies stay isolated.
 
command:
          python3 -m venv venv
          source venv/bin/activate


Inside this venv, I installed the required modules like requests.

 Step 2: Fetching Questions from API

 I learned how to make an API call in Python using the requests library. I used the Open Trivia API to get quiz questions. The response came in JSON format, so I parsed it and extracted fields like:
 -question

 -options (incorrect + correct answers)

 -correct answer

### Step 3: Taking User Inputs

 I gave the player choices like:

 1.selecting category ID

 2.choosing difficulty level

 3.question type (multiple/boolean)

 4.number of questions

 This made the quiz customizable instead of fixed.

### Step 4: Displaying Questions & Checking Answers

 For each question, I displayed options, took input from the user, and checked if the selected option matched the correct answer. Based on that, I printed whether it was correct or wrong.

### Step 5: Adding a Timer with Threading

 This was the most important part.

 I used threading.Timer to give a fixed time for each question.

 If the user didn’t answer within the time, the timer expired, and the quiz automatically moved to the next question.

 If the user answered before time ended, I cancelled the timer and checked the answer.

 This made the quiz more interactive and challenging.

### Step 6: Error Handling

 I also added try/except blocks so that:

 If the user typed something invalid (like a letter instead of a number), the program didn’t crash.

 If the user pressed Enter without typing anything, it was handled properly.

### Step 7: Showing Final Score

 At the end of all questions, the program displayed the final score as:

 Quiz Over! Your final score is: X/Y where X is score and Y is len(questions).

