import requests


class EventBrite():

    def getEvents(orgID):
        response = requests.get('https://www.eventbriteapi.com/v3/{}/organization_id/events'.format(orgID))
        return response.json()

    def getEventsByID(eventID):
        response = requests.get('https://www.eventbriteapi.com/v3/events/{}/').format(eventID)
        return response.json()

    def publishEvent(event):
        """
        '{
                "event": {
                    "name": {
                        "html": "My New Event"
                    },
                    "start":{
                        "timezone": "America/Los_Angeles",
                        "utc": "2019-12-01T02:00:00Z"
                    },
                    "end":{
                        "timezone": "America/Los_Angeles",
                        "utc": "2019-12-01T05:00:00Z"
                    },
                    "currency": "USD"
                }
            }'
        """

        data = {'event':event}
        response = requests.post('https://www.eventbriteapi.com/v3/events/event_id/publish/', data)
        return response.json()

    def unpublishEvent(event_id):
        response = requests.get('https://www.eventbriteapi.com/v3/events/{}/unpublish/').format(event_id)
        return response.json()

    def cancelEvent(event_id):
        response = requests.get('https://www.eventbriteapi.com/v3/events/{}/cancel/').format(event_id)
        return response.json()

    def getUsersInOrg(orgID):
        response = requests.get('https://www.eventbriteapi.com/v3/organizations/{}/members/').format(orgID)
        return response.json()

    def getUsersGoingToEvent(eventID):
        response = requests.get('https://www.eventbriteapi.com/v3/users/{}/').format(eventID)
        return response.json()

    """
    This viewset automatically provides `list`, `create`, `retrieve`,
    `update` and `destroy` actions.

    Additionally we also provide an extra `highlight` action.

    eventBriteRouter.register('getEvents',)
    eventBriteRouter.register('getEventsByID',)
    eventBriteRouter.register('publishEvent',)
    eventBriteRouter.register('unpublishEvent',)
    eventBriteRouter.register('cancelEvent',)
    eventBriteRouter.register('getEUBsers',)
    eventBriteRouter.register('getEBUsersByID',)
    """

    """

        
 
    """
