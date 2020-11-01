from django.shortcuts import render
from django.core.mail import send_mail
from django.conf import settings



def contact_page(request):
    if request.method == "POST":
        first_name = request.POST['first_name']
        last_name  =request.POST['last_name']
        email =request.POST['email']
        phone =request.POST['phone']
        subject =request.POST['Subject']
        message = request.POST['message']
        string = f'Nouveau message {first_name} {last_name} A propos {subject[0:10]}...'
        content = f'Nom : "{first_name}" \Prenom :  "{last_name}"\n Email : "{email}" sujet :"{subject}" \nmessage: "{message}" '
        send_mail(
            string,
            content,
            email,
            [settings.EMAIL_HOST_USER],
        )

    return render(request,'project/contact_page.html')