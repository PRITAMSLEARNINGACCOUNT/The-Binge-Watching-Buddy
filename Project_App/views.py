from django.shortcuts import render
from .models import ReviewModel
from .forms import ReviewFrom, UserRegister, SearchForm
from django.shortcuts import get_object_or_404, redirect
from django.contrib.auth.decorators import login_required
from django.contrib.auth import login


def Get_Reviews(Request):
    Search_Form = SearchForm()
    if Request.method == "POST":
        Search_Form = SearchForm(Request.POST)
        if Search_Form.is_valid():
            print(Search_Form.cleaned_data['Search_Value'])
            All_Review = ReviewModel.objects.filter(
                ReviewMessage__icontains=Search_Form.cleaned_data['Search_Value']
            ).order_by("-Upload_at")
            return render(Request, "Reviews.html", {"Reviews": All_Review, "Search_Form": Search_Form})
    All_Review = ReviewModel.objects.all().order_by("-Upload_at")
    return render(Request, "Reviews.html", {"Reviews": All_Review, "Search_Form": Search_Form})


@login_required
def Create_Review(Request):
    if Request.method == "POST":
        ReviewFromObject = ReviewFrom(Request.POST, Request.FILES)
        if ReviewFromObject.is_valid():
            # print(ReviewFromObject.cleaned_data['ReviewTitle']) --> Just For Debugging
            ReviewFromObject = ReviewFromObject.save(commit=False)
            ReviewFromObject.ReviewUser = Request.user
            ReviewFromObject.save()
            return redirect("All_Reviews")
    else:
        ReviewFromObject = ReviewFrom()
    return render(Request, "CreateReview.html", {"ReviewForm": ReviewFromObject})


@login_required
def Edit_Review(Request, Review_Id):
    Review = get_object_or_404(
        ReviewModel, pk=Review_Id, ReviewUser=Request.user)
    if Request.method == "POST":
        ReviewFromObject = ReviewFrom(
            Request.POST, Request.FILES, instance=Review)
        if ReviewFromObject.is_valid():
            ReviewFromObject.save(commit=False)
            ReviewFromObject.ReviewUser = Request.user
            ReviewFromObject.save()
            return redirect("All_Reviews")
    else:
        ReviewFromObject = ReviewFrom(instance=Review)
    return render(Request, "CreateReview.html", {"ReviewForm": ReviewFromObject})


@login_required
def Delete_Review(Request, Review_Id):
    Review = get_object_or_404(
        ReviewModel, pk=Review_Id, ReviewUser=Request.user)
    if Request.method == "POST":
        Review.delete()
        return redirect("All_Reviews")
    else:
        return render(Request, "ReviewDelete.html", {"Review": Review})


def User_Register(Request):
    Registration_Form = UserRegister()
    if Request.method == "POST":
        Registration_Form = UserRegister(Request.POST)
        if Registration_Form.is_valid():
            Registered_User = Registration_Form.save()
            login(Request, Registered_User)
            return redirect("All_Reviews")

    return render(Request, "registration/register.html", {"Registration_Form": Registration_Form})


# def Experimental_Functionality(Request):
#     Experimental_Form = ExperimentalForm()
#     if Request.method == "POST":
#         Experimental_Form = ExperimentalForm(Request.POST)
#         if Experimental_Form.is_valid():
#             c
#             return redirect("All_Reviews")

#     return render(Request, "ExperimentalForm.html", {"Experimental_Form": Experimental_Form})
