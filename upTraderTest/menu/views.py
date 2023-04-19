from django.shortcuts import render

from menu.models import MenuTitle


def index(request, title=None):
    if title:
        title_ = MenuTitle.objects.get(title_value=title)
        return render(
            request,
            "menu/main.html",
            context={
                "menu_category_select_id": title_.id,
                "menu_category_select": title_.menu_setup.title,
            },
        )
    else:
        return render(
            request,
            "menu/main.html",
            context={"menu_category_select_id": None, "menu_category_select": None},
        )
