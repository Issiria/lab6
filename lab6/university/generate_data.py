from faker import Faker
import random
import json

fake = Faker()

with open("data.json", "r") as file:
    data = json.load(file)

Id = 0

for chair in data["chairs"]:
    for teach in chair["teachers"]:
        teach["id"] = Id
        Id += 1

with open("data.json", "w") as file:
    json.dump(data, file)

"""

data = {"chairs": []}

for i in range(1, 10):
    chair = {}
    chair["name"] = "ИУ"+str(i)
    chair["longname"] = fake.sentence()
    chair["description"] = fake.text(max_nb_chars=random.randrange(300, 500))
    chair["subjects"] = fake.text(max_nb_chars=random.randrange(200, 300))
    chair["teachers"] = []
    for t in range(0, random.randrange(8, 20)):
        teacher = {}
        p = fake.profile()
        teacher["name"] = p["name"]
        teacher["email"] = p["mail"]
        teacher["courses"] = fake.words(nb=10)
        teacher["bio"] = fake.text(max_nb_chars=random.randrange(300, 500))
        chair["teachers"].append(teacher)
    data["chairs"].append(chair)

with open("data.json", "w") as file:
    json.dump(data, file)


"""


