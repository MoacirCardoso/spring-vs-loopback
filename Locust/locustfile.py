from locust import HttpLocust, TaskSet, task

class UserBehavior(TaskSet):

    @task(10)
    def findAllPost(self):
        self.client.get("/api/post")

    @task(1)
    def createPost(self):
        self.client.post("/api/post",
        	{
			    "content": "A Vida e Bela",
			    "author": "Marcos Lisboa",
			    "views": 451,
			    "title": "Lorem Ipsum",
			    "source": "facebook",
			    "tags": "test"
		  	})

class WebsiteUser(HttpLocust):
    task_set = UserBehavior