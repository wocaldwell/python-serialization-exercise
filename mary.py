import sys
import pickle

class Mary(object):
    """
    Provide an interface for interacting with messages file.

    Methods:
    add_message,
    serialize,
    deserialize.
    """
    def __init__(self, message):
        """
        Arguments:
        message, a string.
        """
        self.all_messages = {}
        self.message = message
        self.class_name = 'Mary'
        try:
            self.all_messages = self.deserialize()
        except FileNotFoundError:
            pass

    def add_message(self):
        """
        Add a new message to the all_messages dictionary.
        """
        try:
            self.all_messages[self.class_name].append(self.message)
        except KeyError:
            self.all_messages[self.class_name] = [self.message]
        print(self.all_messages)
        self.serialize()

    def serialize(self):
        """
        Write all_messages dictionary to messages file in a binary format.
        """
        with open('messages', 'wb+') as messages_file:
            pickle.dump(self.all_messages, messages_file)

    def deserialize(self):
        """
        Convert the messages file from binary.

        Return the contents of the messages file.
        """
        try:
            with open('messages', 'rb+') as messages_file:
                self.all_messages = pickle.load(messages_file)
        except EOFError:
            pass

        return self.all_messages

if __name__ == '__main__':
    mary = Mary(sys.argv[1])
    mary.add_message()

