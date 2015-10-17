#!flask/bin/python
import os
import unittest
from flask import (
    Blueprint,
    request,
    render_template,
    flash,
    g,
    session,
    redirect,
    url_for
)
from app import app, db
from app.article.models import Article

BASE_DIR = os.path.abspath(os.path.dirname(__file__))

class articlemodelcase(unittest.TestCase):
    def setUp(self):
        app.config['TESTING'] = True
        app.config['WTF_CSRF_ENABLED'] = False
        app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///' + os.path.join(BASE_DIR, 'test.db')
        self.app = app.test_client()
        db.create_all()
        ctx = app.app_context()
        ctx.push()
        return app


    def tearDown(self):
        db.session.remove()
        db.drop_all()


    def testarticlemodelpost(self):
        user = User(username='testuser',
        email='test@example.com',
        password='test',
        role=1,
        status=1
        )   
        db.session.add(user)
        db.session.commit()
        usertest = User.query.filter(User.username == 'Testuser').first()
        testarticle = Article(title='testtitle',
                        	body='testbody',
                        	created='01-01-2015',
                        	section_name='testname',
                        	section='testsection',
                        	user_name=usertest.username,
                        	user=usertest,
                        	)
        db.session.add(section_todelete)
        db.session.commit()
        self.assertTrue(testarticle.all()!= None)
        self.assertTrue(testarticle.find_by_id()!= None)
        self.assertTrue(testarticle.find_by_author(usertest.username)!= None)
        self.assertTrue(testarticle.find_by_section('testsection')!= None)
        self.assertTrue(testarticle.slug()!= None)
        self.assertTrue(testarticle.create_in_words()!= None)

if __name__ == '__main__':
    unittest.main()
