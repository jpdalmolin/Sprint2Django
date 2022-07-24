from socket import fromshare
from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User


class FamiliarFormulario(forms.Form):
    #especificar los campos
    nombre=forms.CharField(max_length=20)
    edad=forms.IntegerField()
    fechaDeNacimiento=forms.DateField()


class AnimalFormulario(forms.Form):
    nombre=forms.CharField(max_length=20)
    fechaDeNacimiento=forms.DateField()
    tipo=forms.CharField(max_length=20)

class VehiculoFormulario(forms.Form):
    kilometraje=forms.IntegerField()
    modelo=forms.IntegerField()
    tipo=forms.CharField(max_length=20)

class UserRegisterForm(UserCreationForm):

    username=forms.CharField()
    email=forms.EmailField()
    password1 = forms.CharField(label= 'Contraseña', widget=forms.PasswordInput)
    password2 = forms.CharField(label= 'Repite Contraseña', widget=forms.PasswordInput)

    first_name= forms.CharField()
    last_name=forms.CharField()

    class Meta:
        model = User
        print(model)
        fields=['username','email','password1','password2','first_name','last_name']
        labels={'username':'nombre','email':'correo','first_name':'nombre','last_name':'apellido'}
        help_texts={k:"" for k in fields} 

class UserEditForm(UserCreationForm):
    
    email=forms.EmailField(label='modificar email')
    password1=forms.CharField(label='contraseña', widget=forms.PasswordInput)
    password2=forms.CharField(label='repita contraseña', widget=forms.PasswordInput)

    class Meta:
        model=User
        fields=['email','password1','password2']
        help_texts={k:"" for k in fields} 

class BlogFormulario(forms.Form):
    title = forms.CharField(max_length=200)
    content = forms.CharField()
   # published = forms.DateTimeField(disabled=True)
    image = forms.ImageField()
    author = forms.ModelChoiceField(queryset=User.objects.filter())
   # created = forms.DateTimeField(disabled=True)
   # updated = forms.DateTimeField(disabled=True) 
    class Meta:
        model=User   
    
    

       

    