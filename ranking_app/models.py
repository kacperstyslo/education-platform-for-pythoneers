from django.db import models


class RankingTable(models.Model):
    """
    This table store sum of all users points. 'ranking_app' use this
    table to generate ranking table.
    """

    class Meta:
        ordering = ("-sum_of_all_user_points",)

    user_nickname = models.CharField(max_length=50, default="User")
    sum_of_all_user_points = models.IntegerField(default=0)
