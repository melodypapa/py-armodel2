"""SwitchStreamGateEntry AUTOSAR element."""

from typing import Optional, cast
import xml.etree.ElementTree as ET
from armodel.models.M2.AUTOSARTemplates.GenericStructure.GeneralTemplateClasses.Identifiable.identifiable import (
    Identifiable,
)
from armodel.models.M2.AUTOSARTemplates.GenericStructure.GeneralTemplateClasses.PrimitiveTypes import (
    PositiveInteger,
)


class SwitchStreamGateEntry(Identifiable):
    """AUTOSAR SwitchStreamGateEntry."""

    # XML member definitions for this class only (not inherited from parent classes)
    # Format: (member_name, xml_tag_name, is_attribute, is_list, element_class)
    _xml_members = [
        ("internal_priority", None, True, False, None),  # internalPriority
    ]

    def __init__(self) -> None:
        """Initialize SwitchStreamGateEntry."""
        super().__init__()
        self.internal_priority: Optional[PositiveInteger] = None

    def serialize(self, namespace: str, element: Optional[ET.Element] = None) -> ET.Element:
        """Convert SwitchStreamGateEntry to XML element.

        Args:
            namespace: XML namespace for the element
            element: Optional existing element to add members to (for subclass chaining)

        Returns:
            XML element representing this object
        """
        # ARObject.serialize() handles entire class hierarchy automatically
        return super().serialize(namespace, element)

    @classmethod
    def deserialize(cls, element: ET.Element) -> "SwitchStreamGateEntry":
        """Create SwitchStreamGateEntry from XML element.

        Args:
            element: XML element to deserialize from

        Returns:
            SwitchStreamGateEntry instance
        """
        # ARObject.deserialize() handles entire class hierarchy automatically
        obj = super().deserialize(element)
        # Cast to SwitchStreamGateEntry since parent returns ARObject
        return cast("SwitchStreamGateEntry", obj)


class SwitchStreamGateEntryBuilder:
    """Builder for SwitchStreamGateEntry."""

    def __init__(self) -> None:
        """Initialize builder."""
        self._obj: SwitchStreamGateEntry = SwitchStreamGateEntry()

    def build(self) -> SwitchStreamGateEntry:
        """Build and return SwitchStreamGateEntry object.

        Returns:
            SwitchStreamGateEntry instance
        """
        # TODO: Add validation
        return self._obj
