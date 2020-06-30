from django.test import TestCase
from ..models import Author, Article
from django_contacts.article.models import Author, Article


class AuthorTest(TestCase):

    def setUp(self):
        Author.objects.create(name="Samuel Harrison", email="sam@ok.com")
        Author.objects.create(name="Annabel Wasserman", email="bel@bus-em.com")

    def test_saved_authors(self):
        authors = Author.objects.count()
        self.assertEqual(authors, 2)


class ArticleTest(TestCase):

    def setUp(self):
        Article.objects.create(
            title="Tea is dangerous", description="Tea research",
            body="New results for white tea ...",
            category=3,
            author_id=1
        )
        Article.objects.create(
            title="Monkeys may share a key grammar-related skill with humans",
            description="A capacity for recursion evolved early in primate evolution, a contested study suggests",
            category=3,
            body="An aptitude for mentally stringing together related items, "
                 "often cited as a hallmark of human language, "
                 "may have deep roots in primate evolution, a new study suggests.",
            author_id=1
        )
        self.author = Author.objects.get(id=1)

    def test_saved_articles(self):
        articles = Article.objects.count()
        self.assertEqual(articles, 2)
