
import json
from ai_engine import analyze
from system_monitor import monitor
from optimizer import optimize

def main():
    result = {
        "system": analyze(),
        "monitor": monitor(),
        "optimization": optimize()
    }

    print("=" * 35)
    print("J7 PRO AI LITE V1")
    print("=" * 35)
    print(json.dumps(result, indent=4))
    print("AI ENGINE: SUCCESS")

if __name__ == "__main__":
    main()
