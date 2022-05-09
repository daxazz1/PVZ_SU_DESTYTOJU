from django.contrib import admin
from .models import Project, Client, Employee, Job, Invoice

# Register your models here.


class JobInline(admin.TabularInline):
    model = Job
    extra = 0

class InvoiceInline(admin.TabularInline):
    model = Invoice
    extra = 0

class ProjectAdmin(admin.ModelAdmin):
    list_display = ('name', 'start_date', 'end_date', 'client', 'manager')
    inlines = [JobInline, InvoiceInline]
    list_editable = ('start_date', 'end_date', 'client', 'manager')

class ClientAdmin(admin.ModelAdmin):
    list_display = ('name', 'lastname', 'company', 'contacts')


class EmployeeAdmin(admin.ModelAdmin):
    list_display = ('name', 'lastname', 'position')

admin.site.register(Project, ProjectAdmin)
admin.site.register(Client, ClientAdmin)
admin.site.register(Employee, EmployeeAdmin)
admin.site.register(Job)
admin.site.register(Invoice)