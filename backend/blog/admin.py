from django.contrib import admin
from django.db.models.base import Model
from blog.models import Email, Profile, Post, Tag, Message

from blog.email_corpus import EMAIL

from django.core.mail import send_mail


# Register your models here.

@admin.register(Profile)
class ProfileAdmin(admin.ModelAdmin):
    model = Profile


@admin.register(Tag)
class TagAdmin(admin.ModelAdmin):
    model = Tag

@admin.register(Email)
class EmailAdmin(admin.ModelAdmin):
    model = Email

@admin.register(Message)
class MessageAdmin(admin.ModelAdmin):
    model = Message

    list_display = (
        'first_name',
        'email',
        'read'
    )

    list_filter = (
        'read',
    )

@admin.action(description="Send post to newsletter")
def send_to_newsletter(modeladmin, request, queryset):

    email_body = EMAIL

    email_body = email_body.replace('EMAIL_TITLE', str(list(queryset)[0].title))

    email_body = email_body.replace('EMAIL_BODY', list(queryset)[0].truncated_body)

    email_body = email_body.replace('SLUG', list(queryset)[0].slug)


    newsletter = list(Email.objects.all())
    subject = 'New post from Road to Data Science'


    send_mail(subject,
            'Hi a new article is here!',
            from_email='roadtodatascience.newsletter@gmail.com',
            recipient_list=['hovomax415@tst999.com'],
            fail_silently=False,
            html_message=email_body)


@admin.register(Post)
class PostAdmin(admin.ModelAdmin):
    model = Post

    list_display = (
        "id",
        "title",
        "subtitle",
        "slug",
        "publish_date",
        "published",
        "reading_time",

    )
    list_filter = (
        "published",
        "publish_date",
    )
    list_editable = (
        "title",
        "subtitle",
        "slug",
        "publish_date",
        "published",
        "reading_time",
    )
    search_fields = (
        "title",
        "subtitle",
        "slug",
        "body",
        "truncated_body"
    )
    prepopulated_fields = {
        "slug": (
            "title",
            "subtitle",
        )
    }
    date_hierarchy = "publish_date"
    save_on_top = True

    actions = [send_to_newsletter]



