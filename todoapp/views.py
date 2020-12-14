from django.shortcuts import render, redirect, get_object_or_404
from .models import Todo
from datetime import datetime
from django.contrib import messages

# Create your views here.
def home(request):
    if request.method == "POST":
        text = request.POST.get('todotext')
        if len(text) > 3:
            query = Todo(text=text, timestamp=datetime.now())
            query.save()
            messages.success(request, "You todo text added successfully.")
            return redirect('home')
        messages.info(request, "Your todo text either too short or empty")
        return redirect('home')
    getData = Todo.objects.all()
    return render(request, 'index.html', {'data': getData[::-1], 'title': 'Todo Home'})

def edit(request, sl_no):
    query = get_object_or_404(Todo, id=sl_no)
    if request.method == "POST":
        todo = request.POST.get('todotext')
        if len(todo) > 3:
            query.text = todo
            query.timestamp = datetime.now()
            query.save()
            return redirect('home')
        messages.info(request, "Your todo text either too short or empty.")
        return redirect('home')
    return render(request, 'edit.html', {'data': query, 'sl_no': sl_no, 'title': query.text})

def delete(request, sl_no):
    query = get_object_or_404(Todo, id=sl_no).delete()    
    return redirect('home')