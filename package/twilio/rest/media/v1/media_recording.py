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
from twilio.base import deserialize, values
from twilio.base.instance_context import InstanceContext
from twilio.base.instance_resource import InstanceResource
from twilio.base.list_resource import ListResource
from twilio.base.version import Version
from twilio.base.page import Page


class MediaRecordingInstance(InstanceResource):

    class Format(object):
        MP4 = "mp4"
        WEBM = "webm"

    class Order(object):
        ASC = "asc"
        DESC = "desc"

    class Status(object):
        PROCESSING = "processing"
        COMPLETED = "completed"
        DELETED = "deleted"
        FAILED = "failed"

    """
    :ivar account_sid: The SID of the [Account](https://www.twilio.com/docs/iam/api/account) that created the MediaRecording resource.
    :ivar date_created: The date and time in GMT when the resource was created specified in [ISO 8601](https://en.wikipedia.org/wiki/ISO_8601) format.
    :ivar date_updated: The date and time in GMT when the resource was last updated specified in [ISO 8601](https://en.wikipedia.org/wiki/ISO_8601) format.
    :ivar duration: The duration of the MediaRecording in seconds.
    :ivar format: 
    :ivar links: The URLs of related resources.
    :ivar processor_sid: The SID of the MediaProcessor resource which produced the MediaRecording.
    :ivar resolution: The dimensions of the video image in pixels expressed as columns (width) and rows (height).
    :ivar source_sid: The SID of the resource that generated the original media track(s) of the MediaRecording.
    :ivar sid: The unique string generated to identify the MediaRecording resource.
    :ivar media_size: The size of the recording media in bytes.
    :ivar status: 
    :ivar status_callback: The URL to which Twilio will send asynchronous webhook requests for every MediaRecording event. See [Status Callbacks](/docs/live/api/status-callbacks) for more details.
    :ivar status_callback_method: The HTTP method Twilio should use to call the `status_callback` URL. Can be `POST` or `GET` and the default is `POST`.
    :ivar url: The absolute URL of the resource.
    """

    def __init__(
        self, version: Version, payload: Dict[str, Any], sid: Optional[str] = None
    ):
        super().__init__(version)

        self.account_sid: Optional[str] = payload.get("account_sid")
        self.date_created: Optional[datetime] = deserialize.iso8601_datetime(
            payload.get("date_created")
        )
        self.date_updated: Optional[datetime] = deserialize.iso8601_datetime(
            payload.get("date_updated")
        )
        self.duration: Optional[int] = deserialize.integer(payload.get("duration"))
        self.format: Optional["MediaRecordingInstance.Format"] = payload.get("format")
        self.links: Optional[Dict[str, object]] = payload.get("links")
        self.processor_sid: Optional[str] = payload.get("processor_sid")
        self.resolution: Optional[str] = payload.get("resolution")
        self.source_sid: Optional[str] = payload.get("source_sid")
        self.sid: Optional[str] = payload.get("sid")
        self.media_size: Optional[int] = payload.get("media_size")
        self.status: Optional["MediaRecordingInstance.Status"] = payload.get("status")
        self.status_callback: Optional[str] = payload.get("status_callback")
        self.status_callback_method: Optional[str] = payload.get(
            "status_callback_method"
        )
        self.url: Optional[str] = payload.get("url")

        self._solution = {
            "sid": sid or self.sid,
        }
        self._context: Optional[MediaRecordingContext] = None

    @property
    def _proxy(self) -> "MediaRecordingContext":
        """
        Generate an instance context for the instance, the context is capable of
        performing various actions. All instance actions are proxied to the context

        :returns: MediaRecordingContext for this MediaRecordingInstance
        """
        if self._context is None:
            self._context = MediaRecordingContext(
                self._version,
                sid=self._solution["sid"],
            )
        return self._context

    def delete(self) -> bool:
        """
        Deletes the MediaRecordingInstance


        :returns: True if delete succeeds, False otherwise
        """
        return self._proxy.delete()

    async def delete_async(self) -> bool:
        """
        Asynchronous coroutine that deletes the MediaRecordingInstance


        :returns: True if delete succeeds, False otherwise
        """
        return await self._proxy.delete_async()

    def fetch(self) -> "MediaRecordingInstance":
        """
        Fetch the MediaRecordingInstance


        :returns: The fetched MediaRecordingInstance
        """
        return self._proxy.fetch()

    async def fetch_async(self) -> "MediaRecordingInstance":
        """
        Asynchronous coroutine to fetch the MediaRecordingInstance


        :returns: The fetched MediaRecordingInstance
        """
        return await self._proxy.fetch_async()

    def __repr__(self) -> str:
        """
        Provide a friendly representation

        :returns: Machine friendly representation
        """
        context = " ".join("{}={}".format(k, v) for k, v in self._solution.items())
        return "<Twilio.Media.V1.MediaRecordingInstance {}>".format(context)


