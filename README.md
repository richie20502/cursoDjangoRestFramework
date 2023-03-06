# cursoDjangoRestFramework

es del curso de 
https://www.udemy.com/course/restful-api-con-python-usando-django-rest-framework/



# AutoSchema object has no atribute "getlink"

Intentando instalar swagger me tope con este error que no es difícil de resolver,  solo es necesario agregar una linea en el apartado de REST_FRAMEWORK del archivo settings.py

REST_FRAMEWORK ={
    ...
    'DEFAULT_SCHEMA_CLASS' : (
        'rest_framework.schemas.coreapi.AutoSchema'
    ),
    ....
} 
Después de esto otro error apareció que tiene que ver con las librearías importadas de la pagina de swagger:

"staticfiles" is not a regitered tag library

y muestra lineas de codigo desde el archivo:

env/lib//site-packages/rest_framework_swagger/templates/rest_framework_swagger/index

y cambiar {% load staticfiles%} por {% load static%} . Eso fue suficiente para hacer funcionar swagger.