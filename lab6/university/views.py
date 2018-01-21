from django.http import Http404
from django.shortcuts import render
import json

# Create your views here.


with open('C:\data.json', "r") as file:
    data = json.load(file)


def index(request):
    context = {"chair_pairs": [], "title": "Кафедры ИУ"}
    piter = iter(data["chairs"])
    pairs = zip(piter, piter)
    for i in pairs:
        chair_pair = [{}, {}]
        p = list(i)
        print(p[0]["name"])
        print(p[1]["name"])
        chair_pair[0]["name"] = p[0]["name"]
        chair_pair[0]["longname"] = p[0]["longname"]
        short_description = p[0]["description"][:100] + "..."
        chair_pair[0]["description_short"] = short_description
        chair_pair[1]["name"] = p[1]["name"]
        chair_pair[1]["longname"] = p[1]["longname"]
        short_description = p[1]["description"][:100] + "..."
        chair_pair[1]["description_short"] = short_description
        context["chair_pairs"].append(chair_pair)
    if len(data["chairs"]) % 2 == 1:
        c = [{}, {}]
        c[0]["name"] = data["chairs"][len(data["chairs"]) - 1]["name"]
        c[0]["longname"] = data["chairs"][len(data["chairs"]) - 1]["longname"]
        c[0]["description_short"] = data["chairs"][len(data["chairs"]) - 1]["description"][:100] + "..."
        context["chair_pairs"].append(c)
    return render(request=request, template_name="university/faculties.html", context=context)


def single_teacher(request, teacher_id):

    found = False
    context = {}
    for c in data["chairs"]:
        for t in c["teachers"]:
            print(t)
            if int(teacher_id) == t["id"]:
                found = True
                context["name"] = t["name"]
                context["bio"] = t["bio"]
                context["courses"] = t["courses"]
                break
    if not found:
        return Http404()

    return render(request=request, template_name="university/teacher.html", context=context)


def faculty_info(request, faculty_name):
    context = {"name": faculty_name, "description": "", "subjects": "", "teachers": []}
    found = False

    for ch in data["chairs"]:
        if ch["name"] == faculty_name:
            found = True
            context["description"] = ch["description"]
            context["subjects"] = ch["subjects"]
            context["teachers"] = [{"name": teacher["name"], "id": teacher["id"]} for teacher in ch["teachers"]]
            break

    if not found:
        return Http404()

    return render(request=request, template_name="university/chair.html", context=context)


def signin(request):
    pass


def signup(request):
    pass
