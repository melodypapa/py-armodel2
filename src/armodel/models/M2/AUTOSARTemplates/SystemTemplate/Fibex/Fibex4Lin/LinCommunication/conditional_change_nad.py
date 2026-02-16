"""ConditionalChangeNad AUTOSAR element."""

from typing import Optional, cast
import xml.etree.ElementTree as ET
from armodel.models.M2.AUTOSARTemplates.SystemTemplate.Fibex.Fibex4Lin.LinCommunication.lin_configuration_entry import (
    LinConfigurationEntry,
)
from armodel.models.M2.AUTOSARTemplates.GenericStructure.GeneralTemplateClasses.PrimitiveTypes import (
    Integer,
    PositiveInteger,
)


class ConditionalChangeNad(LinConfigurationEntry):
    """AUTOSAR ConditionalChangeNad."""

    # XML member definitions for this class only (not inherited from parent classes)
    # Format: (member_name, xml_tag_name, is_attribute, is_list, element_class)
    _xml_members = [
        ("byte", None, True, False, None),  # byte
        ("id", None, True, False, None),  # id
        ("invert", None, True, False, None),  # invert
        ("mask", None, True, False, None),  # mask
        ("new_nad", None, True, False, None),  # newNad
    ]

    def __init__(self) -> None:
        """Initialize ConditionalChangeNad."""
        super().__init__()
        self.byte: Optional[Integer] = None
        self.id: Optional[PositiveInteger] = None
        self.invert: Optional[Integer] = None
        self.mask: Optional[Integer] = None
        self.new_nad: Optional[Integer] = None

    def serialize(self, namespace: str, element: Optional[ET.Element] = None) -> ET.Element:
        """Convert ConditionalChangeNad to XML element.

        Args:
            namespace: XML namespace for the element
            element: Optional existing element to add members to (for subclass chaining)

        Returns:
            XML element representing this object
        """
        # ARObject.serialize() handles entire class hierarchy automatically
        return super().serialize(namespace, element)

    @classmethod
    def deserialize(cls, element: ET.Element) -> "ConditionalChangeNad":
        """Create ConditionalChangeNad from XML element.

        Args:
            element: XML element to deserialize from

        Returns:
            ConditionalChangeNad instance
        """
        # ARObject.deserialize() handles entire class hierarchy automatically
        obj = super().deserialize(element)
        # Cast to ConditionalChangeNad since parent returns ARObject
        return cast("ConditionalChangeNad", obj)


class ConditionalChangeNadBuilder:
    """Builder for ConditionalChangeNad."""

    def __init__(self) -> None:
        """Initialize builder."""
        self._obj: ConditionalChangeNad = ConditionalChangeNad()

    def build(self) -> ConditionalChangeNad:
        """Build and return ConditionalChangeNad object.

        Returns:
            ConditionalChangeNad instance
        """
        # TODO: Add validation
        return self._obj
