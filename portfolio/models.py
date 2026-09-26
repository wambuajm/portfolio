from django.db import models

class Project(models.Model):
    CATEGORY_CHOICES = [
        ("BI", "Data & BI"),
        ("SYSTEMS", "Data Engineering & Systems"),
        ("DESIGN", "Technical & Graphic Design"),
        ("OPS", "Logistics & Operations"),
        ("QUALITY", "Quality Management"),
    ]

    title = models.CharField(max_length=160)
    slug = models.SlugField(unique=True)
    category = models.CharField(max_length=20, choices=CATEGORY_CHOICES)
    summary = models.TextField()
    tools = models.CharField(max_length=300, blank=True)
    image = models.ImageField(upload_to="projects/", blank=True, null=True)
    featured = models.BooleanField(default=True)
    order = models.PositiveIntegerField(default=0)

    class Meta:
        ordering = ["order", "title"]

    def __str__(self):
        return self.title


class ContactMessage(models.Model):
    name = models.CharField(max_length=120)
    email = models.EmailField()
    subject = models.CharField(max_length=180, blank=True)
    message = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)

    class Meta:
        ordering = ["-created_at"]

    def __str__(self):
        return f"{self.name} — {self.email}"
