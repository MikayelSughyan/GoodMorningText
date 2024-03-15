r"""
    This code was generated by
   ___ _ _ _ _ _    _ ____    ____ ____ _    ____ ____ _  _ ____ ____ ____ ___ __   __
    |  | | | | |    | |  | __ |  | |__| | __ | __ |___ |\ | |___ |__/ |__|  | |  | |__/
    |  |_|_| | |___ | |__|    |__| |  | |    |__] |___ | \| |___ |  \ |  |  | |__| |  \

    Twilio - Verify
    This is the public Twilio REST API.

    NOTE: This class is auto generated by OpenAPI Generator.
    https://openapi-generator.tech
    Do not edit the class manually.
"""

from datetime import datetime
from typing import Any, Dict, Optional, Union
from twilio.base import deserialize, values
from twilio.base.instance_context import InstanceContext
from twilio.base.instance_resource import InstanceResource
from twilio.base.list_resource import ListResource
from twilio.base.version import Version


class AccessTokenInstance(InstanceResource):

    class FactorTypes(object):
        PUSH = "push"

    """
    :ivar sid: A 34 character string that uniquely identifies this Access Token.
    :ivar account_sid: The unique SID identifier of the Account.
    :ivar service_sid: The unique SID identifier of the Verify Service.
    :ivar entity_identity: The unique external identifier for the Entity of the Service.
    :ivar factor_type: 
    :ivar factor_friendly_name: A human readable description of this factor, up to 64 characters. For a push factor, this can be the device's name.
    :ivar token: The access token generated for enrollment, this is an encrypted json web token.
    :ivar url: The URL of this resource.
    :ivar ttl: How long, in seconds, the access token is valid. Max: 5 minutes
    :ivar date_created: The date that this access token was created, given in [ISO 8601](https://en.wikipedia.org/wiki/ISO_8601) format.
    """

    def __init__(
        self,
        version: Version,
        payload: Dict[str, Any],
        service_sid: str,
        sid: Optional[str] = None,
    ):
        super().__init__(version)

        self.sid: Optional[str] = payload.get("sid")
        self.account_sid: Optional[str] = payload.get("account_sid")
        self.service_sid: Optional[str] = payload.get("service_sid")
        self.entity_identity: Optional[str] = payload.get("entity_identity")
        self.factor_type: Optional["AccessTokenInstance.FactorTypes"] = payload.get(
            "factor_type"
        )
        self.factor_friendly_name: Optional[str] = payload.get("factor_friendly_name")
        self.token: Optional[str] = payload.get("token")
        self.url: Optional[str] = payload.get("url")
        self.ttl: Optional[int] = deserialize.integer(payload.get("ttl"))
        self.date_created: Optional[datetime] = deserialize.iso8601_datetime(
            payload.get("date_created")
        )

        self._solution = {
            "service_sid": service_sid,
            "sid": sid or self.sid,
        }
        self._context: Optional[AccessTokenContext] = None

    @property
    def _proxy(self) -> "AccessTokenContext":
        """
        Generate an instance context for the instance, the context is capable of
        performing various actions. All instance actions are proxied to the context

        :returns: AccessTokenContext for this AccessTokenInstance
        """
        if self._context is None:
            self._context = AccessTokenContext(
                self._version,
                service_sid=self._solution["service_sid"],
                sid=self._solution["sid"],
            )
        return self._context

    def fetch(self) -> "AccessTokenInstance":
        """
        Fetch the AccessTokenInstance


        :returns: The fetched AccessTokenInstance
        """
        return self._proxy.fetch()

    async def fetch_async(self) -> "AccessTokenInstance":
        """
        Asynchronous coroutine to fetch the AccessTokenInstance


        :returns: The fetched AccessTokenInstance
        """
        return await self._proxy.fetch_async()

    def __repr__(self) -> str:
        """
        Provide a friendly representation

        :returns: Machine friendly representation
        """
        context = " ".join("{}={}".format(k, v) for k, v in self._solution.items())
        return "<Twilio.Verify.V2.AccessTokenInstance {}>".format(context)


