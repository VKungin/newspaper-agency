from django.urls import path, include

from agency.views import index, TopicListView, NewspaperListView, RedactorListView, NewspaperDetailView

urlpatterns = [
    path("", index, name="index"),
    path("topics/", TopicListView.as_view(), name="topics-list"),
    path("news/", NewspaperListView.as_view(), name="news-list"),
    path("news/<int:pk>", NewspaperDetailView.as_view(), name="news-detail"),
    path("redactors/", RedactorListView.as_view(), name="redactors-list"),
    # path("__debug__/", include("debug_toolbar.urls")),

]
app_name = "agency"
