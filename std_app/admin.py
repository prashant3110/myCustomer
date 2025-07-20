from django.contrib import admin
from .models import Student

# Define ModelAdmin class
class StudentAdmin(admin.ModelAdmin):
    list_display = ['name', 'phone', 'aadhaar', 'address', 'purpose', 'date']  # Use list_display instead of info_list

# Register Student model with StudentAdmin
admin.site.register(Student, StudentAdmin)