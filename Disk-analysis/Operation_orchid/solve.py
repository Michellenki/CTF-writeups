#!/usr/bin/env python3
"""
picoCTF – Operation Orchid
"""

import subprocess
import sys
from pathlib import Path


IMAGE = "disk.flag.img"
ENC_FILE = "flag.txt.enc"
OUT_FILE = "flag.txt"

OFFSET = 411648
COUNT = 1782
PASSWORD = "unbreakablepassword123"



def extract_encrypted_flag():
    """Extract encrypted data from disk image using offset."""
    print("[*] Extracting encrypted flag from disk image (lucky method)...")

    try:
        with open(IMAGE, "rb") as img, open(ENC_FILE, "wb") as out:
            img.seek(OFFSET)
            out.write(img.read(COUNT))
    except Exception as e:
        print(f"[!] Extraction failed: {e}")
        sys.exit(1)

    if not Path(ENC_FILE).exists():
        print("[!] Encrypted file was not created.")
        sys.exit(1)

    print(f"[+] Encrypted file extracted: {ENC_FILE}")


def identify_file_type():
    """Identify file type using the `file` command."""
    print("[*] Identifying file type...")
    subprocess.run(["file", ENC_FILE], check=False)


def decrypt_file():
    """Decrypt encrypted file using OpenSSL AES-256."""
    print("[*] Decrypting using OpenSSL AES-256...")

    result = subprocess.run(
        [
            "openssl",
            "aes256",
            "-d",
            "-salt",
            "-in",
            ENC_FILE,
            "-out",
            OUT_FILE,
            "-k",
            PASSWORD
        ],
        capture_output=True
    )

    if result.returncode != 0:
        print("[!] Decryption failed.")
        print(result.stderr.decode())
        sys.exit(1)

    print("[+] Decryption successful.")
    print("[*] Flag contents:")
    print(Path(OUT_FILE).read_text())


def main():
    extract_encrypted_flag()
    identify_file_type()
    decrypt_file()


if __name__ == "__main__":
    main()

