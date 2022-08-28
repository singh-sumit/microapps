from rest_framework.permissions import BasePermission
from rest_framework_simplejwt.models import TokenUser

SERVICE_IDENTIFIER = 'NOTEBOOK'


class IsServiceAccessible(BasePermission):
    """
    Allow only access to user having corresponding service scope access.
    """

    def has_permission(self, request, view):
        try:
            assert request.user and request.user.is_authenticated
            if isinstance(request.user, TokenUser):
                return SERVICE_IDENTIFIER in request.auth.payload.get('aud')
            else:
                return False
        except AssertionError:
            return False
