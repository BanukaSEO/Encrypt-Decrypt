from PyQt5.QtWidgets import QApplication, QWidget, QVBoxLayout, QHBoxLayout, QLabel, QLineEdit, QPushButton, QTextEdit
from Crypto.Cipher import AES
from Crypto.Util.Padding import pad, unpad
import sys

class EncryptionGUI(QWidget):
    def __init__(self):
        super().__init__()
        self.initUI()

    def initUI(self):
        # Set up the layout
        vbox = QVBoxLayout()

        # Create a label and line edit for the encryption key
        key_label = QLabel('Secret Key:')
        self.key_edit = QLineEdit()
        hbox1 = QHBoxLayout()
        hbox1.addWidget(key_label)
        hbox1.addWidget(self.key_edit)
        vbox.addLayout(hbox1)

        # Create a label and text edit for the plaintext message
        plaintext_label = QLabel('Message:')
        self.plaintext_edit = QTextEdit()
        hbox2 = QHBoxLayout()
        hbox2.addWidget(plaintext_label)
        hbox2.addWidget(self.plaintext_edit)
        vbox.addLayout(hbox2)

        # Create a button to encrypt the plaintext message
        encrypt_button = QPushButton('Encrypt')
        encrypt_button.clicked.connect(self.encrypt)
        vbox.addWidget(encrypt_button)

        # Create a label and line edit for the ciphertext
        ciphertext_label = QLabel('Secret Code:')
        self.ciphertext_edit = QLineEdit()
        hbox3 = QHBoxLayout()
        hbox3.addWidget(ciphertext_label)
        hbox3.addWidget(self.ciphertext_edit)
        vbox.addLayout(hbox3)

        # Create a button to decrypt the ciphertext
        decrypt_button = QPushButton('Decrypt')
        decrypt_button.clicked.connect(self.decrypt)
        vbox.addWidget(decrypt_button)

        # Set the layout
        self.setLayout(vbox)

        # Set the window properties
        self.setGeometry(200, 200, 800, 600)
        self.setWindowTitle('Encrypt Decrypt V1.0')

    def encrypt(self):
        # Get the encryption key and plaintext message
        key = self.key_edit.text().encode()
        plaintext = self.plaintext_edit.toPlainText().encode()

        # Encrypt the plaintext using AES
        cipher = AES.new(key, AES.MODE_ECB)
        ciphertext = cipher.encrypt(pad(plaintext, AES.block_size))

        # Set the ciphertext edit to the encrypted message
        self.ciphertext_edit.setText(ciphertext.hex())

    def decrypt(self):
        # Get the encryption key and ciphertext
        key = self.key_edit.text().encode()
        ciphertext = bytes.fromhex(self.ciphertext_edit.text())

        # Decrypt the ciphertext using AES
        cipher = AES.new(key, AES.MODE_ECB)
        plaintext = unpad(cipher.decrypt(ciphertext), AES.block_size)

        # Set the plaintext edit to the decrypted message
        self.plaintext_edit.setPlainText(plaintext.decode())

if __name__ == '__main__':
    app = QApplication(sys.argv)
    gui = EncryptionGUI()
    gui.show()
    sys.exit(app.exec_())
