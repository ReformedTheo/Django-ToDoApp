from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth import authenticate, login
from django.contrib.auth.decorators import login_required
from django.contrib import messages
from .models import Evento
from django.http import HttpResponse
from django.http.response import Http404


# Create your views here.
def redirectView(request):
    return redirect("/index/")


def loginView(request):
    if request.method == "POST":
        username = request.POST.get("username")
        password = request.POST.get("password")
        user = authenticate(username=username, password=password)
        if user is not None:
            login(request, user)
            return redirect("/index/")
        else:
            messages.error(request, "Usuário ou senha incorretos.")
    return render(request, "login.html")


@login_required(login_url="/login/")
def indexView(request):
    user = request.user
    eventoTodo = Evento.objects.filter(user=user, status="To do")
    eventoInProgress = Evento.objects.filter(user=user, status="in progress")
    eventoDone = Evento.objects.filter(user=user, status="Done")
    context = {
        "eventosTodo": eventoTodo,
        "eventosInProgress": eventoInProgress,
        "eventosDone": eventoDone,
    }
    return render(request, "index.html", context)


@login_required(login_url="/login/")
def novoEventoForm(request):
    if request.method == "POST":
        user = request.user
        title = request.POST.get('title')
        description = request.POST.get('description')
        date = request.POST.get('date')
        status = request.POST.get('status')
        Evento.objects.create(title = title, user = user, description = description, date = date, status = status)
        return redirect('/')
    return render(request, 'novoEventoForm.html')


@login_required(login_url="/login/")
def eventoById(request, evento_id):
    evento = get_object_or_404(Evento, id=evento_id)
    context = {
        "evento":evento,
    }
    if request.method == 'POST':
        user = request.user
        title = request.POST.get('title')
        description = request.POST.get('description')
        date = request.POST.get('date')
        status = request.POST.get('status')
        Evento.objects.filter(id=evento_id).update(title=title,
                                                       date=date,
                                                       user = user,
                                                       description = description,
                                                       status = status)
        return redirect('/')
    return render(request, 'eventoById.html', context)


@login_required(login_url='/login/')
def delete_evento(request, evento_id):
    usuario = request.user
    try:
        evento = Evento.objects.get(id=evento_id)
    except Exception:
        raise Http404()
    if usuario == evento.user:
        evento.delete()
    else:
        return Http404()
    return redirect('/')