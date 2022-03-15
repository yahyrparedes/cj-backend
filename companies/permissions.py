from rest_framework.permissions import IsAuthenticated

from .models import Company


class IsCompany(IsAuthenticated):
    """
    Allows access only to users with a company.

    Checks if the user is authenticated, and then check if has a company
    associated a su model.
    """

    def has_permission(self, request, view):
        is_authenticated = super(IsCompany, self).has_permission(request, view)
        if not is_authenticated:
            return False
        try:
            return request.user.company is not None
        except Company.DoesNotExist:
            return False


class IsCompanyAndActive(IsCompany):
    """
    Allows access only to activated company.

    Checks if the company has activated they account.
    """

    def has_permission(self, request, view):
        is_company = super(IsCompanyAndActive, self).has_permission(request, view)
        if not is_company:
            return False
        return request.user.company.is_active
