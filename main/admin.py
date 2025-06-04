from django.contrib import admin
from .models import Student, Program, Manager, Classmate

@admin.register(Student)
class StudentAdmin(admin.ModelAdmin):
    list_display = ('full_name', 'email', 'phone')
    search_fields = ('full_name', 'email')

@admin.register(Program)
class ProgramAdmin(admin.ModelAdmin):
    list_display = ('title', 'url')
    search_fields = ('title', 'description')
    list_filter = ('title',)

@admin.register(Manager)
class ManagerAdmin(admin.ModelAdmin):
    list_display = ('full_name', 'role', 'email')
    search_fields = ('full_name', 'email')
    list_filter = ('role',)

@admin.register(Classmate)
class ClassmateAdmin(admin.ModelAdmin):
    list_display = ('full_name', 'email', 'phone')
    search_fields = ('full_name', 'email')
