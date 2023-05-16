from django.views import generic
from django.urls import reverse_lazy
from django.contrib.auth.mixins import LoginRequiredMixin
from django.contrib.auth.decorators import login_required
from django.shortcuts import render, get_object_or_404, redirect

from agency.forms import (
    RedactorCreateForm, RedactorUpdateForm,
    ChangeRedactorForm, RedactorSearchForm,
    TopicSearchForm, NewspaperSearchForm
)
from agency.models import Topic, Newspaper, Redactor


@login_required
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


class TopicListView(LoginRequiredMixin, generic.ListView):
    model = Topic
    template_name = "agency/topic_list.html"
    paginate_by = 4

    def get_context_data(self, *, object_list=None, **kwargs):
        context = super().get_context_data(**kwargs)
        name = self.request.GET.get("name", "")

        context["large_welcome_text"] = "Topic list"
        context["small_welcome_text"] = "It displays the number topics"
        context["search_form"] = TopicSearchForm(initial={
            "name": name
        })

        return context

    def get_queryset(self):
        queryset = Topic.objects.all()
        form = TopicSearchForm(self.request.GET)

        if form.is_valid():
            return queryset.filter(name__icontains=form.cleaned_data["name"])
        return queryset


class TopicDetailView(LoginRequiredMixin, generic.DetailView):
    model = Topic
    template_name = "agency/topic_detail.html"

    def get_context_data(self, *, object_list=None, **kwargs):
        context = super().get_context_data(**kwargs)
        name = context.get("topic")
        context["large_welcome_text"] = name
        return context


class TopicCreateView(LoginRequiredMixin, generic.CreateView):
    model = Topic
    fields = "__all__"
    success_url = reverse_lazy("agency:topics-list")


class TopicUpdateView(LoginRequiredMixin, generic.UpdateView):
    model = Topic
    fields = "__all__"
    success_url = reverse_lazy("agency:topics-list")


class TopicDeleteView(LoginRequiredMixin, generic.DeleteView):
    model = Topic
    success_url = reverse_lazy("agency:topics-list")


class RedactorListView(LoginRequiredMixin, generic.ListView):
    model = Redactor
    template_name = "agency/redactor_list.html"
    paginate_by = 4

    def get_context_data(self, *, object_list=None, **kwargs):
        context = super().get_context_data(**kwargs)
        username = self.request.GET.get("username", "")

        context["large_welcome_text"] = "Redactor list"
        context["small_welcome_text"] = "It displays the number redactors. list"
        context["search_form"] = RedactorSearchForm(initial={
            "username": username
        })

        return context

    def get_queryset(self):
        queryset = Redactor.objects.all()
        form = RedactorSearchForm(self.request.GET)

        if form.is_valid():
            return queryset.filter(username__icontains=form.cleaned_data["username"])
        return queryset


class RedactorDetailView(LoginRequiredMixin, generic.DetailView):
    model = Redactor
    template_name = "agency/redactor_detail.html"

    def get_context_data(self, *, object_list=None, **kwargs):
        context = super().get_context_data(**kwargs)
        username = context.get("redactor")
        context["large_welcome_text"] = username
        return context


class RedactorCreateView(LoginRequiredMixin, generic.CreateView):
    model = Redactor
    form_class = RedactorCreateForm


class RedactorUpdateView(LoginRequiredMixin, generic.UpdateView):
    model = Redactor
    form_class = RedactorUpdateForm


class RedactorDeleteView(LoginRequiredMixin, generic.DeleteView):
    model = Redactor
    success_url = reverse_lazy("agency:redactors-list")


class NewspaperListView(LoginRequiredMixin, generic.ListView):
    model = Newspaper
    template_name = "agency/newspaper_list.html"
    paginate_by = 4

    def get_context_data(self, *, object_list=None, **kwargs):
        context = super().get_context_data(**kwargs)
        title = self.request.GET.get("title", "")
        context["large_welcome_text"] = "News list"
        context["small_welcome_text"] = "It displays the number news"
        context["search_form"] = NewspaperSearchForm(initial={
            "title": title
        })

        return context

    def get_queryset(self):
        queryset = Newspaper.objects.all()
        form = NewspaperSearchForm(self.request.GET)

        if form.is_valid():
            return queryset.filter(title__icontains=form.cleaned_data["title"])
        return queryset


class NewspaperDetailView(LoginRequiredMixin, generic.DetailView):
    model = Newspaper

    def get_context_data(self, *, object_list=None, **kwargs):
        context = super().get_context_data(**kwargs)
        title = context.get("newspaper")
        context["large_welcome_text"] = title
        return context


class NewspaperCreateView(LoginRequiredMixin, generic.CreateView):
    model = Newspaper
    fields = "__all__"
    success_url = reverse_lazy("agency:news-list")


class NewspaperUpdateView(LoginRequiredMixin, generic.UpdateView):
    model = Newspaper
    fields = "__all__"

    def get_success_url(self):
        return reverse_lazy("agency:news-detail", kwargs={"pk": self.object.pk})


class NewspaperDeleteView(LoginRequiredMixin, generic.DeleteView):
    model = Newspaper
    success_url = reverse_lazy("agency:news-list")


class BaseUpdateView(LoginRequiredMixin, generic.UpdateView):
    model = Newspaper
    form_class = ChangeRedactorForm

    def post(self, request, pk):
        user = request.user
        if get_object_or_404(Newspaper, pk=pk) in user.newspapers.all():
            user.newspapers.remove(pk)
        else:
            user.newspapers.add(pk)
        return redirect("agency:news-detail", pk=pk)
