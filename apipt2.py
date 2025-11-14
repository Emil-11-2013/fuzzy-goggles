import requests
import random
import html

EDUCATION_CATEGORY_ID = 9
API_URL = f"https://opentdb.com/api.php?amount=10&category={EDUCATION_CATEGORY_ID}&type=multiple"
def get_quiz_questions():
    response = requests.get(API_URL)
    if response.status_code == 200:
     data = response.json()
    if data['response_code'] == 0 and data['results']:
        return data['results']
    else:               
            print("Error: Unable to fetch quiz questions.")
            return []

score = 0
print("Welcome to the Education Quiz!\n")

for i, q in enumerate(get_quiz_questions(), 1):
    question = html.unescape(q['question'])
    correct_answer = html.unescape(q['correct_answer'])
    incorrect_answers = [html.unescape(ans) for ans in q['incorrect_answers']]
    options = incorrect_answers + [correct_answer]
    random.shuffle(options)

    print(f"Q{i}: {question}")
    for idx, option in enumerate(options, 1):
        print(f"  {idx}. {option}")

    while True:
        try:
            answer = int(input("Your answer (1-4): "))
            if 1 <= answer <= 4:
                break
            else:
                print("Please enter a number between 1 and 4.")
        except ValueError:
            print("Invalid input. Please enter a number between 1 and 4.")

    if options[answer - 1] == correct_answer:
        print("Correct!\n")
        score += 1
    else:
        print(f"Wrong! The correct answer was: {correct_answer}\n")
        