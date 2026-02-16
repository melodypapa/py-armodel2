"""SymbolicNameProps AUTOSAR element."""

from typing import Optional, cast
import xml.etree.ElementTree as ET
from armodel.models.M2.AUTOSARTemplates.CommonStructure.Implementation.implementation_props import (
    ImplementationProps,
)


class SymbolicNameProps(ImplementationProps):
    """AUTOSAR SymbolicNameProps."""

    # XML member definitions for this class only (not inherited from parent classes)
    # Format: (member_name, xml_tag_name, is_attribute, is_list, element_class)
    _xml_members = [
    ]

    def __init__(self) -> None:
        """Initialize SymbolicNameProps."""
        super().__init__()

    def serialize(self, namespace: str, element: Optional[ET.Element] = None) -> ET.Element:
        """Convert SymbolicNameProps to XML element.

        Args:
            namespace: XML namespace for the element
            element: Optional existing element to add members to (for subclass chaining)

        Returns:
            XML element representing this object
        """
        # ARObject.serialize() handles entire class hierarchy automatically
        return super().serialize(namespace, element)

    @classmethod
    def deserialize(cls, element: ET.Element) -> "SymbolicNameProps":
        """Create SymbolicNameProps from XML element.

        Args:
            element: XML element to deserialize from

        Returns:
            SymbolicNameProps instance
        """
        # ARObject.deserialize() handles entire class hierarchy automatically
        obj = super().deserialize(element)
        # Cast to SymbolicNameProps since parent returns ARObject
        return cast("SymbolicNameProps", obj)


class SymbolicNamePropsBuilder:
    """Builder for SymbolicNameProps."""

    def __init__(self) -> None:
        """Initialize builder."""
        self._obj: SymbolicNameProps = SymbolicNameProps()

    def build(self) -> SymbolicNameProps:
        """Build and return SymbolicNameProps object.

        Returns:
            SymbolicNameProps instance
        """
        # TODO: Add validation
        return self._obj
