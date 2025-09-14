def generate_unique_slug(instance, new_slug=None):
    import slugify
    from django.utils.text import slugify
    from .models import YourModel  # Replace with your actual model

    if new_slug is not None:
        slug = new_slug
    else:
        slug = slugify(instance.name)  # Assuming 'name' is a field in your model

    unique_slug = slug
    counter = 1
    while YourModel.objects.filter(slug=unique_slug).exists():  # Replace with your actual model
        unique_slug = f"{slug}-{counter}"
        counter += 1

    return unique_slug

def send_email(subject, message, recipient_list):
    from django.core.mail import send_mail
    send_mail(subject, message, 'from@example.com', recipient_list)  # Replace 'from@example.com' with your sender email

def calculate_discount(price, discount_percentage):
    return price - (price * (discount_percentage / 100))