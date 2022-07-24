from django.http import HttpResponse
from django.shortcuts import render
from AppCoder.models import Animales, Familiar,Vehiculos,Avatar
from django.template import Template,Context,loader
from AppCoder.forms import FamiliarFormulario
from AppCoder.forms import AnimalFormulario
from AppCoder.forms import VehiculoFormulario
from AppCoder.forms import BlogFormulario
from AppCoder.forms import UserEditForm
from django.views.generic import ListView
from django.views.generic.detail import DetailView
from django.views.generic.edit import CreateView,UpdateView,DeleteView
from django.urls import reverse_lazy
from django.contrib.auth.forms import AuthenticationForm,UserCreationForm
from django.contrib.auth import login,logout,authenticate
from django.contrib.auth.models import User
from django import forms
from AppCoder.forms import UserRegisterForm
from django.contrib.auth.mixins import LoginRequiredMixin
from django.contrib.auth.decorators import login_required
from django.shortcuts import render, get_object_or_404
from .models import Post
from django.views import generic



def familiar(self):

    familiar1 = Familiar(nombre="juan", edad="20",fechaDeNacimiento="2002-10-20")
    familiar1.save()
    
   
    familiar2 = Familiar(nombre="Maria", edad="40",fechaDeNacimiento="1982-07-13")
    familiar2.save()

    familiar3 = Familiar(nombre="Marcos", edad="30",fechaDeNacimiento="1992-08-20")
    familiar3.save()

    diccionario = {"nombre1":familiar1.nombre, "edad1":familiar1.edad,"fechaDeNacimiento1":familiar1.fechaDeNacimiento,"nombre2":familiar2.nombre, "edad2":familiar2.edad,"fechaDeNacimiento2":familiar2.fechaDeNacimiento,"nombre3":familiar3.nombre, "edad3":familiar3.edad,"fechaDeNacimiento3":familiar3.fechaDeNacimiento}
    
    nueva_plantilla= loader.get_template('template_entregable.html')


    documentoDeTexto = nueva_plantilla.render(diccionario)


    return HttpResponse(documentoDeTexto)



@login_required
def animales(request):

      return render(request, "AppCoder/animales.html")

def vehiculos(request):

      return render(request, "AppCoder/vehiculos.html")

def familiarFormulario(request):
      if request.method == 'POST':

            miFormulario= FamiliarFormulario(request.POST)
            print(miFormulario)
            
            if miFormulario.is_valid:

                  informacion =miFormulario.cleaned_data
                  print(informacion)
                  familiar=Familiar(nombre=informacion['nombre'], edad=informacion['edad'],fechaDeNacimiento=informacion['fechaDeNacimiento'])

                  familiar.save()

                  return render(request, "AppCoder/inicio.html")

      else:

            miFormulario= FamiliarFormulario()

      return render(request, "AppCoder/familiarFormulario.html", {"miFormulario":miFormulario})

def animalFormulario(request):
      if request.method == 'POST':

            miFormulario= AnimalFormulario(request.POST)
            print(miFormulario)
            
            if miFormulario.is_valid:

                  informacion =miFormulario.cleaned_data
                  print(informacion)
                  animal=Animales(nombre=informacion['nombre'], fechaDeNacimiento=informacion['fechaDeNacimiento'],tipo=informacion['tipo'])

                  animal.save()

                  return render(request, "AppCoder/inicio.html")

      else:

            miFormulario= AnimalFormulario()

      return render(request, "AppCoder/animalFormulario.html", {"miFormulario":miFormulario})


def vehiculoFormulario(request):
      if request.method == 'POST':

            miFormulario= VehiculoFormulario(request.POST)
            print(miFormulario)
            
            if miFormulario.is_valid:

                  informacion =miFormulario.cleaned_data
                  print(informacion)
                  vehiculo=Vehiculos(kilometraje=informacion['kilometraje'], modelo=informacion['modelo'],tipo=informacion['tipo'])

                  vehiculo.save()

                  return render(request, "AppCoder/inicio.html")

      else:

            miFormulario= VehiculoFormulario()

      return render(request, "AppCoder/vehiculoFormulario.html", {"miFormulario":miFormulario})


def busquedaNombre(request):

      return render(request, "AppCoder/busquedaNombre.html")


def resultadosBusqueda(request):

      if request.GET['nombre']:
      #respuesta= f" ESTOY BUSCANDO AL FAMILIAR DE NOMBRE : {request.GET['nombre']}"
            nombre= request.GET['nombre']
            familiares=Familiar.objects.filter(nombre__icontains=nombre) 

            return render(request, "AppCoder/resultadosBusqueda.html",{"familiares":familiares,"nombre":nombre})

      else:
            respuesta= "No enviaste datos"

      return HttpResponse(respuesta)

def leerFamiliares(request):

      familiares=Familiar.objects.all()

      contexto={"familiares":familiares}

      return render(request, "AppCoder/leerFamiliares.html",contexto)

