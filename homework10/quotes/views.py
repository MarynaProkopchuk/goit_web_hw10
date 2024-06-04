from django.shortcuts import render
from .utils import get_database
from django.core.paginator import Paginator


def main(request):
    db = get_database()
    quotes = db.quotes.find()
    # return print(quotes)
    return render(request, "quotes/index.html", context={"quotes": quotes})