class AccessTokenContext(InstanceContext):

    def __init__(self, version: Version, service_sid: str, sid: str):
        """
        Initialize the AccessTokenContext

        :param version: Version that contains the resource
        :param service_sid: The unique SID identifier of the Service.
        :param sid: A 34 character string that uniquely identifies this Access Token.
        """
        super().__init__(version)

        # Path Solution
        self._solution = {
            "service_sid": service_sid,
            "sid": sid,
        }
        self._uri = "/Services/{service_sid}/AccessTokens/{sid}".format(
            **self._solution
        )

    def fetch(self) -> AccessTokenInstance:
        """
        Fetch the AccessTokenInstance


        :returns: The fetched AccessTokenInstance
        """

        payload = self._version.fetch(
            method="GET",
            uri=self._uri,
        )

        return AccessTokenInstance(
            self._version,
            payload,
            service_sid=self._solution["service_sid"],
            sid=self._solution["sid"],
        )

    async def fetch_async(self) -> AccessTokenInstance:
        """
        Asynchronous coroutine to fetch the AccessTokenInstance


        :returns: The fetched AccessTokenInstance
        """

        payload = await self._version.fetch_async(
            method="GET",
            uri=self._uri,
        )

        return AccessTokenInstance(
            self._version,
            payload,
            service_sid=self._solution["service_sid"],
            sid=self._solution["sid"],
        )

    def __repr__(self) -> str:
        """
        Provide a friendly representation

        :returns: Machine friendly representation
        """
        context = " ".join("{}={}".format(k, v) for k, v in self._solution.items())
        return "<Twilio.Verify.V2.AccessTokenContext {}>".format(context)


class AccessTokenList(ListResource):

    def __init__(self, version: Version, service_sid: str):
        """
        Initialize the AccessTokenList

        :param version: Version that contains the resource
        :param service_sid: The unique SID identifier of the Service.

        """
        super().__init__(version)

        # Path Solution
        self._solution = {
            "service_sid": service_sid,
        }
        self._uri = "/Services/{service_sid}/AccessTokens".format(**self._solution)

    def create(
        self,
        identity: str,
        factor_type: "AccessTokenInstance.FactorTypes",
        factor_friendly_name: Union[str, object] = values.unset,
        ttl: Union[int, object] = values.unset,
    ) -> AccessTokenInstance:
        """
        Create the AccessTokenInstance

        :param identity: The unique external identifier for the Entity of the Service. This identifier should be immutable, not PII, and generated by your external system, such as your user's UUID, GUID, or SID.
        :param factor_type:
        :param factor_friendly_name: The friendly name of the factor that is going to be created with this access token
        :param ttl: How long, in seconds, the access token is valid. Can be an integer between 60 and 300. Default is 60.

        :returns: The created AccessTokenInstance
        """

        data = values.of(
            {
                "Identity": identity,
                "FactorType": factor_type,
                "FactorFriendlyName": factor_friendly_name,
                "Ttl": ttl,
            }
        )

        payload = self._version.create(
            method="POST",
            uri=self._uri,
            data=data,
        )

        return AccessTokenInstance(
            self._version, payload, service_sid=self._solution["service_sid"]
        )

    async def create_async(
        self,
        identity: str,
        factor_type: "AccessTokenInstance.FactorTypes",
        factor_friendly_name: Union[str, object] = values.unset,
        ttl: Union[int, object] = values.unset,
    ) -> AccessTokenInstance:
        """
        Asynchronously create the AccessTokenInstance

        :param identity: The unique external identifier for the Entity of the Service. This identifier should be immutable, not PII, and generated by your external system, such as your user's UUID, GUID, or SID.
        :param factor_type:
        :param factor_friendly_name: The friendly name of the factor that is going to be created with this access token
        :param ttl: How long, in seconds, the access token is valid. Can be an integer between 60 and 300. Default is 60.

        :returns: The created AccessTokenInstance
        """

        data = values.of(
            {
                "Identity": identity,
                "FactorType": factor_type,
                "FactorFriendlyName": factor_friendly_name,
                "Ttl": ttl,
            }
        )

        payload = await self._version.create_async(
            method="POST",
            uri=self._uri,
            data=data,
        )

        return AccessTokenInstance(
            self._version, payload, service_sid=self._solution["service_sid"]
        )

    def get(self, sid: str) -> AccessTokenContext:
        """
        Constructs a AccessTokenContext

        :param sid: A 34 character string that uniquely identifies this Access Token.
        """
        return AccessTokenContext(
            self._version, service_sid=self._solution["service_sid"], sid=sid
        )

    def __call__(self, sid: str) -> AccessTokenContext:
        """
        Constructs a AccessTokenContext

        :param sid: A 34 character string that uniquely identifies this Access Token.
        """
        return AccessTokenContext(
            self._version, service_sid=self._solution["service_sid"], sid=sid
        )

    def __repr__(self) -> str:
        """
        Provide a friendly representation

        :returns: Machine friendly representation
        """
        return "<Twilio.Verify.V2.AccessTokenList>"
