# quizzes/serializers.py
from rest_framework import serializers
from .models import Quiz, Question, Choice

class QuizSerializer(serializers.ModelSerializer):
    """🔄 Converts Quiz model to/from JSON"""
    class Meta:
        model = Quiz
        fields = ['id', 'title', 'description', 'created_at', 'updated_at']
        read_only_fields = ['created_at', 'updated_at']  # 🔒 Auto-generated fields
        
class ChoiceSerializer(serializers.ModelSerializer):
    """📝 Serializer for answer choices"""
    class Meta:
        model = Choice
        fields = ['id', 'text', 'is_correct']

class QuestionDetailSerializer(serializers.ModelSerializer):
    """❓ Question with all its choices"""
    choices = ChoiceSerializer(many=True, read_only=True)
    
    class Meta:
        model = Question
        fields = ['id', 'text', 'choices']

class QuizDetailSerializer(serializers.ModelSerializer):
    """🎯 Complete quiz with questions and choices"""
    questions = QuestionDetailSerializer(many=True, read_only=True)
    questions_count = serializers.SerializerMethodField()  # 📊 Extra info
    
    class Meta:
        model = Quiz
        fields = ['id', 'title', 'description', 'created_at', 'questions', 'questions_count']
    
    def get_questions_count(self, obj):
        return obj.questions.count()

class AnswerSerializer(serializers.Serializer):
    """✅ For validating submitted answers"""
    question_id = serializers.IntegerField()
    choice_id = serializers.IntegerField()