from pathlib import Path
from datetime import datetime
import json


class ReportManager:

    def __init__(self):

        self.output_dir = Path("outputs/reports")

        self.output_dir.mkdir(parents=True, exist_ok=True)

    def save_markdown(self, report):

        timestamp = datetime.now().strftime("%Y%m%d_%H%M%S")

        filename = self.output_dir / f"report_{timestamp}.md"

        with open(filename, "w", encoding="utf-8") as file:

            file.write(report)

        return filename

    def save_json(self, topic, report):

        timestamp = datetime.now().strftime("%Y%m%d_%H%M%S")

        filename = self.output_dir / f"report_{timestamp}.json"

        data = {

            "topic": topic,

            "generated_at": timestamp,

            "report": report

        }

        with open(filename, "w", encoding="utf-8") as file:

            json.dump(data, file, indent=4)

        return filename