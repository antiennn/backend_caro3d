from rest_framework import viewsets, status
from rest_framework.decorators import action
from rest_framework.response import Response

from .models import Question,Question_grammar
from .serializers import QuestionSerializer


class QuestionViewSet(viewsets.ViewSet):
    queryset = Question_grammar.objects.all()

    @action(methods=["GET"],detail=False, url_path="question_grammar", url_name="question_grammar")
    def question_grammar(self, request):
        try:
            grammar = self.queryset
            return Response(QuestionSerializer(grammar,many=True).data,status=status.HTTP_200_OK)
        except Exception as e:
            return Response({"error": str(e)}, status=status.HTTP_400_BAD_REQUEST)



