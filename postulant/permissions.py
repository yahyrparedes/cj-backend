from rest_framework.permissions import IsAuthenticated

from .models import Postulant


class IsPostulant(IsAuthenticated):
    """
    Allows access only to users with a company.

    Checks if the user is authenticated, and then check if has a company
    associated a su model.
    """

    def has_permission(self, request, view):
        is_authenticated = super(IsPostulant, self).has_permission(request, view)
        if not is_authenticated:
            return False
        try:
            return request.user.postulant is not None
        except Postulant.DoesNotExist:
            return False


class IsPostulantAndActive(IsPostulant):
    """
    Allows access only to activated company.

    Checks if the company has activated they account.
    """

    def has_permission(self, request, view):
        is_postulant = super(IsPostulantAndActive, self).has_permission(request, view)
        if not is_postulant:
            return False
        return request.user.postulant.is_active
