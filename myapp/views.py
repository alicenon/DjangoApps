from django.shortcuts import render

def mostrarcredenciales(request):
    credenciales = {
        'nombre': 'alejandro',
        'apellido': 'lima',
        'edad': 24
    }
    return render(request, "paginaCredenciales/credenciales.html",credenciales)

def jugadores(request):
    listajugadores = [
        {
            "Nombre": "Sergio Ramos",
            "Demarcacion": "Defensa",
            "Numero": 5
        },
        {
            "Nombre": "Eden Hazard",
            "Demarcacion": "Delantero",
            "Numero": 7
        },
        {
            "Nombre": "Karim Benzema",
            "Demarcacion": "Delantero",
            "Numero": 9
        },
        {
            "Nombre": "Toni Kroos",
            "Demarcacion": "Centrocampista",
            "Numero": 8
        },
        {
            "Nombre": "Thibaut Courtois",
            "Demarcacion": "Portero",
            "Numero": 1
        }

    ]
    contex_lista_jugadores = {
        'lista_jugadores' : listajugadores
    }
    #para el urls llamada  a madrid
    return render(request,"jugadores/jugadores.html",contex_lista_jugadores)

def datalistamigos(request):
    listaamigos = [
        {
            "Nombre": "Shannon Hillel"
        },
        {
            "Nombre": "Ariel"
        }
    ]
    contex_lista_amigos = {
        'lista_amigos': listaamigos
    }

    return render (request,"paginaAmigos/amigos.html",contex_lista_amigos)


def showgato(request):
    return render(request, "mostrarGato/gato.html")