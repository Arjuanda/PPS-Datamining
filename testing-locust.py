from locust import HttpUser, task, between

class MyFlaskAppUser(HttpUser):
    wait_time = between(1, 5)

    @task
    def test_prediksi(self):
        self.client.get("/prediksi")

    @task
    def test_card_prodi(self):
        self.client.get("/card-prodi")