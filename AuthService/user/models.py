from django.db import models
from django.db.models import CharField, BooleanField, DateTimeField, ForeignKey


class Role(models.Model):
    name = CharField(max_length=25, unique=True)

    class Meta:
        db_table = "roles"

    def __str__(self):
        return self.name


class Permission(models.Model):
    resource = CharField(max_length=50)
    action = CharField(max_length=50)

    class Meta:
        db_table = "permissions"
        unique_together = ["resource", "action"]

    def __str__(self):
        return f"{self.resource}:{self.action}"


class PermissionRole(models.Model):
    role_id = ForeignKey(Role, on_delete=models.CASCADE)
    permission_id = ForeignKey(Permission, on_delete=models.CASCADE)

    class Meta:
        db_table = "permission_roles"
        unique_together = ["role_id", "permission_id"]


class User(models.Model):
    email = CharField(unique=True)
    password = CharField(max_length=128)
    name = CharField(max_length=50)
    is_active = BooleanField(default=True)
    role_id = ForeignKey(Role, on_delete=models.SET_NULL, null=True)
    created_at = DateTimeField(auto_now_add=True)
    updated_at = DateTimeField(auto_now=True)

    class Meta:
        db_table = "users"

    def __str__(self):
        return f"{self.name}, with email: {self.email}"
