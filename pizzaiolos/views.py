from django.shortcuts import render, redirect
from django.contrib.auth import login, authenticate, logout
from django.contrib.auth.decorators import login_required
from django.contrib.auth.models import User
from django.contrib import messages
from .models import Pizzaiolo, Message
from .forms import UserForm, PizzaioloForm, MessageForm
from .filters import PizzaioloFilter
from django.db.models import Q


# Create your views here.
def loginUser(request):
    if request.method == "POST":
        username = request.POST['username'].lower()
        password = request.POST['password']
        try:
            user = User.objects.get(username=username)
        except:
            messages.error(request, "Username does not exist")
        user = authenticate(request, username=username, password=password)

        if user is not None:
            login(request, user)
            messages.success(request, "Logged in successfully")
            return redirect('pizzas')
        else:
            messages.error(request, "Username or password is incorrect")
    return render(request, 'pizzas/pizzas.html')

def logoutUser(request):
    logout(request)
    messages.success(request, "User was logged out")
    return redirect('pizzas')

def registerUser(request):
    form = UserForm()
    if request.method == "POST":
        form = UserForm(request.POST)
        if form.is_valid():
            user = form.save(commit=False)
            user.username = user.username.lower()
            user.save()
            messages.success(request, "Account was created successfully!")
            login(request, user)
            return redirect('account')
    context = {
        "form": form,
    }
    return render(request, 'pizzaiolos/register.html', context=context)

def pizzaiolos(request):
    all_pizzaiolos = Pizzaiolo.objects.all()
    initial_amount = all_pizzaiolos.count()
    myFilter = PizzaioloFilter(request.GET, queryset=all_pizzaiolos)
    all_pizzaiolos = myFilter.qs
    final_amount = all_pizzaiolos.count()
    if initial_amount != final_amount:
        show_all = True
    else:
        show_all = False
    context = {
        'pizzaiolos': all_pizzaiolos,
        'myFilter': myFilter,
        'show_all': show_all,
    }
    return render(request, 'pizzaiolos/pizzaiolos.html', context)

def pizzaiolo(request, pk):
    if request.user.is_authenticated and request.user.pizzaiolo == Pizzaiolo.objects.get(id=pk):
        return redirect('account')
    else:
        pizzaioloObj = Pizzaiolo.objects.get(id=pk)
        pizzas = pizzaioloObj.pizza_set.all()
        context = {
            'pizzaiolo': pizzaioloObj,
            'pizzas': pizzas,
        }
        return render(request, 'pizzaiolos/pizzaiolo.html', context)

@login_required(login_url='login')
def editPizzaiolo(request):
    pizzaioloObj = request.user.pizzaiolo
    form = PizzaioloForm(instance=pizzaioloObj)
    if request.method == "POST":
        form = PizzaioloForm(request.POST, request.FILES, instance=pizzaioloObj)
        if form.is_valid():
            form.save()
            messages.success(request, "Your Pizzaiolo Profile was updated")
            return redirect('account')
    context = {
        'form': form,
        'pizzaiolo': pizzaioloObj,
    }
    return render(request, 'pizzaiolos/edit.html', context)


@login_required(login_url='login')
def account(request):
    pizzaiolo = request.user.pizzaiolo
    pizzas = pizzaiolo.pizza_set.all()
    context = {
        'pizzaiolo': pizzaiolo,
        'pizzas': pizzas,
    }
    return render(request, 'pizzaiolos/account.html', context)

@login_required(login_url='login')
def inbox(request):
    pizzaioloObj = request.user.pizzaiolo
    inbox = pizzaioloObj.messages.all()
    senders = []
    latest_messages = []
    for message in inbox:
        selected_sender = message.sender
        if selected_sender not in senders:
            senders.append(selected_sender)
            latest_message = Message.objects.filter(Q(sender=selected_sender, recipient=pizzaioloObj) | Q(sender=pizzaioloObj, recipient=selected_sender)).latest('created')
            latest_messages.append(latest_message)
    context = {
        'pizzaiolo': pizzaioloObj,
        'senders': senders,
        'latest': latest_messages,
    }
    return render(request, 'pizzaiolos/inbox.html', context)

@login_required(login_url='login')
def conversation(request, pk):
    form = MessageForm()
    recipient = request.user.pizzaiolo
    sender = Pizzaiolo.objects.get(id=pk)
    conversation = Message.objects.filter(Q(sender=sender, recipient=recipient) | Q(sender=recipient, recipient=sender)).order_by('created')
    not_read = recipient.messages.filter(sender=sender, is_read=False)
    if not_read:
        for message in not_read:
            message.is_read = True
            message.save()
    if conversation:
        latest_id = conversation.latest('created').id
    else:
        latest_id = ""
    if request.method == "POST":
        form = MessageForm(request.POST)
        if form.is_valid():
            newMessage = form.save(commit=False)
            newMessage.sender = recipient
            newMessage.recipient = sender
            newMessage.save()
            return redirect('conversation', pk)
    context = {
        "form": form,
        "sender": sender,
        "conversation": conversation,
        "latest": latest_id,
    }
    return render (request, 'pizzaiolos/message.html', context)



