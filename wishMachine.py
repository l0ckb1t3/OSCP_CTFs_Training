import os
import re
import platform


def detect_os(ttl):
    """Determina el sistema operativo basado en el TTL"""
    if ttl >= 128:
        return "Windows"
    elif ttl >= 64:
        return "Linux/Unix"
    elif ttl >= 255:
        return "Cisco/Networking Device"
    else:
        return "Desconocido"


def get_ttl(ip):
    """Ejecuta un ping y extrae el TTL de la respuesta"""
    try:
        # Comando según el SO
        command = f"ping -c 1 {ip}" if platform.system().lower() != "windows" else f"ping -n 1 {ip}"
        result = os.popen(command).read()

        # Buscar TTL en la salida del ping
        match = re.search(r"ttl[=\s](\d+)", result, re.IGNORECASE)
        if match:
            return int(match.group(1))
    except Exception as e:
        print(f"[-] Error obteniendo TTL: {e}")
    return None


def validate_ip(ip):
    """Valida que la IP tenga el formato correcto"""
    pattern = re.compile(r"^(?:\d{1,3}\.){3}\d{1,3}$")
    return bool(pattern.match(ip))


if __name__ == "__main__":
    # Pedir la IP por consola
    ip = input("Ingrese la IP de la víctima: ")

    if not validate_ip(ip):
        print("[-] IP no válida. Introduzca una IP en formato correcto (Ejemplo: 10.0.2.30)")
    else:
        ttl = get_ttl(ip)
        if ttl:
            os_detected = detect_os(ttl)
            print(f"[+] IP: {ip} | TTL: {ttl} → Posible sistema operativo: {os_detected}")
        else:
            print("[-] No se pudo obtener el TTL. Verifique la conectividad con el objetivo.")
