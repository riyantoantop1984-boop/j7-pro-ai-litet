
import json
from system_monitor import monitor

def optimize():
    data = monitor()

    cpu = data.get("cpu_load")
    ram = data.get("ram")

    recommendations = []

    if cpu is not None and cpu > 2:
        recommendations.append("Check high CPU load")

    if ram and ram["used_percent"] > 85:
        recommendations.append("Check apps using high RAM")

    if not recommendations:
        recommendations.append("System condition looks normal")

    return {
        "optimizer": "J7 PRO AI LITE",
        "status": "ANALYZED",
        "recommendations": recommendations
    }

if __name__ == "__main__":
    print(json.dumps(optimize(), indent=4))
