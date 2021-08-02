from django.contrib import admin

from task_statistics_app.models import TasksStatistics


class TasksStatisticsAdmin(admin.ModelAdmin):
    list_display = (
        "task_title",
        "sum_of_all_tries_per_task",
    )


admin.site.register(TasksStatistics, TasksStatisticsAdmin)
