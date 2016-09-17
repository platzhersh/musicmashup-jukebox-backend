from channels import Channel
from channels.tests import ChannelTestCase

class MyTests(ChannelTestCase):
    def test_a_thing(self):
        # This goes onto an in-memory channel, not the real backend.
        Channel("chat").send({"foo": "bar"})