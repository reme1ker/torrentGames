from django.contrib import admin

from backend.core.models import Games, Categories, Developers, OperationSystems, Processors, VideoCards, Screenchots, \
    InterfaceLanguage, Review, Basket, Order


class ImageInline(admin.StackedInline):
    model = Screenchots


class GamesModelAdmin(admin.ModelAdmin):
    list_display = ["game_name", "price", "discount", "release_date", "developer",
                    "os", "get_categories",
                    "processor", "ram",
                    "video_card", "free_memory"]
    search_fields = ["game_name", "release_date"]
    inlines = [ImageInline]

    class Meta:
        model = Games


class CategoriesModelAdmin(admin.ModelAdmin):
    list_display = ["category_name"]

    class Meta:
        model = Categories


class DevelopersModelAdmin(admin.ModelAdmin):
    list_display = ["developer_name"]

    class Meta:
        model = Developers


class OperationSystemsModelAdmin(admin.ModelAdmin):
    list_display = ["os_name"]

    class Meta:
        model = OperationSystems


class ProcessorsModelAdmin(admin.ModelAdmin):
    list_display = ["processor_name"]

    class Meta:
        model = Processors


class InterfaceLanguageModelAdmin(admin.ModelAdmin):
    list_display = ["language_name"]

    class Meta:
        model = InterfaceLanguage


class VideoCardsModelAdmin(admin.ModelAdmin):
    list_display = ["video_card_name"]

    class Meta:
        model = VideoCards


class RevieWModelAdmin(admin.ModelAdmin):
    list_display = ["name", "text", "parent", "game", ]
    search_fields = ["text"]

    class Meta:
        model = Review


admin.site.register(Developers, DevelopersModelAdmin)
admin.site.register(OperationSystems, OperationSystemsModelAdmin)
admin.site.register(Processors, ProcessorsModelAdmin)
admin.site.register(VideoCards, VideoCardsModelAdmin)
admin.site.register(Categories, CategoriesModelAdmin)
admin.site.register(InterfaceLanguage, InterfaceLanguageModelAdmin)
admin.site.register(Games, GamesModelAdmin)
admin.site.register(Review, RevieWModelAdmin)
# admin.site.register(Order)
