from django.test import TestCase
# from ..models import Author, Article
from django_contacts.api.models import Group, Article


class AuthorTest(TestCase):

    def setUp(self):
        Group.objects.create(name="Samuel Harrison", email="sam@ok.com")
        Group.objects.create(name="Annabel Wasserman", email="bel@em.com")

    def test_saved_authors(self):
        authors = Group.objects.count()
        self.assertEqual(authors, 2)


class ArticleTest(TestCase):

    def setUp(self):
        Article.objects.create(
            title="Monkeys may share a key grammar-related skill with humans",
            description="A capacity for recursion evolved early in primate evolution, a contested study suggests",
            category=3,
            body="An aptitude for mentally stringing together related items, "
                 "often cited as a hallmark of human language, "
                 "may have deep roots in primate evolution, a new study suggests.",
            author_id=1
        )
        self.author = Group.objects.get(id=1)

    def test_saved_articles(self):
        articles = Article.objects.count()
        self.assertEqual(articles, 1)
