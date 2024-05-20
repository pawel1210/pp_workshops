from django.shortcuts import render, redirect
from .models import Pizza, Flour, Style
from .forms import PizzaForm, CommentForm
from django.contrib import messages
from django.contrib.auth.decorators import login_required
from django.db.models import Q
from pizzaiolos.models import Pizzaiolo
from django.contrib.auth.models import User

# Create your views here.
def pizzas(request):
    search_query = ""
    if request.GET.get('search_query'):
        search_query = request.GET.get('search_query')
    pizzaiolos = Pizzaiolo.objects.filter(Q(last_name__icontains=search_query) | Q(first_name__icontains=search_query))
    flours = Flour.objects.filter(name__icontains=search_query)
    styles = Style.objects.filter(name__icontains=search_query)
    pizzas = Pizza.objects.distinct().filter(
        Q(title__icontains=search_query) |
        Q(owner__in=pizzaiolos) |
        Q(flour__in=flours) |
        Q(style__in=styles)
    )
    context = {
        'pizzas': pizzas,
        'search_query': search_query,
    }
    return render(request, 'pizzas/pizzas.html', context)

def pizza(request, pk):
    pizzaObj = Pizza.objects.get(id=pk)
    comments = pizzaObj.comment_set.all()
    form = CommentForm()
    if request.method == "POST":
        try:
            pizzaiolo = request.user.pizzaiolo
        except:
            messages.error(request, "Please log in to add comments")
            return redirect('login')
        else:
            form = CommentForm(request.POST)
            if form.is_valid():
                comment = form.save(commit=False)
                comment.owner = pizzaiolo
                comment.pizza = pizzaObj
                comment.save()
                return redirect('pizza', pk)
    context = {
        "pizza": pizzaObj,
        "comments": comments,
        "form": form,
    }
    return render(request, 'pizzas/pizza.html', context)

@login_required(login_url='login')
def addPizza(request):
    action = "add"
    pizzaiolo = request.user.pizzaiolo
    form = PizzaForm()
    if request.method == "POST":
        form = PizzaForm(request.POST, request.FILES)
        if form.is_valid():
            pizza = form.save(commit=False)
            pizza.owner = pizzaiolo
            pizza.save()
            messages.success(request, "Your pizza was successfully baked")
            return redirect('pizzas')
    context = {
        "form": form,
        "action": action,
    }
    return render(request, 'pizzas/pizza-form.html', context)

@login_required(login_url='login')
def updatePizza(request, pk):
    action = "update"
    pizzaiolo = request.user.pizzaiolo
    pizzaObj = pizzaiolo.pizza_set.get(id=pk)
    form = PizzaForm(instance=pizzaObj)
    if request.method == "POST":
        form = PizzaForm(request.POST, request.FILES, instance=pizzaObj)
        if form.is_valid():
            updatedPizza = form.save(commit=False)
            updatedPizza.was_edited = True
            updatedPizza.save()
            messages.success(request, "Your pizza was successfully updated")
            return redirect('pizza', pk)
    context = {
        "form": form,
        "action": action,
        "id": pk,
    }
    return render(request, 'pizzas/pizza-form.html', context)

@login_required(login_url='login')
def deletePizza(request, pk):
    pizzaiolo = request.user.pizzaiolo
    pizzaObj = pizzaiolo.pizza_set.get(id=pk)
    if request.method == "POST":
        pizzaObj.delete()
        messages.success(request, "Your pizza was successfully removed")
        return redirect('pizzas')
    context = {
        "pizza": pizzaObj,
    }
    return render(request, 'pizzas/delete-pizza.html', context)

@login_required(login_url='login')
def deleteComment(request, pk):
    pizzaiolo = request.user.pizzaiolo
    commentObj = pizzaiolo.comment_set.get(id=pk)
    pizzaid = commentObj.pizza.id
    messages.success(request, "Your comment was deleted")
    commentObj.delete()
    return redirect('pizza', pizzaid)

@login_required(login_url='login')
def updateComment(request, pk):
    pizzaiolo = request.user.pizzaiolo
    commentObj = pizzaiolo.comment_set.get(id=pk)
    pizzaid = commentObj.pizza.id
    form = CommentForm(instance=commentObj)
    if request.method == "POST":
        form = CommentForm(request.POST, instance=commentObj)
        if form.is_valid():
            updatedComment = form.save(commit=False)
            if updatedComment.was_edited == False:
                updatedComment.was_edited = True
            updatedComment.save()
            return redirect('pizza', pizzaid )
    context = {
        "form": form,
    }
    return render(request, 'pizzas/update-comment.html', context)