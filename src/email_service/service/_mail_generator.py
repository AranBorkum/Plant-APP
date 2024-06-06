from sendgrid.helpers.mail import Mail

from email_service.interfaces import IMailGenerator


class MailGenerator(IMailGenerator):
    def build(self) -> Mail:
        return Mail(
            from_email=self._email_information.value.sender,
            to_emails=self._recipient,
            subject=self._email_information.value.subject,
            html_content=self._read_template(),
        )

    def _read_template(self) -> str:
        with open(self._email_information.value.template, "r") as template:
            return template.read()
