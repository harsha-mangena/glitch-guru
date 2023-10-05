"""
Database models for storing bug information and related data
"""

from django.db import models
from .model_validators import (
    validate_bug_type,
    validate_description_not_empty,
    validate_report_date_not_future,
    validate_status,
)


# Create your models here.
class Bug(models.Model):
    """
    Model for storing bug details in a database.

    This model represents various attributes related to bugs, including their description,
    type, reporting date, and status.

    Attributes:
        description (TextField): A detailed description of the bug.
        bug_type (CharField): The type of bug, such as error, feature request, enhancement, documentation
        report_date (DateTimeField): The date when the bug was reported.
        status (CharField): The current status of the bug (e.g., To Do, In Progress, Done, Under Review, Won't Fix).
    """

    description = models.TextField(
        blank=False,
        null=False,
        max_length=500,
        verbose_name="Bug Description",
        validators=[validate_description_not_empty],
    )

    BUG_TYPE_CHOICES = [
        ("error", "Error"),
        ("feature", "Feature Request"),
        ("enhancement", "Enhancement"),
        ("documentation", "Documentation"),
    ]
    bug_type = models.CharField(
        max_length=20,
        choices=BUG_TYPE_CHOICES,
        blank=False,
        null=False,
        verbose_name="Bug Type",
        validators=[validate_bug_type],
    )

    report_date = models.DateTimeField(
        auto_now_add=True,
        verbose_name="Date of Reporting Bug",
        validators=[validate_report_date_not_future],
    )

    STATUS_CHOICES = [
        ("todo", "To Do"),
        ("in_progress", "In Progress"),
        ("under_review", "Under Review"),
        ("done", "Done"),
        ("wont_fix", "Won't Fix"),
    ]
    status = models.CharField(
        max_length=20,
        choices=STATUS_CHOICES,
        blank=False,
        null=False,
        default="todo",
        verbose_name="Bug Status",
        validators=[validate_status],
    )

    def __str__(self):
        return str(self.description)[:50]

    class Meta:
        """
        Meta Attributes:
            verbose_name (str): A human-readable singular name for the model.
            verbose_name_plural (str): A human-readable plural name for the model.
            ordering (list of str): The default ordering of records in the database.
        """

        verbose_name = "Bug"
        verbose_name_plural = "Bugs"
        ordering = ["-report_date"]
