# Encrypt-Decrypt
This repository contains a PyQt5-based GUI application written in Python for AES encryption and decryption. It provides an intuitive interface where the user can input a secret key and a plaintext message, then either encrypt or decrypt the message. 

The application works on ECB(Electronic Code Book) mode of operation for AES and uses the PyCryptoDome library for the actual encryption and decryption process. It also handles padding via the `Crypto.Util.Padding` module, meaning any length of plaintext can be encrypted.

Upon clicking the "Encrypt" button, the plaintext is encrypted using the given secret key, and the resulting ciphertext is displayed in the application. Clicking the "Decrypt" button decrypts the displayed ciphertext back into plaintext using the same key.

This app is a beginner-friendly tool to understand the simple end-to-end working of AES encryption and decryption. It's ideal for anyone studying cryptography or curious about how text encryption and decryption work in a more practical way.

Please note: The use of ECB mode in AES is generally not recommended for securing sensitive data because it does not provide serious message confidentiality. This is a simple demonstration application and not intended for actual secure communications.
