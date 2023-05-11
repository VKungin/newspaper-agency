from django.views import generic
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
        "large_welcome_text": "Newspaper agency",
        "small_welcome_text": "It displays the number of news articles, topics and editors.",

    }
    return render(request, "agency/index.html", context=context)


class TopicListView(generic.ListView):
    model = Topic
    template_name = "agency/topic_list.html"
    # context_object_name = "topic_list"

    def get_context_data(self, *, object_list=None, **kwargs):
        topic_list = Topic.objects.all()
        context = {
            "topic_list": topic_list,
            "large_welcome_text": "Topic list",
            "small_welcome_text": "It displays the number topics.",

        }
        return context


class RedactorListView(generic.ListView):
    model = Redactor
    template_name = "agency/redactor_list.html"

    def get_context_data(self, *, object_list=None, **kwargs):
        redactor_list = Redactor.objects.all()

        context = {
            "redactor_list": redactor_list,
            "large_welcome_text": "Redactor list",
            "small_welcome_text": "It displays the number redactors.",

        }
        return context


class NewspaperListView(generic.ListView):
    model = Newspaper
    template_name = "agency/newspaper_list.html"

    def get_context_data(self, *, object_list=None, **kwargs):
        news_list = Newspaper.objects.all()

        context = {
            "news_list": news_list,
            "large_welcome_text": "News list",
            "small_welcome_text": "It displays the number news.",

        }
        return context


class NewspaperDetailView(generic.DetailView):
    model = Newspaper

    def get_context_data(self, *, object_list=None, **kwargs):
        context = super().get_context_data(**kwargs)
        print(context)
        title = context.get("newspaper")
        context["large_welcome_text"] = title
        return context
