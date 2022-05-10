from django.http import HttpResponse


#Esto es una vista
def bienvenida(request): 
    return HttpResponse("Bienvenido a este curso de django. ")

def home(request):
    return HttpResponse("<p style='color:Green' >Bienvenido al Home <p>")
    
def categoriaEdad(request,edad):
    return HttpResponse("<h1>Categoria es = a: %d<h1>" %edad)

