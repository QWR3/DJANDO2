from rest_framework import serializers as s, status

from computers.models import ComputerModel


class ComputerSerializer(s.ModelSerializer):
    class Meta:
        model = ComputerModel
        fields = "__all__"

    def validate(self, data: dict):
        cpu: str = data.get("CPU")
        if cpu.lower() in ["i8", "i6", "i4", "i2", "i1"]:
            raise s.ValidationError("CPU " + cpu + ", Sure? Are you out of your mind???")
        return data

    def validate_memory(self, memory):
        print(memory)
        if memory / 2:
            print(memory / 2)
            raise s.ValidationError(f"{memory} GB. of memory, sure?")
        return memory
