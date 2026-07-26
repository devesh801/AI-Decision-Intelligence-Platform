from graph.workflow import graph
from utils.report_manager import ReportManager

topic = "Artificial Intelligence in Healthcare"

result = graph.invoke(
    {
        "topic": topic
    }
)

report = result["final_report"]

print(report)

manager = ReportManager()

md_file = manager.save_markdown(report)

json_file = manager.save_json(topic, report)

print("\n------------------------------------")
print("Report Saved Successfully")
print(md_file)
print(json_file)
print("------------------------------------")