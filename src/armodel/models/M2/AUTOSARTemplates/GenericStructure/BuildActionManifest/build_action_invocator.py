"""BuildActionInvocator AUTOSAR element."""

from typing import Optional, cast
import xml.etree.ElementTree as ET
from armodel.models.M2.AUTOSARTemplates.GenericStructure.GeneralTemplateClasses.ar_object import ARObject
from armodel.models.M2.AUTOSARTemplates.GenericStructure.GeneralTemplateClasses.PrimitiveTypes import (
    VerbatimString,
)


class BuildActionInvocator(ARObject):
    """AUTOSAR BuildActionInvocator."""

    # XML member definitions for this class only (not inherited from parent classes)
    # Format: (member_name, xml_tag_name, is_attribute, is_list, element_class)
    _xml_members = [
        ("command", None, True, False, None),  # command
    ]

    def __init__(self) -> None:
        """Initialize BuildActionInvocator."""
        super().__init__()
        self.command: Optional[VerbatimString] = None

    def serialize(self, namespace: str, element: Optional[ET.Element] = None) -> ET.Element:
        """Convert BuildActionInvocator to XML element.

        Args:
            namespace: XML namespace for the element
            element: Optional existing element to add members to (for subclass chaining)

        Returns:
            XML element representing this object
        """
        # ARObject.serialize() handles entire class hierarchy automatically
        return super().serialize(namespace, element)

    @classmethod
    def deserialize(cls, element: ET.Element) -> "BuildActionInvocator":
        """Create BuildActionInvocator from XML element.

        Args:
            element: XML element to deserialize from

        Returns:
            BuildActionInvocator instance
        """
        # ARObject.deserialize() handles entire class hierarchy automatically
        obj = super().deserialize(element)
        # Cast to BuildActionInvocator since parent returns ARObject
        return cast("BuildActionInvocator", obj)


class BuildActionInvocatorBuilder:
    """Builder for BuildActionInvocator."""

    def __init__(self) -> None:
        """Initialize builder."""
        self._obj: BuildActionInvocator = BuildActionInvocator()

    def build(self) -> BuildActionInvocator:
        """Build and return BuildActionInvocator object.

        Returns:
            BuildActionInvocator instance
        """
        # TODO: Add validation
        return self._obj
