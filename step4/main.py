#Вопрос ответ
tasks = (
    {
        "question": "Столица России?",
        "answers": (
            "МОСКВА", 
            "ТУЛА", 
            "ТВЕРЬ", 
            "МАГАДАН"
        ),  
        "right_answer": "МОСКВА",
        "points": 2
    }, 
    {
        "question": "Столица Франции?", 
        "answers": (
            "ПАРИЖ", 
            "МАРСЕЛЬ", 
            "ЛИОН", 
            "НИЦЦА"
        ),
        "right_answer": "ПАРИЖ",
        "points": 3
    }, 
    {
        "question": "Столица Германии?", 
        "asnwers": (
            "БЕРЛИН", 
            "КЁЛЬН", 
            "МЮНХЕН", 
            "ГАМБУРГ"
        ), 
        "right_answer": "БЕРЛИН",
        "points": 3
     }
)

points = 0

for task in tasks: 
    print(*task["answers"], sep="\n")
    users_answer = input(f'{task["question"]}\n').upper()
    if users_answer == task["right_answer"]:
        print("Все верно!")
        points += task["points"]
    else:
        print("Не верно!")

print("Вы набрали баллов:", points)