import pytest
from django.core.management import call_command
from polls.models import Question


@pytest.fixture(scope='session')
def django_db_setup(django_db_setup, django_db_blocker):
    with django_db_blocker.unblock():
        call_command('loaddata', 'initial_data.json')


@pytest.mark.django_db
def test_my_question():
    print(Question.objects.all())
    q1 = Question.objects.get(id=1)
    assert q1.question_text == 'Question One'
