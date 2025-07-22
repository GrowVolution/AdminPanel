from . import KEY_FOLDER, random_password
from cryptography.hazmat.primitives import hashes, serialization
from cryptography.hazmat.primitives.asymmetric import padding, rsa
from cryptography.hazmat.backends import default_backend
from typing import Tuple
import json

_cached_key = None


def generate_keypair(name: str) -> Tuple[str, str]:
    private_key = rsa.generate_private_key(
        public_exponent=65537,
        key_size=2048,
        backend=default_backend()
    )

    password = random_password().encode()

    pem_path = KEY_FOLDER / f"{name}.pem"
    pem_data = private_key.private_bytes(
        encoding=serialization.Encoding.PEM,
        format=serialization.PrivateFormat.PKCS8,
        encryption_algorithm=serialization.BestAvailableEncryption(password)
    )
    pem_path.write_bytes(pem_data)

    public_key = private_key.public_key()
    public_pem = public_key.public_bytes(
        encoding=serialization.Encoding.PEM,
        format=serialization.PublicFormat.SubjectPublicKeyInfo
    ).decode()

    return public_pem, password.decode()


def create_signature(data: dict) -> str:
    if not _cached_key:
        raise ValueError("Private key is not loaded.")

    private_key = _cached_key
    payload = json.dumps(data, separators=(',', ':'), sort_keys=True).encode()
    signature = private_key.sign(
        payload,
        padding.PSS(
            mgf=padding.MGF1(hashes.SHA256()),
            salt_length=padding.PSS.MAX_LENGTH
        ),
        hashes.SHA256()
    )

    return signature.hex()


def check_password(name: str, password: str) -> bool:
    key_path = KEY_FOLDER / f"{name}.pem"
    if not key_path.exists():
        return False

    try:
        serialization.load_pem_private_key(
            key_path.read_bytes(),
            password=password.encode(),
            backend=default_backend()
        )
        return True
    except (ValueError, TypeError):
        return False


def cache_private_key(name: str, password: str) -> None:
    global _cached_key

    if _cached_key is not None:
        return

    key_path = KEY_FOLDER / f"{name}.pem"
    private_key = serialization.load_pem_private_key(
        key_path.read_bytes(),
        password=password.encode(),
        backend=default_backend()
    )

    _cached_key = private_key


def clear_cached_key():
    global _cached_key
    _cached_key = None
