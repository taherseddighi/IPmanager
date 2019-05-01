from django.contrib import admin
from .models import Available_Public_IP, Used_Public_IP, Used_Private_IP, Token
# Register your models here.
admin.site.register(Available_Public_IP)
admin.site.register(Used_Public_IP)
admin.site.register(Used_Private_IP)
admin.site.register(Token)