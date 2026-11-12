
import json
import os
import time

def get_battery():
    base = "/sys/class/power_supply"

    for name in ("battery", "BAT0"):
        path = os.path.join(base, name)

        try:
            with open(os.path.join(path, "capacity")) as f:
                level = int(f.read().strip())

            status_path = os.path.join(path, "status")
            with open(status_path) as f:
                status = f.read().strip()

            return {
                "level": level,
                "status": status,
                "source": "android_sysfs"
            }
        except (OSError, ValueError):
            continue

    return {
        "level": None,
        "status": "UNAVAILABLE",
        "source": "not_supported"
    }

def analyze_battery():
    battery = get_battery()
    level = battery["level"]

    if level is None:
        advice = "Battery data unavailable"
    elif level <= 20:
        advice = "Enable battery saver if needed"
    elif level >= 80:
        advice = "Battery level is high"
    else:
        advice = "Battery level looks normal"

    return {
        "battery": battery,
        "recommendation": advice,
        "time": time.strftime("%H:%M:%S")
    }

if __name__ == "__main__":
    print(json.dumps(analyze_battery(), indent=4))
