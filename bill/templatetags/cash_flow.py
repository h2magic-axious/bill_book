from django import template

register = template.Library()


@register.filter
def cash_flow(result_list):
    cash = round(sum(i.amount for i in result_list) / 100, 2)
    color = "red" if cash < 0 else "black"

    return f"<span style='color: {color}; font-weight: bold'>{cash}</span>"
