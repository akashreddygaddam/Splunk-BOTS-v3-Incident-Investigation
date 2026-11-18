import json

def analyze_aws_event(event):
    event_name = event.get("eventName", "Unknown")
    username = event.get("userIdentity", {}).get("userName", "Unknown")

    print("AWS Security Event Detected")
    print("Event:", event_name)
    print("User:", username)

    if event_name in ["ConsoleLogin", "CreateAccessKey", "StopLogging"]:
        print("Potentially suspicious activity detected!")

# Example event
sample_event = {
    "eventName": "ConsoleLogin",
    "userIdentity": {
        "userName": "test-user"
    }
}

analyze_aws_event(sample_event)
