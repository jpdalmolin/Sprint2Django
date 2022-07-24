from dataclasses import fields
from django import forms 
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User

#clase ModelForm¶ Si está creando una aplicación basada en una base de datos,
#  es probable que tenga formularios que se correspondan estrechamente con los modelos de Django.
#  Por ejemplo, puede tener un modelo BlogComment y desea crear un formulario que
#  permita a las personas enviar comentarios.
#  En este caso, sería redundante definir los tipos de campo en su formulario,
#  porque ya ha definido los campos en su modelo. Por esta razón,
#  Django proporciona una clase auxiliar que te permite crear una clase Form
#  a partir de un modelo Django.

class CursoFormulario(forms.Form):

    #Especificar los campos
    curso = forms.CharField()
    camada = forms.IntegerField()


class ProfesorFormulario(forms.Form):   
    nombre= forms.CharField(max_length=30)
    apellido= forms.CharField(max_length=30)
    email= forms.EmailField()
    profesion= forms.CharField(max_length=30)

class UserRegisterForm(UserCreationForm):
    # email = forms.EmailField()
    password1 = forms.CharField(label= 'Contraseña', widget= forms.PasswordInput)
    password2 = forms.CharField(label= 'repite la contraseña', widget=forms.PasswordInput)
    #extendemos el contenido de el formulario viejo agregando dos campos más
    # last_name: forms.CharField()
    # first_name: forms.CharField()

    class Meta:
        model = User                                               #agregamos los campos
        fields = ['username', 'email', 'password1', 'password2', 'last_name', 'first_name']
        labels = {'username': 'nombre', 'email':'correo','last_name': 'apellido', 'first_name':'nombre'}
        help_texts= {k:"" for k in fields}

#La clase meta es una clase interna en los modelos de Django.
#Que contienen opciones Meta (metadatos) que se utilizan para
#cambiar el comportamiento de los campos de su modelo,
#como cambiar las opciones de orden, si el modelo es abstracto o no,
#versiones singulares y plurales del nombre, etc. 

class UserEditForm(UserCreationForm): 
    #definimos lo básico para modificar del usuario

    email = forms.EmailField(label='modificar email')
    password1 = forms.CharField(label='contraseña', widget=forms.PasswordInput)
    password2 = forms.CharField(label= 'repita contraseña', widget=forms.PasswordInput)

    class Meta:
        model = User
        fields = ['email', 'password1', 'password2']
        help_texts= {k:"" for k in fields}


#class models.User
# User objects have the following fields:

# username¶
# Required. 150 characters or fewer. Usernames may contain alphanumeric, _, @, +, . and - characters.

# The max_length should be sufficient for many use cases. If you need a longer length, please use a custom user model. If you use MySQL with the utf8mb4 encoding (recommended for proper Unicode support), specify at most max_length=191 because MySQL can only create unique indexes with 191 characters in that case by default.

# first_name¶
# Optional (blank=True). 150 characters or fewer.

# last_name¶
# Optional (blank=True). 150 characters or fewer.

# email¶
# Optional (blank=True). Email address.

# password¶
# Required. A hash of, and metadata about, the password. (Django doesn’t store the raw password.) Raw passwords can be arbitrarily long and can contain any character. See the password documentation.

# groups¶
# Many-to-many relationship to Group