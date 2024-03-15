r"""
    This code was generated by
   ___ _ _ _ _ _    _ ____    ____ ____ _    ____ ____ _  _ ____ ____ ____ ___ __   __
    |  | | | | |    | |  | __ |  | |__| | __ | __ |___ |\ | |___ |__/ |__|  | |  | |__/
    |  |_|_| | |___ | |__|    |__| |  | |    |__] |___ | \| |___ |  \ |  |  | |__| |  \

    Twilio - Trunking
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


class PhoneNumberInstance(InstanceResource):

    class AddressRequirement(object):
        NONE = "none"
        ANY = "any"
        LOCAL = "local"
        FOREIGN = "foreign"

    """
    :ivar account_sid: The SID of the [Account](https://www.twilio.com/docs/iam/api/account) that created the PhoneNumber resource.
    :ivar address_requirements: 
    :ivar api_version: The API version used to start a new TwiML session.
    :ivar beta: Whether the phone number is new to the Twilio platform. Can be: `true` or `false`.
    :ivar capabilities: The set of Boolean properties that indicate whether a phone number can receive calls or messages.  Capabilities are  `Voice`, `SMS`, and `MMS` and each capability can be: `true` or `false`.
    :ivar date_created: The date and time in GMT when the resource was created specified in [RFC 2822](https://www.ietf.org/rfc/rfc2822.txt) format.
    :ivar date_updated: The date and time in GMT when the resource was last updated specified in [RFC 2822](https://www.ietf.org/rfc/rfc2822.txt) format.
    :ivar friendly_name: The string that you assigned to describe the resource.
    :ivar links: The URLs of related resources.
    :ivar phone_number: The phone number in [E.164](https://www.twilio.com/docs/glossary/what-e164) format, which consists of a + followed by the country code and subscriber number.
    :ivar sid: The unique string that we created to identify the PhoneNumber resource.
    :ivar sms_application_sid: The SID of the application that handles SMS messages sent to the phone number. If an `sms_application_sid` is present, we ignore all `sms_*_url` values and use those of the application.
    :ivar sms_fallback_method: The HTTP method we use to call `sms_fallback_url`. Can be: `GET` or `POST`.
    :ivar sms_fallback_url: The URL that we call using the `sms_fallback_method` when an error occurs while retrieving or executing the TwiML from `sms_url`.
    :ivar sms_method: The HTTP method we use to call `sms_url`. Can be: `GET` or `POST`.
    :ivar sms_url: The URL we call using the `sms_method` when the phone number receives an incoming SMS message.
    :ivar status_callback: The URL we call using the `status_callback_method` to send status information to your application.
    :ivar status_callback_method: The HTTP method we use to call `status_callback`. Can be: `GET` or `POST`.
    :ivar trunk_sid: The SID of the Trunk that handles calls to the phone number. If a `trunk_sid` is present, we ignore all of the voice URLs and voice applications and use those set on the Trunk. Setting a `trunk_sid` will automatically delete your `voice_application_sid` and vice versa.
    :ivar url: The absolute URL of the resource.
    :ivar voice_application_sid: The SID of the application that handles calls to the phone number. If a `voice_application_sid` is present, we ignore all of the voice URLs and use those set on the application. Setting a `voice_application_sid` will automatically delete your `trunk_sid` and vice versa.
    :ivar voice_caller_id_lookup: Whether we look up the caller's caller-ID name from the CNAM database ($0.01 per look up). Can be: `true` or `false`.
    :ivar voice_fallback_method: The HTTP method that we use to call `voice_fallback_url`. Can be: `GET` or `POST`.
    :ivar voice_fallback_url: The URL that we call using the `voice_fallback_method` when an error occurs retrieving or executing the TwiML requested by `url`.
    :ivar voice_method: The HTTP method we use to call `voice_url`. Can be: `GET` or `POST`.
    :ivar voice_url: The URL we call using the `voice_method` when the phone number receives a call. The `voice_url` is not be used if a `voice_application_sid` or a `trunk_sid` is set.
    """

    def __init__(
        self,
        version: Version,
        payload: Dict[str, Any],
        trunk_sid: str,
        sid: Optional[str] = None,
    ):
        super().__init__(version)

        self.account_sid: Optional[str] = payload.get("account_sid")
        self.address_requirements: Optional[
            "PhoneNumberInstance.AddressRequirement"
        ] = payload.get("address_requirements")
        self.api_version: Optional[str] = payload.get("api_version")
        self.beta: Optional[bool] = payload.get("beta")
        self.capabilities: Optional[Dict[str, object]] = payload.get("capabilities")
        self.date_created: Optional[datetime] = deserialize.iso8601_datetime(
            payload.get("date_created")
        )
        self.date_updated: Optional[datetime] = deserialize.iso8601_datetime(
            payload.get("date_updated")
        )
        self.friendly_name: Optional[str] = payload.get("friendly_name")
        self.links: Optional[Dict[str, object]] = payload.get("links")
        self.phone_number: Optional[str] = payload.get("phone_number")
        self.sid: Optional[str] = payload.get("sid")
        self.sms_application_sid: Optional[str] = payload.get("sms_application_sid")
        self.sms_fallback_method: Optional[str] = payload.get("sms_fallback_method")
        self.sms_fallback_url: Optional[str] = payload.get("sms_fallback_url")
        self.sms_method: Optional[str] = payload.get("sms_method")
        self.sms_url: Optional[str] = payload.get("sms_url")
        self.status_callback: Optional[str] = payload.get("status_callback")
        self.status_callback_method: Optional[str] = payload.get(
            "status_callback_method"
        )
        self.trunk_sid: Optional[str] = payload.get("trunk_sid")
        self.url: Optional[str] = payload.get("url")
        self.voice_application_sid: Optional[str] = payload.get("voice_application_sid")
        self.voice_caller_id_lookup: Optional[bool] = payload.get(
            "voice_caller_id_lookup"
        )
        self.voice_fallback_method: Optional[str] = payload.get("voice_fallback_method")
        self.voice_fallback_url: Optional[str] = payload.get("voice_fallback_url")
        self.voice_method: Optional[str] = payload.get("voice_method")
        self.voice_url: Optional[str] = payload.get("voice_url")

        self._solution = {
            "trunk_sid": trunk_sid,
            "sid": sid or self.sid,
        }
        self._context: Optional[PhoneNumberContext] = None

    @property
    def _proxy(self) -> "PhoneNumberContext":
        """
        Generate an instance context for the instance, the context is capable of
        performing various actions. All instance actions are proxied to the context

        :returns: PhoneNumberContext for this PhoneNumberInstance
        """
        if self._context is None:
            self._context = PhoneNumberContext(
                self._version,
                trunk_sid=self._solution["trunk_sid"],
                sid=self._solution["sid"],
            )
        return self._context

    def delete(self) -> bool:
        """
        Deletes the PhoneNumberInstance


        :returns: True if delete succeeds, False otherwise
        """
        return self._proxy.delete()

    async def delete_async(self) -> bool:
        """
        Asynchronous coroutine that deletes the PhoneNumberInstance


        :returns: True if delete succeeds, False otherwise
        """
        return await self._proxy.delete_async()

    def fetch(self) -> "PhoneNumberInstance":
        """
        Fetch the PhoneNumberInstance


        :returns: The fetched PhoneNumberInstance
        """
        return self._proxy.fetch()

    async def fetch_async(self) -> "PhoneNumberInstance":
        """
        Asynchronous coroutine to fetch the PhoneNumberInstance


        :returns: The fetched PhoneNumberInstance
        """
        return await self._proxy.fetch_async()

    def __repr__(self) -> str:
        """
        Provide a friendly representation

        :returns: Machine friendly representation
        """
        context = " ".join("{}={}".format(k, v) for k, v in self._solution.items())
        return "<Twilio.Trunking.V1.PhoneNumberInstance {}>".format(context)


class PhoneNumberContext(InstanceContext):

    def __init__(self, version: Version, trunk_sid: str, sid: str):
        """
        Initialize the PhoneNumberContext

        :param version: Version that contains the resource
        :param trunk_sid: The SID of the Trunk from which to fetch the PhoneNumber resource.
        :param sid: The unique string that we created to identify the PhoneNumber resource to fetch.
        """
        super().__init__(version)

        # Path Solution
        self._solution = {
            "trunk_sid": trunk_sid,
            "sid": sid,
        }
        self._uri = "/Trunks/{trunk_sid}/PhoneNumbers/{sid}".format(**self._solution)

    def delete(self) -> bool:
        """
        Deletes the PhoneNumberInstance


        :returns: True if delete succeeds, False otherwise
        """
        return self._version.delete(
            method="DELETE",
            uri=self._uri,
        )

    async def delete_async(self) -> bool:
        """
        Asynchronous coroutine that deletes the PhoneNumberInstance


        :returns: True if delete succeeds, False otherwise
        """
        return await self._version.delete_async(
            method="DELETE",
            uri=self._uri,
        )

    def fetch(self) -> PhoneNumberInstance:
        """
        Fetch the PhoneNumberInstance


        :returns: The fetched PhoneNumberInstance
        """

        payload = self._version.fetch(
            method="GET",
            uri=self._uri,
        )

        return PhoneNumberInstance(
            self._version,
            payload,
            trunk_sid=self._solution["trunk_sid"],
            sid=self._solution["sid"],
        )

    async def fetch_async(self) -> PhoneNumberInstance:
        """
        Asynchronous coroutine to fetch the PhoneNumberInstance


        :returns: The fetched PhoneNumberInstance
        """

        payload = await self._version.fetch_async(
            method="GET",
            uri=self._uri,
        )

        return PhoneNumberInstance(
            self._version,
            payload,
            trunk_sid=self._solution["trunk_sid"],
            sid=self._solution["sid"],
        )

    def __repr__(self) -> str:
        """
        Provide a friendly representation

        :returns: Machine friendly representation
        """
        context = " ".join("{}={}".format(k, v) for k, v in self._solution.items())
        return "<Twilio.Trunking.V1.PhoneNumberContext {}>".format(context)


class PhoneNumberPage(Page):

    def get_instance(self, payload: Dict[str, Any]) -> PhoneNumberInstance:
        """
        Build an instance of PhoneNumberInstance

        :param payload: Payload response from the API
        """
        return PhoneNumberInstance(
            self._version, payload, trunk_sid=self._solution["trunk_sid"]
        )

    def __repr__(self) -> str:
        """
        Provide a friendly representation

        :returns: Machine friendly representation
        """
        return "<Twilio.Trunking.V1.PhoneNumberPage>"


class PhoneNumberList(ListResource):

    def __init__(self, version: Version, trunk_sid: str):
        """
        Initialize the PhoneNumberList

        :param version: Version that contains the resource
        :param trunk_sid: The SID of the Trunk from which to read the PhoneNumber resources.

        """
        super().__init__(version)

        # Path Solution
        self._solution = {
            "trunk_sid": trunk_sid,
        }
        self._uri = "/Trunks/{trunk_sid}/PhoneNumbers".format(**self._solution)

    def create(self, phone_number_sid: str) -> PhoneNumberInstance:
        """
        Create the PhoneNumberInstance

        :param phone_number_sid: The SID of the [Incoming Phone Number](https://www.twilio.com/docs/phone-numbers/api/incomingphonenumber-resource) that you want to associate with the trunk.

        :returns: The created PhoneNumberInstance
        """

        data = values.of(
            {
                "PhoneNumberSid": phone_number_sid,
            }
        )

        payload = self._version.create(
            method="POST",
            uri=self._uri,
            data=data,
        )

        return PhoneNumberInstance(
            self._version, payload, trunk_sid=self._solution["trunk_sid"]
        )

    async def create_async(self, phone_number_sid: str) -> PhoneNumberInstance:
        """
        Asynchronously create the PhoneNumberInstance

        :param phone_number_sid: The SID of the [Incoming Phone Number](https://www.twilio.com/docs/phone-numbers/api/incomingphonenumber-resource) that you want to associate with the trunk.

        :returns: The created PhoneNumberInstance
        """

        data = values.of(
            {
                "PhoneNumberSid": phone_number_sid,
            }
        )

        payload = await self._version.create_async(
            method="POST",
            uri=self._uri,
            data=data,
        )

        return PhoneNumberInstance(
            self._version, payload, trunk_sid=self._solution["trunk_sid"]
        )

    def stream(
        self,
        limit: Optional[int] = None,
        page_size: Optional[int] = None,
    ) -> Iterator[PhoneNumberInstance]:
        """
        Streams PhoneNumberInstance records from the API as a generator stream.
        This operation lazily loads records as efficiently as possible until the limit
        is reached.
        The results are returned as a generator, so this operation is memory efficient.

        :param limit: Upper limit for the number of records to return. stream()
                      guarantees to never return more than limit.  Default is no limit
        :param page_size: Number of records to fetch per request, when not set will use
                          the default value of 50 records.  If no page_size is defined
                          but a limit is defined, stream() will attempt to read the
                          limit with the most efficient page size, i.e. min(limit, 1000)

        :returns: Generator that will yield up to limit results
        """
        limits = self._version.read_limits(limit, page_size)
        page = self.page(page_size=limits["page_size"])

        return self._version.stream(page, limits["limit"])

    async def stream_async(
        self,
        limit: Optional[int] = None,
        page_size: Optional[int] = None,
    ) -> AsyncIterator[PhoneNumberInstance]:
        """
        Asynchronously streams PhoneNumberInstance records from the API as a generator stream.
        This operation lazily loads records as efficiently as possible until the limit
        is reached.
        The results are returned as a generator, so this operation is memory efficient.

        :param limit: Upper limit for the number of records to return. stream()
                      guarantees to never return more than limit.  Default is no limit
        :param page_size: Number of records to fetch per request, when not set will use
                          the default value of 50 records.  If no page_size is defined
                          but a limit is defined, stream() will attempt to read the
                          limit with the most efficient page size, i.e. min(limit, 1000)

        :returns: Generator that will yield up to limit results
        """
        limits = self._version.read_limits(limit, page_size)
        page = await self.page_async(page_size=limits["page_size"])

        return self._version.stream_async(page, limits["limit"])

    def list(
        self,
        limit: Optional[int] = None,
        page_size: Optional[int] = None,
    ) -> List[PhoneNumberInstance]:
        """
        Lists PhoneNumberInstance records from the API as a list.
        Unlike stream(), this operation is eager and will load `limit` records into
        memory before returning.

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
                limit=limit,
                page_size=page_size,
            )
        )

    async def list_async(
        self,
        limit: Optional[int] = None,
        page_size: Optional[int] = None,
    ) -> List[PhoneNumberInstance]:
        """
        Asynchronously lists PhoneNumberInstance records from the API as a list.
        Unlike stream(), this operation is eager and will load `limit` records into
        memory before returning.

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
                limit=limit,
                page_size=page_size,
            )
        ]

    def page(
        self,
        page_token: Union[str, object] = values.unset,
        page_number: Union[int, object] = values.unset,
        page_size: Union[int, object] = values.unset,
    ) -> PhoneNumberPage:
        """
        Retrieve a single page of PhoneNumberInstance records from the API.
        Request is executed immediately

        :param page_token: PageToken provided by the API
        :param page_number: Page Number, this value is simply for client state
        :param page_size: Number of records to return, defaults to 50

        :returns: Page of PhoneNumberInstance
        """
        data = values.of(
            {
                "PageToken": page_token,
                "Page": page_number,
                "PageSize": page_size,
            }
        )

        response = self._version.page(method="GET", uri=self._uri, params=data)
        return PhoneNumberPage(self._version, response, self._solution)

    async def page_async(
        self,
        page_token: Union[str, object] = values.unset,
        page_number: Union[int, object] = values.unset,
        page_size: Union[int, object] = values.unset,
    ) -> PhoneNumberPage:
        """
        Asynchronously retrieve a single page of PhoneNumberInstance records from the API.
        Request is executed immediately

        :param page_token: PageToken provided by the API
        :param page_number: Page Number, this value is simply for client state
        :param page_size: Number of records to return, defaults to 50

        :returns: Page of PhoneNumberInstance
        """
        data = values.of(
            {
                "PageToken": page_token,
                "Page": page_number,
                "PageSize": page_size,
            }
        )

        response = await self._version.page_async(
            method="GET", uri=self._uri, params=data
        )
        return PhoneNumberPage(self._version, response, self._solution)

    def get_page(self, target_url: str) -> PhoneNumberPage:
        """
        Retrieve a specific page of PhoneNumberInstance records from the API.
        Request is executed immediately

        :param target_url: API-generated URL for the requested results page

        :returns: Page of PhoneNumberInstance
        """
        response = self._version.domain.twilio.request("GET", target_url)
        return PhoneNumberPage(self._version, response, self._solution)

    async def get_page_async(self, target_url: str) -> PhoneNumberPage:
        """
        Asynchronously retrieve a specific page of PhoneNumberInstance records from the API.
        Request is executed immediately

        :param target_url: API-generated URL for the requested results page

        :returns: Page of PhoneNumberInstance
        """
        response = await self._version.domain.twilio.request_async("GET", target_url)
        return PhoneNumberPage(self._version, response, self._solution)

    def get(self, sid: str) -> PhoneNumberContext:
        """
        Constructs a PhoneNumberContext

        :param sid: The unique string that we created to identify the PhoneNumber resource to fetch.
        """
        return PhoneNumberContext(
            self._version, trunk_sid=self._solution["trunk_sid"], sid=sid
        )

    def __call__(self, sid: str) -> PhoneNumberContext:
        """
        Constructs a PhoneNumberContext

        :param sid: The unique string that we created to identify the PhoneNumber resource to fetch.
        """
        return PhoneNumberContext(
            self._version, trunk_sid=self._solution["trunk_sid"], sid=sid
        )

    def __repr__(self) -> str:
        """
        Provide a friendly representation

        :returns: Machine friendly representation
        """
        return "<Twilio.Trunking.V1.PhoneNumberList>"