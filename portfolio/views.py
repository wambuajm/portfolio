from django.contrib import messages
from django.shortcuts import get_object_or_404, redirect, render
from .models import ContactMessage, Project

def home(request):
    projects = Project.objects.filter(featured=True)[:6]
    return render(request, "portfolio/home.html", {"projects": projects})

def projects(request):
    category = request.GET.get("category", "")
    qs = Project.objects.all()
    if category:
        qs = qs.filter(category=category)
    return render(request, "portfolio/projects.html", {
        "projects": qs,
        "categories": Project.CATEGORY_CHOICES,
        "active_category": category,
    })

def project_detail(request, slug):
    project = get_object_or_404(Project, slug=slug)
    return render(request, "portfolio/project_detail.html", {"project": project})

def contact(request):
    if request.method == "POST":
        ContactMessage.objects.create(
            name=request.POST.get("name", "").strip(),
            email=request.POST.get("email", "").strip(),
            subject=request.POST.get("subject", "").strip(),
            message=request.POST.get("message", "").strip(),
        )
        messages.success(request, "Thank you. Your message has been received.")
        return redirect("portfolio:contact")
    return render(request, "portfolio/contact.html")
