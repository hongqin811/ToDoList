from django.contrib import admin

# Register your models here.
from .models import Member, Work, Action

admin.site.register(Member)
admin.site.register(Work)
admin.site.register(Action)

