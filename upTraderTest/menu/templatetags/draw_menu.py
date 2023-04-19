from django import template

from menu.models import MenuTitle, MenuSubtitle

register = template.Library()


@register.inclusion_tag("menu/draw_menu.html")
def draw_menu(
    setup_select=None, menu_category_select_id=None, menu_category_select=None
):
    if setup_select:
        categories_dict = {}
        menu_subcategories = MenuSubtitle.objects.select_related("title").all()
        for subcategory in menu_subcategories:
            if subcategory.title.menu_setup.title == setup_select:
                if subcategory.title.title_value in categories_dict.keys():
                    categories_dict[str(subcategory.title.title_value)].append(
                        {
                            "category_id": subcategory.title.id,
                            "subcategories": subcategory.subtitle_value,
                            "theme": subcategory.title.menu_setup.title,
                        }
                    )
                else:
                    categories_dict[subcategory.title.title_value] = []
        categories_list = []
        for item in categories_dict.keys():
            dict_ = categories_dict[item][0]
            dict_["category"] = item
            categories_list.append(dict_)
        return {
            "setup_select": setup_select,
            "menu_categories": categories_list,
            "menu_category_select_id": menu_category_select_id,
            "menu_category_select": menu_category_select,
        }
