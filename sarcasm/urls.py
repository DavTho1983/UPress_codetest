from django.urls import path
from .views import HeadlineAPIListView, HeadlineAPIID

urlpatterns = [
    path("", HeadlineAPIListView.as_view(), name="results_api_list"),
    path("<int:pk>", HeadlineAPIID.as_view(), name="results_api_detail"),
]