"""TransmissionComSpecProps AUTOSAR element."""

from typing import Optional, cast
import xml.etree.ElementTree as ET
from armodel.models.M2.AUTOSARTemplates.GenericStructure.GeneralTemplateClasses.ar_object import ARObject
from armodel.models.M2.AUTOSARTemplates.GenericStructure.GeneralTemplateClasses.PrimitiveTypes import (
    TimeValue,
)


class TransmissionComSpecProps(ARObject):
    """AUTOSAR TransmissionComSpecProps."""

    # XML member definitions for this class only (not inherited from parent classes)
    # Format: (member_name, xml_tag_name, is_attribute, is_list, element_class)
    _xml_members = [
        ("data_update", None, True, False, None),  # dataUpdate
        ("minimum_send", None, True, False, None),  # minimumSend
        ("transmission", None, False, False, any (TransmissionMode)),  # transmission
    ]

    def __init__(self) -> None:
        """Initialize TransmissionComSpecProps."""
        super().__init__()
        self.data_update: Optional[TimeValue] = None
        self.minimum_send: Optional[TimeValue] = None
        self.transmission: Optional[Any] = None

    def serialize(self, namespace: str, element: Optional[ET.Element] = None) -> ET.Element:
        """Convert TransmissionComSpecProps to XML element.

        Args:
            namespace: XML namespace for the element
            element: Optional existing element to add members to (for subclass chaining)

        Returns:
            XML element representing this object
        """
        # ARObject.serialize() handles entire class hierarchy automatically
        return super().serialize(namespace, element)

    @classmethod
    def deserialize(cls, element: ET.Element) -> "TransmissionComSpecProps":
        """Create TransmissionComSpecProps from XML element.

        Args:
            element: XML element to deserialize from

        Returns:
            TransmissionComSpecProps instance
        """
        # ARObject.deserialize() handles entire class hierarchy automatically
        obj = super().deserialize(element)
        # Cast to TransmissionComSpecProps since parent returns ARObject
        return cast("TransmissionComSpecProps", obj)


class TransmissionComSpecPropsBuilder:
    """Builder for TransmissionComSpecProps."""

    def __init__(self) -> None:
        """Initialize builder."""
        self._obj: TransmissionComSpecProps = TransmissionComSpecProps()

    def build(self) -> TransmissionComSpecProps:
        """Build and return TransmissionComSpecProps object.

        Returns:
            TransmissionComSpecProps instance
        """
        # TODO: Add validation
        return self._obj
