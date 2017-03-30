from locust import HttpLocust, TaskSet, task

class UserBehavior(TaskSet):

    @task(10)
    def findAllPost(self):
        self.client.get("/api/post")

    @task(1)
    def createPost(self):
        self.client.post("/api/post", 
        	{
			    "content": "Lorem ipsum dolor sit amet, consectetur adipiscing elit. Morbi mollis, lacus eu vestibulum varius, nibh ipsum mattis elit, nec dapibus dolor ante nec elit. Nulla erat leo, gravida quis aliquet quis, ultrices at purus. Vivamus et ante vitae justo aliquam tristique nec vitae ipsum. Praesent molestie ac mauris sit amet fringilla. Nullam et interdum lorem. In ut eleifend erat. Sed ultricies felis turpis. Pellentesque egestas facilisis pharetra.",
			    "createAt": "2017-03-30T17:46:10.000Z",
			    "updateAt": "2017-03-30T17:46:10.000Z",
			    "deleted": "true",
			    "author": "Marcos Lisboa",
			    "views": 451,
			    "title": "Lorem Ipsum",
			    "source": "facebook",
			    "tags": "test"
		  	})

class WebsiteUser(HttpLocust):
    task_set = UserBehavior