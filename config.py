# these will be used as defaults and overridden by CLI arguments

#### general config ####
API_TOKEN = None
MODULE_NAME = None
PORT = None
ENABLE_2FA = None
CREDS = None
SEEN = set()
VERBOSE = False
HOSTNAME = None
FINAL_URL = None

#### webhook config ####
# should a webhook be sent when new creds are received?
WEBHOOKS = False
# where should the webhook be sent?
# this can include the port and should be a full http URI
WEBHOOK_URL = "http://localhost:8000"
# what should be in the webhook?
# must be set as a dict, and will be sent as JSON
WEBHOOK_PAYLOAD = {'message': 'test'}
