from django import template

register = template.Library()

@register.filter()
def currency(value):
    stopfilter = ["редиска", "морковка", "кабачок"]

    for word in value.split():
        if word.lower() in stopfilter:
            value = value.replace(word, f"{word[0]}{'*' * (len(word) - 1)}")
    return value

