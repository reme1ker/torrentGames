from django.contrib import admin

from backend.core.models import Games


class GamesModelAdmin(admin.ModelAdmin):
    list_display = ["game_name", "upload_date", "release_date", "developer", "description", "os",
                    "processor", "ram", "video_card", "free_memory"]
    list_editable = []

    class Meta:
        model = Games


admin.site.register(Games, GamesModelAdmin)

