# TODO здесь производится настройка пермишенов для нашего проекта
from rest_framework import permissions


class UserPermission(permissions.BasePermission):

    def has_permission(self, request, view):
        if view.action == 'list':
            return True #request.user.is_authenticated and request.user.is_admin
        elif view.action == 'create':
            return request.user.is_authenticated
        elif view.action in ['retrieve', 'update', 'partial_update', 'destroy']:
            return True #request.user.is_admin
        else:
            return False

    def has_object_permission(self, request, view, obj):
        # Deny actions on objects if the user is not authenticated
        if not request.user.is_authenticated:
            return False

        if view.action == 'retrieve':
            return True # request.user.is_admin #obj.author == request.user or
        elif view.action in ['update', 'partial_update']:
            return obj.author == request.user or request.user.is_admin
        elif view.action == 'destroy':
            return obj.author == request.user or request.user.is_admin
        else:
            return False


class IsAdminOrOwner(permissions.BasePermission):
    message = 'None of permissions requirements fulfilled.'

    def has_object_permission(self, request, view, obj):
        # return request.user.is_admin()
        return request.user.is_superuser or request.user and request.user.is_authenticated