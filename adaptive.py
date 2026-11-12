
from system_monitor import monitor
from battery_monitor import analyze_battery

def adaptive_ai():
    system = monitor()
    battery = analyze_battery()

    cpu = system.get("cpu_load")
    ram = system.get("ram")
    level = battery["battery"]["level"]

    mode = "NORMAL"
    actions = []

    if cpu is not None and cpu > 2:
        mode = "CPU_ALERT"
        actions.append("Check CPU usage")

    if ram and ram["used_percent"] > 85:
        mode = "RAM_SAVER"
        actions.append("Check heavy applications")

    if level is not None and level <= 20:
        mode = "BATTERY_SAVER"
        actions.append("Recommend battery saver")

    if not actions:
        actions.append("System condition normal")

    return {
        "AI": "J7 PRO ADAPTIVE V3",
        "MODE": mode,
        "ACTIONS": actions,
        "STATUS": "ANALYSIS COMPLETE"
    }

if __name__ == "__main__":
    import json
    print(json.dumps(adaptive_ai(), indent=4))
