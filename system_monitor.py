
import os
import time
import json
import platform

def get_cpu_info():
    try:
        load = os.getloadavg()
        return round(load[0], 2)
    except (AttributeError, OSError):
        return None

def get_ram_info():
    try:
        with open("/proc/meminfo") as f:
            data = f.readlines()

        mem = {}
        for line in data:
            key, value = line.split(":", 1)
            mem[key] = int(value.strip().split()[0])

        total = mem["MemTotal"]
        available = mem["MemAvailable"]

        return {
            "total_mb": round(total / 1024),
            "available_mb": round(available / 1024),
            "used_percent": round(
                (total - available) / total * 100, 1
            )
        }
    except (OSError, KeyError, ValueError):
        return None

def monitor():
    return {
        "device": platform.machine(),
        "cpu_load": get_cpu_info(),
        "ram": get_ram_info(),
        "time": time.strftime("%Y-%m-%d %H:%M:%S")
    }

if __name__ == "__main__":
    print(json.dumps(monitor(), indent=4))
