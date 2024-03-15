r"""
    This code was generated by
   ___ _ _ _ _ _    _ ____    ____ ____ _    ____ ____ _  _ ____ ____ ____ ___ __   __
    |  | | | | |    | |  | __ |  | |__| | __ | __ |___ |\ | |___ |__/ |__|  | |  | |__/
    |  |_|_| | |___ | |__|    |__| |  | |    |__] |___ | \| |___ |  \ |  |  | |__| |  \

    Twilio - Monitor
    This is the public Twilio REST API.

    NOTE: This class is auto generated by OpenAPI Generator.
    https://openapi-generator.tech
    Do not edit the class manually.
"""

from datetime import datetime
from typing import Any, Dict, List, Optional, Union, Iterator, AsyncIterator
from twilio.base import deserialize, serialize, values
from twilio.base.instance_context import InstanceContext
from twilio.base.instance_resource import InstanceResource
from twilio.base.list_resource import ListResource
from twilio.base.version import Version
from twilio.base.page import Page


class EventInstance(InstanceResource):
    """
    :ivar account_sid: The SID of the [Account](https://www.twilio.com/docs/iam/api/account) that created the Event resource.
    :ivar actor_sid: The SID of the actor that caused the event, if available. Can be `null`.
    :ivar actor_type: The type of actor that caused the event. Can be: `user` for a change made by a logged-in user in the Twilio Console, `account` for an event caused by an API request by an authenticating Account, `twilio-admin` for an event caused by a Twilio employee, and so on.
    :ivar description: A description of the event. Can be `null`.
    :ivar event_data: An object with additional data about the event. The  contents depend on `event_type`. For example, event-types of the form `RESOURCE.updated`, this value contains a `resource_properties` dictionary that describes the previous and updated properties of the resource.
    :ivar event_date: The date and time in GMT when the event was recorded specified in [ISO 8601](https://en.wikipedia.org/wiki/ISO_8601) format.
    :ivar event_type: The event's type. Event-types are typically in the form: `RESOURCE_TYPE.ACTION`, where `RESOURCE_TYPE` is the type of resource that was affected and `ACTION` is what happened to it. For example, `phone-number.created`. For a full list of all event-types, see the [Monitor Event Types](https://www.twilio.com/docs/usage/monitor-events#event-types).
    :ivar resource_sid: The SID of the resource that was affected.
    :ivar resource_type: The type of resource that was affected. For a full list of all resource-types, see the [Monitor Event Types](https://www.twilio.com/docs/usage/monitor-events#event-types).
    :ivar sid: The unique string that we created to identify the Event resource.
    :ivar source: The originating system or interface that caused the event.  Can be: `web` for events caused by user action in the Twilio Console, `api` for events caused by a request to our API, or   `twilio` for events caused by an automated or internal Twilio system.
    :ivar source_ip_address: The IP address of the source, if the source is outside the Twilio cloud. This value is `null` for events with `source` of `twilio`
    :ivar url: The absolute URL of the resource that was affected. Can be `null`.
    :ivar links: The absolute URLs of related resources.
    """

    def __init__(
        self, version: Version, payload: Dict[str, Any], sid: Optional[str] = None
    ):
        super().__init__(version)

        self.account_sid: Optional[str] = payload.get("account_sid")
        self.actor_sid: Optional[str] = payload.get("actor_sid")
        self.actor_type: Optional[str] = payload.get("actor_type")
        self.description: Optional[str] = payload.get("description")
        self.event_data: Optional[Dict[str, object]] = payload.get("event_data")
        self.event_date: Optional[datetime] = deserialize.iso8601_datetime(
            payload.get("event_date")
        )
        self.event_type: Optional[str] = payload.get("event_type")
        self.resource_sid: Optional[str] = payload.get("resource_sid")
        self.resource_type: Optional[str] = payload.get("resource_type")
        self.sid: Optional[str] = payload.get("sid")
        self.source: Optional[str] = payload.get("source")
        self.source_ip_address: Optional[str] = payload.get("source_ip_address")
        self.url: Optional[str] = payload.get("url")
        self.links: Optional[Dict[str, object]] = payload.get("links")

        self._solution = {
            "sid": sid or self.sid,
        }
        self._context: Optional[EventContext] = None

    @property
    def _proxy(self) -> "EventContext":
        """
        Generate an instance context for the instance, the context is capable of
        performing various actions. All instance actions are proxied to the context

        :returns: EventContext for this EventInstance
        """
        if self._context is None:
            self._context = EventContext(
                self._version,
                sid=self._solution["sid"],
            )
        return self._context

    def fetch(self) -> "EventInstance":
        """
        Fetch the EventInstance


        :returns: The fetched EventInstance
        """
        return self._proxy.fetch()

    async def fetch_async(self) -> "EventInstance":
        """
        Asynchronous coroutine to fetch the EventInstance


        :returns: The fetched EventInstance
        """
        return await self._proxy.fetch_async()

    def __repr__(self) -> str:
        """
        Provide a friendly representation

        :returns: Machine friendly representation
        """
        context = " ".join("{}={}".format(k, v) for k, v in self._solution.items())
        return "<Twilio.Monitor.V1.EventInstance {}>".format(context)