class MediaRecordingContext(InstanceContext):

    def __init__(self, version: Version, sid: str):
        """
        Initialize the MediaRecordingContext

        :param version: Version that contains the resource
        :param sid: The SID of the MediaRecording resource to fetch.
        """
        super().__init__(version)

        # Path Solution
        self._solution = {
            "sid": sid,
        }
        self._uri = "/MediaRecordings/{sid}".format(**self._solution)

    def delete(self) -> bool:
        """
        Deletes the MediaRecordingInstance


        :returns: True if delete succeeds, False otherwise
        """
        return self._version.delete(
            method="DELETE",
            uri=self._uri,
        )

    async def delete_async(self) -> bool:
        """
        Asynchronous coroutine that deletes the MediaRecordingInstance


        :returns: True if delete succeeds, False otherwise
        """
        return await self._version.delete_async(
            method="DELETE",
            uri=self._uri,
        )

    def fetch(self) -> MediaRecordingInstance:
        """
        Fetch the MediaRecordingInstance


        :returns: The fetched MediaRecordingInstance
        """

        payload = self._version.fetch(
            method="GET",
            uri=self._uri,
        )

        return MediaRecordingInstance(
            self._version,
            payload,
            sid=self._solution["sid"],
        )

    async def fetch_async(self) -> MediaRecordingInstance:
        """
        Asynchronous coroutine to fetch the MediaRecordingInstance


        :returns: The fetched MediaRecordingInstance
        """

        payload = await self._version.fetch_async(
            method="GET",
            uri=self._uri,
        )

        return MediaRecordingInstance(
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
        return "<Twilio.Media.V1.MediaRecordingContext {}>".format(context)


class MediaRecordingPage(Page):

    def get_instance(self, payload: Dict[str, Any]) -> MediaRecordingInstance:
        """
        Build an instance of MediaRecordingInstance

        :param payload: Payload response from the API
        """
        return MediaRecordingInstance(self._version, payload)

    def __repr__(self) -> str:
        """
        Provide a friendly representation

        :returns: Machine friendly representation
        """
        return "<Twilio.Media.V1.MediaRecordingPage>"


class MediaRecordingList(ListResource):

    def __init__(self, version: Version):
        """
        Initialize the MediaRecordingList

        :param version: Version that contains the resource

        """
        super().__init__(version)

        self._uri = "/MediaRecordings"

    def stream(
        self,
        order: Union["MediaRecordingInstance.Order", object] = values.unset,
        status: Union["MediaRecordingInstance.Status", object] = values.unset,
        processor_sid: Union[str, object] = values.unset,
        source_sid: Union[str, object] = values.unset,
        limit: Optional[int] = None,
        page_size: Optional[int] = None,
    ) -> Iterator[MediaRecordingInstance]:
        """
        Streams MediaRecordingInstance records from the API as a generator stream.
        This operation lazily loads records as efficiently as possible until the limit
        is reached.
        The results are returned as a generator, so this operation is memory efficient.

        :param &quot;MediaRecordingInstance.Order&quot; order: The sort order of the list by `date_created`. Can be: `asc` (ascending) or `desc` (descending) with `desc` as the default.
        :param &quot;MediaRecordingInstance.Status&quot; status: Status to filter by, with possible values `processing`, `completed`, `deleted`, or `failed`.
        :param str processor_sid: SID of a MediaProcessor to filter by.
        :param str source_sid: SID of a MediaRecording source to filter by.
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
            order=order,
            status=status,
            processor_sid=processor_sid,
            source_sid=source_sid,
            page_size=limits["page_size"],
        )

        return self._version.stream(page, limits["limit"])

    async def stream_async(
        self,
        order: Union["MediaRecordingInstance.Order", object] = values.unset,
        status: Union["MediaRecordingInstance.Status", object] = values.unset,
        processor_sid: Union[str, object] = values.unset,
        source_sid: Union[str, object] = values.unset,
        limit: Optional[int] = None,
        page_size: Optional[int] = None,
    ) -> AsyncIterator[MediaRecordingInstance]:
        """
        Asynchronously streams MediaRecordingInstance records from the API as a generator stream.
        This operation lazily loads records as efficiently as possible until the limit
        is reached.
        The results are returned as a generator, so this operation is memory efficient.

        :param &quot;MediaRecordingInstance.Order&quot; order: The sort order of the list by `date_created`. Can be: `asc` (ascending) or `desc` (descending) with `desc` as the default.
        :param &quot;MediaRecordingInstance.Status&quot; status: Status to filter by, with possible values `processing`, `completed`, `deleted`, or `failed`.
        :param str processor_sid: SID of a MediaProcessor to filter by.
        :param str source_sid: SID of a MediaRecording source to filter by.
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
            order=order,
            status=status,
            processor_sid=processor_sid,
            source_sid=source_sid,
            page_size=limits["page_size"],
        )

        return self._version.stream_async(page, limits["limit"])

    def list(
        self,
        order: Union["MediaRecordingInstance.Order", object] = values.unset,
        status: Union["MediaRecordingInstance.Status", object] = values.unset,
        processor_sid: Union[str, object] = values.unset,
        source_sid: Union[str, object] = values.unset,
        limit: Optional[int] = None,
        page_size: Optional[int] = None,
    ) -> List[MediaRecordingInstance]:
        """
        Lists MediaRecordingInstance records from the API as a list.
        Unlike stream(), this operation is eager and will load `limit` records into
        memory before returning.

        :param &quot;MediaRecordingInstance.Order&quot; order: The sort order of the list by `date_created`. Can be: `asc` (ascending) or `desc` (descending) with `desc` as the default.
        :param &quot;MediaRecordingInstance.Status&quot; status: Status to filter by, with possible values `processing`, `completed`, `deleted`, or `failed`.
        :param str processor_sid: SID of a MediaProcessor to filter by.
        :param str source_sid: SID of a MediaRecording source to filter by.
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
                processor_sid=processor_sid,
                source_sid=source_sid,
                limit=limit,
                page_size=page_size,
            )
        )

    async def list_async(
        self,
        order: Union["MediaRecordingInstance.Order", object] = values.unset,
        status: Union["MediaRecordingInstance.Status", object] = values.unset,
        processor_sid: Union[str, object] = values.unset,
        source_sid: Union[str, object] = values.unset,
        limit: Optional[int] = None,
        page_size: Optional[int] = None,
    ) -> List[MediaRecordingInstance]:
        """
        Asynchronously lists MediaRecordingInstance records from the API as a list.
        Unlike stream(), this operation is eager and will load `limit` records into
        memory before returning.

        :param &quot;MediaRecordingInstance.Order&quot; order: The sort order of the list by `date_created`. Can be: `asc` (ascending) or `desc` (descending) with `desc` as the default.
        :param &quot;MediaRecordingInstance.Status&quot; status: Status to filter by, with possible values `processing`, `completed`, `deleted`, or `failed`.
        :param str processor_sid: SID of a MediaProcessor to filter by.
        :param str source_sid: SID of a MediaRecording source to filter by.
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
                processor_sid=processor_sid,
                source_sid=source_sid,
                limit=limit,
                page_size=page_size,
            )
        ]

    def page(
        self,
        order: Union["MediaRecordingInstance.Order", object] = values.unset,
        status: Union["MediaRecordingInstance.Status", object] = values.unset,
        processor_sid: Union[str, object] = values.unset,
        source_sid: Union[str, object] = values.unset,
        page_token: Union[str, object] = values.unset,
        page_number: Union[int, object] = values.unset,
        page_size: Union[int, object] = values.unset,
    ) -> MediaRecordingPage:
        """
        Retrieve a single page of MediaRecordingInstance records from the API.
        Request is executed immediately

        :param order: The sort order of the list by `date_created`. Can be: `asc` (ascending) or `desc` (descending) with `desc` as the default.
        :param status: Status to filter by, with possible values `processing`, `completed`, `deleted`, or `failed`.
        :param processor_sid: SID of a MediaProcessor to filter by.
        :param source_sid: SID of a MediaRecording source to filter by.
        :param page_token: PageToken provided by the API
        :param page_number: Page Number, this value is simply for client state
        :param page_size: Number of records to return, defaults to 50

        :returns: Page of MediaRecordingInstance
        """
        data = values.of(
            {
                "Order": order,
                "Status": status,
                "ProcessorSid": processor_sid,
                "SourceSid": source_sid,
                "PageToken": page_token,
                "Page": page_number,
                "PageSize": page_size,
            }
        )

        response = self._version.page(method="GET", uri=self._uri, params=data)
        return MediaRecordingPage(self._version, response)

    async def page_async(
        self,
        order: Union["MediaRecordingInstance.Order", object] = values.unset,
        status: Union["MediaRecordingInstance.Status", object] = values.unset,
        processor_sid: Union[str, object] = values.unset,
        source_sid: Union[str, object] = values.unset,
        page_token: Union[str, object] = values.unset,
        page_number: Union[int, object] = values.unset,
        page_size: Union[int, object] = values.unset,
    ) -> MediaRecordingPage:
        """
        Asynchronously retrieve a single page of MediaRecordingInstance records from the API.
        Request is executed immediately

        :param order: The sort order of the list by `date_created`. Can be: `asc` (ascending) or `desc` (descending) with `desc` as the default.
        :param status: Status to filter by, with possible values `processing`, `completed`, `deleted`, or `failed`.
        :param processor_sid: SID of a MediaProcessor to filter by.
        :param source_sid: SID of a MediaRecording source to filter by.
        :param page_token: PageToken provided by the API
        :param page_number: Page Number, this value is simply for client state
        :param page_size: Number of records to return, defaults to 50

        :returns: Page of MediaRecordingInstance
        """
        data = values.of(
            {
                "Order": order,
                "Status": status,
                "ProcessorSid": processor_sid,
                "SourceSid": source_sid,
                "PageToken": page_token,
                "Page": page_number,
                "PageSize": page_size,
            }
        )

        response = await self._version.page_async(
            method="GET", uri=self._uri, params=data
        )
        return MediaRecordingPage(self._version, response)

    def get_page(self, target_url: str) -> MediaRecordingPage:
        """
        Retrieve a specific page of MediaRecordingInstance records from the API.
        Request is executed immediately

        :param target_url: API-generated URL for the requested results page

        :returns: Page of MediaRecordingInstance
        """
        response = self._version.domain.twilio.request("GET", target_url)
        return MediaRecordingPage(self._version, response)

    async def get_page_async(self, target_url: str) -> MediaRecordingPage:
        """
        Asynchronously retrieve a specific page of MediaRecordingInstance records from the API.
        Request is executed immediately

        :param target_url: API-generated URL for the requested results page

        :returns: Page of MediaRecordingInstance
        """
        response = await self._version.domain.twilio.request_async("GET", target_url)
        return MediaRecordingPage(self._version, response)

    def get(self, sid: str) -> MediaRecordingContext:
        """
        Constructs a MediaRecordingContext

        :param sid: The SID of the MediaRecording resource to fetch.
        """
        return MediaRecordingContext(self._version, sid=sid)

    def __call__(self, sid: str) -> MediaRecordingContext:
        """
        Constructs a MediaRecordingContext

        :param sid: The SID of the MediaRecording resource to fetch.
        """
        return MediaRecordingContext(self._version, sid=sid)

    def __repr__(self) -> str:
        """
        Provide a friendly representation

        :returns: Machine friendly representation
        """
        return "<Twilio.Media.V1.MediaRecordingList>"
