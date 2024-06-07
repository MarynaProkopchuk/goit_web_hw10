import os
import sys

# Додавання кореневої директорії проекту до PYTHONPATH
project_root = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
sys.path.append(project_root)

os.environ.setdefault("DJANGO_SETTINGS_MODULE", "homework10.settings")


import django

django.setup()

from pymongo import MongoClient
from quotes.models import Author, Quote, Tag  # noqa

client = MongoClient(
    "mongodb+srv://user01:26100510@cluster0.yzrztho.mongodb.net/?retryWrites=true&w=majority"
)
db = client.home_work10

# authors = db.authors.find()
#
# for author in authors:
#     Author.objects.get_or_create(
#         fullname=author["fullname"],
#         born_date=author["born_date"],
#         born_location=author["born_location"],
#         description=author["description"],
#     )

quotes = db.quotes.find()

for quote in quotes:
    tags = []
    for tag in quote["tags"]:
        t, *_ = Tag.objects.get_or_create(name=tag)
        tags.append(t)
    author = db.authors.find_one({"_id": quote["author"]})
    a = Author.objects.get(fullname=author["fullname"])
    q = Quote.objects.create(quote=quote["quote"], author=a)
    for tag in tags:
        q.tags.add(tag)
