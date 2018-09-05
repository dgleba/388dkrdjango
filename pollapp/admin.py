from django.contrib import admin

# Register your models here.
BOOTSTRAP_ADMIN_SIDEBAR_MENU = False
from pollapp.models import Question
admin.site.register(Question)