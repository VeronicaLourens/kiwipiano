from django.contrib import admin
from .models import Booking, Lesson, Profile
from django_summernote.admin import SummernoteModelAdmin


@admin.register(Booking)
class BookingAdmin(SummernoteModelAdmin):

    list_display = ('user', 'date', 'start_time', 'lesson_name')
    list_filter = ('user', 'date')
    search_fields = ['lesson_name', 'user']



    def confirmed_booking(self, queryset):
        queryset.update(confirmed=True)



@admin.register(Lesson)
class LessonAdmin(admin.ModelAdmin):
    list_display = ('lesson_name', 'lesson_date', 'start_time', 'lesson_status')
    list_filter = ('lesson_date', 'lesson_name')
    search_fields = ('lesson_status', 'lesson_name')



# admin.site.register(Profile)

@admin.register(Profile)
class ProfileAdmin(admin.ModelAdmin):

    list_display = ('user', 'email_address')
    list_filter = ('user', 'email_address')
    search_fields = ('user', 'email_address')



