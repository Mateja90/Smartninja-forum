from handlers.base import BaseHandler
from models.topic import Topic
from google.appengine.api import users
class TopicHandler(BaseHandler):
    def get(self):
        return self.render_template("topic_add.html")
    def post(self):
        user = users.get_current_user()
        if not user:
            return self.write("You have to login before you can post a topic!")

        title = self.request.get("title")
        content = self.request.get("text")

        new_topic = Topic(title=title, content=content, author_email=user.email())
        new_topic.put()

        return self.redirect_to("topic-details", topic_id=new_topic.key.id())

class TopicDetailHandler(BaseHandler):
    def get(self, topic_id):
        topic = Topic.get_by_id(int(topic_id))
        params={"topic": topic}
        return self.render_template("topic_details.html", params=params)