class EventContext(InstanceContext):

    def __init__(self, version: Version, sid: str):
        """
        Initialize the EventContext

        :param version: Version that contains the resource
        :param sid: The SID of the Event resource to fetch.
        """
        super().__init__(version)

        # Path Solution
        self._solution = {
            "sid": sid,
        }
        self._uri = "/Events/{sid}".format(**self._solution)

    def fetch(self) -> EventInstance:
        """
        Fetch the EventInstance


        :returns: The fetched EventInstance
        """

        payload = self._version.fetch(
            method="GET",
            uri=self._uri,
        )

        return EventInstance(
            self._version,
            payload,
            sid=self._solution["sid"],
        )

    async def fetch_async(self) -> EventInstance:
        """
        Asynchronous coroutine to fetch the EventInstance


        :returns: The fetched EventInstance
        """

        payload = await self._version.fetch_async(
            method="GET",
            uri=self._uri,
        )

        return EventInstance(
            self._version,
            payload,
            sid=self._solution["sid"],
        )

    def __repr__(self) -> str:
        """
        Provide a friendly representation

        :returns: Machine friendly representation
        """
        context = " ".join("{}={}".format(k, v) for k, v in self._solution.items())
        return "<Twilio.Monitor.V1.EventContext {}>".format(context)


class EventPage(Page):

    def get_instance(self, payload: Dict[str, Any]) -> EventInstance:
        """
        Build an instance of EventInstance

        :param payload: Payload response from the API
        """
        return EventInstance(self._version, payload)

    def __repr__(self) -> str:
        """
        Provide a friendly representation

        :returns: Machine friendly representation
        """
        return "<Twilio.Monitor.V1.EventPage>"


