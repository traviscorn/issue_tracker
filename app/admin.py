from django.contrib import admin
from .models import Team, Employee, Issue, Update

admin.site.register(Team)
admin.site.register(Employee)
admin.site.register(Issue)
admin.site.register(Update)