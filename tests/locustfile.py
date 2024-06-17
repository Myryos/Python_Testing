from locust import HttpUser, task, between


class WebsiteUser(HttpUser):
    wait_time = between(1, 5)

    @task
    def load_index(self):
        self.client.get("/")

    @task
    def login(self):
        self.client.post("/showSummary", {"email": "admin@irontemple.com"})

    @task
    def book(self):
        self.client.get("/book/Spring Festival/Simply Lift")
        self.client.post(
            "/purchasePlaces",
            {"competition": "Spring Festival", "club": "Simply Lift", "places": "1"},
        )

    @task
    def leaderboard(self):
        self.client.get("/leaderboard")
