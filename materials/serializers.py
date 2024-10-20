from rest_framework.serializers import ModelSerializer

from materials.models import Course, Lesson


class CourseSerializer(ModelSerializer):
    class Meta:
        model = Course
        fields = ("title",)


class LessonSerializer(ModelSerializer):
    class Meta:
        model = Lesson
        fields = (
            "title",
            "course",
        )
