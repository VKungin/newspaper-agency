from django.urls import path

from agency.views import (
    index, TopicListView,
    TopicCreateView, TopicDetailView,
    TopicDeleteView, TopicUpdateView,
    NewspaperListView, NewspaperDetailView,
    NewspaperUpdateView, NewspaperDeleteView,
    NewspaperCreateView,
    RedactorCreateView, RedactorListView,
    RedactorDeleteView, RedactorDetailView,
    RedactorUpdateView, UpdateRedactorInNewspaperView
)

urlpatterns = [
    path("", index, name="index"),

    path("topics/", TopicListView.as_view(), name="topics-list"),
    path("topics/deetail/<int:pk>/", TopicDetailView.as_view(), name="topics-detail"),
    path("topics/create/", TopicCreateView.as_view(), name="topic-create"),
    path("topics/update/<int:pk>/", TopicUpdateView.as_view(), name="topic-update"),
    path("topics/delete/<int:pk>/", TopicDeleteView.as_view(), name="topic-delete"),

    path("news/", NewspaperListView.as_view(), name="news-list"),
    path("news/<int:pk>/", NewspaperDetailView.as_view(), name="news-detail"),
    path("news/create/", NewspaperCreateView.as_view(), name="news-create"),
    path("news/update/<int:pk>/", NewspaperUpdateView.as_view(), name="news-update"),
    path("news/delete/<int:pk>/", NewspaperDeleteView.as_view(), name="news-delete"),
    path("news/change-redactor/<int:pk>/", UpdateRedactorInNewspaperView.as_view(), name="news-change-redactor"),

    path("redactors/", RedactorListView.as_view(), name="redactors-list"),
    path("redactors/<int:pk>/", RedactorDetailView.as_view(), name="redactors-detail"),
    path("redactors/create/", RedactorCreateView.as_view(), name="redactors-create"),
    path("redactors/update/<int:pk>/", RedactorUpdateView.as_view(), name="redactors-update"),
    path("redactors/delete/<int:pk>/", RedactorDeleteView.as_view(), name="redactors-delete"),

]
app_name = "agency"
