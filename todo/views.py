from django.shortcuts import render, redirect
from django.views.decorators.http import require_POST
import smtplib
import js2py

from todo import  config

from .models import Todo
from .forms import TodoForm,UserForm
from django.urls import reverse
from django.contrib.auth.decorators import login_required
from django.http import HttpResponseRedirect,HttpResponse
from django.contrib.auth import authenticate,login,logout

def index(request):
    todo_list = Todo.objects.order_by('-id')

    form = TodoForm()

    context = {'todo_list' : todo_list, 'form' : form}

    return render(request, 'todo/index.html', context)

@login_required
@require_POST
def addTodo(request):
    form = TodoForm(request.POST)
    send_email_addtodo(subjects, msgs)


    if form.is_valid():
        new_todo = Todo(text=request.POST['text'])
        new_todo.save()

    return redirect('index')

def completeTodo(request, todo_id):
    todo = Todo.objects.get(pk=todo_id)
    todo.complete = True
    todo.save()

    return redirect('index')

def deleteCompleted(request):
    Todo.objects.filter(complete__exact=True).delete()

    return redirect('index')

def deleteAll(request):
    Todo.objects.all().delete()

    return redirect('index')

def register(request):

    registered = False

    if request.method == 'POST':
        user_form = UserForm(data=request.POST)

        if user_form.is_valid():
            user = user_form.save()
            user.set_password(user.password)
            user.save()

            registered = True
        else:
            print(user_form.errors)

    else:
        user_form = UserForm()

    return render(request,'todo/registration.html',{'user_form':user_form,'registered':registered})


                                # function to send Email when loogged in
                                # you must enter your email-id and password in config.py
                                # you should change the google settings to allow less secure apps
def send_email(subject, msg):
    try:
        server = smtplib.SMTP('smtp.gmail.com:587')
        server.ehlo()
        server.starttls()
        server.login(config.EMAIL_ADDRESS, config.PASSWORD)
        message = 'Subject: {}\n\n{}'.format(subject, msg)
        server.sendmail(config.EMAIL_ADDRESS, config.EMAIL_ADDRESS, message)
        server.quit()
        print("Success: Email sent!")
    except:
        print("Email failed to send.")


subject = "logged in to Todo app"
msg = "you have just logged into ToDO Application"



                            #function for adding item to list
def send_email_addtodo(subjects, msgs):
    try:
        server = smtplib.SMTP('smtp.gmail.com:587')
        server.ehlo()
        server.starttls()
        server.login(config.EMAIL_ADDRESS, config.PASSWORD)
        message = 'Subject: {}\n\n{}'.format(subjects, msgs)
        server.sendmail(config.EMAIL_ADDRESS, config.EMAIL_ADDRESS, message)
        server.quit()
        print("Success: Email sent!")
    except:
        print("Email failed to send.")


subjects = " You created a ToDo"
msgs = Todo.objects.order_by('id').last()                     # sends a mail of what is added to tod list

@login_required
def special(request):
    return HttpResponse('logged in successfully..! check your mailbox')

@login_required
def user_logout(request):
    logout(request)
    return HttpResponseRedirect(reverse('index'))



def user_login(request):
    if request.method =='POST':
        username = request.POST.get('username')
        password = request.POST.get('password')

        user = authenticate(username=username,password=password)
        if user:
            if user.is_active:
                login(request,user)

                send_email(subject, msg)                                # calling send_email function after logging in to send email

                return render(request,'todo/after_login.html',{})
            else:
                return HttpResponse("Account not active")
        else:
            return HttpResponse('please enter login details correctly')
    else:
        return render(request,'todo/login.html',{})



from django.http import HttpResponse
from .resources import PersonResource

def export(request):
    person_resource = PersonResource()
    dataset = person_resource.export()
    response = HttpResponse(dataset.csv, content_type='text/csv')
    response['Content-Disposition'] = 'attachment; filename="persons.csv"'
    return response
