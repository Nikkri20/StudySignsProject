from django.contrib import admin

from app1.models import Sign, Test, Category


@admin.register(Sign)
class SignRegister(admin.ModelAdmin):
    pass


@admin.register(Test)
class TestRegister(admin.ModelAdmin):
    fieldsets = (
        ("Сторона карточки с вопросами", {
            'fields': ('question', 'answer'),
        }),
        ("Общее", {
            'fields': ('photo',),
        }),
        ("Сторона карточки с ответами", {
            'fields': ('realObjectPhoto',),
        }),
    )


@admin.register(Category)
class CategoryRegister(admin.ModelAdmin):
    pass


admin.site.site_header = 'Топографические (картографические) условные знаки'
