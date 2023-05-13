from django.contrib import admin

from backend.core.models import Games, Categories, Developers, OperationSystems, Processors, VideoCards


class GamesModelAdmin(admin.ModelAdmin):
    list_display = ["game_name", "upload_date", "release_date", "developer", "description", "os", "get_categories",
                    "processor", "ram",
                    "video_card", "free_memory"]
    list_editable = []

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


class VideoCardsModelAdmin(admin.ModelAdmin):
    list_display = ["video_card_name"]

    class Meta:
        model = VideoCards


admin.site.register(Developers, DevelopersModelAdmin)
admin.site.register(OperationSystems, OperationSystemsModelAdmin)
admin.site.register(Processors, ProcessorsModelAdmin)
admin.site.register(VideoCards, VideoCardsModelAdmin)
admin.site.register(Categories, CategoriesModelAdmin)
admin.site.register(Games, GamesModelAdmin)
