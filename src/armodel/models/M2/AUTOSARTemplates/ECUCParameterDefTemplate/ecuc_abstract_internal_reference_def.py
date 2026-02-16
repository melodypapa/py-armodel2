"""EcucAbstractInternalReferenceDef AUTOSAR element."""

from typing import Optional, cast
import xml.etree.ElementTree as ET
from armodel.models.M2.AUTOSARTemplates.ECUCParameterDefTemplate.ecuc_abstract_reference_def import (
    EcucAbstractReferenceDef,
)
from armodel.models.M2.AUTOSARTemplates.GenericStructure.GeneralTemplateClasses.PrimitiveTypes import (
    Boolean,
)


class EcucAbstractInternalReferenceDef(EcucAbstractReferenceDef):
    """AUTOSAR EcucAbstractInternalReferenceDef."""
    """Abstract base class - do not instantiate directly."""

    # XML member definitions for this class only (not inherited from parent classes)
    # Format: (member_name, xml_tag_name, is_attribute, is_list, element_class)
    _xml_members = [
        ("requires", None, True, False, None),  # requires
    ]

    def __init__(self) -> None:
        """Initialize EcucAbstractInternalReferenceDef."""
        super().__init__()
        self.requires: Optional[Boolean] = None

    def serialize(self, namespace: str, element: Optional[ET.Element] = None) -> ET.Element:
        """Convert EcucAbstractInternalReferenceDef to XML element.

        Args:
            namespace: XML namespace for the element
            element: Optional existing element to add members to (for subclass chaining)

        Returns:
            XML element representing this object
        """
        # ARObject.serialize() handles entire class hierarchy automatically
        return super().serialize(namespace, element)

    @classmethod
    def deserialize(cls, element: ET.Element) -> "EcucAbstractInternalReferenceDef":
        """Create EcucAbstractInternalReferenceDef from XML element.

        Args:
            element: XML element to deserialize from

        Returns:
            EcucAbstractInternalReferenceDef instance
        """
        # ARObject.deserialize() handles entire class hierarchy automatically
        obj = super().deserialize(element)
        # Cast to EcucAbstractInternalReferenceDef since parent returns ARObject
        return cast("EcucAbstractInternalReferenceDef", obj)


class EcucAbstractInternalReferenceDefBuilder:
    """Builder for EcucAbstractInternalReferenceDef."""

    def __init__(self) -> None:
        """Initialize builder."""
        self._obj: EcucAbstractInternalReferenceDef = EcucAbstractInternalReferenceDef()

    def build(self) -> EcucAbstractInternalReferenceDef:
        """Build and return EcucAbstractInternalReferenceDef object.

        Returns:
            EcucAbstractInternalReferenceDef instance
        """
        # TODO: Add validation
        return self._obj
