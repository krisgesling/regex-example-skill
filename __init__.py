
from adapt.intent import IntentBuilder
from mycroft import MycroftSkill, intent_handler


class Regex(MycroftSkill):
    def __init__(self):
        MycroftSkill.__init__(self)

    @intent_handler(IntentBuilder("").require("test").require("alpha").optionally("Location"))
    def handle_query_time(self, message):
        print(message.data.keys())
        location = message.data['Location']
        print(location)
        self.speak_dialog('regex', {'location': location})


def create_skill():
    return Regex()
