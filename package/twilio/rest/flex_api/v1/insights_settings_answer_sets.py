r"""
    This code was generated by
   ___ _ _ _ _ _    _ ____    ____ ____ _    ____ ____ _  _ ____ ____ ____ ___ __   __
    |  | | | | |    | |  | __ |  | |__| | __ | __ |___ |\ | |___ |__/ |__|  | |  | |__/
    |  |_|_| | |___ | |__|    |__| |  | |    |__] |___ | \| |___ |  \ |  |  | |__| |  \

    Twilio - Flex
    This is the public Twilio REST API.

    NOTE: This class is auto generated by OpenAPI Generator.
    https://openapi-generator.tech
    Do not edit the class manually.
"""

from typing import Any, Dict, Optional, Union
from twilio.base import values

from twilio.base.instance_resource import InstanceResource
from twilio.base.list_resource import ListResource
from twilio.base.version import Version


class InsightsSettingsAnswerSetsInstance(InstanceResource):
    """
    :ivar account_sid: The SID of the [Account](https://www.twilio.com/docs/iam/api/account) that created the Flex Insights resource and owns this resource.
    :ivar answer_sets: The lis of answer sets
    :ivar answer_set_categories: The list of answer set categories
    :ivar not_applicable: The details for not applicable answer set
    :ivar url:
    """

    def __init__(self, version: Version, payload: Dict[str, Any]):
        super().__init__(version)

        self.account_sid: Optional[str] = payload.get("account_sid")
        self.answer_sets: Optional[Dict[str, object]] = payload.get("answer_sets")
        self.answer_set_categories: Optional[Dict[str, object]] = payload.get(
            "answer_set_categories"
        )
        self.not_applicable: Optional[Dict[str, object]] = payload.get("not_applicable")
        self.url: Optional[str] = payload.get("url")

    def __repr__(self) -> str:
        """
        Provide a friendly representation

        :returns: Machine friendly representation
        """

        return "<Twilio.FlexApi.V1.InsightsSettingsAnswerSetsInstance>"


class InsightsSettingsAnswerSetsList(ListResource):

    def __init__(self, version: Version):
        """
        Initialize the InsightsSettingsAnswerSetsList

        :param version: Version that contains the resource

        """
        super().__init__(version)

        self._uri = "/Insights/QualityManagement/Settings/AnswerSets"

    def fetch(
        self, authorization: Union[str, object] = values.unset
    ) -> InsightsSettingsAnswerSetsInstance:
        """
        Asynchronously fetch the InsightsSettingsAnswerSetsInstance

        :param authorization: The Authorization HTTP request header
        :returns: The fetched InsightsSettingsAnswerSetsInstance
        """
        headers = values.of(
            {
                "Authorization": authorization,
            }
        )

        payload = self._version.fetch(method="GET", uri=self._uri, headers=headers)

        return InsightsSettingsAnswerSetsInstance(self._version, payload)

    async def fetch_async(
        self, authorization: Union[str, object] = values.unset
    ) -> InsightsSettingsAnswerSetsInstance:
        """
        Asynchronously fetch the InsightsSettingsAnswerSetsInstance

        :param authorization: The Authorization HTTP request header
        :returns: The fetched InsightsSettingsAnswerSetsInstance
        """
        headers = values.of(
            {
                "Authorization": authorization,
            }
        )

        payload = await self._version.fetch_async(
            method="GET", uri=self._uri, headers=headers
        )

        return InsightsSettingsAnswerSetsInstance(self._version, payload)

    def __repr__(self) -> str:
        """
        Provide a friendly representation

        :returns: Machine friendly representation
        """
        return "<Twilio.FlexApi.V1.InsightsSettingsAnswerSetsList>"
