from django.contrib import admin
from .models import Tags, BlogPost
from ckeditor.widgets import CKEditorWidget
from django import forms


class BlogPostAdminForm(forms.ModelForm):
    content = forms.CharField(widget=CKEditorWidget())

    class Meta:
        model = BlogPost
        fields = '__all__'


@admin.register(BlogPost)
class BlogAdmin(admin.ModelAdmin):
    prepopulated_fields = {"slug": ("title", )}
    filter = ('tags',"date_added")


@admin.register(Tags)
class TagsAdmin(admin.ModelAdmin):
    prepopulated_fields = {"slug": ("name", )}
    