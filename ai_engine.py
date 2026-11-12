
import os
import time
import json
import platform

APP_NAME = "J7 PRO AI LITE"
VERSION = "1.0"

def get_system_info():
    return {
        "device": platform.machine(),
        "system": platform.system(),
        "python": platform.python_version(),
        "time": time.strftime("%Y-%m-%d %H:%M:%S")
    }

def analyze():
    info = get_system_info()

    result = {
        "project": APP_NAME,
        "version": VERSION,
        "status": "ACTIVE",
        "mode": "LIGHT",
        "system_info": info,
        "recommendation": "Monitor system usage"
    }

    return result

if __name__ == "__main__":
    print(json.dumps(analyze(), indent=4))
