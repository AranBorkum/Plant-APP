from dataclasses import dataclass, field

from rest_framework import status
from rest_framework.response import Response


@dataclass
class ServiceAPIDataclass:
    status: int | None
    data: dict | None = field(default_factory=dict)
    cookie: str | None = None
    cookie_name: str | None = None

    def generate_response(self) -> Response:
        response: Response = Response(data=self.data, status=self.status)
        if self.cookie and self.cookie_name:
            response.set_cookie(self.cookie_name, self.cookie)
        return response

    @classmethod
    def default_404(cls) -> Response:
        return Response(status=status.HTTP_404_NOT_FOUND)
