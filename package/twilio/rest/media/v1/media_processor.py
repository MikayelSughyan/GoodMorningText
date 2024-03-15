r"""
    This code was generated by
   ___ _ _ _ _ _    _ ____    ____ ____ _    ____ ____ _  _ ____ ____ ____ ___ __   __
    |  | | | | |    | |  | __ |  | |__| | __ | __ |___ |\ | |___ |__/ |__|  | |  | |__/
    |  |_|_| | |___ | |__|    |__| |  | |    |__] |___ | \| |___ |  \ |  |  | |__| |  \

    Twilio - Media
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


class MediaProcessorInstance(InstanceResource):

    class Order(object):
        ASC = "asc"
        DESC = "desc"

    class Status(object):
        FAILED = "failed"
        STARTED = "started"
        ENDED = "ended"

    class UpdateStatus(object):
        ENDED = "ended"

    """
    :ivar account_sid: The SID of the [Account](https://www.twilio.com/docs/iam/api/account) that created the MediaProcessor resource.
    :ivar sid: The unique string generated to identify the MediaProcessor resource.
    :ivar date_created: The date and time in GMT when the resource was created specified in [ISO 8601](https://en.wikipedia.org/wiki/ISO_8601) format.
    :ivar date_updated: The date and time in GMT when the resource was last updated specified in [ISO 8601](https://en.wikipedia.org/wiki/ISO_8601) format.
    :ivar extension: The [Media Extension](/docs/live/media-extensions-overview) name or URL. Ex: `video-composer-v2`
    :ivar extension_context: The context of the Media Extension, represented as a JSON dictionary. See the documentation for the specific [Media Extension](/docs/live/media-extensions-overview) you are using for more information about the context to send.
    :ivar status: 
    :ivar url: The absolute URL of the resource.
    :ivar ended_reason: The reason why a MediaProcessor ended. When a MediaProcessor is in progress, will be `null`. When a MediaProcessor is completed, can be `ended-via-api`, `max-duration-exceeded`, `error-loading-extension`, `error-streaming-media` or `internal-service-error`. See [ended reasons](/docs/live/api/mediaprocessors#mediaprocessor-ended-reason-values) for more details.
    :ivar status_callback: The URL to which Twilio will send asynchronous webhook requests for every MediaProcessor event. See [Status Callbacks](/docs/live/api/status-callbacks) for details.
    :ivar status_callback_method: The HTTP method Twilio should use to call the `status_callback` URL. Can be `POST` or `GET` and the default is `POST`.
    :ivar max_duration: The maximum time, in seconds, that the MediaProcessor can run before automatically ends. The default value is 300 seconds, and the maximum value is 90000 seconds. Once this maximum duration is reached, Twilio will end the MediaProcessor, regardless of whether media is still streaming.
    """

    def __init__(
        self, version: Version, payload: Dict[str, Any], sid: Optional[str] = None
    ):
        super().__init__(version)

        self.account_sid: Optional[str] = payload.get("account_sid")
        self.sid: Optional[str] = payload.get("sid")
        self.date_created: Optional[datetime] = deserialize.iso8601_datetime(
            payload.get("date_created")
        )
        self.date_updated: Optional[datetime] = deserialize.iso8601_datetime(
            payload.get("date_updated")
        )
        self.extension: Optional[str] = payload.get("extension")
        self.extension_context: Optional[str] = payload.get("extension_context")
        self.status: Optional["MediaProcessorInstance.Status"] = payload.get("status")
        self.url: Optional[str] = payload.get("url")
        self.ended_reason: Optional[str] = payload.get("ended_reason")
        self.status_callback: Optional[str] = payload.get("status_callback")
        self.status_callback_method: Optional[str] = payload.get(
            "status_callback_method"
        )
        self.max_duration: Optional[int] = deserialize.integer(
            payload.get("max_duration")
        )

        self._solution = {
            "sid": sid or self.sid,
        }
        self._context: Optional[MediaProcessorContext] = None

    @property
    def _proxy(self) -> "MediaProcessorContext":
        """
        Generate an instance context for the instance, the context is capable of
        performing various actions. All instance actions are proxied to the context

        :returns: MediaProcessorContext for this MediaProcessorInstance
        """
        if self._context is None:
            self._context = MediaProcessorContext(
                self._version,
                sid=self._solution["sid"],
            )
        return self._context

    def fetch(self) -> "MediaProcessorInstance":
        """
        Fetch the MediaProcessorInstance


        :returns: The fetched MediaProcessorInstance
        """
        return self._proxy.fetch()

    async def fetch_async(self) -> "MediaProcessorInstance":
        """
        Asynchronous coroutine to fetch the MediaProcessorInstance


        :returns: The fetched MediaProcessorInstance
        """
        return await self._proxy.fetch_async()

    def update(
        self, status: "MediaProcessorInstance.UpdateStatus"
    ) -> "MediaProcessorInstance":
        """
        Update the MediaProcessorInstance

        :param status:

        :returns: The updated MediaProcessorInstance
        """
        return self._proxy.update(
            status=status,
        )

    async def update_async(
        self, status: "MediaProcessorInstance.UpdateStatus"
    ) -> "MediaProcessorInstance":
        """
        Asynchronous coroutine to update the MediaProcessorInstance

        :param status:

        :returns: The updated MediaProcessorInstance
        """
        return await self._proxy.update_async(
            status=status,
        )

    def __repr__(self) -> str:
        """
        Provide a friendly representation

        :returns: Machine friendly representation
        """
        context = " ".join("{}={}".format(k, v) for k, v in self._solution.items())
        return "<Twilio.Media.V1.MediaProcessorInstance {}>".format(context)


class MediaProcessorContext(InstanceContext):

    def __init__(self, version: Version, sid: str):
        """
        Initialize the MediaProcessorContext

        :param version: Version that contains the resource
        :param sid: The SID of the MediaProcessor resource to update.
        """
        super().__init__(version)

        # Path Solution
        self._solution = {
            "sid": sid,
        }
        self._uri = "/MediaProcessors/{sid}".format(**self._solution)

    def fetch(self) -> MediaProcessorInstance:
        """
        Fetch the MediaProcessorInstance


        :returns: The fetched MediaProcessorInstance
        """

        payload = self._version.fetch(
            method="GET",
            uri=self._uri,
        )

        return MediaProcessorInstance(
            self._version,
            payload,
            sid=self._solution["sid"],
        )

    async def fetch_async(self) -> MediaProcessorInstance:
        """
        Asynchronous coroutine to fetch the MediaProcessorInstance


        :returns: The fetched MediaProcessorInstance
        """

        payload = await self._version.fetch_async(
            method="GET",
            uri=self._uri,
        )

        return MediaProcessorInstance(
            self._version,
            payload,
            sid=self._solution["sid"],
        )

    def update(
        self, status: "MediaProcessorInstance.UpdateStatus"
    ) -> MediaProcessorInstance:
        """
        Update the MediaProcessorInstance

        :param status:

        :returns: The updated MediaProcessorInstance
        """
        data = values.of(
            {
                "Status": status,
            }
        )

        payload = self._version.update(
            method="POST",
            uri=self._uri,
            data=data,
        )

        return MediaProcessorInstance(self._version, payload, sid=self._solution["sid"])

    async def update_async(
        self, status: "MediaProcessorInstance.UpdateStatus"
    ) -> MediaProcessorInstance:
        """
        Asynchronous coroutine to update the MediaProcessorInstance

        :param status:

        :returns: The updated MediaProcessorInstance
        """
        data = values.of(
            {
                "Status": status,
            }
        )

        payload = await self._version.update_async(
            method="POST",
            uri=self._uri,
            data=data,
        )

        return MediaProcessorInstance(self._version, payload, sid=self._solution["sid"])

    def __repr__(self) -> str:
        """
        Provide a friendly representation

        :returns: Machine friendly representation
        """
        context = " ".join("{}={}".format(k, v) for k, v in self._solution.items())
        return "<Twilio.Media.V1.MediaProcessorContext {}>".format(context)


class MediaProcessorPage(Page):

    def get_instance(self, payload: Dict[str, Any]) -> MediaProcessorInstance:
        """
        Build an instance of MediaProcessorInstance

        :param payload: Payload response from the API
        """
        return MediaProcessorInstance(self._version, payload)

    def __repr__(self) -> str:
        """
        Provide a friendly representation

        :returns: Machine friendly representation
        """
        return "<Twilio.Media.V1.MediaProcessorPage>"


class MediaProcessorList(ListResource):

    def __init__(self, version: Version):
        """
        Initialize the MediaProcessorList

        :param version: Version that contains the resource

        """
        super().__init__(version)

        self._uri = "/MediaProcessors"

    def create(
        self,
        extension: str,
        extension_context: str,
        extension_environment: Union[object, object] = values.unset,
        status_callback: Union[str, object] = values.unset,
        status_callback_method: Union[str, object] = values.unset,
        max_duration: Union[int, object] = values.unset,
    ) -> MediaProcessorInstance:
        """
        Create the MediaProcessorInstance

        :param extension: The [Media Extension](/docs/live/media-extensions-overview) name or URL. Ex: `video-composer-v2`
        :param extension_context: The context of the Media Extension, represented as a JSON dictionary. See the documentation for the specific [Media Extension](/docs/live/media-extensions-overview) you are using for more information about the context to send.
        :param extension_environment: User-defined environment variables for the Media Extension, represented as a JSON dictionary of key/value strings. See the documentation for the specific [Media Extension](/docs/live/media-extensions-overview) you are using for more information about whether you need to provide this.
        :param status_callback: The URL to which Twilio will send asynchronous webhook requests for every MediaProcessor event. See [Status Callbacks](/docs/live/api/status-callbacks) for details.
        :param status_callback_method: The HTTP method Twilio should use to call the `status_callback` URL. Can be `POST` or `GET` and the default is `POST`.
        :param max_duration: The maximum time, in seconds, that the MediaProcessor can run before automatically ends. The default value is 300 seconds, and the maximum value is 90000 seconds. Once this maximum duration is reached, Twilio will end the MediaProcessor, regardless of whether media is still streaming.

        :returns: The created MediaProcessorInstance
        """

        data = values.of(
            {
                "Extension": extension,
                "ExtensionContext": extension_context,
                "ExtensionEnvironment": serialize.object(extension_environment),
                "StatusCallback": status_callback,
                "StatusCallbackMethod": status_callback_method,
                "MaxDuration": max_duration,
            }
        )

        payload = self._version.create(
            method="POST",
            uri=self._uri,
            data=data,
        )

        return MediaProcessorInstance(self._version, payload)

    async def create_async(
        self,
        extension: str,
        extension_context: str,
        extension_environment: Union[object, object] = values.unset,
        status_callback: Union[str, object] = values.unset,
        status_callback_method: Union[str, object] = values.unset,
        max_duration: Union[int, object] = values.unset,
    ) -> MediaProcessorInstance:
        """
        Asynchronously create the MediaProcessorInstance

        :param extension: The [Media Extension](/docs/live/media-extensions-overview) name or URL. Ex: `video-composer-v2`
        :param extension_context: The context of the Media Extension, represented as a JSON dictionary. See the documentation for the specific [Media Extension](/docs/live/media-extensions-overview) you are using for more information about the context to send.
        :param extension_environment: User-defined environment variables for the Media Extension, represented as a JSON dictionary of key/value strings. See the documentation for the specific [Media Extension](/docs/live/media-extensions-overview) you are using for more information about whether you need to provide this.
        :param status_callback: The URL to which Twilio will send asynchronous webhook requests for every MediaProcessor event. See [Status Callbacks](/docs/live/api/status-callbacks) for details.
        :param status_callback_method: The HTTP method Twilio should use to call the `status_callback` URL. Can be `POST` or `GET` and the default is `POST`.
        :param max_duration: The maximum time, in seconds, that the MediaProcessor can run before automatically ends. The default value is 300 seconds, and the maximum value is 90000 seconds. Once this maximum duration is reached, Twilio will end the MediaProcessor, regardless of whether media is still streaming.

        :returns: The created MediaProcessorInstance
        """

        data = values.of(
            {
                "Extension": extension,
                "ExtensionContext": extension_context,
                "ExtensionEnvironment": serialize.object(extension_environment),
                "StatusCallback": status_callback,
                "StatusCallbackMethod": status_callback_method,
                "MaxDuration": max_duration,
            }
        )

        payload = await self._version.create_async(
            method="POST",
            uri=self._uri,
            data=data,
        )

        return MediaProcessorInstance(self._version, payload)

    def stream(
        self,
        order: Union["MediaProcessorInstance.Order", object] = values.unset,
        status: Union["MediaProcessorInstance.Status", object] = values.unset,
        limit: Optional[int] = None,
        page_size: Optional[int] = None,
    ) -> Iterator[MediaProcessorInstance]:
        """
        Streams MediaProcessorInstance records from the API as a generator stream.
        This operation lazily loads records as efficiently as possible until the limit
        is reached.
        The results are returned as a generator, so this operation is memory efficient.

        :param &quot;MediaProcessorInstance.Order&quot; order: The sort order of the list by `date_created`. Can be: `asc` (ascending) or `desc` (descending) with `desc` as the default.
        :param &quot;MediaProcessorInstance.Status&quot; status: Status to filter by, with possible values `started`, `ended` or `failed`.
        :param limit: Upper limit for the number of records to return. stream()
                      guarantees to never return more than limit.  Default is no limit
        :param page_size: Number of records to fetch per request, when not set will use
                          the default value of 50 records.  If no page_size is defined
                          but a limit is defined, stream() will attempt to read the
                          limit with the most efficient page size, i.e. min(limit, 1000)

        :returns: Generator that will yield up to limit results
        """
        limits = self._version.read_limits(limit, page_size)
        page = self.page(order=order, status=status, page_size=limits["page_size"])

        return self._version.stream(page, limits["limit"])

    async def stream_async(
        self,
        order: Union["MediaProcessorInstance.Order", object] = values.unset,
        status: Union["MediaProcessorInstance.Status", object] = values.unset,
        limit: Optional[int] = None,
        page_size: Optional[int] = None,
    ) -> AsyncIterator[MediaProcessorInstance]:
        """
        Asynchronously streams MediaProcessorInstance records from the API as a generator stream.
        This operation lazily loads records as efficiently as possible until the limit
        is reached.
        The results are returned as a generator, so this operation is memory efficient.

        :param &quot;MediaProcessorInstance.Order&quot; order: The sort order of the list by `date_created`. Can be: `asc` (ascending) or `desc` (descending) with `desc` as the default.
        :param &quot;MediaProcessorInstance.Status&quot; status: Status to filter by, with possible values `started`, `ended` or `failed`.
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
            order=order, status=status, page_size=limits["page_size"]
        )

        return self._version.stream_async(page, limits["limit"])

    def list(
        self,
        order: Union["MediaProcessorInstance.Order", object] = values.unset,
        status: Union["MediaProcessorInstance.Status", object] = values.unset,
        limit: Optional[int] = None,
        page_size: Optional[int] = None,
    ) -> List[MediaProcessorInstance]:
        """
        Lists MediaProcessorInstance records from the API as a list.
        Unlike stream(), this operation is eager and will load `limit` records into
        memory before returning.

        :param &quot;MediaProcessorInstance.Order&quot; order: The sort order of the list by `date_created`. Can be: `asc` (ascending) or `desc` (descending) with `desc` as the default.
        :param &quot;MediaProcessorInstance.Status&quot; status: Status to filter by, with possible values `started`, `ended` or `failed`.
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
                order=order,
                status=status,
                limit=limit,
                page_size=page_size,
            )
        )

    async def list_async(
        self,
        order: Union["MediaProcessorInstance.Order", object] = values.unset,
        status: Union["MediaProcessorInstance.Status", object] = values.unset,
        limit: Optional[int] = None,
        page_size: Optional[int] = None,
    ) -> List[MediaProcessorInstance]:
        """
        Asynchronously lists MediaProcessorInstance records from the API as a list.
        Unlike stream(), this operation is eager and will load `limit` records into
        memory before returning.

        :param &quot;MediaProcessorInstance.Order&quot; order: The sort order of the list by `date_created`. Can be: `asc` (ascending) or `desc` (descending) with `desc` as the default.
        :param &quot;MediaProcessorInstance.Status&quot; status: Status to filter by, with possible values `started`, `ended` or `failed`.
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
                order=order,
                status=status,
                limit=limit,
                page_size=page_size,
            )
        ]

    def page(
        self,
        order: Union["MediaProcessorInstance.Order", object] = values.unset,
        status: Union["MediaProcessorInstance.Status", object] = values.unset,
        page_token: Union[str, object] = values.unset,
        page_number: Union[int, object] = values.unset,
        page_size: Union[int, object] = values.unset,
    ) -> MediaProcessorPage:
        """
        Retrieve a single page of MediaProcessorInstance records from the API.
        Request is executed immediately

        :param order: The sort order of the list by `date_created`. Can be: `asc` (ascending) or `desc` (descending) with `desc` as the default.
        :param status: Status to filter by, with possible values `started`, `ended` or `failed`.
        :param page_token: PageToken provided by the API
        :param page_number: Page Number, this value is simply for client state
        :param page_size: Number of records to return, defaults to 50

        :returns: Page of MediaProcessorInstance
        """
        data = values.of(
            {
                "Order": order,
                "Status": status,
                "PageToken": page_token,
                "Page": page_number,
                "PageSize": page_size,
            }
        )

        response = self._version.page(method="GET", uri=self._uri, params=data)
        return MediaProcessorPage(self._version, response)

    async def page_async(
        self,
        order: Union["MediaProcessorInstance.Order", object] = values.unset,
        status: Union["MediaProcessorInstance.Status", object] = values.unset,
        page_token: Union[str, object] = values.unset,
        page_number: Union[int, object] = values.unset,
        page_size: Union[int, object] = values.unset,
    ) -> MediaProcessorPage:
        """
        Asynchronously retrieve a single page of MediaProcessorInstance records from the API.
        Request is executed immediately

        :param order: The sort order of the list by `date_created`. Can be: `asc` (ascending) or `desc` (descending) with `desc` as the default.
        :param status: Status to filter by, with possible values `started`, `ended` or `failed`.
        :param page_token: PageToken provided by the API
        :param page_number: Page Number, this value is simply for client state
        :param page_size: Number of records to return, defaults to 50

        :returns: Page of MediaProcessorInstance
        """
        data = values.of(
            {
                "Order": order,
                "Status": status,
                "PageToken": page_token,
                "Page": page_number,
                "PageSize": page_size,
            }
        )

        response = await self._version.page_async(
            method="GET", uri=self._uri, params=data
        )
        return MediaProcessorPage(self._version, response)

    def get_page(self, target_url: str) -> MediaProcessorPage:
        """
        Retrieve a specific page of MediaProcessorInstance records from the API.
        Request is executed immediately

        :param target_url: API-generated URL for the requested results page

        :returns: Page of MediaProcessorInstance
        """
        response = self._version.domain.twilio.request("GET", target_url)
        return MediaProcessorPage(self._version, response)

    async def get_page_async(self, target_url: str) -> MediaProcessorPage:
        """
        Asynchronously retrieve a specific page of MediaProcessorInstance records from the API.
        Request is executed immediately

        :param target_url: API-generated URL for the requested results page

        :returns: Page of MediaProcessorInstance
        """
        response = await self._version.domain.twilio.request_async("GET", target_url)
        return MediaProcessorPage(self._version, response)

    def get(self, sid: str) -> MediaProcessorContext:
        """
        Constructs a MediaProcessorContext

        :param sid: The SID of the MediaProcessor resource to update.
        """
        return MediaProcessorContext(self._version, sid=sid)

    def __call__(self, sid: str) -> MediaProcessorContext:
        """
        Constructs a MediaProcessorContext

        :param sid: The SID of the MediaProcessor resource to update.
        """
        return MediaProcessorContext(self._version, sid=sid)

    def __repr__(self) -> str:
        """
        Provide a friendly representation

        :returns: Machine friendly representation
        """
        return "<Twilio.Media.V1.MediaProcessorList>"