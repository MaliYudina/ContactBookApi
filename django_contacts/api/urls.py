from django.urls import path
from .views import ContactView, SingleContactView, GroupView, SingleGroupView
app_name = "contacts"

urlpatterns = [
    path('contacts/', ContactView.as_view()),
    path('contacts/<int:pk>', SingleContactView.as_view()),
    path('groups/', GroupView.as_view()),
    path('groups/<int:pk>', SingleGroupView.as_view())
]
