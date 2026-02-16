"""GlobalTimeSlave AUTOSAR element."""

from typing import Optional, cast
import xml.etree.ElementTree as ET
from armodel.models.M2.AUTOSARTemplates.GenericStructure.GeneralTemplateClasses.Identifiable.identifiable import (
    Identifiable,
)
from armodel.models.M2.AUTOSARTemplates.GenericStructure.GeneralTemplateClasses.PrimitiveTypes import (
    PositiveInteger,
    TimeValue,
)
from armodel.models.M2.AUTOSARTemplates.SystemTemplate.Fibex.FibexCore.CoreTopology.communication_connector import (
    CommunicationConnector,
)


class GlobalTimeSlave(Identifiable):
    """AUTOSAR GlobalTimeSlave."""
    """Abstract base class - do not instantiate directly."""

    # XML member definitions for this class only (not inherited from parent classes)
    # Format: (member_name, xml_tag_name, is_attribute, is_list, element_class)
    _xml_members = [
        ("communication_connector", None, False, False, CommunicationConnector),  # communicationConnector
        ("follow_up_timeout_value", None, True, False, None),  # followUpTimeoutValue
        ("icv_verification", None, False, False, any (GlobalTimeIcv)),  # icvVerification
        ("time_leap_future", None, True, False, None),  # timeLeapFuture
        ("time_leap", None, True, False, None),  # timeLeap
        ("time_leap_past", None, True, False, None),  # timeLeapPast
    ]

    def __init__(self) -> None:
        """Initialize GlobalTimeSlave."""
        super().__init__()
        self.communication_connector: Optional[CommunicationConnector] = None
        self.follow_up_timeout_value: Optional[TimeValue] = None
        self.icv_verification: Optional[Any] = None
        self.time_leap_future: Optional[TimeValue] = None
        self.time_leap: Optional[PositiveInteger] = None
        self.time_leap_past: Optional[TimeValue] = None

    def serialize(self, namespace: str, element: Optional[ET.Element] = None) -> ET.Element:
        """Convert GlobalTimeSlave to XML element.

        Args:
            namespace: XML namespace for the element
            element: Optional existing element to add members to (for subclass chaining)

        Returns:
            XML element representing this object
        """
        # ARObject.serialize() handles entire class hierarchy automatically
        return super().serialize(namespace, element)

    @classmethod
    def deserialize(cls, element: ET.Element) -> "GlobalTimeSlave":
        """Create GlobalTimeSlave from XML element.

        Args:
            element: XML element to deserialize from

        Returns:
            GlobalTimeSlave instance
        """
        # ARObject.deserialize() handles entire class hierarchy automatically
        obj = super().deserialize(element)
        # Cast to GlobalTimeSlave since parent returns ARObject
        return cast("GlobalTimeSlave", obj)


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
