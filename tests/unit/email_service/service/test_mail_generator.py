from pytest import raises

from email_service.enums import Email
from email_service.service import MailGenerator


class TestCaseMailGenerator:
    def test_case_initialise_mail_generator_with_no_recipient(self) -> None:
        with raises(AssertionError):
            MailGenerator(Email.CONFIRM_SIGN_UP, "")

    def test_case_initialise_mail_generator_with_invalid_email(self) -> None:
        with raises(AssertionError):
            MailGenerator(Email.CONFIRM_SIGN_UP, "hello")

    def test_case_initialise_mail_generator_with_valid_email(self) -> None:
        MailGenerator(Email.CONFIRM_SIGN_UP, "test@mail.com")
        MailGenerator(Email.CONFIRM_SIGN_UP, "test.test@mail.com")
        MailGenerator(Email.CONFIRM_SIGN_UP, "test-test@mail.com")
        MailGenerator(Email.CONFIRM_SIGN_UP, "test_test@mail.com")
        MailGenerator(Email.CONFIRM_SIGN_UP, "test@mail.co.uk")
        MailGenerator(Email.CONFIRM_SIGN_UP, "test.test@mail.co.uk")
        MailGenerator(Email.CONFIRM_SIGN_UP, "test-test@mail.co.uk")
        MailGenerator(Email.CONFIRM_SIGN_UP, "test_test@mail.co.uk")

    def test_read_template(self) -> None:
        MailGenerator(Email.CONFIRM_SIGN_UP, "test@test.com")._read_template()
