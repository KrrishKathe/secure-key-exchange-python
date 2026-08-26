from key_exchange import KeyExchange
from encryption import SecureMessenger


print("=" * 60)
print("          MESSAGE TAMPERING SIMULATION")
print("=" * 60)


# ------------------------------------------------------------
# 1. Establish secure session
# ------------------------------------------------------------

key_exchange = KeyExchange()

private_a, public_a = key_exchange.generate_key_pair()
private_b, public_b = key_exchange.generate_key_pair()

shared_key_a = key_exchange.derive_shared_key(
    private_a,
    public_b
)

shared_key_b = key_exchange.derive_shared_key(
    private_b,
    public_a
)


# ------------------------------------------------------------
# 2. Create secure messengers
# ------------------------------------------------------------

user_a = SecureMessenger(shared_key_a)
user_b = SecureMessenger(shared_key_b)


# ------------------------------------------------------------
# 3. Send original message
# ------------------------------------------------------------

message = "This message must not be modified."

print("\nOriginal Message:")
print(message)

encrypted_message = user_a.encrypt_message(message)

print("\n🔐 Original Encrypted Message:")
print(encrypted_message)


# ------------------------------------------------------------
# 4. Simulate attacker tampering
# ------------------------------------------------------------

print("\n👀 ATTACKER TAMPERING WITH MESSAGE")
print("-" * 60)

tampered_message = list(encrypted_message)

# Modify one character
if tampered_message[10] != "A":
    tampered_message[10] = "A"
else:
    tampered_message[10] = "B"

tampered_message = "".join(tampered_message)

print("✓ Ciphertext modified by attacker.")

print("\nTampered Encrypted Message:")
print(tampered_message)


# ------------------------------------------------------------
# 5. User B attempts decryption
# ------------------------------------------------------------

print("\n🔓 USER B ATTEMPTS DECRYPTION")
print("-" * 60)

try:

    decrypted_message = user_b.decrypt_message(
        tampered_message
    )

    print("Message:")
    print(decrypted_message)

except Exception:

    print("❌ DECRYPTION FAILED")
    print("❌ MESSAGE TAMPERING DETECTED")
    print("❌ AES-256-GCM authentication failed.")


print("\n" + "=" * 60)
print("             TEST COMPLETED")
print("=" * 60)