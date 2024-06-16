from models import Authors, Quotes
from mongoengine import connect
import json

connect(
    db="home_work10",
    host="mongodb+srv://************@cluster0.yzrztho.mongodb.net/?retryWrites=true&w=majority",
)


def insert_authors():
    with open("authors.json", "r", encoding="utf-8") as file:
        data = json.load(file)
        for d in data:
            author = Authors(
                fullname=d["fullname"],
                born_date=d["born_date"],
                born_location=d["born_location"],
                description=d["description"],
            )
            author.save()
        return author


def insert_quotes():
    with open("quotes.json", "r", encoding="utf-8") as file:
        data = json.load(file)
        for d in data:
            author, *_ = Authors.objects(fullname=d.get("author"))
            quote = Quotes(
                tags=d["tags"],
                author=author,
                quote=d["quotes"],
            )
            quote.save()
        return quote


if __name__ == "__main__":
    insert_authors()
    insert_quotes()
