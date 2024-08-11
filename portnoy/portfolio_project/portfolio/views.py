from django.shortcuts import render, get_object_or_404, redirect
from django.contrib.auth.decorators import login_required
from .models import Skill, Project
from .forms import SkillForm, ProjectForm


def home(request):
    # Представление для главной страницы
    skills = Skill.objects.all()
    # Получаем все объекты модели Skill
    projects = Project.objects.all()
    # Получаем все объекты модели Project
    return render(request, 'portfolio/home.html', {'skills': skills, 'projects': projects})
    # Рендерим шаблон home.html и передаем в контексте данные о навыках и проектах





@login_required
def add_skill(request):
    # Представление для добавления нового навыка, доступно только аутентифицированным пользователям
    if request.method == 'POST':
        # Если запрос методом POST (пользователь отправил данные формы)
        form = SkillForm(request.POST)
        # Создаем форму и заполняем её данными из запроса
        if form.is_valid():
            # Если форма валидна, сохраняем новый навык
            form.save()
            return redirect('home')
            # После сохранения перенаправляем на главную страницу
    else:
        form = SkillForm()
        # Если запрос методом GET, создаем пустую форму для добавления навыка
    return render(request, 'portfolio/skill_form.html', {'form': form})
    # Рендерим шаблон skill_form.html с формой для заполнения





@login_required
def edit_skill(request, pk):
    # Представление для редактирования существующего навыка, доступно только аутентифицированным пользователям
    skill = get_object_or_404(Skill, pk=pk)
    # Получаем объект навыка по первичному ключу или возвращаем 404 ошибку, если не найден
    if request.method == 'POST':
        form = SkillForm(request.POST, instance=skill)
        # Создаем форму и заполняем её данными из запроса, редактируя существующий объект
        if form.is_valid():
            form.save()
            # Сохраняем изменения и перенаправляем на главную страницу
            return redirect('home')
    else:
        form = SkillForm(instance=skill)
        # Если запрос методом GET, заполняем форму данными существующего навыка
    return render(request, 'portfolio/skill_form.html', {'form': form})
    # Рендерим шаблон skill_form.html с формой для редактирования





@login_required
def delete_skill(request, pk):
    # Представление для удаления навыка, доступно только аутентифицированным пользователям
    skill = get_object_or_404(Skill, pk=pk)
    # Получаем объект навыка по первичному ключу или возвращаем 404 ошибку, если не найден
    if request.method == 'POST':
        # Если запрос методом POST (пользователь подтвердил удаление)
        skill.delete()
        # Удаляем навык
        return redirect('home')
        # Перенаправляем на главную страницу после удаления
    return render(request, 'portfolio/confirm_delete.html', {'object': skill})
    # Рендерим шаблон confirm_delete.html для подтверждения удаления





@login_required
def add_project(request):
    # Представление для добавления нового проекта, доступно только аутентифицированным пользователям
    if request.method == 'POST':
        form = ProjectForm(request.POST, request.FILES)
        # Создаем форму и заполняем её данными из запроса, включая файлы
        if form.is_valid():
            form.save()
            # Сохраняем новый проект и перенаправляем на главную страницу
            return redirect('home')
    else:
        form = ProjectForm()
        # Если запрос методом GET, создаем пустую форму для добавления проекта
    return render(request, 'portfolio/project_form.html', {'form': form})
    # Рендерим шаблон project_form.html с формой для заполнения




@login_required
def edit_project(request, pk):
    # Представление для редактирования существующего проекта, доступно только аутентифицированным пользователям
    project = get_object_or_404(Project, pk=pk)
    # Получаем объект проекта по первичному ключу или возвращаем 404 ошибку, если не найден
    if request.method == 'POST':
        form = ProjectForm(request.POST, request.FILES, instance=project)
        # Создаем форму и заполняем её данными из запроса, редактируя существующий объект
        if form.is_valid():
            form.save()
            # Сохраняем изменения и перенаправляем на главную страницу
            return redirect('home')
    else:
        form = ProjectForm(instance=project)
        # Если запрос методом GET, заполняем форму данными существующего проекта
    return render(request, 'portfolio/project_form.html', {'form': form})
    # Рендерим шаблон project_form.html с формой для редактирования




@login_required
def delete_project(request, pk):
    # Представление для удаления проекта, доступно только аутентифицированным пользователям
    project = get_object_or_404(Project, pk=pk)
    # Получаем объект проекта по первичному ключу или возвращаем 404 ошибку, если не найден
    if request.method == 'POST':
        # Если запрос методом POST (пользователь подтвердил удаление)
        project.delete()
        # Удаляем проект
        return redirect('home')
        # Перенаправляем на главную страницу после удаления
    return render(request, 'portfolio/confirm_delete.html', {'object': project})








def contact(request):
    # Представление для страницы контактов
    return render(request, 'portfolio/contact.html')
    # Рендерим шаблон contact.html
