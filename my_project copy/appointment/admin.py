from django.contrib import admin

# Register your models here.
class AppointmentAdmin(admin.ModelAdmin):
    list_display = ('id', 'user_id', 'date_time', 'status', 'is_approved', 'notes')
    list_filter = ('status', 'is_approved', 'date_time')
    search_fields = ('user_id', 'notes')
    actions = ['approve_appointments']

    def approve_appointments(self, request, queryset):
        queryset.update(is_approved=True)
    approve_appointments.short_description = "Approve selected appointments"
