from django.urls import path

from myapp import views
#componente importado
urlpatterns=[
    # path('',views.index,name='index'),
    path('inicio',views.mostrarcredenciales,name='mostrarcredenciales'),
    path('madrid',views.jugadores,name='jugadores'),
    path('amigos',views.datalistamigos,name='datalistamigos'),
    path('gato', views.showgato, name='showgato')
]