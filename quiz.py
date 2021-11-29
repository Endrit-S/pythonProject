from question import Question

questions_prompts = [
    "What color are apples?\n(a) Red/Green\n(b) Purple\n(c) Orange\n\n",
    "What color are bananas?\n(a) Yellow\n(b) Red\n (c) White\n\n",
    "What color are watermelons?\n(a) Black\n(b) Blue\n(c) Green\n\n"
]

questions = [
    Question(questions_prompts[0], "a"),
    Question(questions_prompts[1], "a"),
    Question(questions_prompts[2], "c"),
]

def run_test(questions):
    score = 0
    for question in questions:
        answer = input(question.prompt)
        if answer == question.answer:
            score += 1

    print("You got " + str(score) + "/" + str(len(questions)) + " correct")

run_test(questions)