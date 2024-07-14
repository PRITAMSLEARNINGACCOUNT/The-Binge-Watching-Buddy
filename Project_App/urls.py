from . import views
from django.urls import path
urlpatterns = [
    path("", views.Get_Reviews, name="All_Reviews"),
    path("<int:Review_Id>/DeleteReview/",
         views.Delete_Review, name="Delete_Review"),
    path("<int:Review_Id>/EditReview/", views.Edit_Review, name="Edit_Review"),
    path("CreateReview/", views.Create_Review, name="Create_Review"),
    path("Register/", views.User_Register, name="User_Register"),
]
