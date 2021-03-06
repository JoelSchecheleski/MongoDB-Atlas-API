from enum import Enum
import os
from .errors import AtlasEnvironmentError

class AtlasEnv(Enum):

    ATLAS_PUBLIC_KEY  = "ATLAS_PUBLIC_KEY"
    ATLAS_PRIVATE_KEY = "ATLAS_PRIVATE_KEY"


    def __str__(self):
        return self.value





class AtlasKey:

    def __init__(self, public_key, private_key):

        self._public_key = public_key
        self._private_key = private_key


    @staticmethod
    def getenv(key_string):
        key = os.getenv(key_string)
        if key is None:
            raise AtlasEnvironmentError(f"Private key environment variable '{key_string}' is not set")
        return key

    @classmethod
    def get_from_env(cls):
        public_key = AtlasKey.getenv(AtlasEnv.ATLAS_PUBLIC_KEY.value)
        private_key = AtlasKey.getenv(AtlasEnv.ATLAS_PRIVATE_KEY.value)
        return AtlasKey(public_key, private_key)

    @property
    def private_key(self):
        return self._private_key

    @property
    def public_key(self):
        return self._public_key

    @staticmethod
    def obfuscate(s,show=4,hide_char="x"):
        l = len(s)
        if show > l:
            return s
        else:
            return (hide_char * (l-show)) + s[:show]

    def __repr__(self):
        return (f"AtlasKey(public_key='{AtlasKey.obfuscate(self._public_key)}', " +
               f"private_key='{AtlasKey.obfuscate(self._private_key)}')")

