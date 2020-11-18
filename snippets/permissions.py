from rest_framework import permissions


class IsOwnerOrReadOnly(permissions.BasePermission):
    """
    Custom permission to only allow owners of an object to edit it.
    BasePermission 클래스를 상속받아 has_permission 또는 has_object_permission를 메소드오버라이딩한다.
    """

    def has_object_permission(self, request, view, obj):
        # SAFE_METHODS: permissions 내부에 GET, HEAD, OPTIONS 메소드를 담고 있는 튜플 형태의 변수이다.
        if request.method in permissions.SAFE_METHODS:
            return True

        # Write permissions are only allowed to the owner of the snippet.
        return obj.owner == request.user