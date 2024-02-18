import pytest
from blogDjango.factories import PostFactory


@pytest.fixture
def post_published():
    return PostFactory(title='Olá Django com Fabrica', content='Conteúdo do post')

@pytest.mark.django_db
def test_create_published_post(post_published):
    assert post_published.title == 'Olá Django com Fabrica'
    assert post_published.content == 'Conteúdo do post'


@pytest.fixture
def post_published2():
    return PostFactory(title='Fabrica de chocolate', content='Conteúdo do chocolate', slug='lesma')

@pytest.mark.django_db
def test_create_published_post(post_published2):
    assert post_published2.title == 'Fabrica de chocolate'
    assert post_published2.content == 'Conteúdo do chocolate'
    assert post_published2.slug == 'lesma'


