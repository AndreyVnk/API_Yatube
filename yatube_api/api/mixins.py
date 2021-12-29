from rest_framework import viewsets, mixins


class CreateListViewSet(viewsets.GenericViewSet, mixins.ListModelMixin,
                        mixins.CreateModelMixin):
    pass


class CreateViewSet(viewsets.GenericViewSet, mixins.CreateModelMixin):
    pass
