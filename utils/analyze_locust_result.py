import pandas as pd
import matplotlib.pyplot as plt

# Charger les données CSV
stats_history_df = pd.read_csv("example_stats_history.csv")

# Afficher un aperçu des données
print(stats_history_df.head())

# Convertir le timestamp en datetime pour une meilleure manipulation
stats_history_df["Timestamp"] = pd.to_datetime(stats_history_df["Timestamp"])

# Graphique du temps de réponse moyen au fil du temps
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
plt.savefig("average_response_time.png")
plt.show()

# Graphique du temps de réponse médian au fil du temps
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
plt.savefig("median_response_time.png")
plt.show()

# Graphique des requêtes par seconde au fil du temps
plt.figure(figsize=(10, 6))
plt.plot(
    stats_history_df["Timestamp"], stats_history_df["Requests/s"], label="Requests/s"
)
plt.xlabel("Timestamp")
plt.ylabel("Requests per Second")
plt.title("Requests per Second Over Time")
plt.legend()
plt.savefig("requests_per_second.png")
plt.show()

# Graphique des échecs par seconde au fil du temps
plt.figure(figsize=(10, 6))
plt.plot(
    stats_history_df["Timestamp"], stats_history_df["Failures/s"], label="Failures/s"
)
plt.xlabel("Timestamp")
plt.ylabel("Failures per Second")
plt.title("Failures per Second Over Time")
plt.legend()
plt.savefig("failures_per_second.png")
plt.show()

# Graphique du temps de réponse aux percentiles 50%, 75%, 95% et 99% au fil du temps
plt.figure(figsize=(10, 6))
plt.plot(stats_history_df["Timestamp"], stats_history_df["50%"], label="50%")
plt.plot(stats_history_df["Timestamp"], stats_history_df["75%"], label="75%")
plt.plot(stats_history_df["Timestamp"], stats_history_df["95%"], label="95%")
plt.plot(stats_history_df["Timestamp"], stats_history_df["99%"], label="99%")
plt.xlabel("Timestamp")
plt.ylabel("Response Time (ms)")
plt.title("Response Time Percentiles Over Time")
plt.legend()
plt.savefig("response_time_percentiles.png")
plt.show()
