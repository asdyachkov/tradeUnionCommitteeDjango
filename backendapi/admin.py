from django.contrib import admin
from django.utils.safestring import mark_safe
from .models import News, Pins, Documents, Benefits, StudentsContacts, TeachersContacts


class NewsAdmin(admin.ModelAdmin):
    list_display = ("id", "theme", "created_at")
    list_display_links = (
        "id",
        "theme",
    )
    search_fields = ("id", "theme", "created_at")


class PinsAdmin(admin.ModelAdmin):
    list_display = ("id", "theme", "get_image")
    list_display_links = ("id", "theme", "get_image")
    search_fields = ("id", "theme", "get_image")
    readonly_fields = ("get_image",)

    def get_image(self, obj):
        return mark_safe(f"<img src={obj.image_link} width='50' height='50'")

    get_image.short_description = "Изображение пина"


class DocumentsAdmin(admin.ModelAdmin):
    list_display = ("id", "theme", "description")
    list_display_links = (
        "id",
        "theme",
    )
    search_fields = ("id", "theme", "description")


class BenefitsAdmin(admin.ModelAdmin):
    list_display = ("id", "theme", "description")
    list_display_links = (
        "id",
        "theme",
    )
    search_fields = ("id", "theme", "description")


class StudentsContactsAdmin(admin.ModelAdmin):
    list_display = ("id", "lecture_hall", "working_hours", "phone", "mail")
    list_display_links = ("id", "phone", "mail")
    search_fields = ("id", "lecture_hall", "phone", "mail")


class TeachersContactsAdmin(admin.ModelAdmin):
    list_display = ("id", "lecture_hall", "working_hours", "phone", "mail")
    list_display_links = ("id", "phone", "mail")
    search_fields = ("id", "lecture_hall", "phone", "mail")


admin.site.register(News, NewsAdmin)
admin.site.register(Pins, PinsAdmin)
admin.site.register(Documents, DocumentsAdmin)
admin.site.register(Benefits, BenefitsAdmin)
admin.site.register(StudentsContacts, StudentsContactsAdmin)
admin.site.register(TeachersContacts, TeachersContactsAdmin)