def eliminarFamiliar(request,familiar_nombre):

      familiar=Familiar.objects.get(nombre=familiar_nombre)
      familiar.delete()

      familiares=Familiar.objects.all()

      contexto={"familiares":familiares}
      
      return render(request,"AppCoder/leerFamiliares.html",contexto)

def editarFamiliar(request,familiar_nombre):

      familiar=Familiar.objects.get(nombre=familiar_nombre)

      if request.method =='POST':
            miFormulario=FamiliarFormulario(request.POST)

            print (miFormulario)

            if miFormulario.is_valid:
                  informacion= miFormulario.cleaned_data

                  familiar.nombre=informacion['nombre']
                  familiar.edad=informacion['edad']
                  familiar.fechaDeNacimiento=informacion['fechaDeNacimiento']

                  familiar.save()

                  return render(request, "AppCoder/inicio.html")

      else:
            miFormulario=FamiliarFormulario(initial={'nombre':familiar.nombre, 'edad':familiar.edad,'fechaDeNacimiento':familiar.fechaDeNacimiento})

      return render(request,"AppCoder/editarFamiliar.html", {"miFormulario":miFormulario, "familiar_nombre":familiar_nombre}) 
                 

class AnimalesList(LoginRequiredMixin,ListView):

      model=Animales
      template_name ="AppCoder/animales_list.html"

class AnimalesDetalle(generic.DetailView):

      model=Animales
      template_name="AppCoder/animales_detalle.html"

class AnimalesCreacion(CreateView):

      model=Animales
      success_url="/AppCoder/animales/list"
      fields=['nombre','tipo','fechaDeNacimiento']

class AnimalesUpdate(UpdateView):

      model=Animales
      success_url="/AppCoder/animales/list"
      fields=['nombre','tipo','fechaDeNacimiento']

class AnimalesDelete(DeleteView):

      model=Animales
      success_url="/AppCoder/animales/list"
      
def login_request(request):

      if request.method =="POST":
            form = AuthenticationForm(request,data=request.POST)
            print(form)
            if form.is_valid():
                  usuario=form.cleaned_data.get('username')
                  contra=form.cleaned_data.get('password')
                  print(usuario,contra)
                  user= authenticate(username=usuario, password=contra)
                  print(user)
                  if user is not None:
                        login(request,user)

                        return render(request,"AppCoder/inicio.html", {"mensaje":f"Bienvenido {usuario}"})
                  else:
                        print(2)
                        return render(request,"AppCoder/inicio.html", {"mensaje":"Error datos incorrectos"})

            else:

                  return render(request,"AppCoder/inicio.html", {"mensaje":"Error, formulario erroneo"})
      form=AuthenticationForm()
      print(3)
      return render(request,"AppCoder/login.html", {'form':form})

def register(request):

      if request.method == 'POST':

            form= UserCreationForm(request.POST)

            if form.is_valid():

                  username=form.cleaned_data['username']
                  form.save()
                  return render(request,"AppCoder/inicio.html", {"mensaje":"Usuario Creado !"})

      else:
            form=UserRegisterForm()

      return render(request,"AppCoder/registro.html",{"form":form})      

@login_required
def editarPerfil(request):
      #Instancia del login
      usuario =request.user
      
      if request.method =='POST':
            miFormulario=UserEditForm(request.POST)
            if miFormulario.is_valid():

                  informacion=miFormulario.cleaned_data
                  #datos que se modificaran
                  usuario.email=informacion['email']
                  usuario.password1=informacion['password1']
                  usuario.password2=informacion['password1']
                  usuario.save()

                  return render(request, "AppCoder/inicio.html") #vuelve al inicio
            
      else:

            miFormulario=UserEditForm(initial={'email':usuario.email})

      return render(request, "AppCoder/editarPerfil.html",{"miFormulario":miFormulario, "usuario":usuario})


def inicio(request):

      avatares = Avatar.objects.filter(user=request.user.id)

      try:
            return render(request, "AppCoder/inicio.html", {"url":avatares[0].imagen.url} )
      except IndexError:
            return render(request, "AppCoder/inicio.html")


def blogFormulario(request):
      
      if request.method == 'POST':

            miFormulario= BlogFormulario(request.POST,request.FILES)
            print(miFormulario)
            
            if miFormulario.is_valid:

                  informacion =miFormulario.cleaned_data
                  print(informacion)
                  
                  posts=Post(title=informacion['title'], content=informacion['content'],image=informacion['image'],author=informacion['author'])

                  posts.save()

                  return render(request, "AppCoder/inicio.html")

      else:

            miFormulario= BlogFormulario()

      return render(request, "AppCoder/blogFormulario.html", {"miFormulario":miFormulario})


def blog(request):
    posts = Post.objects.all()
    return render(request, "AppCoder/blog.html", {'posts':posts})

class BlogList(ListView):

      model=Post
      template_name= "AppCoder/post_list.html"

class BlogDetalle(DetailView):

      model=Post
      template_name ="AppCoder/post_detalle.html"

    