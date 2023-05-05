from django.shortcuts import render

from agency.models import Topic, Newspaper, Redactor


def index(request):

    num_topics = Topic.objects.count()
    num_news = Newspaper.objects.count()
    num_redactors = Redactor.objects.count()

    context = {
        "num_topics": num_topics,
        "num_news": num_news,
        "num_redactors": num_redactors,
    }
    return render(request, "agency/index.html", context=context)
