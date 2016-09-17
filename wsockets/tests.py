from channels import Channel, Group
from channels.tests import ChannelTestCase
from app.consumers import ws_message

"""
class MyTests(ChannelTestCase):

    def test_channels(self):

    	Channel("websocket.receive").send({'text': "TEST"})
		


    def test_groups(self):
    	# Add a test channel to a test group
        Group("test-group").add("websocket.receive")
        # Send to the group
        Group("test-group").send({"value": 42})
        # Verify the message got into the destination channel
        result = self.get_next_message("websocket.receive", require=True)
        self.assertEqual(result['value'], 42)
"""