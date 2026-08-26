import tkinter as tk
from tkinter import messagebox, scrolledtext
import base64

from key_exchange import KeyExchange
from encryption import SecureMessenger
from attacker import Eavesdropper


class SecureCommunicationApp:

    def __init__(self, root):

        self.root = root
        self.root.title("Secure Key Exchange & Communication System")
        self.root.geometry("1000x750")
        self.root.minsize(900, 700)

        # Colors
        self.bg_color = "#0F172A"
        self.card_color = "#1E293B"
        self.accent_color = "#38BDF8"
        self.success_color = "#22C55E"
        self.warning_color = "#F59E0B"
        self.danger_color = "#EF4444"
        self.text_color = "#F8FAFC"
        self.secondary_text = "#94A3B8"

        self.root.configure(bg=self.bg_color)

        # Cryptographic objects
        self.key_exchange = KeyExchange()

        self.private_a = None
        self.public_a = None

        self.private_b = None
        self.public_b = None

        self.shared_key_a = None
        self.shared_key_b = None

        self.user_a = None
        self.user_b = None

        self.last_encrypted_message = None

        self.create_header()
        self.create_key_exchange_section()
        self.create_message_section()
        self.create_security_monitor()

    # =========================================================
    # HEADER
    # =========================================================

    def create_header(self):

        header = tk.Frame(
            self.root,
            bg=self.bg_color
        )

        header.pack(
            fill="x",
            padx=25,
            pady=(20, 10)
        )

        tk.Label(
            header,
            text="🔐 Secure Key Exchange & Communication",
            font=("Segoe UI", 22, "bold"),
            bg=self.bg_color,
            fg=self.text_color
        ).pack()

        tk.Label(
            header,
            text="Diffie-Hellman + HKDF + AES-256-GCM",
            font=("Segoe UI", 11),
            bg=self.bg_color,
            fg=self.secondary_text
        ).pack(pady=(5, 0))

    # =========================================================
    # KEY EXCHANGE
    # =========================================================

    def create_key_exchange_section(self):

        section = tk.Frame(
            self.root,
            bg=self.card_color
        )

        section.pack(
            fill="x",
            padx=25,
            pady=8
        )

        tk.Label(
            section,
            text="🔑 1. Secure Key Exchange",
            font=("Segoe UI", 14, "bold"),
            bg=self.card_color,
            fg=self.accent_color
        ).pack(
            anchor="w",
            padx=20,
            pady=(15, 10)
        )

        users_frame = tk.Frame(
            section,
            bg=self.card_color
        )

        users_frame.pack(
            fill="x",
            padx=20
        )

        # USER A
        user_a_frame = tk.Frame(
            users_frame,
            bg="#273449"
        )

        user_a_frame.pack(
            side="left",
            fill="both",
            expand=True,
            padx=(0, 10)
        )

        tk.Label(
            user_a_frame,
            text="USER A",
            font=("Segoe UI", 13, "bold"),
            bg="#273449",
            fg=self.text_color
        ).pack(pady=(10, 5))

        self.user_a_status = tk.Label(
            user_a_frame,
            text="Private Key: Not Generated\n"
                 "Public Key: Not Generated",
            font=("Segoe UI", 10),
            bg="#273449",
            fg=self.secondary_text
        )

        self.user_a_status.pack(pady=(0, 10))

        # USER B
        user_b_frame = tk.Frame(
            users_frame,
            bg="#273449"
        )

        user_b_frame.pack(
            side="left",
            fill="both",
            expand=True,
            padx=(10, 0)
        )

        tk.Label(
            user_b_frame,
            text="USER B",
            font=("Segoe UI", 13, "bold"),
            bg="#273449",
            fg=self.text_color
        ).pack(pady=(10, 5))

        self.user_b_status = tk.Label(
            user_b_frame,
            text="Private Key: Not Generated\n"
                 "Public Key: Not Generated",
            font=("Segoe UI", 10),
            bg="#273449",
            fg=self.secondary_text
        )

        self.user_b_status.pack(pady=(0, 10))

        self.generate_button = tk.Button(
            section,
            text="GENERATE KEYS & ESTABLISH SESSION",
            command=self.establish_session,
            font=("Segoe UI", 11, "bold"),
            bg=self.accent_color,
            fg="#0F172A",
            relief="flat",
            cursor="hand2",
            padx=15,
            pady=8
        )

        self.generate_button.pack(
            pady=(10, 8)
        )

        self.session_status = tk.Label(
            section,
            text="● Secure session not established",
            font=("Segoe UI", 10, "bold"),
            bg=self.card_color,
            fg=self.secondary_text
        )

        self.session_status.pack(
            pady=(0, 12)
        )

    # =========================================================
    # ESTABLISH SESSION
    # =========================================================

    def establish_session(self):

        try:

            self.private_a, self.public_a = \
                self.key_exchange.generate_key_pair()

            self.private_b, self.public_b = \
                self.key_exchange.generate_key_pair()

            self.shared_key_a = \
                self.key_exchange.derive_shared_key(
                    self.private_a,
                    self.public_b
                )

            self.shared_key_b = \
                self.key_exchange.derive_shared_key(
                    self.private_b,
                    self.public_a
                )

            if self.shared_key_a != self.shared_key_b:

                messagebox.showerror(
                    "Security Error",
                    "Session keys do not match!"
                )

                return

            self.user_a = SecureMessenger(
                self.shared_key_a
            )

            self.user_b = SecureMessenger(
                self.shared_key_b
            )

            self.user_a_status.config(
                text="Private Key: 🔒 Protected\n"
                     "Public Key: 🌐 Generated",
                fg=self.success_color
            )

            self.user_b_status.config(
                text="Private Key: 🔒 Protected\n"
                     "Public Key: 🌐 Generated",
                fg=self.success_color
            )

            self.session_status.config(
                text="● SECURE SESSION ESTABLISHED",
                fg=self.success_color
            )

            self.log(
                "✓ Diffie-Hellman key exchange completed."
            )

            self.log(
                "✓ User A and User B generated matching session keys."
            )

            self.log(
                "✓ Session protected using AES-256-GCM."
            )

            messagebox.showinfo(
                "Secure Session",
                "Secure session established successfully!"
            )

        except Exception as error:

            messagebox.showerror(
                "Error",
                str(error)
            )

    # =========================================================
    # MESSAGE SECTION
    # =========================================================

    def create_message_section(self):

        section = tk.Frame(
            self.root,
            bg=self.card_color
        )

        section.pack(
            fill="x",
            padx=25,
            pady=8
        )

        tk.Label(
            section,
            text="💬 2. Secure Communication",
            font=("Segoe UI", 14, "bold"),
            bg=self.card_color,
            fg=self.accent_color
        ).pack(
            anchor="w",
            padx=20,
            pady=(15, 10)
        )

        input_frame = tk.Frame(
            section,
            bg=self.card_color
        )

        input_frame.pack(
            fill="x",
            padx=20
        )

        self.message_entry = tk.Entry(
            input_frame,
            font=("Segoe UI", 11),
            bg="#273449",
            fg=self.text_color,
            insertbackground=self.text_color,
            relief="flat"
        )

        self.message_entry.pack(
            side="left",
            fill="x",
            expand=True,
            ipady=8
        )

        self.send_button = tk.Button(
            input_frame,
            text="🔒 SEND",
            command=self.send_message,
            font=("Segoe UI", 10, "bold"),
            bg=self.success_color,
            fg="#052E16",
            relief="flat",
            cursor="hand2",
            padx=20,
            pady=7
        )

        self.send_button.pack(
            side="right",
            padx=(10, 0)
        )

        tk.Label(
            section,
            text="Encrypted Message:",
            font=("Segoe UI", 10, "bold"),
            bg=self.card_color,
            fg=self.secondary_text
        ).pack(
            anchor="w",
            padx=20,
            pady=(12, 3)
        )

        self.encrypted_display = tk.Label(
            section,
            text="No encrypted message yet.",
            font=("Consolas", 9),
            bg="#273449",
            fg=self.secondary_text,
            wraplength=850,
            justify="left",
            anchor="w"
        )

        self.encrypted_display.pack(
            fill="x",
            padx=20,
            pady=(0, 8),
            ipady=8
        )

        self.decrypted_display = tk.Label(
            section,
            text="User B: No message received.",
            font=("Segoe UI", 10, "bold"),
            bg=self.card_color,
            fg=self.secondary_text
        )

        self.decrypted_display.pack(
            anchor="w",
            padx=20,
            pady=(0, 8)
        )

        # Attack buttons
        attack_frame = tk.Frame(
            section,
            bg=self.card_color
        )

        attack_frame.pack(
            pady=(5, 12)
        )

        self.eavesdrop_button = tk.Button(
            attack_frame,
            text="👀 SIMULATE EAVESDROPPER",
            command=self.simulate_eavesdropper,
            font=("Segoe UI", 9, "bold"),
            bg=self.warning_color,
            fg="#451A03",
            relief="flat",
            cursor="hand2",
            padx=12,
            pady=6
        )

        self.eavesdrop_button.pack(
            side="left",
            padx=5
        )

        self.tamper_button = tk.Button(
            attack_frame,
            text="🛡️ SIMULATE TAMPERING",
            command=self.simulate_tampering,
            font=("Segoe UI", 9, "bold"),
            bg=self.danger_color,
            fg="white",
            relief="flat",
            cursor="hand2",
            padx=12,
            pady=6
        )

        self.tamper_button.pack(
            side="left",
            padx=5
        )

    # =========================================================
    # SEND MESSAGE
    # =========================================================

    def send_message(self):

        if self.user_a is None:

            messagebox.showwarning(
                "No Secure Session",
                "Please establish a secure session first."
            )

            return

        message = self.message_entry.get().strip()

        if not message:

            messagebox.showwarning(
                "Empty Message",
                "Please enter a message."
            )

            return

        try:

            encrypted_message = \
                self.user_a.encrypt_message(message)

            self.last_encrypted_message = encrypted_message

            self.encrypted_display.config(
                text=encrypted_message,
                fg=self.accent_color
            )

            decrypted_message = \
                self.user_b.decrypt_message(
                    encrypted_message
                )

            self.decrypted_display.config(
                text=f"✓ User B received: {decrypted_message}",
                fg=self.success_color
            )

            self.log(
                "→ User A sent encrypted message."
            )

            self.log(
                "✓ AES-256-GCM encryption applied."
            )

            self.log(
                "✓ User B successfully decrypted message."
            )

            self.message_entry.delete(
                0,
                tk.END
            )

        except Exception as error:

            messagebox.showerror(
                "Encryption Error",
                str(error)
            )

    # =========================================================
    # EAVESDROPPER SIMULATION
    # =========================================================

    def simulate_eavesdropper(self):

        if self.user_a is None:

            messagebox.showwarning(
                "No Session",
                "Establish a secure session first."
            )

            return

        attacker = Eavesdropper()

        self.log("")
        self.log("👀 EAVESDROPPER SIMULATION STARTED")
        self.log("-" * 45)

        attacker.intercept_public_keys(
            self.public_a,
            self.public_b
        )

        self.log(
            "✓ Attacker intercepted User A's public key."
        )

        self.log(
            "✓ Attacker intercepted User B's public key."
        )

        if self.last_encrypted_message:

            attacker.intercept_message(
                self.last_encrypted_message
            )

            self.log(
                "✓ Attacker intercepted ciphertext."
            )

        attacker.attempt_decryption()

        self.log(
            "✗ Private keys unavailable to attacker."
        )

        self.log(
            "✗ Session key unavailable to attacker."
        )

        self.log(
            "❌ EAVESDROPPING ATTACK FAILED"
        )

        messagebox.showinfo(
            "Eavesdropper Simulation",
            "Attacker intercepted public information and ciphertext,\n"
            "but could not decrypt the message."
        )

    # =========================================================
    # TAMPERING SIMULATION
    # =========================================================

    def simulate_tampering(self):

        if self.user_a is None:

            messagebox.showwarning(
                "No Session",
                "Establish a secure session first."
            )

            return

        if not self.last_encrypted_message:

            messagebox.showwarning(
                "No Message",
                "Send a message first."
            )

            return

        original = self.last_encrypted_message

        tampered = list(original)

        # Modify one character
        index = 10

        if tampered[index] != "A":
            tampered[index] = "A"
        else:
            tampered[index] = "B"

        tampered = "".join(tampered)

        self.log("")
        self.log("🛡️ TAMPERING SIMULATION STARTED")
        self.log("-" * 45)

        self.log(
            "✓ Attacker modified the ciphertext."
        )

        self.log(
            "→ User B attempting decryption..."
        )

        try:

            self.user_b.decrypt_message(
                tampered
            )

            self.log(
                "⚠ WARNING: Tampering was not detected."
            )

        except Exception:

            self.log(
                "❌ AES-256-GCM authentication failed."
            )

            self.log(
                "❌ MESSAGE TAMPERING DETECTED."
            )

            self.log(
                "✓ Modified ciphertext rejected."
            )

            messagebox.showwarning(
                "Tampering Detected",
                "❌ MESSAGE TAMPERING DETECTED!\n\n"
                "AES-256-GCM authentication failed.\n"
                "The modified message was rejected."
            )

    # =========================================================
    # SECURITY MONITOR
    # =========================================================

    def create_security_monitor(self):

        section = tk.Frame(
            self.root,
            bg=self.card_color
        )

        section.pack(
            fill="both",
            expand=True,
            padx=25,
            pady=8
        )

        tk.Label(
            section,
            text="👀 3. Security Monitor",
            font=("Segoe UI", 14, "bold"),
            bg=self.card_color,
            fg=self.accent_color
        ).pack(
            anchor="w",
            padx=20,
            pady=(12, 5)
        )

        self.security_log = scrolledtext.ScrolledText(
            section,
            height=7,
            font=("Consolas", 9),
            bg="#111827",
            fg=self.success_color,
            insertbackground=self.text_color,
            relief="flat"
        )

        self.security_log.pack(
            fill="both",
            expand=True,
            padx=20,
            pady=(5, 12)
        )

        self.security_log.insert(
            tk.END,
            "SECURITY MONITOR READY\n"
        )

        self.security_log.insert(
            tk.END,
            "Waiting for secure session...\n"
        )

    # =========================================================
    # LOG FUNCTION
    # =========================================================

    def log(self, message):

        self.security_log.insert(
            tk.END,
            message + "\n"
        )

        self.security_log.see(
            tk.END
        )


# =============================================================
# RUN APPLICATION
# =============================================================

if __name__ == "__main__":

    root = tk.Tk()

    app = SecureCommunicationApp(root)

    root.mainloop()