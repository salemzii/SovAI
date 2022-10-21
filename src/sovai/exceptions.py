from cgitb import html
import http

from aiohttp import HttpVersion


class Exceptions(Exception):

    ErrUnAuthorized = http.HTTPStatus.FORBIDDEN
    ErrApiVersionNotFound = http.HTTPStatus.HTTP_VERSION_NOT_SUPPORTED
    ErrCommandNotFound = "command not found"
    ErrSubCommandNotFound = "Subcommand not found"

    def __init__(self, *args: object) -> None:
        super().__init__(*args)
