from rest_framework import serializers

from materials.models import Course, Lesson


class CourseSerializer(serializers.ModelSerializer):
    class Meta:
        model = Course
        fields = "__all__"


class CourseDetailSerializer(serializers.ModelSerializer):
    count_lesson = serializers.SerializerMethodField()

    class Meta:
        model = Course
        fields = (
            "title",
            "count_lesson",
        )

    def get_count_lesson(self, obj):
        return obj.lesson_set.count()


class LessonSerializer(serializers.ModelSerializer):
    class Meta:
        model = Lesson
        fields = (
            "title",
            "course",
        )
