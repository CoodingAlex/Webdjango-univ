import datetime
from django.test import TestCase
from django.urls.base import reverse
from django.utils import timezone

from .models import Question

# vas a testear modelos y vistas
class QuestionModelTEst(TestCase):
    
    def test_was_published_recently_with_future_questions(self):
        """was_published_recently returns False for quesitons whose pub_date is in the future"""
        time = timezone.now() + datetime.timedelta(days=30)
        future_question = Question(question_text="Quien es el mejor Director de Platzi", pub_date=time)
        self.assertIs(future_question.was_published_recently(), False)

def create_question(question_text, days):
    """
    Create a question with the given "question_text", and published the given number
    of days offset to now (negative for questios published in the past,
    positive for questions thaat have yet to be published)
    """
    time = timezone.now() + datetime.timedelta(days=days)
    return Question.objects.create(question_text=question_text, pub_date=time)

        
class QuestionIndexViewTest(TestCase):
    def test_no_questions(self):
        """If no question exist, an appropiate message is displayed"""
        response = self.client.get(reverse("polls:index"))
        self.assertEqual(response.status_code, 200)
        self.assertContains(response, "No polls are available.")
        self.assertQuerysetEqual(response.context["latest_question_list"], [])

    def test_future_question(self):
        """
        Questions with a pub_date in the future aren't displayed on the index page.
        """
        create_question("Future question", days=30)
        response = self.client.get(reverse("polls:index"))
        self.assertContains(response, "No polls are available.")
        self.assertQuerysetEqual(response.context["latest_question_list"], [])  