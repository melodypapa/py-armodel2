"""AtpPrototype AUTOSAR element."""

from typing import Optional, cast
import xml.etree.ElementTree as ET
from armodel.models.M2.AUTOSARTemplates.GenericStructure.GeneralTemplateClasses.Identifiable.identifiable import (
    Identifiable,
)
from armodel.models.M2.AUTOSARTemplates.GenericStructure.AbstractStructure.atp_type import (
    AtpType,
)


class AtpPrototype(Identifiable):
    """AUTOSAR AtpPrototype."""
    """Abstract base class - do not instantiate directly."""

    # XML member definitions for this class only (not inherited from parent classes)
    # Format: (member_name, xml_tag_name, is_attribute, is_list, element_class)
    _xml_members = [
        ("atp_type", None, False, False, AtpType),  # atpType
    ]

    def __init__(self) -> None:
        """Initialize AtpPrototype."""
        super().__init__()
        self.atp_type: AtpType = None

    def serialize(self, namespace: str, element: Optional[ET.Element] = None) -> ET.Element:
        """Convert AtpPrototype to XML element.

        Args:
            namespace: XML namespace for the element
            element: Optional existing element to add members to (for subclass chaining)

        Returns:
            XML element representing this object
        """
        # ARObject.serialize() handles entire class hierarchy automatically
        return super().serialize(namespace, element)

    @classmethod
    def deserialize(cls, element: ET.Element) -> "AtpPrototype":
        """Create AtpPrototype from XML element.

        Args:
            element: XML element to deserialize from

        Returns:
            AtpPrototype instance
        """
        # ARObject.deserialize() handles entire class hierarchy automatically
        obj = super().deserialize(element)
        # Cast to AtpPrototype since parent returns ARObject
        return cast("AtpPrototype", obj)


class AtpPrototypeBuilder:
    """Builder for AtpPrototype."""

    def __init__(self) -> None:
        """Initialize builder."""
        self._obj: AtpPrototype = AtpPrototype()

    def build(self) -> AtpPrototype:
        """Build and return AtpPrototype object.

        Returns:
            AtpPrototype instance
        """
        # TODO: Add validation
        return self._obj
