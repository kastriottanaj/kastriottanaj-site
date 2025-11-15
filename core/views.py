from django.core.mail import send_mail
from django.shortcuts import render, redirect
from blog.models import Post   # ← correct model name
from .forms import ContactForm
from .models import ContactMessage


def home(request):
    featured_posts = Post.objects.filter(
        is_published=True).order_by('-created_at')[:3]
    return render(request, 'core/home.html', {'featured_posts': featured_posts})


def about(request):
    return render(request, 'core/about.html')


def contact(request):
    if request.method == "POST":
        form = ContactForm(request.POST)
        if form.is_valid():
            name = form.cleaned_data['name']
            email = form.cleaned_data['email']
            message = form.cleaned_data['message']

            # 1. Save lead to DB
            ContactMessage.objects.create(
                name=name,
                email=email,
                message=message
            )

            # 2. Send Email
            subject = f"New message from {name}"
            full_message = f"From: {name} <{email}>\n\n{message}"

            send_mail(
                subject,
                full_message,
                email,  # from
                ['kastriot.sym@gmail.com'],  # ← change to your email
            )

            return redirect('contact-success')

    else:
        form = ContactForm()

    # ✅ THIS LINE WAS MISSING — REQUIRED for GET requests!
    return render(request, 'core/contact.html', {'form': form})


def contact_success(request):
    return render(request, 'core/contact_success.html')
