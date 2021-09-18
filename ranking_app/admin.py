from django.contrib import admin

# Own
from ranking_app.models import RankingTable


class RankingTableAdmin(admin.ModelAdmin):
    list_display = ("user_nickname", "sum_of_all_user_points")


admin.site.register(RankingTable, RankingTableAdmin)
