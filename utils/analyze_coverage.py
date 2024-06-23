import xml.etree.ElementTree as ET
import matplotlib.pyplot as plt
from setup_folder_path import setup_reports_folders

setup_reports_folders()

tree = ET.parse("coverage.xml")
root = tree.getroot()

files = []
line_rates = []

for package in root.findall("packages/package"):
    for class_ in package.findall("classes/class"):
        filename = class_.get("filename")
        line_rate = float(class_.get("line-rate", 0))

        files.append(filename)
        line_rates.append(line_rate * 100)

plt.figure(figsize=(12, 6))

max_width = 0.8
num_files = len(files)
print(num_files)
bar_width = min(max_width, num_files * 0.04)

plt.bar(files, line_rates, color="b", label="Line Coverage (%)", width=bar_width)
plt.xlabel("Files")
plt.ylabel("Coverage (%)")
plt.title("Line Coverage by File")
plt.xticks(rotation=90)
plt.legend()
plt.tight_layout()
plt.savefig("reports/line_coverage.png")
plt.show()
