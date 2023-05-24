from django import template
from django.template.defaultfilters import stringfilter

from backend.core.models import Games, Categories, Review, Basket
from backend.users.models import Profile

register = template.Library()


@register.simple_tag()
def get_games():
    return Games.objects.filter(show_in_slider=True)


@register.simple_tag()
def get_games_new():
    return Games.objects.filter(new=True).order_by('-id')[:7]


@register.simple_tag()
def get_categories():
    return Categories.objects.all()


@register.simple_tag()
def get_reviews():
    profile = Profile.objects.all()
    reviews = Review.objects.all()
    return {
        'reviews': reviews,
        'profile': profile,
    }


@register.simple_tag()
def get_baskets():
    return Basket.objects.all()
