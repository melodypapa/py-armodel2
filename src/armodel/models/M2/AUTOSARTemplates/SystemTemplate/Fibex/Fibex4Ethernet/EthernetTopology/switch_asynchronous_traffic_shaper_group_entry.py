"""SwitchAsynchronousTrafficShaperGroupEntry AUTOSAR element."""

from typing import Optional, cast
import xml.etree.ElementTree as ET
from armodel.models.M2.AUTOSARTemplates.GenericStructure.GeneralTemplateClasses.Identifiable.identifiable import (
    Identifiable,
)
from armodel.models.M2.AUTOSARTemplates.GenericStructure.GeneralTemplateClasses.PrimitiveTypes import (
    PositiveInteger,
)


class SwitchAsynchronousTrafficShaperGroupEntry(Identifiable):
    """AUTOSAR SwitchAsynchronousTrafficShaperGroupEntry."""

    # XML member definitions for this class only (not inherited from parent classes)
    # Format: (member_name, xml_tag_name, is_attribute, is_list, element_class)
    _xml_members = [
        ("maximum", None, True, False, None),  # maximum
    ]

    def __init__(self) -> None:
        """Initialize SwitchAsynchronousTrafficShaperGroupEntry."""
        super().__init__()
        self.maximum: Optional[PositiveInteger] = None

    def serialize(self, namespace: str, element: Optional[ET.Element] = None) -> ET.Element:
        """Convert SwitchAsynchronousTrafficShaperGroupEntry to XML element.

        Args:
            namespace: XML namespace for the element
            element: Optional existing element to add members to (for subclass chaining)

        Returns:
            XML element representing this object
        """
        # ARObject.serialize() handles entire class hierarchy automatically
        return super().serialize(namespace, element)

    @classmethod
    def deserialize(cls, element: ET.Element) -> "SwitchAsynchronousTrafficShaperGroupEntry":
        """Create SwitchAsynchronousTrafficShaperGroupEntry from XML element.

        Args:
            element: XML element to deserialize from

        Returns:
            SwitchAsynchronousTrafficShaperGroupEntry instance
        """
        # ARObject.deserialize() handles entire class hierarchy automatically
        obj = super().deserialize(element)
        # Cast to SwitchAsynchronousTrafficShaperGroupEntry since parent returns ARObject
        return cast("SwitchAsynchronousTrafficShaperGroupEntry", obj)


class SwitchAsynchronousTrafficShaperGroupEntryBuilder:
    """Builder for SwitchAsynchronousTrafficShaperGroupEntry."""

    def __init__(self) -> None:
        """Initialize builder."""
        self._obj: SwitchAsynchronousTrafficShaperGroupEntry = SwitchAsynchronousTrafficShaperGroupEntry()

    def build(self) -> SwitchAsynchronousTrafficShaperGroupEntry:
        """Build and return SwitchAsynchronousTrafficShaperGroupEntry object.

        Returns:
            SwitchAsynchronousTrafficShaperGroupEntry instance
        """
        # TODO: Add validation
        return self._obj
