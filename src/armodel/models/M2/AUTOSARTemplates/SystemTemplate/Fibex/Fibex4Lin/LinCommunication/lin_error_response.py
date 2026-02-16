"""LinErrorResponse AUTOSAR element."""

from typing import Optional, cast
import xml.etree.ElementTree as ET
from armodel.models.M2.AUTOSARTemplates.GenericStructure.GeneralTemplateClasses.ar_object import ARObject
from armodel.models.M2.AUTOSARTemplates.SystemTemplate.Fibex.FibexCore.CoreCommunication.i_signal_triggering import (
    ISignalTriggering,
)


class LinErrorResponse(ARObject):
    """AUTOSAR LinErrorResponse."""

    # XML member definitions for this class only (not inherited from parent classes)
    # Format: (member_name, xml_tag_name, is_attribute, is_list, element_class)
    _xml_members = [
        ("response_error", None, False, False, ISignalTriggering),  # responseError
    ]

    def __init__(self) -> None:
        """Initialize LinErrorResponse."""
        super().__init__()
        self.response_error: Optional[ISignalTriggering] = None

    def serialize(self, namespace: str, element: Optional[ET.Element] = None) -> ET.Element:
        """Convert LinErrorResponse to XML element.

        Args:
            namespace: XML namespace for the element
            element: Optional existing element to add members to (for subclass chaining)

        Returns:
            XML element representing this object
        """
        # ARObject.serialize() handles entire class hierarchy automatically
        return super().serialize(namespace, element)

    @classmethod
    def deserialize(cls, element: ET.Element) -> "LinErrorResponse":
        """Create LinErrorResponse from XML element.

        Args:
            element: XML element to deserialize from

        Returns:
            LinErrorResponse instance
        """
        # ARObject.deserialize() handles entire class hierarchy automatically
        obj = super().deserialize(element)
        # Cast to LinErrorResponse since parent returns ARObject
        return cast("LinErrorResponse", obj)


class LinErrorResponseBuilder:
    """Builder for LinErrorResponse."""

    def __init__(self) -> None:
        """Initialize builder."""
        self._obj: LinErrorResponse = LinErrorResponse()

    def build(self) -> LinErrorResponse:
        """Build and return LinErrorResponse object.

        Returns:
            LinErrorResponse instance
        """
        # TODO: Add validation
        return self._obj
