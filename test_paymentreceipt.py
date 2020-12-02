from Project.profile import Profile
from Project.emailaddress import EmailAddress
from Project.emaildelivery import EmailDelivery

def test_add_valid_email_to_profile():
    profile = Profile()
    email = EmailAddress()

    assert len(email) == 0, "The profile has no email address"

    email = EmailAddress("ngangf@mcmaster.ca")
    profile.add_email(email)

    assert len(email) == 1, "An email address has been added to the profile"

def test_add_invalid_email():
    profile = Profile()
    email = EmailAddress()

    assert len(email) == 0, "The profile has no email address"

    email = EmailAddress("ngangf@mcmaster.ca")
    email.invalidate_email()
    profile.add_email(email)

    assert len(email) == 0, "An invalid email address should not be added to the profile"

def test_email_delivery():
    valid_notification = [
        "successful",
     ]

    emaildelivery = EmailDelivery()
    for notification in valid_notification:
        assert emaildelivery.verify_delivery(notification) == True, "Ensure email address is valid"

