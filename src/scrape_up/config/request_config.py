from typing import Dict, Union
import requests


class RequestConfig:
    """
    A class used to configure requests.

    Args
    ----
    timeout: int
        The timeout in seconds.
    redirect: bool
        Whether to follow redirects.
    """

    def __init__(
        self,
        timeout: Union[int, None] = None,
        redirect: bool = False,
        headers: Dict[str, str] = {},
        proxies: Dict[str, str] = {},
    ):
        self._timeout = timeout
        self._redirect = redirect
        self._headers = headers
        self._proxies = proxies

    def set_timeout(self, timeout: int):
        self._timeout = timeout

    def set_redirect(self, redirect: bool):
        self._redirect = redirect

    def set_headers(self, headers: Dict[str, str]):
        self._headers = headers

    def set_proxies(self, proxies: Dict[str, str]):
        self._proxies = proxies

    @property
    def timeout(self):
        return self._timeout

    @property
    def redirect(self):
        return self._redirect

    @property
    def headers(self):
        return self._headers

    @property
    def proxies(self):
        return self._proxies


def get(url: str, config: RequestConfig):
    r = requests.get(
        url=url,
        headers=config.headers,
        timeout=config.timeout,
        allow_redirects=config.redirect,
        proxies=config.proxies,
    )
    return r
