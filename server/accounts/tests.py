from django.test import TestCase,Client
from selenium import webdriver
from selenium.webdriver import FirefoxOptions
from selenium.webdriver.common.by import By
from requests import Session
from selenium.webdriver.common.action_chains import ActionChains
from .forms import UserForm
from .models import AccountUser
from django.contrib.auth.models import User

import time

# Create your tests here.
class FunctionalTestCase(TestCase):
    def setUp(self):
        opts = FirefoxOptions()
        opts.add_argument("--headless")
        self.browser = webdriver.Firefox(options=opts)

    def test_there_is_homepage(self):
        self.browser.get('http://127.0.0.1:8000')
        self.assertIn('test', self.browser.page_source)
    def test_login_function(self):
        self.browser.get('http://127.0.0.1:8000/accounts/login/')
        username = self.browser.find_element(By.NAME,'login')
        #time.sleep(2)
        username.send_keys('rakuten-panda')
        password = self.browser.find_element(By.NAME,'password')
        #time.sleep(2)
        username.send_keys('lovepy123')
        double_click = self.browser.find_element(By.XPATH, '//button[text()="ログイン"]')
        ActionChains(self.browser).double_click(double_click).perform()
        username.submit()
        password.submit()
        #print(submit)
        #submit.click()
        #self.browser.implicitly_wait(3)
        #self.browser.switch_to.window(self.browser.window_handles[-1])
        self.browser.refresh()
        print(self.browser.current_url)
        #self.browser.get('http://127.0.0.1:8000/')
        print(self.browser.current_url)
        #print(self.browser.page_source)

        if 'ログアウト' in self.browser.page_source:
            print("successfully login!")
    def tearDown(self):
        self.browser.quit()

    '''
    session  = None
    @classmethod
    def setUpClass(cls):
        print("setUpClass")
        # construct account
        info  = {
            'username': 'rakuten-panda',
            'password': 'lovepy123',
        }
        # initialize the session
        cls.session = Session()
        # login
        resp = cls.session.post(
            'http://127.0.0.1:8000/login/',
            json=info
        )
        # get response json
        result = resp.json()
        # whether successfully login
    '''

class UnitTestCase(TestCase):
    def test_login(self):
        response = self.client.get('/accounts/login/')
        self.assertTemplateUsed(response, 'accounts/login.html')

        print("There is login page!")
    def test_user_from(self):
        User.objects.create_user(username='rakuten-panda',email=None, password='lovepy123')
        user = User.objects.get(id=1)
        AccountUser.objects.create(
            user_name= user,
            profile= 'my name is rakuten panda',
            sound_profile='sounds/1.mp3',
            user_icon='icons/1.png',
            birthday= '1998-09-10'

        )
        accountUser = AccountUser.objects.get(id=1)
        print(accountUser.profile)

        #print(user)

        form = UserForm( instance=accountUser)


        print(form.is_valid())
        self.assertTrue(form.is_valid())
        #form.save()
        print("UserForm is well done!")






