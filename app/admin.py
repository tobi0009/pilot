from django.contrib import admin # type: ignore
from .models import GeneralInfo, Service, Testimonial, FrequentlyAskedQuestion, ContactFormLog, Author, Blog

# Register your models here.
@admin.register(GeneralInfo)



class GeneralInfoAdmin(admin.ModelAdmin):
       list_display =[
              'company_name',
              'location',
              'email',
              'phone',
              'open_hours',
              ]


@admin.register(Service)
class ServiceAdmin(admin.ModelAdmin):
       
       list_display =[
              'title',
              'description'
       ]

       search_fields: list
       search_fields = [
              'title',
              'description'
       ]

@admin.register(Testimonial)
class TestimonialAdmin(admin.ModelAdmin):
       list_display = [
              'username',
              'user_job_title',
              'display_rating_count'
       ]

       def display_rating_count(self, obj):
              return '*' * obj.rating_count
       
       display_rating_count.short_description = 'Rating'

@admin.register(FrequentlyAskedQuestion)
class FrequentlyAskedQuestionAdmin(admin.ModelAdmin):
       pass

@admin.register(ContactFormLog)
class ContactFormLogAdmin(admin.ModelAdmin):
       
       list_display= [
              'email',
              'is_success',
              'is_error',
              'action_time'
       ]

@admin.register(Author)
class AuthorAdmin(admin.ModelAdmin):
       list_display = [
              'first_name',
              'last_name'
       ]


@admin.register(Blog)
class BlogAdmin(admin.ModelAdmin):
       list_display = [
              'title',
              'author',
              'created_at'
       ]