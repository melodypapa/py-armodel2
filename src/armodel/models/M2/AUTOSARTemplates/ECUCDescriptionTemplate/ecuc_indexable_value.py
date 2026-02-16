"""EcucIndexableValue AUTOSAR element."""

from typing import Optional, cast
import xml.etree.ElementTree as ET
from armodel.models.M2.AUTOSARTemplates.GenericStructure.GeneralTemplateClasses.ar_object import ARObject
from armodel.models.M2.AUTOSARTemplates.GenericStructure.GeneralTemplateClasses.PrimitiveTypes import (
    PositiveInteger,
)


class EcucIndexableValue(ARObject):
    """AUTOSAR EcucIndexableValue."""
    """Abstract base class - do not instantiate directly."""

    # XML member definitions for this class only (not inherited from parent classes)
    # Format: (member_name, xml_tag_name, is_attribute, is_list, element_class)
    _xml_members = [
        ("index", None, True, False, None),  # index
    ]

    def __init__(self) -> None:
        """Initialize EcucIndexableValue."""
        super().__init__()
        self.index: Optional[PositiveInteger] = None

    def serialize(self, namespace: str, element: Optional[ET.Element] = None) -> ET.Element:
        """Convert EcucIndexableValue to XML element.

        Args:
            namespace: XML namespace for the element
            element: Optional existing element to add members to (for subclass chaining)

        Returns:
            XML element representing this object
        """
        # ARObject.serialize() handles entire class hierarchy automatically
        return super().serialize(namespace, element)

    @classmethod
    def deserialize(cls, element: ET.Element) -> "EcucIndexableValue":
        """Create EcucIndexableValue from XML element.

        Args:
            element: XML element to deserialize from

        Returns:
            EcucIndexableValue instance
        """
        # ARObject.deserialize() handles entire class hierarchy automatically
        obj = super().deserialize(element)
        # Cast to EcucIndexableValue since parent returns ARObject
        return cast("EcucIndexableValue", obj)


class EcucIndexableValueBuilder:
    """Builder for EcucIndexableValue."""

    def __init__(self) -> None:
        """Initialize builder."""
        self._obj: EcucIndexableValue = EcucIndexableValue()

    def build(self) -> EcucIndexableValue:
        """Build and return EcucIndexableValue object.

        Returns:
            EcucIndexableValue instance
        """
        # TODO: Add validation
        return self._obj
