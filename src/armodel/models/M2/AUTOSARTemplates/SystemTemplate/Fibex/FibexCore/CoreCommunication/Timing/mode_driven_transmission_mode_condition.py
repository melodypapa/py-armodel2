"""ModeDrivenTransmissionModeCondition AUTOSAR element."""

from typing import Optional, cast
import xml.etree.ElementTree as ET
from armodel.models.M2.AUTOSARTemplates.GenericStructure.GeneralTemplateClasses.ar_object import ARObject
from armodel.models.M2.AUTOSARTemplates.CommonStructure.ModeDeclaration.mode_declaration import (
    ModeDeclaration,
)


class ModeDrivenTransmissionModeCondition(ARObject):
    """AUTOSAR ModeDrivenTransmissionModeCondition."""

    # XML member definitions for this class only (not inherited from parent classes)
    # Format: (member_name, xml_tag_name, is_attribute, is_list, element_class)
    _xml_members = [
        ("modes", None, False, True, ModeDeclaration),  # modes
    ]

    def __init__(self) -> None:
        """Initialize ModeDrivenTransmissionModeCondition."""
        super().__init__()
        self.modes: list[ModeDeclaration] = []

    def serialize(self, namespace: str, element: Optional[ET.Element] = None) -> ET.Element:
        """Convert ModeDrivenTransmissionModeCondition to XML element.

        Args:
            namespace: XML namespace for the element
            element: Optional existing element to add members to (for subclass chaining)

        Returns:
            XML element representing this object
        """
        # ARObject.serialize() handles entire class hierarchy automatically
        return super().serialize(namespace, element)

    @classmethod
    def deserialize(cls, element: ET.Element) -> "ModeDrivenTransmissionModeCondition":
        """Create ModeDrivenTransmissionModeCondition from XML element.

        Args:
            element: XML element to deserialize from

        Returns:
            ModeDrivenTransmissionModeCondition instance
        """
        # ARObject.deserialize() handles entire class hierarchy automatically
        obj = super().deserialize(element)
        # Cast to ModeDrivenTransmissionModeCondition since parent returns ARObject
        return cast("ModeDrivenTransmissionModeCondition", obj)


class ModeDrivenTransmissionModeConditionBuilder:
    """Builder for ModeDrivenTransmissionModeCondition."""

    def __init__(self) -> None:
        """Initialize builder."""
        self._obj: ModeDrivenTransmissionModeCondition = ModeDrivenTransmissionModeCondition()

    def build(self) -> ModeDrivenTransmissionModeCondition:
        """Build and return ModeDrivenTransmissionModeCondition object.

        Returns:
            ModeDrivenTransmissionModeCondition instance
        """
        # TODO: Add validation
        return self._obj
