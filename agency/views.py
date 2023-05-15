from django.contrib.auth.forms import UserCreationForm
from django.urls import reverse_lazy
from django.views import generic
from django.shortcuts import render

from agency.forms import RedactorCreateForm
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
    paginate_by = 5

    def get_context_data(self, *, object_list=None, **kwargs):
        context = super().get_context_data(**kwargs)
        context["large_welcome_text"] = "Topic list"
        context["small_welcome_text"] = "It displays the number topics"

        return context


class TopicCreateView(generic.CreateView):
    model = Topic
    fields = "__all__"
    success_url = reverse_lazy("agency:topics-list")


class RedactorListView(generic.ListView):
    model = Redactor
    template_name = "agency/redactor_list.html"
    paginate_by = 3

    def get_context_data(self, *, object_list=None, **kwargs):
        context = super().get_context_data(**kwargs)
        context["large_welcome_text"] = "Redactor list"
        context["small_welcome_text"] = "It displays the number redactors. list"

        return context


class RedactorDetailView(generic.DetailView):
    model = Redactor
    template_name = "agency/redactor_detail.html"

    def get_context_data(self, *, object_list=None, **kwargs):
        context = super().get_context_data(**kwargs)
        username = context.get("redactor")
        context["large_welcome_text"] = username
        return context


class RedactorCreateView(generic.CreateView):
    model = Redactor
    form_class = RedactorCreateForm


class NewspaperListView(generic.ListView):
    model = Newspaper
    template_name = "agency/newspaper_list.html"
    paginate_by = 3

    def get_context_data(self, *, object_list=None, **kwargs):
        context = super().get_context_data(**kwargs)
        news_list = Newspaper.objects.all()

        context["news_list"] = news_list
        context["large_welcome_text"] = "News list"
        context["small_welcome_text"] = "It displays the number news"

        return context


class NewspaperDetailView(generic.DetailView):
    model = Newspaper

    def get_context_data(self, *, object_list=None, **kwargs):
        context = super().get_context_data(**kwargs)
        title = context.get("newspaper")
        context["large_welcome_text"] = title
        return context


class NewspaperCreateView(generic.CreateView):
    model = Newspaper
    fields = "__all__"
    success_url = reverse_lazy("agency:news-list")


