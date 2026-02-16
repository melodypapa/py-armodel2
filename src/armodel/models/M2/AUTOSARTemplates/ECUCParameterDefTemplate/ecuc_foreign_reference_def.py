"""EcucForeignReferenceDef AUTOSAR element."""

from typing import Optional, cast
import xml.etree.ElementTree as ET
from armodel.models.M2.AUTOSARTemplates.ECUCParameterDefTemplate.ecuc_abstract_external_reference_def import (
    EcucAbstractExternalReferenceDef,
)
from armodel.models.M2.AUTOSARTemplates.GenericStructure.GeneralTemplateClasses.PrimitiveTypes import (
    String,
)


class EcucForeignReferenceDef(EcucAbstractExternalReferenceDef):
    """AUTOSAR EcucForeignReferenceDef."""

    # XML member definitions for this class only (not inherited from parent classes)
    # Format: (member_name, xml_tag_name, is_attribute, is_list, element_class)
    _xml_members = [
        ("destination_type", None, True, False, None),  # destinationType
    ]

    def __init__(self) -> None:
        """Initialize EcucForeignReferenceDef."""
        super().__init__()
        self.destination_type: Optional[String] = None

    def serialize(self, namespace: str, element: Optional[ET.Element] = None) -> ET.Element:
        """Convert EcucForeignReferenceDef to XML element.

        Args:
            namespace: XML namespace for the element
            element: Optional existing element to add members to (for subclass chaining)

        Returns:
            XML element representing this object
        """
        # ARObject.serialize() handles entire class hierarchy automatically
        return super().serialize(namespace, element)

    @classmethod
    def deserialize(cls, element: ET.Element) -> "EcucForeignReferenceDef":
        """Create EcucForeignReferenceDef from XML element.

        Args:
            element: XML element to deserialize from

        Returns:
            EcucForeignReferenceDef instance
        """
        # ARObject.deserialize() handles entire class hierarchy automatically
        obj = super().deserialize(element)
        # Cast to EcucForeignReferenceDef since parent returns ARObject
        return cast("EcucForeignReferenceDef", obj)


class EcucForeignReferenceDefBuilder:
    """Builder for EcucForeignReferenceDef."""

    def __init__(self) -> None:
        """Initialize builder."""
        self._obj: EcucForeignReferenceDef = EcucForeignReferenceDef()

    def build(self) -> EcucForeignReferenceDef:
        """Build and return EcucForeignReferenceDef object.

        Returns:
            EcucForeignReferenceDef instance
        """
        # TODO: Add validation
        return self._obj
