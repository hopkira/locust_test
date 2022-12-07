from locust import HttpUser, between, task

class ApiUser(HttpUser):
    wait_time = between(5, 30)

    @task(1)
    def get_analysis(self):
        self.client.post(url = "/api/ESGPortfolio",
                        json = {"portfolio": ["ABNP","AEF","BVUE","CPR","DAG","FEC","SRH","UGO","VVF","XTN","ZAF"],
                                "categories": ["CO2","TotalWaste","WaterUse","EnergyUse","WomenEmployees"],}
         )