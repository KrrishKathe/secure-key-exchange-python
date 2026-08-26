class Eavesdropper:

    def __init__(self):
        self.intercepted_public_key_a = None
        self.intercepted_public_key_b = None
        self.intercepted_message = None

    def intercept_public_keys(self, public_key_a, public_key_b):

        self.intercepted_public_key_a = public_key_a
        self.intercepted_public_key_b = public_key_b

        print("\n👀 EAVESDROPPER")
        print("-" * 60)

        print("✓ Intercepted User A's public key")
        print("✓ Intercepted User B's public key")

    def intercept_message(self, encrypted_message):

        self.intercepted_message = encrypted_message

        print("\n👀 EAVESDROPPER INTERCEPTED MESSAGE")
        print("-" * 60)

        print("Encrypted data:")
        print(encrypted_message)

        print("\n⚠ The attacker can see the ciphertext.")
        print("✗ The attacker does NOT have the session key.")

    def attempt_decryption(self):

        print("\n🔓 EAVESDROPPER ATTEMPTING DECRYPTION")
        print("-" * 60)

        print("Searching for session key...")
        print("✗ Session key not available.")

        print("\n❌ DECRYPTION FAILED")
        print("The attacker cannot recover the original message.")

        return False


# ============================================================
# TEST THE EAVESDROPPER
# ============================================================

if __name__ == "__main__":

    attacker = Eavesdropper()

    print("=" * 60)
    print("       EAVESDROPPER SIMULATION")
    print("=" * 60)

    attacker.intercept_public_keys(
        "USER_A_PUBLIC_KEY",
        "USER_B_PUBLIC_KEY"
    )

    attacker.intercept_message(
        "Encrypted_Message_12345"
    )

    attacker.attempt_decryption()