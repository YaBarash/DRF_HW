from rest_framework.viewsets import ModelViewSet

from materials.models import Course


class CourseViewSet(ModelViewSet):
    def list(self, request):
        queryset = Course.objects.all()
        serializer_class = CourseSerializer
