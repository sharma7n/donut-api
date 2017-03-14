from twilio.rest import TwilioRestClient

import config


cfg = config.TestingConfig
client = TwilioRestClient(cfg.TWILIO_ACCOUNT_SID, cfg.TWILIO_AUTH_TOKEN)

message = client.messages.create(
    to="+18477574663",
    from_="+13124706976",
    body="Hello, World!")