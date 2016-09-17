from channels import Channel, Group
from channels.tests import ChannelTestCase
from app.consumers import ws_message

class MyTests(ChannelTestCase):

    def test_a_thing(self):
        # Add a test channel to a test group
        Group("room").send({'text': "TEST"})
        """
        # Run the consumer with the new Message object
        ws_message(self.get_next_message("room", require=True))

        Group("room").add("app.receive")
        # Send to the group
        Group("room").send({"text": "TEST"})
        # Verify the message got into the destination channel
        result = self.get_next_message("test-channel", require=True)
        self.assertEqual(result['value'], 42)
        """