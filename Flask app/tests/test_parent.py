import unittest
from app import app, db
from app.models import Parent

class ParentTestCase(unittest.TestCase):

    def setUp(self):
        app.config['TESTING'] = True
        app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///test.db'
        self.app = app.test_client()
        db.create_all()

    def tearDown(self):
        db.session.remove()
        db.drop_all()

    def test_create_parent(self):
        response = self.app.post('/parents', json={
            'name': 'John Doe',
            'email': 'john@example.com',
            'parent_type': 'first-time'
        })
        self.assertEqual(response.status_code, 201)

if __name__ == '__main__':
    unittest.main()