class EventList(ListResource):

    def __init__(self, version: Version):
        """
        Initialize the EventList

        :param version: Version that contains the resource

        """
        super().__init__(version)

        self._uri = "/Events"

    def stream(
        self,
        actor_sid: Union[str, object] = values.unset,
        event_type: Union[str, object] = values.unset,
        resource_sid: Union[str, object] = values.unset,
        source_ip_address: Union[str, object] = values.unset,
        start_date: Union[datetime, object] = values.unset,
        end_date: Union[datetime, object] = values.unset,
        limit: Optional[int] = None,
        page_size: Optional[int] = None,
    ) -> Iterator[EventInstance]:
        """
        Streams EventInstance records from the API as a generator stream.
        This operation lazily loads records as efficiently as possible until the limit
        is reached.
        The results are returned as a generator, so this operation is memory efficient.

        :param str actor_sid: Only include events initiated by this Actor. Useful for auditing actions taken by specific users or API credentials.
        :param str event_type: Only include events of this [Event Type](https://www.twilio.com/docs/usage/monitor-events#event-types).
        :param str resource_sid: Only include events that refer to this resource. Useful for discovering the history of a specific resource.
        :param str source_ip_address: Only include events that originated from this IP address. Useful for tracking suspicious activity originating from the API or the Twilio Console.
        :param datetime start_date: Only include events that occurred on or after this date. Specify the date in GMT and [ISO 8601](https://en.wikipedia.org/wiki/ISO_8601) format.
        :param datetime end_date: Only include events that occurred on or before this date. Specify the date in GMT and [ISO 8601](https://en.wikipedia.org/wiki/ISO_8601) format.
        :param limit: Upper limit for the number of records to return. stream()
                      guarantees to never return more than limit.  Default is no limit
        :param page_size: Number of records to fetch per request, when not set will use
                          the default value of 50 records.  If no page_size is defined
                          but a limit is defined, stream() will attempt to read the
                          limit with the most efficient page size, i.e. min(limit, 1000)

        :returns: Generator that will yield up to limit results
        """
        limits = self._version.read_limits(limit, page_size)
        page = self.page(
            actor_sid=actor_sid,
            event_type=event_type,
            resource_sid=resource_sid,
            source_ip_address=source_ip_address,
            start_date=start_date,
            end_date=end_date,
            page_size=limits["page_size"],
        )

        return self._version.stream(page, limits["limit"])

    async def stream_async(
        self,
        actor_sid: Union[str, object] = values.unset,
        event_type: Union[str, object] = values.unset,
        resource_sid: Union[str, object] = values.unset,
        source_ip_address: Union[str, object] = values.unset,
        start_date: Union[datetime, object] = values.unset,
        end_date: Union[datetime, object] = values.unset,
        limit: Optional[int] = None,
        page_size: Optional[int] = None,
    ) -> AsyncIterator[EventInstance]:
        """
        Asynchronously streams EventInstance records from the API as a generator stream.
        This operation lazily loads records as efficiently as possible until the limit
        is reached.
        The results are returned as a generator, so this operation is memory efficient.

        :param str actor_sid: Only include events initiated by this Actor. Useful for auditing actions taken by specific users or API credentials.
        :param str event_type: Only include events of this [Event Type](https://www.twilio.com/docs/usage/monitor-events#event-types).
        :param str resource_sid: Only include events that refer to this resource. Useful for discovering the history of a specific resource.
        :param str source_ip_address: Only include events that originated from this IP address. Useful for tracking suspicious activity originating from the API or the Twilio Console.
        :param datetime start_date: Only include events that occurred on or after this date. Specify the date in GMT and [ISO 8601](https://en.wikipedia.org/wiki/ISO_8601) format.
        :param datetime end_date: Only include events that occurred on or before this date. Specify the date in GMT and [ISO 8601](https://en.wikipedia.org/wiki/ISO_8601) format.
        :param limit: Upper limit for the number of records to return. stream()
                      guarantees to never return more than limit.  Default is no limit
        :param page_size: Number of records to fetch per request, when not set will use
                          the default value of 50 records.  If no page_size is defined
                          but a limit is defined, stream() will attempt to read the
                          limit with the most efficient page size, i.e. min(limit, 1000)

        :returns: Generator that will yield up to limit results
        """
        limits = self._version.read_limits(limit, page_size)
        page = await self.page_async(
            actor_sid=actor_sid,
            event_type=event_type,
            resource_sid=resource_sid,
            source_ip_address=source_ip_address,
            start_date=start_date,
            end_date=end_date,
            page_size=limits["page_size"],
        )

        return self._version.stream_async(page, limits["limit"])

    def list(
        self,
        actor_sid: Union[str, object] = values.unset,
        event_type: Union[str, object] = values.unset,
        resource_sid: Union[str, object] = values.unset,
        source_ip_address: Union[str, object] = values.unset,
        start_date: Union[datetime, object] = values.unset,
        end_date: Union[datetime, object] = values.unset,
        limit: Optional[int] = None,
        page_size: Optional[int] = None,
    ) -> List[EventInstance]:
        """
        Lists EventInstance records from the API as a list.
        Unlike stream(), this operation is eager and will load `limit` records into
        memory before returning.

        :param str actor_sid: Only include events initiated by this Actor. Useful for auditing actions taken by specific users or API credentials.
        :param str event_type: Only include events of this [Event Type](https://www.twilio.com/docs/usage/monitor-events#event-types).
        :param str resource_sid: Only include events that refer to this resource. Useful for discovering the history of a specific resource.
        :param str source_ip_address: Only include events that originated from this IP address. Useful for tracking suspicious activity originating from the API or the Twilio Console.
        :param datetime start_date: Only include events that occurred on or after this date. Specify the date in GMT and [ISO 8601](https://en.wikipedia.org/wiki/ISO_8601) format.
        :param datetime end_date: Only include events that occurred on or before this date. Specify the date in GMT and [ISO 8601](https://en.wikipedia.org/wiki/ISO_8601) format.
        :param limit: Upper limit for the number of records to return. list() guarantees
                      never to return more than limit.  Default is no limit
        :param page_size: Number of records to fetch per request, when not set will use
                          the default value of 50 records.  If no page_size is defined
                          but a limit is defined, list() will attempt to read the limit
                          with the most efficient page size, i.e. min(limit, 1000)

        :returns: list that will contain up to limit results
        """
        return list(
            self.stream(
                actor_sid=actor_sid,
                event_type=event_type,
                resource_sid=resource_sid,
                source_ip_address=source_ip_address,
                start_date=start_date,
                end_date=end_date,
                limit=limit,
                page_size=page_size,
            )
        )

    async def list_async(
        self,
        actor_sid: Union[str, object] = values.unset,
        event_type: Union[str, object] = values.unset,
        resource_sid: Union[str, object] = values.unset,
        source_ip_address: Union[str, object] = values.unset,
        start_date: Union[datetime, object] = values.unset,
        end_date: Union[datetime, object] = values.unset,
        limit: Optional[int] = None,
        page_size: Optional[int] = None,
    ) -> List[EventInstance]:
        """
        Asynchronously lists EventInstance records from the API as a list.
        Unlike stream(), this operation is eager and will load `limit` records into
        memory before returning.

        :param str actor_sid: Only include events initiated by this Actor. Useful for auditing actions taken by specific users or API credentials.
        :param str event_type: Only include events of this [Event Type](https://www.twilio.com/docs/usage/monitor-events#event-types).
        :param str resource_sid: Only include events that refer to this resource. Useful for discovering the history of a specific resource.
        :param str source_ip_address: Only include events that originated from this IP address. Useful for tracking suspicious activity originating from the API or the Twilio Console.
        :param datetime start_date: Only include events that occurred on or after this date. Specify the date in GMT and [ISO 8601](https://en.wikipedia.org/wiki/ISO_8601) format.
        :param datetime end_date: Only include events that occurred on or before this date. Specify the date in GMT and [ISO 8601](https://en.wikipedia.org/wiki/ISO_8601) format.
        :param limit: Upper limit for the number of records to return. list() guarantees
                      never to return more than limit.  Default is no limit
        :param page_size: Number of records to fetch per request, when not set will use
                          the default value of 50 records.  If no page_size is defined
                          but a limit is defined, list() will attempt to read the limit
                          with the most efficient page size, i.e. min(limit, 1000)

        :returns: list that will contain up to limit results
        """
        return [
            record
            async for record in await self.stream_async(
                actor_sid=actor_sid,
                event_type=event_type,
                resource_sid=resource_sid,
                source_ip_address=source_ip_address,
                start_date=start_date,
                end_date=end_date,
                limit=limit,
                page_size=page_size,
            )
        ]

    def page(
        self,
        actor_sid: Union[str, object] = values.unset,
        event_type: Union[str, object] = values.unset,
        resource_sid: Union[str, object] = values.unset,
        source_ip_address: Union[str, object] = values.unset,
        start_date: Union[datetime, object] = values.unset,
        end_date: Union[datetime, object] = values.unset,
        page_token: Union[str, object] = values.unset,
        page_number: Union[int, object] = values.unset,
        page_size: Union[int, object] = values.unset,
    ) -> EventPage:
        """
        Retrieve a single page of EventInstance records from the API.
        Request is executed immediately

        :param actor_sid: Only include events initiated by this Actor. Useful for auditing actions taken by specific users or API credentials.
        :param event_type: Only include events of this [Event Type](https://www.twilio.com/docs/usage/monitor-events#event-types).
        :param resource_sid: Only include events that refer to this resource. Useful for discovering the history of a specific resource.
        :param source_ip_address: Only include events that originated from this IP address. Useful for tracking suspicious activity originating from the API or the Twilio Console.
        :param start_date: Only include events that occurred on or after this date. Specify the date in GMT and [ISO 8601](https://en.wikipedia.org/wiki/ISO_8601) format.
        :param end_date: Only include events that occurred on or before this date. Specify the date in GMT and [ISO 8601](https://en.wikipedia.org/wiki/ISO_8601) format.
        :param page_token: PageToken provided by the API
        :param page_number: Page Number, this value is simply for client state
        :param page_size: Number of records to return, defaults to 50

        :returns: Page of EventInstance
        """
        data = values.of(
            {
                "ActorSid": actor_sid,
                "EventType": event_type,
                "ResourceSid": resource_sid,
                "SourceIpAddress": source_ip_address,
                "StartDate": serialize.iso8601_datetime(start_date),
                "EndDate": serialize.iso8601_datetime(end_date),
                "PageToken": page_token,
                "Page": page_number,
                "PageSize": page_size,
            }
        )

        response = self._version.page(method="GET", uri=self._uri, params=data)
        return EventPage(self._version, response)

    async def page_async(
        self,
        actor_sid: Union[str, object] = values.unset,
        event_type: Union[str, object] = values.unset,
        resource_sid: Union[str, object] = values.unset,
        source_ip_address: Union[str, object] = values.unset,
        start_date: Union[datetime, object] = values.unset,
        end_date: Union[datetime, object] = values.unset,
        page_token: Union[str, object] = values.unset,
        page_number: Union[int, object] = values.unset,
        page_size: Union[int, object] = values.unset,
    ) -> EventPage:
        """
        Asynchronously retrieve a single page of EventInstance records from the API.
        Request is executed immediately

        :param actor_sid: Only include events initiated by this Actor. Useful for auditing actions taken by specific users or API credentials.
        :param event_type: Only include events of this [Event Type](https://www.twilio.com/docs/usage/monitor-events#event-types).
        :param resource_sid: Only include events that refer to this resource. Useful for discovering the history of a specific resource.
        :param source_ip_address: Only include events that originated from this IP address. Useful for tracking suspicious activity originating from the API or the Twilio Console.
        :param start_date: Only include events that occurred on or after this date. Specify the date in GMT and [ISO 8601](https://en.wikipedia.org/wiki/ISO_8601) format.
        :param end_date: Only include events that occurred on or before this date. Specify the date in GMT and [ISO 8601](https://en.wikipedia.org/wiki/ISO_8601) format.
        :param page_token: PageToken provided by the API
        :param page_number: Page Number, this value is simply for client state
        :param page_size: Number of records to return, defaults to 50

        :returns: Page of EventInstance
        """
        data = values.of(
            {
                "ActorSid": actor_sid,
                "EventType": event_type,
                "ResourceSid": resource_sid,
                "SourceIpAddress": source_ip_address,
                "StartDate": serialize.iso8601_datetime(start_date),
                "EndDate": serialize.iso8601_datetime(end_date),
                "PageToken": page_token,
                "Page": page_number,
                "PageSize": page_size,
            }
        )

        response = await self._version.page_async(
            method="GET", uri=self._uri, params=data
        )
        return EventPage(self._version, response)

    def get_page(self, target_url: str) -> EventPage:
        """
        Retrieve a specific page of EventInstance records from the API.
        Request is executed immediately

        :param target_url: API-generated URL for the requested results page

        :returns: Page of EventInstance
        """
        response = self._version.domain.twilio.request("GET", target_url)
        return EventPage(self._version, response)

    async def get_page_async(self, target_url: str) -> EventPage:
        """
        Asynchronously retrieve a specific page of EventInstance records from the API.
        Request is executed immediately

        :param target_url: API-generated URL for the requested results page

        :returns: Page of EventInstance
        """
        response = await self._version.domain.twilio.request_async("GET", target_url)
        return EventPage(self._version, response)

    def get(self, sid: str) -> EventContext:
        """
        Constructs a EventContext

        :param sid: The SID of the Event resource to fetch.
        """
        return EventContext(self._version, sid=sid)

    def __call__(self, sid: str) -> EventContext:
        """
        Constructs a EventContext

        :param sid: The SID of the Event resource to fetch.
        """
        return EventContext(self._version, sid=sid)

    def __repr__(self) -> str:
        """
        Provide a friendly representation

        :returns: Machine friendly representation
        """
        return "<Twilio.Monitor.V1.EventList>"
