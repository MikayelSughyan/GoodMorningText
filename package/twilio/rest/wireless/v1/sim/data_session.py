r"""
    This code was generated by
   ___ _ _ _ _ _    _ ____    ____ ____ _    ____ ____ _  _ ____ ____ ____ ___ __   __
    |  | | | | |    | |  | __ |  | |__| | __ | __ |___ |\ | |___ |__/ |__|  | |  | |__/
    |  |_|_| | |___ | |__|    |__| |  | |    |__] |___ | \| |___ |  \ |  |  | |__| |  \

    Twilio - Wireless
    This is the public Twilio REST API.

    NOTE: This class is auto generated by OpenAPI Generator.
    https://openapi-generator.tech
    Do not edit the class manually.
"""

from datetime import datetime
from typing import Any, Dict, List, Optional, Union, Iterator, AsyncIterator
from twilio.base import deserialize, values

from twilio.base.instance_resource import InstanceResource
from twilio.base.list_resource import ListResource
from twilio.base.version import Version
from twilio.base.page import Page


class DataSessionInstance(InstanceResource):
    """
    :ivar sid: The unique string that we created to identify the DataSession resource.
    :ivar sim_sid: The SID of the [Sim resource](https://www.twilio.com/docs/iot/wireless/api/sim-resource) that the Data Session is for.
    :ivar account_sid: The SID of the [Account](https://www.twilio.com/docs/iam/api/account) that created the DataSession resource.
    :ivar radio_link: The generation of wireless technology that the device was using.
    :ivar operator_mcc: The 'mobile country code' is the unique ID of the home country where the Data Session took place. See: [MCC/MNC lookup](http://mcc-mnc.com/).
    :ivar operator_mnc: The 'mobile network code' is the unique ID specific to the mobile operator network where the Data Session took place.
    :ivar operator_country: The three letter country code representing where the device's Data Session took place. This is determined by looking up the `operator_mcc`.
    :ivar operator_name: The friendly name of the mobile operator network that the [SIM](https://www.twilio.com/docs/iot/wireless/api/sim-resource)-connected device is attached to. This is determined by looking up the `operator_mnc`.
    :ivar cell_id: The unique ID of the cellular tower that the device was attached to at the moment when the Data Session was last updated.
    :ivar cell_location_estimate: An object that describes the estimated location in latitude and longitude where the device's Data Session took place. The location is derived from the `cell_id` when the Data Session was last updated. See [Cell Location Estimate Object](https://www.twilio.com/docs/iot/wireless/api/datasession-resource#cell-location-estimate-object).
    :ivar packets_uploaded: The number of packets uploaded by the device between the `start` time and when the Data Session was last updated.
    :ivar packets_downloaded: The number of packets downloaded by the device between the `start` time and when the Data Session was last updated.
    :ivar last_updated: The date that the resource was last updated, given as GMT in [ISO 8601](https://www.iso.org/iso-8601-date-and-time-format.html) format.
    :ivar start: The date that the Data Session started, given as GMT in [ISO 8601](https://www.iso.org/iso-8601-date-and-time-format.html) format.
    :ivar end: The date that the record ended, given as GMT in [ISO 8601](https://www.iso.org/iso-8601-date-and-time-format.html) format.
    :ivar imei: The 'international mobile equipment identity' is the unique ID of the device using the SIM to connect. An IMEI is a 15-digit string: 14 digits for the device identifier plus a check digit calculated using the Luhn formula.
    """

    def __init__(self, version: Version, payload: Dict[str, Any], sim_sid: str):
        super().__init__(version)

        self.sid: Optional[str] = payload.get("sid")
        self.sim_sid: Optional[str] = payload.get("sim_sid")
        self.account_sid: Optional[str] = payload.get("account_sid")
        self.radio_link: Optional[str] = payload.get("radio_link")
        self.operator_mcc: Optional[str] = payload.get("operator_mcc")
        self.operator_mnc: Optional[str] = payload.get("operator_mnc")
        self.operator_country: Optional[str] = payload.get("operator_country")
        self.operator_name: Optional[str] = payload.get("operator_name")
        self.cell_id: Optional[str] = payload.get("cell_id")
        self.cell_location_estimate: Optional[Dict[str, object]] = payload.get(
            "cell_location_estimate"
        )
        self.packets_uploaded: Optional[int] = deserialize.integer(
            payload.get("packets_uploaded")
        )
        self.packets_downloaded: Optional[int] = deserialize.integer(
            payload.get("packets_downloaded")
        )
        self.last_updated: Optional[datetime] = deserialize.iso8601_datetime(
            payload.get("last_updated")
        )
        self.start: Optional[datetime] = deserialize.iso8601_datetime(
            payload.get("start")
        )
        self.end: Optional[datetime] = deserialize.iso8601_datetime(payload.get("end"))
        self.imei: Optional[str] = payload.get("imei")

        self._solution = {
            "sim_sid": sim_sid,
        }

    def __repr__(self) -> str:
        """
        Provide a friendly representation

        :returns: Machine friendly representation
        """
        context = " ".join("{}={}".format(k, v) for k, v in self._solution.items())
        return "<Twilio.Wireless.V1.DataSessionInstance {}>".format(context)


