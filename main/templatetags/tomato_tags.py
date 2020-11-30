from django import template

register = template.Library()

@register.filter(name='get_quantity') 
def get_quantity(items_dict,product):
	return items_dict[product]

@register.filter(name='get_total')
def get_total(cart_items):
	total = sum([int(i.quantity)*int((i.price).strip('₹')) for i in cart_items])
	return total