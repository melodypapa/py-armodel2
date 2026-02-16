"""EcucChoiceReferenceDef AUTOSAR element."""

from typing import Optional, cast
import xml.etree.ElementTree as ET
from armodel.models.M2.AUTOSARTemplates.ECUCParameterDefTemplate.ecuc_abstract_internal_reference_def import (
    EcucAbstractInternalReferenceDef,
)
from armodel.models.M2.AUTOSARTemplates.ECUCParameterDefTemplate.ecuc_container_def import (
    EcucContainerDef,
)


class EcucChoiceReferenceDef(EcucAbstractInternalReferenceDef):
    """AUTOSAR EcucChoiceReferenceDef."""

    # XML member definitions for this class only (not inherited from parent classes)
    # Format: (member_name, xml_tag_name, is_attribute, is_list, element_class)
    _xml_members = [
        ("destinations", None, False, True, EcucContainerDef),  # destinations
    ]

    def __init__(self) -> None:
        """Initialize EcucChoiceReferenceDef."""
        super().__init__()
        self.destinations: list[EcucContainerDef] = []

    def serialize(self, namespace: str, element: Optional[ET.Element] = None) -> ET.Element:
        """Convert EcucChoiceReferenceDef to XML element.

        Args:
            namespace: XML namespace for the element
            element: Optional existing element to add members to (for subclass chaining)

        Returns:
            XML element representing this object
        """
        # ARObject.serialize() handles entire class hierarchy automatically
        return super().serialize(namespace, element)

    @classmethod
    def deserialize(cls, element: ET.Element) -> "EcucChoiceReferenceDef":
        """Create EcucChoiceReferenceDef from XML element.

        Args:
            element: XML element to deserialize from

        Returns:
            EcucChoiceReferenceDef instance
        """
        # ARObject.deserialize() handles entire class hierarchy automatically
        obj = super().deserialize(element)
        # Cast to EcucChoiceReferenceDef since parent returns ARObject
        return cast("EcucChoiceReferenceDef", obj)


class EcucChoiceReferenceDefBuilder:
    """Builder for EcucChoiceReferenceDef."""

    def __init__(self) -> None:
        """Initialize builder."""
        self._obj: EcucChoiceReferenceDef = EcucChoiceReferenceDef()

    def build(self) -> EcucChoiceReferenceDef:
        """Build and return EcucChoiceReferenceDef object.

        Returns:
            EcucChoiceReferenceDef instance
        """
        # TODO: Add validation
        return self._obj
