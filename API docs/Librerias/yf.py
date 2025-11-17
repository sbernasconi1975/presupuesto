import subprocess
import sys
import importlib
import os

#!/usr/bin/env python3
# GitHub Copilot
# Script para instalar librerías requeridas para análisis financiero y de datos.
# Uso: python yf.py  (añade --yes para instalar sin confirmación)


# Mapeo pip_name -> import_name (a veces difieren)
PACKAGES = {
    "pandas": "pandas",
    "numpy": "numpy",
    "scipy": "scipy",
    "matplotlib": "matplotlib",
    "seaborn": "seaborn",
    "plotly": "plotly",
    "scikit-learn": "sklearn",
    "statsmodels": "statsmodels",
    "yfinance": "yfinance",
    "pandas-datareader": "pandas_datareader",
    "pandas-ta": "pandas_ta",   # alternativa: 'ta'
    "ta": "ta",
    "openpyxl": "openpyxl",
    "XlsxWriter": "xlsxwriter",
    "jupyterlab": "jupyterlab"
}

REQ_FILENAME = "requirements_finance.txt"


def is_installed(import_name):
    try:
        importlib.import_module(import_name)
        return True
    except Exception:
        return False


def pip_install(package):
    cmd = [sys.executable, "-m", "pip", "install", "--upgrade", package]
    print(f"Ejecutando: {' '.join(cmd)}")
    try:
        subprocess.check_call(cmd)
        return True
    except subprocess.CalledProcessError as e:
        print(f"Error instalando {package}: {e}")
        return False


def write_requirements(packages, filename=REQ_FILENAME):
    with open(filename, "w", encoding="utf-8") as f:
        for pkg in packages:
            f.write(pkg + "\n")
    print(f"Archivo de requisitos guardado en: {filename}")


def main(auto_confirm=False):
    to_install = []
    for pip_name, import_name in PACKAGES.items():
        if is_installed(import_name):
            print(f"Ya instalado: {pip_name} (importe: {import_name})")
        else:
            print(f"No instalado: {pip_name} (importe: {import_name})")
            to_install.append(pip_name)

    if not to_install:
        print("Todas las librerías requeridas ya están instaladas.")
    else:
        print("\nLibrerías pendientes de instalación:")
        for p in to_install:
            print(" -", p)
        if not auto_confirm:
            ans = input("\n¿Desea instalarlas ahora? [y/N]: ").strip().lower()
            if ans != "y":
                print("Instalación cancelada por el usuario.")
                write_requirements(list(PACKAGES.keys()))
                return

        for pkg in to_install:
            success = pip_install(pkg)
            if not success:
                print(f"Fallo instalando {pkg}, continuar con las demás.")

    # Escribe un requirements.txt con todas las dependencias sugeridas
    write_requirements(list(PACKAGES.keys()))
    print("Proceso finalizado.")


if __name__ == "__main__":
    AUTO = "--yes" in sys.argv or "--y" in sys.argv or "-y" in sys.argv
    main(auto_confirm=AUTO)