from django.test import LiveServerTestCase
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from webdriver_manager.chrome import ChromeDriverManager


class AccountTestCase(LiveServerTestCase):
    def setUp(self):
        self.driver = webdriver.Chrome(ChromeDriverManager().install())
        base_url = 'http://127.0.0.1:8000/'
        self.home_url = '{}{}'.format(base_url, '')
        self.signup_url = '{}{}'.format(base_url, 'accounts/signup')
        self.login_url = '{}{}'.format(base_url, 'accounts/login')
        self.meet_leadership = '{}{}'.format(base_url, 'employment-attorneys-jesse-unruh.html')
        self.contact_jet = '{}{}'.format(base_url, 'jet-contact.html')
        self.flas_claim = '{}{}'.format(base_url, 'flsa-claims-attorney-florida.html')
        self.disability_lawyer = '{}{}'.format(base_url, 'disability-lawyer-florida.html')
        self.medical_leave = '{}{}'.format(base_url, 'medical-leave-fmla-lawyer-florida.html')
        self.harasment = '{}{}'.format(base_url, 'discrimination-attorney-florida.html')
        self.defense = '{}{}'.format(base_url, 'flsa-employment-attorney-florida.html')
        self.fixed_services = '{}{}'.format(base_url, 'fixed-fee-employment-contracts.html')
        self.how_we = '{}{}'.format(base_url, 'fixed-fee-litigation-defense.html')
        self.blogs = '{}{}'.format(base_url, 'blogs')

        super(AccountTestCase, self).setUp()

    def tearDown(self):
        self.driver.quit()
        super(AccountTestCase, self).tearDown()

    def test_signup_page_and_title(self):
        self.driver.get(self.signup_url)
        assert 'Sign Up' in self.driver.title

    def test_login_page_and_title(self):
        self.driver.get(self.login_url)
        assert 'Login' in self.driver.title

    def test_home_page_and_title(self):
        self.driver.get(self.home_url)
        assert 'jet.law | (407) 494-0135 - Data-driven employer attorneys' in self.driver.title

    def test_leadership_page_and_title(self):
        self.driver.get(self.meet_leadership)
        assert 'Jesse I Unruh Attorney in Florida - jet.law | (407) 494-0135' in self.driver.title

    def test_contact_page_and_title(self):
        self.driver.get(self.contact_jet)
        assert 'Contact jet.law - jet.law | (407) 494-0135' in self.driver.title

    def test_claim_page_and_title(self):
        self.driver.get(self.flas_claim)
        assert 'Fight FLSA Claims in Florida - jet.law | (407) 494-0135' in self.driver.title

    def test_disability_lawyer_page_and_title(self):
        self.driver.get(self.disability_lawyer)
        assert 'Disability Lawyer in Florida - jet.law | (407) 494-0135' in self.driver.title

    def test_medical_leave_lawyer_page_and_title(self):
        self.driver.get(self.medical_leave)
        assert 'Medical Leave Lawyer in Florida - jet.law | (407) 494-0135' in self.driver.title

    def test_harasment_lawyer_page_and_title(self):
        self.driver.get(self.harasment)
        assert 'Discrimination Attorney in Florida - jet.law | (407) 494-0135' in self.driver.title

    def test_defense_lawyer_page_and_title(self):
        self.driver.get(self.defense)
        assert 'Fixed Price Employment Attorney in Florida - jet.law | (407) 494-0135' in self.driver.title

    def test_fixed_service_lawyer_page_and_title(self):
        self.driver.get(self.fixed_services)
        assert 'Employment Services' in self.driver.title

    def test_how_we_lawyer_page_and_title(self):
        self.driver.get(self.how_we)
        assert 'How jet.law offers fixed fee litigation defense - jet.law | (407) 494-0135' in self.driver.title

    def test_blogs_lawyer_page_and_title(self):
        self.driver.get(self.blogs)
        assert 'jet.law-blogs' in self.driver.title

    def test_all_pages_and_titles_in_system(self):
        selenium = self.driver
        # Opening the link we want to test




        # selenium.get(login_url)
        # assert 'Sign Up' in selenium.title
        #
        # selenium.get(meet_leadership)
        # selenium.get(contact_jet)
        # selenium.get(flas_claim)
        # selenium.get(disability_lawyer)
        # selenium.get(medical_leave)
        # selenium.get(harasment)
        # selenium.get(defense)
        # selenium.get(fixed_services)
        # selenium.get(how_we)
        # selenium.get(blogs)



        # find the form element
        # first_name = selenium.find_element_by_id('id_first_name')
        # last_name = selenium.find_element_by_id('id_last_name')
        #
        #
        #
        #
        #
        #
        # email = selenium.find_element_by_id('id_email')
        # phone = selenium.find_element_by_id('id_phone')
        # position = selenium.find_element_by_id('id_position_company')
        # company_name = selenium.find_element_by_id('id_company_name')
        # password1 = selenium.find_element_by_id('id_password1')
        # password2 = selenium.find_element_by_id('id_password2')
        #
        #
        #
        # #Fill the form with data
        # first_name.send_keys('Yusuf')
        # last_name.send_keys('Unary')
        # email.send_keys('test1@qawba.com')
        # phone.send_keys('11111111111')
        # position.send_keys('Test')
        # company_name.send_keys('Test123')
        # password1.send_keys('123456')
        # password2.send_keys('123456')
        #
        # #submitting the form
        # selenium.find_elements_by_class_name('btn-success')[0].click()
        # selenium.implicitly_wait(6)

        # check the returned result
        # assert 'Check your email' in selenium.page_source

    def test_login(self):
        email = 'admin@gmail.com'
        password = 'admin'

        self.driver.get(self.login_url)

        email_element = self.driver.find_element_by_name('username')
        password_element = self.driver.find_element_by_name('password')

        email_element.send_keys(email)
        password_element.send_keys(password)

        self.driver.find_elements_by_class_name('btn-success')[0].click()

        self.driver.implicitly_wait(8)

        assert 'Dashboard' in self.driver.title

    def test_contact_us(self):
        self.driver.get(self.contact_jet)

        first_name = self.driver.find_element_by_name('firstName')
        last_name = self.driver.find_element_by_name('lastName')
        email = self.driver.find_element_by_name('email')
        company = self.driver.find_element_by_name('company')
        phone_number = self.driver.find_element_by_name('phone')
        case_name = self.driver.find_element_by_name('case')

        first_name.send_keys('test_name')
        last_name.send_keys('test_last_name')
        email.send_keys('test@g.com')
        company.send_keys('company_test')
        phone_number.send_keys('12345678901')
        case_name.send_keys('test case name')

        self.driver.find_element_by_name('submit').click()

        self.driver.implicitly_wait(8)

    def test_subscribe_email(self):
        self.driver.get(self.home_url)

        email = self.driver.find_element_by_id('email_sub')
        email.send_keys('test@g.com')
        self.driver.find_element_by_id('email_sub_button').click()

        self.driver.implicitly_wait(8)
