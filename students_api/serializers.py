from rest_framework import serializers
from students.models import Student

class StudentSerializer(serializers.ModelSerializer):
    class Meta:
        model = Student
        # fields = ['student_id', 'name', 'branch'] # fields to be serialized
        fields = '__all__'
        # exclude = ['student_id'] # fields to be excluded from serialization
        # read_only_fields = ['student_id'] # fields to be read only
        # extra_kwargs = {'student_id': {'read_only': True}} # fields to be read only   
