from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.decorators import login_required
from .models import Time
from .forms import TimeForm


def cadastro(request):
    if request.method == 'POST':
        form = UserCreationForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('login')
    else:
        form = UserCreationForm()
    return render(request, 'times/cadastro.html', {'form': form})


@login_required
def listar(request):
    times = Time.objects.filter(usuario=request.user)
    return render(request, 'times/listar.html', {'times': times})


@login_required
def adicionar(request):
    if request.method == 'POST':
        form = TimeForm(request.POST)
        if form.is_valid():
            time = form.save(commit=False)
            time.usuario = request.user
            time.save()
            return redirect('listar')
    else:
        form = TimeForm()
    return render(request, 'times/form_time.html', {'form': form, 'titulo': 'Adicionar Time'})


@login_required
def editar(request, pk):
    time = get_object_or_404(Time, pk=pk, usuario=request.user)
    if request.method == 'POST':
        form = TimeForm(request.POST, instance=time)
        if form.is_valid():
            form.save()
            return redirect('listar')
    else:
        form = TimeForm(instance=time)
    return render(request, 'times/form_time.html', {'form': form, 'titulo': 'Editar Time'})


@login_required
def excluir(request, pk):
    time = get_object_or_404(Time, pk=pk, usuario=request.user)
    if request.method == 'POST':
        time.delete()
        return redirect('listar')
    return render(request, 'times/confirmar_exclusao.html', {'time': time})