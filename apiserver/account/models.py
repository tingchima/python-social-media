from django.contrib.auth.models import AbstractBaseUser
from django.db import models
from shared.models import Base


class User(AbstractBaseUser, Base):
    """Represents a user model."""

    class Meta:
        db_table_comment = "user data"
        db_table = "users"

    class UserType(models.IntegerChoices):
        """Represents a user type choices."""

        COMMON = 1
        OFFICIAL = 2

    username = models.CharField(
        max_length=255,
        default="",
        db_comment="username",
    )
    email = models.EmailField(
        db_index=True,
        max_length=255,
        unique=True,
        db_comment="email",
    )
    user_type = models.CharField(
        choices=UserType,
        default=UserType.COMMON,
        db_comment="type of user",
    )
    avatar_url = models.URLField(
        default="",
        db_comment="url of user avatar",
    )
    is_disabled = models.BooleanField(
        default=False,
        db_comment="status of user was not actived",
    )
    disabled_at = models.DateTimeField(
        null=True,
        db_comment="the datetime of user was not actived",
    )
