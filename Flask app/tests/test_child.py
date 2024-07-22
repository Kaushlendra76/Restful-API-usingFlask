import unittest
from app import app, db
from app.models import Parent, Child

class ChildTestCase(unittest.TestCase):

    def setUp(self):
        app.config['TESTING'] = True
        app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///test.db'
        self.app = app.test_client()
        db.create_all()
        parent = Parent(name='John Doe', email='john@example.com', parent_type='first-time')
        db.session.add(parent)
        db.session.commit()

    def tearDown(self):
        db.session.remove()
        db.drop_all()

    def test_create_child(self):
        response = self.app.post('/children', json={
            'parent_id': 1,
            'name': 'Jane Doe',
            'age': 5,
            'gender': 'female'
        })
        self.assertEqual(response.status_code, 201)

if __name__ == '__main__':
    unittest.main()