import pytest
from blogDjango.factories import PostFactory


@pytest.fixture
def post_published():
    return PostFactory(title='Olá Django com Fabrica')


@pytest.mark.django_db
def test_create_published_post(post_published):
    assert post_published.title == 'Olá Django com Fabrica'


