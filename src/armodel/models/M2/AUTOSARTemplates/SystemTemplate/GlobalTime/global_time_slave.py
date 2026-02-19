"""GlobalTimeSlave AUTOSAR element.

References:
  - AUTOSAR_CP_TPS_SystemTemplate.pdf (page 860)

JSON Source: docs/json/packages/M2_AUTOSARTemplates_SystemTemplate_GlobalTime.classes.json"""

from __future__ import annotations
from typing import TYPE_CHECKING, Optional, Any
import xml.etree.ElementTree as ET

from armodel.models.M2.AUTOSARTemplates.GenericStructure.GeneralTemplateClasses.Identifiable.identifiable import (
    Identifiable,
)
from armodel.models.M2.AUTOSARTemplates.GenericStructure.GeneralTemplateClasses.ArObject.ar_object import ARObject
from armodel.models.M2.AUTOSARTemplates.GenericStructure.GeneralTemplateClasses.PrimitiveTypes import (
    PositiveInteger,
    TimeValue,
)
from armodel.models.M2.AUTOSARTemplates.SystemTemplate.Fibex.FibexCore.CoreTopology.communication_connector import (
    CommunicationConnector,
)
from abc import ABC, abstractmethod


class GlobalTimeSlave(Identifiable, ABC):
    """AUTOSAR GlobalTimeSlave."""

    @property
    def is_abstract(self) -> bool:
        """Check if this class is abstract.

        Returns:
            True for abstract classes
        """
        return True

    communication_connector: Optional[CommunicationConnector]
    follow_up_timeout_value: Optional[TimeValue]
    icv_verification: Optional[Any]
    time_leap_future: Optional[TimeValue]
    time_leap: Optional[PositiveInteger]
    time_leap_past: Optional[TimeValue]
    def __init__(self) -> None:
        """Initialize GlobalTimeSlave."""
        super().__init__()
        self.communication_connector: Optional[CommunicationConnector] = None
        self.follow_up_timeout_value: Optional[TimeValue] = None
        self.icv_verification: Optional[Any] = None
        self.time_leap_future: Optional[TimeValue] = None
        self.time_leap: Optional[PositiveInteger] = None
        self.time_leap_past: Optional[TimeValue] = None
    @classmethod
    def deserialize(cls, element: ET.Element) -> "GlobalTimeSlave":
        """Deserialize XML element to GlobalTimeSlave object.

        Args:
            element: XML element to deserialize from

        Returns:
            Deserialized GlobalTimeSlave object
        """
        # Create instance and initialize with default values
        obj = cls.__new__(cls)
        obj.__init__()

        # Parse communication_connector
        child = ARObject._find_child_element(element, "COMMUNICATION-CONNECTOR")
        if child is not None:
            communication_connector_value = ARObject._deserialize_by_tag(child, "CommunicationConnector")
            obj.communication_connector = communication_connector_value

        # Parse follow_up_timeout_value
        child = ARObject._find_child_element(element, "FOLLOW-UP-TIMEOUT-VALUE")
        if child is not None:
            follow_up_timeout_value_value = child.text
            obj.follow_up_timeout_value = follow_up_timeout_value_value

        # Parse icv_verification
        child = ARObject._find_child_element(element, "ICV-VERIFICATION")
        if child is not None:
            icv_verification_value = child.text
            obj.icv_verification = icv_verification_value

        # Parse time_leap_future
        child = ARObject._find_child_element(element, "TIME-LEAP-FUTURE")
        if child is not None:
            time_leap_future_value = child.text
            obj.time_leap_future = time_leap_future_value

        # Parse time_leap
        child = ARObject._find_child_element(element, "TIME-LEAP")
        if child is not None:
            time_leap_value = child.text
            obj.time_leap = time_leap_value

        # Parse time_leap_past
        child = ARObject._find_child_element(element, "TIME-LEAP-PAST")
        if child is not None:
            time_leap_past_value = child.text
            obj.time_leap_past = time_leap_past_value

        return obj



class GlobalTimeSlaveBuilder:
    """Builder for GlobalTimeSlave."""

    def __init__(self) -> None:
        """Initialize builder."""
        self._obj: GlobalTimeSlave = GlobalTimeSlave()

    def build(self) -> GlobalTimeSlave:
        """Build and return GlobalTimeSlave object.

        Returns:
            GlobalTimeSlave instance
        """
        # TODO: Add validation
        return self._obj
