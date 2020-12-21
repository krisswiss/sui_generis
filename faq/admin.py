from django.contrib import admin
from .models import faq


# Register your models here.

class faqAdmin(admin.ModelAdmin):
    list_display = (
        'question',
        'answer',
    )

admin.site.register(faq, faqAdmin)

