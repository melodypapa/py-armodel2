"""UserDefinedGlobalTimeSlave AUTOSAR element."""

from typing import Optional, cast
import xml.etree.ElementTree as ET
from armodel.models.M2.AUTOSARTemplates.SystemTemplate.GlobalTime.global_time_slave import (
    GlobalTimeSlave,
)


class UserDefinedGlobalTimeSlave(GlobalTimeSlave):
    """AUTOSAR UserDefinedGlobalTimeSlave."""

    # XML member definitions for this class only (not inherited from parent classes)
    # Format: (member_name, xml_tag_name, is_attribute, is_list, element_class)
    _xml_members = [
    ]

    def __init__(self) -> None:
        """Initialize UserDefinedGlobalTimeSlave."""
        super().__init__()

    def serialize(self, namespace: str, element: Optional[ET.Element] = None) -> ET.Element:
        """Convert UserDefinedGlobalTimeSlave to XML element.

        Args:
            namespace: XML namespace for the element
            element: Optional existing element to add members to (for subclass chaining)

        Returns:
            XML element representing this object
        """
        # ARObject.serialize() handles entire class hierarchy automatically
        return super().serialize(namespace, element)

    @classmethod
    def deserialize(cls, element: ET.Element) -> "UserDefinedGlobalTimeSlave":
        """Create UserDefinedGlobalTimeSlave from XML element.

        Args:
            element: XML element to deserialize from

        Returns:
            UserDefinedGlobalTimeSlave instance
        """
        # ARObject.deserialize() handles entire class hierarchy automatically
        obj = super().deserialize(element)
        # Cast to UserDefinedGlobalTimeSlave since parent returns ARObject
        return cast("UserDefinedGlobalTimeSlave", obj)


class UserDefinedGlobalTimeSlaveBuilder:
    """Builder for UserDefinedGlobalTimeSlave."""

    def __init__(self) -> None:
        """Initialize builder."""
        self._obj: UserDefinedGlobalTimeSlave = UserDefinedGlobalTimeSlave()

    def build(self) -> UserDefinedGlobalTimeSlave:
        """Build and return UserDefinedGlobalTimeSlave object.

        Returns:
            UserDefinedGlobalTimeSlave instance
        """
        # TODO: Add validation
        return self._obj
