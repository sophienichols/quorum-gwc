import requests

class QuorumAPI(object):
    """
    An overall wrapper for Quorum's API that enables chainable
    filters and abstracts away the actual HTTP requests to the API.

    Typical usage:
    1. initialize a QuorumAPI object, passing in the username and API key
    2. set the endpoint of this particular QuorumAPI object (optionally can be specified at initialization)
    3. create a set of filters and set the settings on a given API object
    4. run GET to return relevant results

    Example:
    quorum_api = QuorumAPI(username="gwc", api_key="")
    quorum_api.set_endpoint("person")
    print quorum_api.count(True) \
                    .limit(100) \
                    .offset(20) \
                    .filter(role_type = RoleType.senator, current=True) \
                    .GET()
    """

    # supported endpoints allows
    SUPPORTED_ENDPOINTS = ["person", "bill", "vote"]

    def __init__(self, username, api_key, endpoint = None):

        self.username = username
        self.api_key = api_key

        if self.endpoint:
            self.set_endpoint(endpoint)

    def set_endpoint(self, endpoint):
        if endpoint in self.SUPPORTED_ENDPOINTS:
            self.endpoint = endpoint
        else:
            raise Exception('Unsupported Endpoint')

    def GET(self):
        """
        The final step in calling the API -- actually
        go out and make the request. Returns a dictionary
        of results.
        """


