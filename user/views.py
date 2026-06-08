from django.shortcuts import render, reverse
from django.contrib import messages
from django.http import HttpResponseRedirect, HttpResponse, HttpResponseForbidden, HttpResponseBadRequest
from django.contrib.auth import get_user_model, authenticate, login as user_login, logout as user_logout, update_session_auth_hash
from django.utils.http import urlsafe_base64_decode
from django.utils.encoding import force_str
from django.contrib.auth.decorators import login_required

from user import forms, emails, utils

User = get_user_model()


def signup(request):
    if request.method == "POST":
        form = forms.SignUpForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            messages.success(request, "Account Created Successfully! Please Log in.")
            return HttpResponseRedirect(reverse("index"))
        return render(request, "user/signup.html", {"form": form})
    # GET
    context = {
        "form": forms.SignUpForm()
    }
    return render(request, "user/signup.html", context)


def login(request):
    if request.method == "POST":
        form = forms.LogInForm(request, request.POST)
        if form.is_valid():
            email = form.cleaned_data["username"]
            password = form.cleaned_data["password"]
            user = authenticate(email=email, password=password)
            if user is not None:
                user_login(request, user)
                messages.success(request, "Logged In Successfully!")
                return HttpResponseRedirect(reverse("index"))
            messages.error(request, "Please Enter Valid Credentials!")
            return HttpResponseRedirect(reverse("user:login"))
        messages.error(request, "Please enter valid credentials!")
        return HttpResponseRedirect(reverse("user:login"))
    # GET
    context = {
        "form": forms.LogInForm()
    }
    return render(request, "user/login.html", context)

@login_required
def logout(request):
    user_logout(request)
    messages.info(request, "Logged out Successfully!")
    return HttpResponseRedirect(reverse("index"))

@login_required
def change_password(request):
    if request.method == "POST":
        form = forms.ChangePasswordForm(request.user, request.POST)
        if form.is_valid():
            form.save()
            update_session_auth_hash(request, form.user)
            messages.success(request, "Password Changed Successfully!")
            return HttpResponseRedirect(reverse("index"))
        messages.error(request, "Please Enter Valid Password!")
        return render(request, "user/change-password.html", {"form": form})
    # GET
    context = {
        "form": forms.ChangePasswordForm(request.user)
    }
    return render(request, "user/change-password.html", context)

@login_required
def profile_view(request):
    context = {
        "user": request.user
    }
    return render(request, "user/profile-view.html", context)

@login_required
def update_profile(request):
    if request.method == "POST":
        form = forms.ProfileUpdateForm(request.POST, request.FILES, instance=request.user)
        if form.is_valid():
            form.save()
            messages.success(request, "Profile Updated Successfully!")
            return HttpResponseRedirect(reverse("user:profile"))
        messages.error(request, "Please Enter Valid Data!")
        return render(request, "user/profile-update.html", {"form": form})
    # GET
    context = {
        "form": forms.ProfileUpdateForm(instance=request.user)
    }
    return render(request, "user/profile-update.html", context)

@login_required
def email_verification_request(request):
    if not request.user.is_email_verified:
        emails.send_verification_email(request, request.user.id)
        return HttpResponse("Email Verification Link Send To Your Email Address!")
    return HttpResponseForbidden("Email Already Verified!")

@login_required
def email_verifier(request, uidb64, token):
    try:
        uid = force_str(urlsafe_base64_decode(uidb64))
        user = User.objects.get(id=uid)
    except:
        user = None
    if user == request.user:
        if utils.EmailVerificationTokenGenerator.check_token(user, token):
            user.is_email_verified = True
            user.save()
            messages.success(request, "Email Verified Successfully!")
            return HttpResponseRedirect(reverse("user:profile"))
        return HttpResponseBadRequest("Invadid Token!")
    return HttpResponseForbidden("You Don't Have Permission To Use This Link!")
