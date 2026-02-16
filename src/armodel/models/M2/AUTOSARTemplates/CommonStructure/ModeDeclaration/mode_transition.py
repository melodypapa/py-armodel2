"""ModeTransition AUTOSAR element."""

from typing import Optional, cast
import xml.etree.ElementTree as ET
from armodel.models.M2.AUTOSARTemplates.GenericStructure.GeneralTemplateClasses.Identifiable.identifiable import (
    Identifiable,
)
from armodel.models.M2.AUTOSARTemplates.CommonStructure.ModeDeclaration.mode_declaration import (
    ModeDeclaration,
)


class ModeTransition(Identifiable):
    """AUTOSAR ModeTransition."""

    # XML member definitions for this class only (not inherited from parent classes)
    # Format: (member_name, xml_tag_name, is_attribute, is_list, element_class)
    _xml_members = [
        ("entered_mode", None, False, False, ModeDeclaration),  # enteredMode
        ("exited_mode", None, False, False, ModeDeclaration),  # exitedMode
    ]

    def __init__(self) -> None:
        """Initialize ModeTransition."""
        super().__init__()
        self.entered_mode: Optional[ModeDeclaration] = None
        self.exited_mode: Optional[ModeDeclaration] = None

    def serialize(self, namespace: str, element: Optional[ET.Element] = None) -> ET.Element:
        """Convert ModeTransition to XML element.

        Args:
            namespace: XML namespace for the element
            element: Optional existing element to add members to (for subclass chaining)

        Returns:
            XML element representing this object
        """
        # ARObject.serialize() handles entire class hierarchy automatically
        return super().serialize(namespace, element)

    @classmethod
    def deserialize(cls, element: ET.Element) -> "ModeTransition":
        """Create ModeTransition from XML element.

        Args:
            element: XML element to deserialize from

        Returns:
            ModeTransition instance
        """
        # ARObject.deserialize() handles entire class hierarchy automatically
        obj = super().deserialize(element)
        # Cast to ModeTransition since parent returns ARObject
        return cast("ModeTransition", obj)


class ModeTransitionBuilder:
    """Builder for ModeTransition."""

    def __init__(self) -> None:
        """Initialize builder."""
        self._obj: ModeTransition = ModeTransition()

    def build(self) -> ModeTransition:
        """Build and return ModeTransition object.

        Returns:
            ModeTransition instance
        """
        # TODO: Add validation
        return self._obj
