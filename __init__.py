from mycroft import MycroftSkill, intent_file_handler


class Regex(MycroftSkill):
    def __init__(self):
        MycroftSkill.__init__(self)

    @intent_file_handler('regex.intent')
    def handle_regex(self, message):
        self.speak_dialog('regex')


def create_skill():
    return Regex()

