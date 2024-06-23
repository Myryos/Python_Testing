import pandas as pd
import matplotlib.pyplot as plt
from setup_folder_path import setup_reports_folders

setup_reports_folders()

stats_history_df = pd.read_csv("reports/locust/locust_result_stats_history.csv")


print(stats_history_df.head())

stats_history_df["Timestamp"] = pd.to_datetime(stats_history_df["Timestamp"])

plt.figure(figsize=(10, 6))
plt.plot(
    stats_history_df["Timestamp"],
    stats_history_df["Total Average Response Time"],
    label="Average response time",
)
plt.xlabel("Timestamp")
plt.ylabel("Response Time (ms)")
plt.title("Average Response Time Over Time")
plt.legend()
plt.savefig("reports/media/locust/average_response_time.png")


plt.figure(figsize=(10, 6))
plt.plot(
    stats_history_df["Timestamp"],
    stats_history_df["Total Median Response Time"],
    label="Median response time",
)
plt.xlabel("Timestamp")
plt.ylabel("Response Time (ms)")
plt.title("Median Response Time Over Time")
plt.legend()
plt.savefig("reports/media/locust/median_response_time.png")


plt.figure(figsize=(10, 6))
plt.plot(
    stats_history_df["Timestamp"], stats_history_df["Requests/s"], label="Requests/s"
)
plt.xlabel("Timestamp")
plt.ylabel("Requests per Second")
plt.title("Requests per Second Over Time")
plt.legend()
plt.savefig("reports/media/locust/requests_per_second.png")


plt.figure(figsize=(10, 6))
plt.plot(
    stats_history_df["Timestamp"], stats_history_df["Failures/s"], label="Failures/s"
)
plt.xlabel("Timestamp")
plt.ylabel("Failures per Second")
plt.title("Failures per Second Over Time")
plt.legend()
plt.savefig("reports/media/locust/failures_per_second.png")


plt.figure(figsize=(10, 6))
plt.plot(stats_history_df["Timestamp"], stats_history_df["50%"], label="50%")
plt.plot(stats_history_df["Timestamp"], stats_history_df["75%"], label="75%")
plt.plot(stats_history_df["Timestamp"], stats_history_df["95%"], label="95%")
plt.plot(stats_history_df["Timestamp"], stats_history_df["99%"], label="99%")
plt.xlabel("Timestamp")
plt.ylabel("Response Time (ms)")
plt.title("Response Time Percentiles Over Time")
plt.legend()
plt.savefig("reports/media/locust/response_time_percentiles.png")
