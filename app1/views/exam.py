import json
import random

from django.http import JsonResponse
from django.views.decorators.csrf import csrf_exempt

from app1.models import Sign, Category, ExamInfo


# формирует экзамен
def send_exam(request):
    data = Sign.objects.all().values("photo", "realObjectPhoto", "category", "complexity", "question1", "answer1",
                                     "question2", "answer2",
                                     "question3", "answer3", "question4", "answer4", "question5", "answer5")
    questions = []
    answers = []
    textQuestions = []
    answersList = []
    for row in data:
        questions.append(row["question1"])
        questions.append(row["question2"])
        questions.append(row["question3"])
        questions.append(row["question4"])
        questions.append(row["question5"])

        answers.append(row["answer1"])
        answers.append(row["answer2"])
        answers.append(row["answer3"])
        answers.append(row["answer4"])
        answers.append(row["answer5"])

        count = 0
        for i in questions:
            if i == "":
                count += 1
        for i in range(count):
            questions.remove("")

        count = 0
        for i in answers:
            if i == "":
                count += 1
        for i in range(count):
            answers.remove("")

        textQuestions.append(questions)
        answersList.append(answers)

        questions = []
        answers = []

    data_from_database = {}

    id = 0
    for row in data:
        id += 1
        data_from_database[f'{id}'] = {'number': id, 'picture': "/static/" + row["photo"],
                                       'textQuestions': textQuestions[id - 1],
                                       'answersList': answersList[id - 1],
                                       'pictureWorld': "/static/" + row["realObjectPhoto"],
                                       'category': row['category'], 'complexity': row["complexity"]}

    keys = [*data_from_database]
    random.shuffle(keys)
    new_data = dict()
    count = 0
    for key in keys:
        count += 1
        new_data.update({key: data_from_database[key]})

        new_data[count] = new_data[key]
        del new_data[key]

    categories = []
    filtered_data = {}

    for i in Category.objects.all().values("category"):
        categories.append(i["category"])

    index = 1
    for i in categories:
        count = 1
        for j in range(1, len(new_data)):
            if i == new_data[j]["category"] and new_data[j]["complexity"] == str(count):
                filtered_data[f'{index}'] = new_data[j]
                filtered_data[str(index)]["number"] = str(index)
                count += 1
                index += 1
            if count > 3:
                break

    return JsonResponse(filtered_data)


# сохраняет информацию о прохождении экзамена
@csrf_exempt
def get_exam_data(request):
    if request.user.is_authenticated:
        username = request.user.username
        t = ExamInfo.objects.create(
            login=username,
            res=json.loads(request.body)['res'],
            startTime=json.loads(request.body)['startTime'],
            time=json.loads(request.body)['time']
        )

        if (ExamInfo.objects.filter(login=username).count() > 10):
            ExamInfo.objects.filter(login=username)[0].delete()
            t.save(update_fields=["login", "res", "startTime", "time"])
    return JsonResponse({}, status=204)
