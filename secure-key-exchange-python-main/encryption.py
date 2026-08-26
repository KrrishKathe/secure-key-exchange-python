from cryptography.hazmat.primitives.ciphers.aead import AESGCM
import os
import base64


class SecureMessenger:

    def __init__(self, session_key):
        self.session_key = session_key
        self.aes = AESGCM(session_key)

    def encrypt_message(self, message):
        """
        Encrypt message using AES-256-GCM.
        """

        # Generate unique nonce
        nonce = os.urandom(12)

        # Convert message to bytes
        message_bytes = message.encode("utf-8")

        # Encrypt message
        ciphertext = self.aes.encrypt(
            nonce,
            message_bytes,
            None
        )

        # Combine nonce and ciphertext
        encrypted_data = nonce + ciphertext

        # Encode for transmission/display
        return base64.b64encode(
            encrypted_data
        ).decode("utf-8")

    def decrypt_message(self, encrypted_message):
        """
        Decrypt and verify message using AES-256-GCM.
        """

        encrypted_data = base64.b64decode(
            encrypted_message
        )

        # Extract nonce
        nonce = encrypted_data[:12]

        # Extract ciphertext + authentication tag
        ciphertext = encrypted_data[12:]

        # AES-GCM automatically verifies integrity
        plaintext = self.aes.decrypt(
            nonce,
            ciphertext,
            None
        )

        return plaintext.decode("utf-8")