class DataSessionPage(Page):

    def get_instance(self, payload: Dict[str, Any]) -> DataSessionInstance:
        """
        Build an instance of DataSessionInstance

        :param payload: Payload response from the API
        """
        return DataSessionInstance(
            self._version, payload, sim_sid=self._solution["sim_sid"]
        )

    def __repr__(self) -> str:
        """
        Provide a friendly representation

        :returns: Machine friendly representation
        """
        return "<Twilio.Wireless.V1.DataSessionPage>"


class DataSessionList(ListResource):

    def __init__(self, version: Version, sim_sid: str):
        """
        Initialize the DataSessionList

        :param version: Version that contains the resource
        :param sim_sid: The SID of the [Sim resource](https://www.twilio.com/docs/iot/wireless/api/sim-resource) with the Data Sessions to read.

        """
        super().__init__(version)

        # Path Solution
        self._solution = {
            "sim_sid": sim_sid,
        }
        self._uri = "/Sims/{sim_sid}/DataSessions".format(**self._solution)

    def stream(
        self,
        limit: Optional[int] = None,
        page_size: Optional[int] = None,
    ) -> Iterator[DataSessionInstance]:
        """
        Streams DataSessionInstance records from the API as a generator stream.
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
    ) -> AsyncIterator[DataSessionInstance]:
        """
        Asynchronously streams DataSessionInstance records from the API as a generator stream.
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
    ) -> List[DataSessionInstance]:
        """
        Lists DataSessionInstance records from the API as a list.
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
    ) -> List[DataSessionInstance]:
        """
        Asynchronously lists DataSessionInstance records from the API as a list.
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
    ) -> DataSessionPage:
        """
        Retrieve a single page of DataSessionInstance records from the API.
        Request is executed immediately

        :param page_token: PageToken provided by the API
        :param page_number: Page Number, this value is simply for client state
        :param page_size: Number of records to return, defaults to 50

        :returns: Page of DataSessionInstance
        """
        data = values.of(
            {
                "PageToken": page_token,
                "Page": page_number,
                "PageSize": page_size,
            }
        )

        response = self._version.page(method="GET", uri=self._uri, params=data)
        return DataSessionPage(self._version, response, self._solution)

    async def page_async(
        self,
        page_token: Union[str, object] = values.unset,
        page_number: Union[int, object] = values.unset,
        page_size: Union[int, object] = values.unset,
    ) -> DataSessionPage:
        """
        Asynchronously retrieve a single page of DataSessionInstance records from the API.
        Request is executed immediately

        :param page_token: PageToken provided by the API
        :param page_number: Page Number, this value is simply for client state
        :param page_size: Number of records to return, defaults to 50

        :returns: Page of DataSessionInstance
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
        return DataSessionPage(self._version, response, self._solution)

    def get_page(self, target_url: str) -> DataSessionPage:
        """
        Retrieve a specific page of DataSessionInstance records from the API.
        Request is executed immediately

        :param target_url: API-generated URL for the requested results page

        :returns: Page of DataSessionInstance
        """
        response = self._version.domain.twilio.request("GET", target_url)
        return DataSessionPage(self._version, response, self._solution)

    async def get_page_async(self, target_url: str) -> DataSessionPage:
        """
        Asynchronously retrieve a specific page of DataSessionInstance records from the API.
        Request is executed immediately

        :param target_url: API-generated URL for the requested results page

        :returns: Page of DataSessionInstance
        """
        response = await self._version.domain.twilio.request_async("GET", target_url)
        return DataSessionPage(self._version, response, self._solution)

    def __repr__(self) -> str:
        """
        Provide a friendly representation

        :returns: Machine friendly representation
        """
        return "<Twilio.Wireless.V1.DataSessionList>"
