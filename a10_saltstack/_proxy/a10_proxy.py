'''
Connect to an a10 device using the a10 proxy by specifying the host information in the
pillar found at '/srv/pillar/a10/a10_proxy.sls'
.. code-block:: yaml
    proxy:
      proxytype: a10
      host: <ip or dns name of host>
      username: <username>
      port: <port number>
      protocol: <https, https, tcp, etc.>
      password: <supersecret>
In '/srv/pillar/a10/top.sls' map the device details with the proxy name.
.. code-block:: yaml
    base:
      'ax':
        - a10_proxy 
After storing the device information in the pillar, configure the proxy \
in '/etc/salt/proxy'
.. code-block:: yaml
    master: <ip or hostname of salt-master>
Run the salt proxy via the following command:
.. code-block:: bash
    salt-proxy --proxyid=ax
'''
from __future__ import absolute_import

import logging

try:
    import acos_client
    HAS_ACOS_CLIENT = True
except ImportError:
    HAS_ACOS_CLIENT = False

__proxyenabled__ = ['a10_proxy']


GRAINS_CACHE = {}
DETAILS = {}

LOG = logging.getLogger(__file__)

session = None


def __virtual__():
    '''
    Only return if all the modules are available
    '''
    if not HAS_ACOS_CLIENT:
        return False, 'Missing dependency: The a10 proxy minion requires the acos-client Python module.'

    return __virtualname__ 


def proxytype():
    '''
    Returns the name of this proxy
    '''
    return 'a10'


def init(opts):
    http_cli = axapi_http.HttpClient(opts['host'], opts['port'], opts['protocol'])
    ax_session = session.Session(http_cli, opts['username'], opts['password'])  


def alive(opts):
    '''
    This function returns a flag with the connection state.
    It is very useful when the proxy minion establishes the communication
    via a channel that requires a more elaborated keep-alive mechanism, e.g.
    NETCONF over SSH.
    '''
    return True 


def initialized():
    '''
    Since grains are loaded in many different places and some of those
    places occur before the proxy can be initialized, return whether
    our init() function has been called
    '''
    return True 

def get_session():
    return session


def ping():
    '''
    Is the REST server up?
    '''
    LOG.debug('a10 proxy ping called')
    return True 


def shutdown(opts):
    '''
    For this proxy shutdown is a no-op
    '''
    session.close()
    LOG.debug('a10 proxy shutdown() called...')
