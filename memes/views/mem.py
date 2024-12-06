from django.db.models import Count, Q
from rest_framework.generics import (CreateAPIView, UpdateAPIView,
                                     RetrieveAPIView, DestroyAPIView,
                                     ListAPIView)
from rest_framework.permissions import IsAuthenticated

from memes.models import Mem
from memes.permissions import IsModerator, IsOwner
from memes.serializers.mem import MemSerializer


class MemCreateView(CreateAPIView):
    queryset = Mem.objects.all()
    serializer_class = MemSerializer
    permission_classes = [IsAuthenticated]


class MemUpdateView(UpdateAPIView):
    queryset = Mem.objects.all()
    serializer_class = MemSerializer
    permission_classes = [IsAuthenticated, IsModerator | IsOwner]


class MemRetrieveView(RetrieveAPIView):
    serializer_class = MemSerializer
    permission_classes = [IsAuthenticated]

    def get_queryset(self):
        mem_id = self.kwargs['id']
        mem = Mem.objects.get(id=mem_id)
        queryset = []
        queryset.append(mem)
        return queryset


class MemDestroyView(DestroyAPIView):
    queryset = Mem.objects.all()
    serializer_class = MemSerializer
    permission_classes = [IsAuthenticated, IsOwner | IsModerator]


class MemListView(ListAPIView):
    queryset = Mem.objects.all()
    serializer_class = MemSerializer
    permission_classes = [IsAuthenticated]




