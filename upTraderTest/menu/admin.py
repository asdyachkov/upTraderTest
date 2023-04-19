from django.contrib import admin
from .models import MenuTitle, MenuSubtitle, MenuSetup


class MenuTitleInline(admin.TabularInline):
    model = MenuTitle
    fk_name = "menu_setup"
    verbose_name = "Id набора тем"
    verbose_name_plural = "Id наборов тем"
    extra = 1


class MenuSubtitleInline(admin.TabularInline):
    model = MenuSubtitle
    fk_name = "title"
    verbose_name = "Id темы"
    verbose_name_plural = "Id тем"
    extra = 1


class MenuSetupAdmin(admin.ModelAdmin):
    list_display = ("id", "title")
    list_display_links = ("id", "title")
    search_fields = ("title",)
    inlines = [
        MenuTitleInline,
    ]


class MenuTitleAdmin(admin.ModelAdmin):
    list_display = ("id", "title_value", "menu_setup_id")
    list_display_links = ("id", "title_value", "menu_setup_id")
    search_fields = ("title_value", "menu_setup_id")
    inlines = [
        MenuSubtitleInline,
    ]


class MenuSubtitleAdmin(admin.ModelAdmin):
    list_display = ("id", "subtitle_value", "title_id")
    list_display_links = ("id", "subtitle_value", "title_id")
    search_fields = ("subtitle_value", "title_id")


admin.site.register(MenuSetup, MenuSetupAdmin)
admin.site.register(MenuTitle, MenuTitleAdmin)
admin.site.register(MenuSubtitle, MenuSubtitleAdmin)
