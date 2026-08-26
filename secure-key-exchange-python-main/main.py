from key_exchange import KeyExchange
from encryption import SecureMessenger


def print_separator():
    print("=" * 65)


# ============================================================
# START
# ============================================================

print_separator()
print("          SECURE KEY EXCHANGE & COMMUNICATION")
print("             Diffie-Hellman + AES-256-GCM")
print_separator()


# ============================================================
# 1. KEY GENERATION
# ============================================================

key_exchange = KeyExchange()

print("\n[1] GENERATING CRYPTOGRAPHIC KEYS")
print("-" * 65)

private_a, public_a = key_exchange.generate_key_pair()

print("\nUSER A")
print("Private Key : GENERATED 🔒")
print("Public Key  : GENERATED 🌐")

private_b, public_b = key_exchange.generate_key_pair()

print("\nUSER B")
print("Private Key : GENERATED 🔒")
print("Public Key  : GENERATED 🌐")


# ============================================================
# 2. PUBLIC KEY EXCHANGE
# ============================================================

print("\n[2] PUBLIC KEY EXCHANGE")
print("-" * 65)

print("User A  ─────── Public Key A ───────>  User B")
print("User B  ─────── Public Key B ───────>  User A")

print("\n✓ Public keys exchanged successfully.")


# ============================================================
# 3. SHARED SESSION KEY
# ============================================================

print("\n[3] ESTABLISHING SHARED SESSION KEY")
print("-" * 65)

shared_key_a = key_exchange.derive_shared_key(
    private_a,
    public_b
)

shared_key_b = key_exchange.derive_shared_key(
    private_b,
    public_a
)

print("\nUser A Session Key:")
print(shared_key_a.hex())

print("\nUser B Session Key:")
print(shared_key_b.hex())


# ============================================================
# 4. VERIFY SESSION KEY
# ============================================================

print("\n[4] VERIFYING SESSION KEYS")
print("-" * 65)

if shared_key_a == shared_key_b:

    print("✓ SUCCESS!")
    print("Both users generated the SAME session key.")

else:

    print("✗ FAILURE!")
    print("Session keys do not match.")
    exit()


# ============================================================
# 5. CREATE SECURE MESSENGERS
# ============================================================

user_a = SecureMessenger(shared_key_a)
user_b = SecureMessenger(shared_key_b)


# ============================================================
# 6. EAVESDROPPER SIMULATION
# ============================================================

print("\n[5] EAVESDROPPER SIMULATION 👀")
print("-" * 65)

print("""
An attacker is monitoring the communication channel.

The attacker can observe:
✓ User A's Public Key
✓ User B's Public Key

The attacker CANNOT see:
✗ User A's Private Key
✗ User B's Private Key
✗ Shared Session Key
""")

print("Eavesdropper is listening...")
print("✓ Public information intercepted.")
print("✗ Private keys remain protected.")


# ============================================================
# 7. SECURE MESSAGE
# ============================================================

print("\n[6] SECURE COMMUNICATION")
print("-" * 65)

message = input("\nUser A, enter your message for User B:\n> ")

print("\nEncrypting message...")

encrypted_message = user_a.encrypt_message(message)

print("\n🔐 Encrypted Message:")
print(encrypted_message)


# ============================================================
# 8. EAVESDROPPER SEES CIPHERTEXT
# ============================================================

print("\n[7] EAVESDROPPER INTERCEPTS MESSAGE")
print("-" * 65)

print("Eavesdropper intercepted:")

print("\n" + encrypted_message)

print("\n⚠ The attacker sees ciphertext, NOT the original message.")


# ============================================================
# 9. ATTACKER ATTEMPTS DECRYPTION
# ============================================================

print("\n[8] EAVESDROPPER ATTEMPTS DECRYPTION")
print("-" * 65)

print("Attacker does not possess the session key.")

print("\n❌ Decryption cannot be performed.")
print("The session key is known only to User A and User B.")


# ============================================================
# 10. USER B DECRYPTS
# ============================================================

print("\n[9] USER B RECEIVES MESSAGE")
print("-" * 65)

try:

    decrypted_message = user_b.decrypt_message(
        encrypted_message
    )

    print("✓ Message successfully decrypted!")

    print("\nUser B received:")
    print("> " + decrypted_message)

except Exception:

    print("✗ Decryption failed.")


# ============================================================
# END
# ============================================================

print_separator()
print("             SECURE COMMUNICATION COMPLETED")
print_separator()