from abc import ABC, abstractmethod
from fastapi import Request


class Auth(ABC):

    @property
    def auth(self):
        pass

    @auth.setter
    def auth(self, value):
        self._auth = value

    @auth.getter
    def auth(self):
        return self._auth

    @abstractmethod
    async def authorize_redirect(self, request: Request, redirect_url: str):
        pass

    @abstractmethod
    async def get_google_user_profile(self, profile_info_url: str, token: str):
        pass

    @abstractmethod
    async def create_user(self, first_name, last_name, email):
        pass
