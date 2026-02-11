from django.contrib import admin
from .models import Department
from .models import Placementcell
from .models import Search

admin.site.register(Department)
admin.site.register(Placementcell)
admin.site.register(Search)