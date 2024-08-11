from django.contrib import admin
from django.urls import path
from django.conf import settings
from django.conf.urls.static import static
from portfolio import views

urlpatterns = [
    path('admin/', admin.site.urls),
    # Путь к административной панели Django

    path('', views.home, name='home'),
    # Главная страница сайта, отображается при переходе на корневой URL

    path('add_skill/', views.add_skill, name='add_skill'),
    # Страница для добавления нового навыка

    path('edit_skill/<int:pk>/', views.edit_skill, name='edit_skill'),
    # Страница для редактирования существующего навыка по его первичному ключу (pk)

    path('delete_skill/<int:pk>/', views.delete_skill, name='delete_skill'),
    # Страница для удаления навыка по его первичному ключу (pk)

    path('add_project/', views.add_project, name='add_project'),
    # Страница для добавления нового проекта

    path('edit_project/<int:pk>/', views.edit_project, name='edit_project'),
    # Страница для редактирования существующего проекта по его первичному ключу (pk)

    path('delete_project/<int:pk>/', views.delete_project, name='delete_project'),
    # Страница для удаления проекта по его первичному ключу (pk)

    path('contact/', views.contact, name='contact'),
    # Страница с формой для связи или обратной связи
]

if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
    # Добавляем маршруты для обслуживания медиафайлов (например, загруженных изображений) в режиме отладки
