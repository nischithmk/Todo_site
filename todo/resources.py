from import_export import resources
from .models import Todo

class PersonResource(resources.ModelResource):
    class Meta:
        model = Todo