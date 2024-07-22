import unittest
from app import app, db
from app.models import Blog

class BlogTestCase(unittest.TestCase):

    def setUp(self):
        app.config['TESTING'] = True
        app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///test.db'
        self.app = app.test_client()
        db.create_all()

    def tearDown(self):
        db.session.remove()
        db.drop_all()

    def test_create_blog(self):
        response = self.app.post('/blogs', json={
            'title': 'Parenting Tips',
            'content': 'Some useful content here.',
            'age_group': '0-2',
            'gender': 'all',
            'vlog_url': 'http://kasuhlendra.com/vlog'
        })
        self.assertEqual(response.status_code, 201)

if __name__ == '__main__':
    unittest.main()