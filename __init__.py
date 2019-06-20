
from adapt.intent import IntentBuilder
from mycroft import MycroftSkill, intent_handler


class RegexExample(MycroftSkill):
    def __init__(self):
        MycroftSkill.__init__(self)

    @intent_handler(IntentBuilder('').require('example').optionally('entity'))
    def handle_query_time(self, message):
        # We can see which values are available in message.data
        self.log.info(message.data.keys())
        # We access entities using the .get() method.
        entity = message.data.get('entity')
        self.log.info("Our example entity is: {}".format(entity))
        # We can then process this in some way and respond to the User.
        self.speak_dialog('response', {'entity': entity})

def create_skill():
    return RegexExample()
