
import json
from ai_engine import analyze
from system_monitor import monitor
from optimizer import optimize
from battery_monitor import analyze_battery

def main():
    result = {
        "AI_ENGINE": analyze(),
        "SYSTEM_MONITOR": monitor(),
        "OPTIMIZER": optimize(),
        "BATTERY_AI": analyze_battery()
    }

    print("=" * 40)
    print("J7 PRO AI LITE V2")
    print("=" * 40)
    print(json.dumps(result, indent=4))
    print("ALL MODULES CONNECTED")

if __name__ == "__main__":
    main()
