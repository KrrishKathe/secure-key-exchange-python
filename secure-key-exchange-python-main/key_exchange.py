from cryptography.hazmat.primitives.asymmetric import dh
from cryptography.hazmat.primitives import serialization
from cryptography.hazmat.primitives.kdf.hkdf import HKDF
from cryptography.hazmat.primitives import hashes


class KeyExchange:

    def __init__(self):
        # Generate Diffie-Hellman parameters
        self.parameters = dh.generate_parameters(
            generator=2,
            key_size=2048
        )

    def generate_key_pair(self):
        """
        Generates a private key and corresponding public key.
        """
        private_key = self.parameters.generate_private_key()
        public_key = private_key.public_key()

        return private_key, public_key

    def derive_shared_key(self, private_key, peer_public_key):
        """
        Derives a shared secret using Diffie-Hellman
        and converts it into a secure session key using HKDF.
        """

        shared_secret = private_key.exchange(peer_public_key)

        # Derive a 256-bit session key
        session_key = HKDF(
            algorithm=hashes.SHA256(),
            length=32,
            salt=None,
            info=b"secure-key-exchange"
        ).derive(shared_secret)

        return session_key

    @staticmethod
    def public_key_to_string(public_key):
        """
        Converts public key into a printable format.
        """

        public_bytes = public_key.public_bytes(
            encoding=serialization.Encoding.PEM,
            format=serialization.PublicFormat.SubjectPublicKeyInfo
        )

        return public_bytes.decode()