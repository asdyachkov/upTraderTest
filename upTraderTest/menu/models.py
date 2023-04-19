from django.db import models


class MenuSetup(models.Model):
    title = models.TextField(
        null=False, verbose_name="Название набора тем", db_index=True, unique=True
    )

    class Meta:
        verbose_name = "Набор тем для меню"
        verbose_name_plural = "Набор тем для меню"
        db_table = "menu_setup"
        ordering = [
            "title",
        ]

    def __str__(self):
        return str(self.title)


class MenuTitle(models.Model):
    title_value = models.TextField(
        null=False, verbose_name="Тема", db_index=True, unique=True
    )
    menu_setup = models.ForeignKey(
        "MenuSetup", on_delete=models.CASCADE, verbose_name="Id набора тем"
    )

    class Meta:
        verbose_name = "Тема"
        verbose_name_plural = "Темы"
        db_table = "titles"
        ordering = [
            "title_value",
        ]

    def __str__(self):
        return str(self.title_value)


class MenuSubtitle(models.Model):
    subtitle_value = models.TextField(null=False, verbose_name="Подтема", db_index=True)
    title = models.ForeignKey(
        "MenuTitle", on_delete=models.CASCADE, verbose_name="Id темы"
    )

    class Meta:
        verbose_name = "Подтема"
        verbose_name_plural = "Подтемы"
        db_table = "subtitles"
        ordering = [
            "subtitle_value",
        ]

    def __str__(self):
        return str(self.subtitle_value)
