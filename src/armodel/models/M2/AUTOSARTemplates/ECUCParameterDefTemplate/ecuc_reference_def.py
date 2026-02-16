"""EcucReferenceDef AUTOSAR element."""

from typing import Optional, cast
import xml.etree.ElementTree as ET
from armodel.models.M2.AUTOSARTemplates.ECUCParameterDefTemplate.ecuc_abstract_internal_reference_def import (
    EcucAbstractInternalReferenceDef,
)
from armodel.models.M2.AUTOSARTemplates.ECUCParameterDefTemplate.ecuc_container_def import (
    EcucContainerDef,
)


class EcucReferenceDef(EcucAbstractInternalReferenceDef):
    """AUTOSAR EcucReferenceDef."""

    # XML member definitions for this class only (not inherited from parent classes)
    # Format: (member_name, xml_tag_name, is_attribute, is_list, element_class)
    _xml_members = [
        ("destination", None, False, False, EcucContainerDef),  # destination
    ]

    def __init__(self) -> None:
        """Initialize EcucReferenceDef."""
        super().__init__()
        self.destination: Optional[EcucContainerDef] = None

    def serialize(self, namespace: str, element: Optional[ET.Element] = None) -> ET.Element:
        """Convert EcucReferenceDef to XML element.

        Args:
            namespace: XML namespace for the element
            element: Optional existing element to add members to (for subclass chaining)

        Returns:
            XML element representing this object
        """
        # ARObject.serialize() handles entire class hierarchy automatically
        return super().serialize(namespace, element)

    @classmethod
    def deserialize(cls, element: ET.Element) -> "EcucReferenceDef":
        """Create EcucReferenceDef from XML element.

        Args:
            element: XML element to deserialize from

        Returns:
            EcucReferenceDef instance
        """
        # ARObject.deserialize() handles entire class hierarchy automatically
        obj = super().deserialize(element)
        # Cast to EcucReferenceDef since parent returns ARObject
        return cast("EcucReferenceDef", obj)


class EcucReferenceDefBuilder:
    """Builder for EcucReferenceDef."""

    def __init__(self) -> None:
        """Initialize builder."""
        self._obj: EcucReferenceDef = EcucReferenceDef()

    def build(self) -> EcucReferenceDef:
        """Build and return EcucReferenceDef object.

        Returns:
            EcucReferenceDef instance
        """
        # TODO: Add validation
        return self._obj
