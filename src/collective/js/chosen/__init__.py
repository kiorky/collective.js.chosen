import logging
from zope.i18nmessageid import MessageFactory
MessageFactory = collectivejschosenMessageFactory = MessageFactory('collective.js.chosen') 
logger = logging.getLogger('collective.js.chosen')
def initialize(context):
    """Initializer called when used as a Zope 2 product.""" 
