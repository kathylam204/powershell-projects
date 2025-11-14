import re
import csv
import os
from datetime import datetime

# Input and output file names
IN_PATH = "calllog_raw.txt"
OUT_PATH = "calllog_export_readable.csv"

def main():
    if not os.path.exists(IN_PATH):
        print(f"Input file '{IN_PATH}' not found.")
        print("Make sure you ran the PowerShell script first so calllog_raw.txt is created.")
        return

    records = []

    with open(IN_PATH, "r", encoding="utf-8", errors="ignore") as f:
        for raw_line in f:
            line = raw_line.strip()
            if not line:
                continue

            # Remove "Row: ## " at the start if present
            line = re.sub(r"^Row:\s\d+\s", "", line)

            # Split the line into key=value pairs
            parts = [p.strip() for p in line.split(",") if "=" in p]
            kv = {}
            for p in parts:
                key, value = p.split("=", 1)
                kv[key.strip()] = value.strip()

            # Extract main fields
            number = kv.get("number", kv.get("formatted_number", ""))
            duration = kv.get("duration", "")
            call_type = kv.get("type", "")
            name = kv.get("name", "")
            timestamp = kv.get("date", kv.get("last_modified", ""))

            # Convert timestamp → readable date/time
            date_str, time_str = "", ""
            if timestamp.isdigit():
                try:
                    dt = datetime.fromtimestamp(int(timestamp) / 1000.0)
                    date_str = dt.strftime("%Y-%m-%d")
                    time_str = dt.strftime("%H:%M:%S")
                except Exception:
                    # If conversion fails, just leave blank
                    pass

            records.append({
                "Date": date_str,
                "Time": time_str,
                "Number": number,
                "Type": call_type,
                "Duration (sec)": duration,
                "Name": name
            })

    # Map numeric type codes to human-readable text
    type_map = {
        "1": "Incoming",
        "2": "Outgoing",
        "3": "Missed",
        "4": "Voicemail",
        "5": "Rejected",
        "6": "Blocked",
        "7": "Answered externally"
    }

    # Write final CSV
    with open(OUT_PATH, "w", newline="", encoding="utf-8") as f:
        writer = csv.writer(f)
        writer.writerow(["Date", "Time", "Number", "Type", "Duration (sec)", "Name"])
        for r in records:
            call_type_value = str(r["Type"]).strip()
            call_type_readable = type_map.get(call_type_value, call_type_value)
            writer.writerow([
                r["Date"],
                r["Time"],
                r["Number"],
                call_type_readable,
                r["Duration (sec)"],
                r["Name"]
            ])

    print(f"Done! CSV saved as {OUT_PATH}")

if __name__ == "__main__":
    main()
