"""EcucAbstractExternalReferenceDef AUTOSAR element."""

from typing import Optional, cast
import xml.etree.ElementTree as ET
from armodel.models.M2.AUTOSARTemplates.ECUCParameterDefTemplate.ecuc_abstract_reference_def import (
    EcucAbstractReferenceDef,
)


class EcucAbstractExternalReferenceDef(EcucAbstractReferenceDef):
    """AUTOSAR EcucAbstractExternalReferenceDef."""
    """Abstract base class - do not instantiate directly."""

    # XML member definitions for this class only (not inherited from parent classes)
    # Format: (member_name, xml_tag_name, is_attribute, is_list, element_class)
    _xml_members = [
    ]

    def __init__(self) -> None:
        """Initialize EcucAbstractExternalReferenceDef."""
        super().__init__()

    def serialize(self, namespace: str, element: Optional[ET.Element] = None) -> ET.Element:
        """Convert EcucAbstractExternalReferenceDef to XML element.

        Args:
            namespace: XML namespace for the element
            element: Optional existing element to add members to (for subclass chaining)

        Returns:
            XML element representing this object
        """
        # ARObject.serialize() handles entire class hierarchy automatically
        return super().serialize(namespace, element)

    @classmethod
    def deserialize(cls, element: ET.Element) -> "EcucAbstractExternalReferenceDef":
        """Create EcucAbstractExternalReferenceDef from XML element.

        Args:
            element: XML element to deserialize from

        Returns:
            EcucAbstractExternalReferenceDef instance
        """
        # ARObject.deserialize() handles entire class hierarchy automatically
        obj = super().deserialize(element)
        # Cast to EcucAbstractExternalReferenceDef since parent returns ARObject
        return cast("EcucAbstractExternalReferenceDef", obj)


class EcucAbstractExternalReferenceDefBuilder:
    """Builder for EcucAbstractExternalReferenceDef."""

    def __init__(self) -> None:
        """Initialize builder."""
        self._obj: EcucAbstractExternalReferenceDef = EcucAbstractExternalReferenceDef()

    def build(self) -> EcucAbstractExternalReferenceDef:
        """Build and return EcucAbstractExternalReferenceDef object.

        Returns:
            EcucAbstractExternalReferenceDef instance
        """
        # TODO: Add validation
        return self._obj
