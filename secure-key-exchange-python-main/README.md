#  Secure Key Exchange & Communication System

## 1. Project Overview

The Secure Key Exchange & Communication System is a Python-based
cryptographic application that demonstrates how two users can establish
a secure communication session over an untrusted communication channel.

The project combines Diffie-Hellman key exchange with HKDF and
AES-256-GCM encryption to provide secure message communication.

It also demonstrates two common security threats:

- Eavesdropping
- Message Tampering

A graphical user interface is provided using Tkinter for easy
demonstration and interaction.

---

## 2. Objectives

The main objectives of this project are:

1. To simulate secure key exchange between two users.
2. To demonstrate the Diffie-Hellman key exchange protocol.
3. To derive a common session key using HKDF.
4. To encrypt messages using AES-256-GCM.
5. To demonstrate secure message transmission.
6. To simulate an eavesdropper attempting to intercept communication.
7. To demonstrate detection of message tampering.
8. To provide a simple graphical user interface for the system.

---

## 3. Technologies Used

### Programming Language

- Python 3

### Cryptographic Algorithms

- Diffie-Hellman Key Exchange
- HKDF
- SHA-256
- AES-256-GCM

### Libraries

- cryptography
- tkinter
- base64
- os

---

## 4. System Architecture

The system follows the following communication flow:

User A
   |
   | Generate Private/Public Key
   ↓
Diffie-Hellman Key Exchange
   ↑
   | Generate Private/Public Key
   |
User B

Both users independently derive the same shared secret.

Shared Secret
      |
      ↓
HKDF + SHA-256
      |
      ↓
Session Key
      |
      ↓
AES-256-GCM
      |
      ↓
Encrypted Message
      |
      ↓
User B
      |
      ↓
Decryption + Authentication
      |
      ↓
Original Message

---

## 5. Key Exchange Process

### Step 1: Key Generation

User A generates:

- Private Key A
- Public Key A

User B generates:

- Private Key B
- Public Key B

Private keys remain protected.

---

### Step 2: Public Key Exchange

User A sends Public Key A to User B.

User B sends Public Key B to User A.

Public keys do not need to be kept secret.

---

### Step 3: Shared Secret Generation

User A combines:

- Private Key A
- Public Key B

User B combines:

- Private Key B
- Public Key A

Both users independently calculate the same shared secret.

---

### Step 4: Session Key Derivation

The shared secret is processed using HKDF with SHA-256 to derive
a suitable session key for symmetric encryption.

---

## 6. Secure Communication

After establishing the session key, User A can send a message.

The message is encrypted using:

AES-256-GCM

The encrypted message contains:

- Nonce
- Ciphertext
- Authentication Tag

The resulting encrypted data is encoded using Base64 for transmission
and display.

User B uses the same session key to decrypt the message.

---

## 7. Eavesdropper Simulation

The project includes a controlled eavesdropper simulation.

The attacker can observe:

- User A's public key
- User B's public key
- Encrypted ciphertext

However, the attacker does not possess:

- User A's private key
- User B's private key
- Shared session key

Therefore, the attacker cannot decrypt the encrypted message.

This demonstrates the confidentiality provided by the key exchange
and encryption process.

---

## 8. Message Tampering Detection

The project also simulates an attacker modifying the encrypted
ciphertext before it reaches User B.

AES-256-GCM provides authenticated encryption.

When User B attempts to decrypt the modified ciphertext, the
authentication verification fails.

The system therefore rejects the modified message.

Example:

Original Message
      ↓
AES-256-GCM
      ↓
Encrypted Message
      ↓
Attacker modifies ciphertext
      ↓
User B attempts decryption
      ↓
Authentication Failed
      ↓
Message Rejected

---

## 9. Security Properties

The system demonstrates the following security properties:

### Confidentiality

AES-256-GCM prevents unauthorized users from reading the original
message.

### Integrity

Any modification to the encrypted message is detected.

### Authentication

AES-GCM verifies that the encrypted data has not been modified.

### Secure Key Establishment

Diffie-Hellman allows two users to establish a shared secret without
directly transmitting the secret key.

---

## 10. Project Structure

```text
CRYPTO MINI PROJ/
│
├── main.py
├── gui.py
├── key_exchange.py
├── encryption.py
├── attacker.py
├── tampering_test.py
├── requirements.txt
└── README.md