from django.urls import path

from agency.views import (
    index, TopicListView,
    NewspaperListView, RedactorListView,
    NewspaperDetailView, RedactorDetailView,
    TopicCreateView, NewspaperCreateView,
    RedactorCreateView, TopicDeleteView, TopicDetailView,
)

urlpatterns = [
    path("", index, name="index"),
    path("topics/", TopicListView.as_view(), name="topics-list"),
    path("topics/deetail/<int:pk>", TopicDetailView.as_view(), name="topics-detail"),
    path("topics/create/", TopicCreateView.as_view(), name="topic-create"),
    path("topics/delete/<int:pk>", TopicDeleteView.as_view(), name="topic-delete"),
    path("news/", NewspaperListView.as_view(), name="news-list"),
    path("news/<int:pk>", NewspaperDetailView.as_view(), name="news-detail"),
    path("news/create/", NewspaperCreateView.as_view(), name="news-create"),
    path("redactors/", RedactorListView.as_view(), name="redactors-list"),
    path("redactors/<int:pk>", RedactorDetailView.as_view(), name="redactors-detail"),
    path("redactors/create/", RedactorCreateView.as_view(), name="redactors-create"),

]
app_name = "agency"
