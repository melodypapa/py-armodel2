"""CanTpAddress AUTOSAR element."""

from typing import Optional, cast
import xml.etree.ElementTree as ET
from armodel.models.M2.AUTOSARTemplates.GenericStructure.GeneralTemplateClasses.Identifiable.identifiable import (
    Identifiable,
)
from armodel.models.M2.AUTOSARTemplates.GenericStructure.GeneralTemplateClasses.PrimitiveTypes import (
    Integer,
)


class CanTpAddress(Identifiable):
    """AUTOSAR CanTpAddress."""

    # XML member definitions for this class only (not inherited from parent classes)
    # Format: (member_name, xml_tag_name, is_attribute, is_list, element_class)
    _xml_members = [
        ("tp_address", None, True, False, None),  # tpAddress
    ]

    def __init__(self) -> None:
        """Initialize CanTpAddress."""
        super().__init__()
        self.tp_address: Optional[Integer] = None

    def serialize(self, namespace: str, element: Optional[ET.Element] = None) -> ET.Element:
        """Convert CanTpAddress to XML element.

        Args:
            namespace: XML namespace for the element
            element: Optional existing element to add members to (for subclass chaining)

        Returns:
            XML element representing this object
        """
        # ARObject.serialize() handles entire class hierarchy automatically
        return super().serialize(namespace, element)

    @classmethod
    def deserialize(cls, element: ET.Element) -> "CanTpAddress":
        """Create CanTpAddress from XML element.

        Args:
            element: XML element to deserialize from

        Returns:
            CanTpAddress instance
        """
        # ARObject.deserialize() handles entire class hierarchy automatically
        obj = super().deserialize(element)
        # Cast to CanTpAddress since parent returns ARObject
        return cast("CanTpAddress", obj)


class CanTpAddressBuilder:
    """Builder for CanTpAddress."""

    def __init__(self) -> None:
        """Initialize builder."""
        self._obj: CanTpAddress = CanTpAddress()

    def build(self) -> CanTpAddress:
        """Build and return CanTpAddress object.

        Returns:
            CanTpAddress instance
        """
        # TODO: Add validation
        return self._obj
