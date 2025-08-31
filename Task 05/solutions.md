## Task 05
##### Actually this is the task to create a quiz with a timer.
### Goal:

##### I built a quiz game that fetches questions from the Open Trivia Database API.

##### Each question has a time limit using threading and timers.

### Technologies Used:

##### Python

##### requests → to fetch categories and questions from API

##### threading.Timer → to enforce a time limit

##### random → to shuffle answer options
 
##### time → for countdown functionality

### How it works:

##### The program first fetches categories from the API.

##### User selects category, difficulty, type of questions, and number of questions.

### For each question:

#####  Options are shown in random order.

##### A 15-second timer runs in the background.

#####If the user answers in time → program checks correctness.

##### If time runs out → automatically moves to the next question.

##### At the end → user’s final score is displayed.

### Key Features:

##### Real-time countdown using threading.Timer.

#####  Error handling with try/except for invalid input.

##### Automatic skip when time finishes.

#####  Learning Outcome:

##### I learned about API usage, threading in Python, and exception handling.

##### Understood how to combine different Python modules to build an interactive program.
