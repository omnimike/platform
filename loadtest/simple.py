from locust import HttpLocust, TaskSet, task


class UserBehavior(TaskSet):

    @task()
    def profile(self):
        self.client.get("/")


class WebsiteUser(HttpLocust):
    host = 'http://api.omnimike.net'
    task_set = UserBehavior
    min_wait = 5000
    max_wait = 10000
