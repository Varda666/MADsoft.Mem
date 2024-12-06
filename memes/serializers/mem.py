from rest_framework import serializers

from memes.models import Mem


class MemSerializer(serializers.ModelSerializer):

    def validate_name(self, data):
        if Mem.objects.filter(name=data).exists():
            raise serializers.ValidationError("Такое название уже существует.")
        return data

    def validate_text(self, data):
        list_of_forbidden_words = ['голова', 'нога', 'рука']
        for word in list_of_forbidden_words:
            if word in data:
                raise serializers.ValidationError(
                    f"Текст не может содержать слово {word}"
                )
        else:
            return data

    class Meta:
        model = Mem
        fields = "__all__"




