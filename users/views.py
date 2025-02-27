from django.shortcuts import render, redirect
from django.contrib import messages
from django.contrib.auth import authenticate, login as logiin, logout as logoutt
from .models import User
from django.contrib.auth.decorators import login_required
from .models import VerificationCode
from django.core.mail import send_mail
import random
from django.http import HttpResponse

def login(request):
    if request.method == "POST":
        login_input = request.POST.get("login_input")  
        password = request.POST.get("password")

        user = None
        if "@" in login_input:  
            user = authenticate(request, email=login_input, password=password)
        else:  
            try:
                user_obj = User.objects.get(phone_number=login_input)
                user = authenticate(request, email=user_obj.email, password=password)
            except User.DoesNotExist:
                user = None

        if user:
            logiin(request, user)
            return redirect("home")
        else:
            return render(request, "login.html", {"error": "Login yoki parol xato!"})

    return render(request, "login.html")

def register(request):
    if request.method == "POST":
        username = request.POST.get("username")
        login_input = request.POST.get("login_input")
        password = request.POST.get("password")

        if User.objects.filter(username=username).exists():
            return render(request, "register.html", {"error": "Bu username allaqachon olingan!"})

        if login_input and "@" in login_input:  # Email orqali ro‘yxatdan o‘tish
            if User.objects.filter(email=login_input).exists():
                return render(request, "register.html", {"error": "Bu email allaqachon mavjud!"})

            code = str(random.randint(1000, 9999))
            VerificationCode.objects.filter(email=login_input).delete()
            VerificationCode.objects.create(email=login_input, code=code)

            send_mail(
                "Ro‘yxatdan o‘tish tasdiqlash kodi",
                f"Sizning tasdiqlash kodingiz: {code}",
                "mutalovnuriddin651@gmail.com",
                [login_input],
                fail_silently=False,
            )

            request.session["verification_email"] = login_input  # ✅ Emailni sessionga saqlash
            request.session["username"] = username  # ✅ Username ham saqlanadi
            request.session["password"] = password  # ✅ Parol ham saqlanadi

            return redirect("verify")  # ✅ Tasdiqlash sahifasiga o‘tish
        
        else:  # Telefon orqali ro‘yxatdan o‘tish
            if User.objects.filter(phone_number=login_input).exists():
                return render(request, "register.html", {"error": "Bu telefon allaqachon mavjud!"})

            user = User.objects.create(username=username, phone_number=login_input)
            user.set_password(password)
            user.save()
            logiin(request, user)
            return redirect("home")

    return render(request, "register.html")

def logout(request):
    logoutt(request)
    messages.success(request, "Tizimdan chiqdingiz!")
    return redirect("login")

@login_required
def home(request):
    return render(request, "home.html")


def verify_view(request):

    if request.method == "GET":
        return render(request, "verify.html")
    
    if request.method == "POST":
        email = request.session.get("verification_email")
        username = request.session.get("username")
        password = request.session.get("password")
        entered_code = request.POST.get("code")

        if not email or not username or not password:
            return render(request, "verify.html", {"error": "Ma'lumotlar topilmadi, qayta ro‘yxatdan o‘ting!"})

        try:
            verification = VerificationCode.objects.get(email=email)

            if entered_code == verification.code:
                user = User.objects.create(username=username, email=email)
                user.set_password(password)
                user.save()

                logiin(request, user)  # ✅ Login qilish
                verification.delete()  # ✅ Kodni o‘chirish

                # Sessionni tozalash
                del request.session["verification_email"]
                del request.session["username"]
                del request.session["password"]

                return redirect("home")

            return render(request, "verify.html", {"error": "Kod noto‘g‘ri!"})

        except VerificationCode.DoesNotExist:
            return render(request, "verify.html", {"error": "Tasdiqlash kodini oldin olishingiz kerak!"})

    return HttpResponse("Noto‘g‘ri so‘rov", status=400)