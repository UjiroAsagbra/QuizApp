import random
import time
from string import ascii_lowercase

Welcome_msg = '''----------Lets see how smart you are----------
----------Pick a topic and answer some questions----------
----------The more scores you get, the smarter you are----------'''
print(Welcome_msg)
time.sleep(1)
Name = input("Whats your name?: ")
time.sleep(1)
print(f"Welcome {Name.capitalize()}, shall we begin?" )
time.sleep(2)

Questions = {"How many legs does the Legs of Man have?":["Three", "Two", "Five", "Four"],
"How many tails does a Manx cat have?" :["None", "One", "THree", "Six"],
"How many teeth does an aardvark have?" :["None", "Seven", "Four", "Two"],
"Which sea creature has three hearts?" :["Octopus", "Sea horse", "Shark", "Dolphin"],
"Which instrument has forty-seven strings and seven pedals?" :["Harp", "Guitar", "Cello", "Violin"],
"Whose face was said to have launched 1,000 ships?" :["Helen of Troy", "Cleopatra", "Athena", "Hera"],
"In the traditional rhyme, how many mice were blind?": ["Three", "Five", "Eight", "Four"],
"How many bones does an adult human have?" :["Two hundred and six", "One hundred and seven", "One hundred and six", "Two hundred and seven"],
"How many pedals do most modern pianos have?": ["Three", "One", "Two", "None"],
"Water boils at 212 degrees on which temperature scale?": ["Fahrenheit","Celsius", "Kelvin", "Newton"]}

Num_questions_per_quiz = 5

def run_quiz():
    questions = prepare_questions(
        Questions, num_questions=Num_questions_per_quiz
    )

    num_correct = 0
    for num, (question, options) in enumerate(questions, start=1):
        print(f"\nQuestion {num}:")
        num_correct += ask_question(question, options)

    print(f"\nYou got {num_correct} correct out of {num} questions")


def prepare_questions(questions, num_questions):
    num_questions = min(num_questions, len(questions))
    return random.sample(list(questions.items()), k=num_questions)

def ask_question(question, options):
    correct_answer = options[0]
    ordered_options = random.sample(options, k=len(options))

    answer = get_answer(question, ordered_options)
    if answer == correct_answer:
        print("⭐ Correct! ⭐")
        return 1
    else:
        print(f"The answer is {correct_answer!r}, not {answer!r}")
        return 0

def get_answer(question, options):
    print(f"{question}?")
    labeled_options = dict(zip(ascii_lowercase, options))
    for label, options in labeled_options.items():
        print(f"  {label}) {options}")

    while (answer_label := input("\nChoice? ")) not in labeled_options:
        print(f"Please answer one of {', '.join(labeled_options)}")

    return labeled_options[answer_label]



if __name__ =="__main__":
    run_quiz()

