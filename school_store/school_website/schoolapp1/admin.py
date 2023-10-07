from django.contrib import admin
from .models import Department, Course, Material, User


@admin.register(Department)
class DepartmentAdmin(admin.ModelAdmin):
    list_display = ('name',)

@admin.register(Course)
class CourseAdmin(admin.ModelAdmin):
    list_display = ('department', 'name')

@admin.register(Material)
class MaterialAdmin(admin.ModelAdmin):
    list_display = ('name',)

@admin.register(User)
class UserAdmin(admin.ModelAdmin):
    list_display = ('name', 'dob', 'age', 'gender', 'phone_number', 'email', 'department', 'course', 'purpose')
    list_filter = ('gender', 'department', 'course')

