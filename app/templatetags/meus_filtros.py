from django import template

register = template.Library()


# filtro para adicionar uma classe no input gerado pelo django
@register.filter(name='addclass')
def addclass(value, arg):
    # recebe uma classe como parâmetro e aplica a classe no input
    return value.as_widget(attrs={'class': arg})

@register.filter(name='get_item')
def get_item(dictionary, key):
    return dictionary.get(key)