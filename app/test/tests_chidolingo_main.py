import unittest
import assertion_plugin
from classesfortests import validate_email, EmailSyntaxError, DateTimeField, Future_Date_Time, Name_Validation
from wtforms import ValidationError



"""Email accounts are critical to our product for both signing up on the promotion and creating an account"""
"""After testing for all the cases, we refactored some of the legacy code to validate emails for our business purpose"""


class MyTestCase(unittest.TestCase, assertion_plugin.Exceptions):
    """Test to make sure users are not able to sign up without an email or with a blank email"""
    def test_blank_email(self):
        test_email = ''
        with self.assertRaises(EmailSyntaxError):
            validate_email(self,test_email)

    """Test to make sure a regular email is allowed valid"""
    def test_valid_email(self):
        test_email = 'test@chidolingo.com'
        with self.assertNothingRaised():
            validate_email(self,test_email)

    """Test whether emails can contain spaces. Our assumption was that it should raise an error."""
    def test_email_with_space(self):
        test_email = 'test @chidolingo.com'
        with self.assertRaises(EmailSyntaxError):
            validate_email(self,test_email)

    """Test to make sure email must contain at least one @ symbol but no more than one"""
    def test_email_without_at_symbol(self):
        test_email = 'testchidolingo.com'
        with self.assertRaises(EmailSyntaxError):
            validate_email(self,test_email)

    """Test to make sure emails cannot contain foreign or non-ASCII characters. Customers must have regular email"""
    def test_email_with_non_ascii_characters(self):
        test_email = 'test汉字@chidolingo.com'
        with self.assertRaises(EmailSyntaxError):
            validate_email(self,test_email)

    def test_email_more_than_one_at_symbol(self):
        test_email = 'test@@chidolingo.com'
        with self.assertRaises(EmailSyntaxError):
            validate_email(self,test_email)

 
    """Test whether emails can contain space as long as they are in quotes."""
    def test_email_with_quoted_space(self):
        test_email = '"test c"@chidolingo.com'
        with self.assertRaises(EmailSyntaxError):
            validate_email(self,test_email)

    """Test to make sure that emails without a local part or a user name are not allowed"""
    def test_email_for_without_username(self):
        test_email = '@chidolingo.com'
        with self.assertRaises(EmailSyntaxError):
            validate_email(self,test_email)

    """Test to make sure that emails without a valid domain (either domain name or top level domain) are not allowed"""
    def test_email_for_without_domain_name(self):
        test_email = 'test@.com'
        with self.assertRaises(EmailSyntaxError):
            validate_email(self,test_email)

    def test_email_for_without_top_level_domain(self):
        test_email = 'test@chidolingo.'
        with self.assertRaises(EmailSyntaxError):
            validate_email(self,test_email)

    """Test to make sure that the minimum length of top level domain for the email must be more than 1 char"""
    def test_email_for_minimum_top_level_domain_characters(self):
        test_email = 'test@chidolingo.c'
        with self.assertRaises(EmailSyntaxError):
            validate_email(self,test_email)

    """Test for the shortest possible email allowed i.e.has at least 1 char long username & 2 char long domain parts """
    def test_shortest_possible_email(self):
        test_email = 't@co.co'
        with self.assertNothingRaised():
            validate_email(self,test_email)

    """Test to make sure top level domain name emails are allowed due to variety of customers on Chidolingo"""
    def test_long_top_level_domain_email(self):
        test_email = 'test@chidolingo.international'
        with self.assertNothingRaised():
            validate_email(self,test_email)

    """Test assertion about longest domain name allowed. Error must be raised for domain names greater than 64 chars"""
    def test_longest_allowed_domain_name(self):
        test_email = 'test@chidiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiolingo.international'
        with self.assertRaises(EmailSyntaxError):
            validate_email(self,test_email)

    """Test assertion that any poorly terminated emails i.e. one with special characters are not validated"""
    def test_email_terminated_with_special_character(self):
        test_email = 'test@chidolingo.com#'
        with self.assertRaises(EmailSyntaxError):
            validate_email(self,test_email)

    """Test to make sure that emails containing special characters besides the ones allowed (.,_-@) are not validated"""
    def test_email_containing_special_character(self):
        test_email = 'test@chid#lingo.com'
        with self.assertRaises(EmailSyntaxError):
            validate_email(self,test_email)

    """Test assertion hyphenated and double hyphenated usernames are allowed """
    def test_hyphenated_emails(self):
        test_email = 'test-1@chidolingo.com'
        with self.assertNothingRaised():
            validate_email(self,test_email)

        test_email = 'test--1@chidolingo.com'
        with self.assertNothingRaised():
            validate_email(self,test_email)

    """Test for emails with underscored usernames are allowed but no underscored domains are"""
    def test_underscored_email(self):
        test_email = 'test_1@chidolingo.com'
        with self.assertNothingRaised():
            validate_email(self,test_email)

    def test_underscored_email(self):
        test_email = 'test_1@chid_olingo.com'
        with self.assertRaises(EmailSyntaxError):
            validate_email(self,test_email)

    def test_blankdate(self):
        test_datetime = ''
        with self.assertRaises(ValueError):
            DateTimeField.validate_datetime(test_datetime)

    def test_date_time_with_hour_minutes(self):
        test_datetime = '2018-02-21 12:00'
        with self.assertRaises(ValueError):
            DateTimeField.validate_datetime(test_datetime)

    def test_date_without_time(self):
        test_datetime = '2018-02-21'
        with self.assertRaises(ValueError):
            DateTimeField.validate_datetime(test_datetime)

    def test_date_with_seconds(self):
        test_datetime = '2018-02-21 12:00:00'
        with self.assertNothingRaised():
            DateTimeField.validate_datetime(test_datetime)

    def test_date_with_slashes_on_dates(self):
        test_datetime = '2018/02/21 12:00:00'
        with self.assertRaises(ValueError):
            DateTimeField.validate_datetime(test_datetime)

    def test_date_with_am_pm(self):
        test_datetime = '2018-02-21 12:00:00 AM'
        with self.assertRaises(ValueError):
            DateTimeField.validate_datetime(test_datetime)

    def test_date_with_alpha_characters(self):
        test_datetime = '2018/02/21 Twelve:00:00'
        with self.assertRaises(ValueError):
            DateTimeField.validate_datetime(test_datetime)

    def test_date_with_reverse_time_date(self):
        test_datetime = '12:00:00 2018-02-21'
        with self.assertRaises(ValueError):
            DateTimeField.validate_datetime(test_datetime)

    def test_date_time_after_today(self):
        test_datetime = '2023-02-21 12:00:00'
        with self.assertNothingRaised():
            Future_Date_Time.validate_futuredate(test_datetime)
    def test_date_time_before_today(self):
        test_datetime = '2022-02-21 12:00:00'
        with self.assertRaises(ValidationError):
            Future_Date_Time.validate_futuredate(test_datetime)

    def test_name_with_alphabets_only(self):
        test_name = 'Christina'
        with self.assertNothingRaised():
            Name_Validation.validate_name(test_name)

    def test_name_with_alphabets_characters(self):
        test_name = 'Christin@'
        with self.assertRaises(ValueError):
            Name_Validation.validate_name(test_name)

    def test_name_with_alphabets_dashes(self):
        test_name = 'Lopez-Islam'
        with self.assertNothingRaised():
            Name_Validation.validate_name(test_name)

    def test_name_with_foreign_characters(self):
        test_name = 'کرستینه'
        with self.assertRaises(ValueError):
            Name_Validation.validate_name(test_name)


if __name__ == '__main__':
    unittest.main()