# James D. K. Professional Portfolio — Django

## Setup

1. Create and activate a virtual environment:
   - Windows: `python -m venv venv` then `venv\\Scripts\\activate`
2. Install dependencies:
   `pip install -r requirements.txt`
3. Run migrations:
   `python manage.py migrate`
4. Create an admin account:
   `python manage.py createsuperuser`
5. Start the server:
   `python manage.py runserver`
6. Open:
   `http://127.0.0.1:8000/`
7. Admin:
   `http://127.0.0.1:8000/admin/`

## Add portfolio projects

Use Django Admin → Projects. Add title, category, summary, tools and an optional image. Featured projects appear on the homepage.

## Replace profile links

Update LinkedIn/GitHub/email placeholders in `base.html` and `contact.html`.

## Production

Change SECRET_KEY, DEBUG, ALLOWED_HOSTS, database configuration, static/media deployment and security settings before production.
