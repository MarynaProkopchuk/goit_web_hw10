from django.shortcuts import render
from .utils import get_database
from django.core.paginator import Paginator
from bson import ObjectId


def main(request, page=1):
    db = get_database()
    quotes = db.quotes.find()
    per_page = 10
    paginator = Paginator(list(quotes), per_page)
    quotes_on_page = paginator.page(page)
    return render(request, "quotes/index.html", context={"quotes": quotes_on_page})


def author_detail(request, author_id):
    db = get_database()
    author = db.authors.find_one({"_id": ObjectId(author_id)})

    return render(request, "quotes/author.html", context={"author": author})
