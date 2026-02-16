"""RequestResponseDelay AUTOSAR element."""

from typing import Optional, cast
import xml.etree.ElementTree as ET
from armodel.models.M2.AUTOSARTemplates.GenericStructure.GeneralTemplateClasses.ar_object import ARObject
from armodel.models.M2.AUTOSARTemplates.GenericStructure.GeneralTemplateClasses.PrimitiveTypes import (
    TimeValue,
)


class RequestResponseDelay(ARObject):
    """AUTOSAR RequestResponseDelay."""

    # XML member definitions for this class only (not inherited from parent classes)
    # Format: (member_name, xml_tag_name, is_attribute, is_list, element_class)
    _xml_members = [
        ("max_value", None, True, False, None),  # maxValue
        ("min_value", None, True, False, None),  # minValue
    ]

    def __init__(self) -> None:
        """Initialize RequestResponseDelay."""
        super().__init__()
        self.max_value: Optional[TimeValue] = None
        self.min_value: Optional[TimeValue] = None

    def serialize(self, namespace: str, element: Optional[ET.Element] = None) -> ET.Element:
        """Convert RequestResponseDelay to XML element.

        Args:
            namespace: XML namespace for the element
            element: Optional existing element to add members to (for subclass chaining)

        Returns:
            XML element representing this object
        """
        # ARObject.serialize() handles entire class hierarchy automatically
        return super().serialize(namespace, element)

    @classmethod
    def deserialize(cls, element: ET.Element) -> "RequestResponseDelay":
        """Create RequestResponseDelay from XML element.

        Args:
            element: XML element to deserialize from

        Returns:
            RequestResponseDelay instance
        """
        # ARObject.deserialize() handles entire class hierarchy automatically
        obj = super().deserialize(element)
        # Cast to RequestResponseDelay since parent returns ARObject
        return cast("RequestResponseDelay", obj)


class RequestResponseDelayBuilder:
    """Builder for RequestResponseDelay."""

    def __init__(self) -> None:
        """Initialize builder."""
        self._obj: RequestResponseDelay = RequestResponseDelay()

    def build(self) -> RequestResponseDelay:
        """Build and return RequestResponseDelay object.

        Returns:
            RequestResponseDelay instance
        """
        # TODO: Add validation
        return self._obj
