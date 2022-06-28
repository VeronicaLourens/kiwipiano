from django.test import TestCase, Client
from django.test import SimpleTestCase
from django.urls import reverse, resolve
from booking.views import home, sign_up, login
from booking.views import logout_view, admin_login, feedback, profile
from booking.views import booking_form, BookingDetailView
from booking.models import Booking, Profile
from booking.forms import BookingForm


class TestUrls(SimpleTestCase):
    """
    To test urls.
    """
    def test_home_url_is_resolves(self):
        """ To test the home url """
        url = reverse('home')
        response = self.client.get('')
        print(resolve(url))
        self.assertEquals(resolve(url).func, home)
        self.assertTemplateUsed(response, 'index.html')


    def test_sign_up_url_is_resolves(self):
        """ To test the signup url """
        url = reverse('signup')
        print(resolve(url))
        self.assertEquals(resolve(url).func, sign_up)


    def test_login_url_is_resolves(self):
        """ To test the login url """
        url = reverse('login')
        print(resolve(url))
        self.assertEquals(resolve(url).func, login)
       

    def test_logout_url_is_resolves(self):
        """ To test the logout url """
        url = reverse('logout')
        print(resolve(url))
        self.assertEquals(resolve(url).func, logout_view)


    def test_profile_url_is_resolves(self):
        """ To test the profile url """
        url = reverse('profile')
        print(resolve(url))
        self.assertEquals(resolve(url).func, profile)
       

    def test_booking_form_url_is_resolves(self):
        """ To test the booking form url """
        url = reverse('booking_form')
        print(resolve(url))
        self.assertEquals(resolve(url).func, booking_form)


class TestModels(TestCase):
    """
    To test the models.
    """
    def test_booking_model(self):
        """
        To test the booking model.
        """
        booking = Booking.objects.create(
            session_name='Beginner',
            date='2022-06-28',
            timeslot='09:00 - 10:00',
            message='Hello'
        )

        self.assertEquals(booking.session_name, 'Beginner')
        self.assertEquals(booking.date, '2022-06-28')
        self.assertEquals(booking.timeslot, '09:00 - 10:00')
        self.assertEquals(booking.message, 'Hello')



    def test_profile_model(self):
        """
        To test the profile model.
        """

        profile = Profile.objects.create(
            profile_image= 'default_bxixmd.jpg',
            phone_number='0222222222222222222',
            first_name_profile='Veronica',
            last_name_profile='Lourens',

        )

        self.assertEquals(profile.profile_image, 'default_bxixmd.jpg')
        self.assertEquals(profile.phone_number, '0222222222222222222')
        self.assertEquals(profile.first_name_profile, 'Veronica')
        self.assertEquals(profile.last_name_profile, 'Lourens')
      



