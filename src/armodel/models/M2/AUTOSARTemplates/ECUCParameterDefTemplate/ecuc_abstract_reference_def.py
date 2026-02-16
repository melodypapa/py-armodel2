"""EcucAbstractReferenceDef AUTOSAR element."""

from typing import Optional, cast
import xml.etree.ElementTree as ET
from armodel.models.M2.AUTOSARTemplates.ECUCParameterDefTemplate.ecuc_common_attributes import (
    EcucCommonAttributes,
)
from armodel.models.M2.AUTOSARTemplates.GenericStructure.GeneralTemplateClasses.PrimitiveTypes import (
    Boolean,
)


class EcucAbstractReferenceDef(EcucCommonAttributes):
    """AUTOSAR EcucAbstractReferenceDef."""
    """Abstract base class - do not instantiate directly."""

    # XML member definitions for this class only (not inherited from parent classes)
    # Format: (member_name, xml_tag_name, is_attribute, is_list, element_class)
    _xml_members = [
        ("with_auto", None, True, False, None),  # withAuto
    ]

    def __init__(self) -> None:
        """Initialize EcucAbstractReferenceDef."""
        super().__init__()
        self.with_auto: Optional[Boolean] = None

    def serialize(self, namespace: str, element: Optional[ET.Element] = None) -> ET.Element:
        """Convert EcucAbstractReferenceDef to XML element.

        Args:
            namespace: XML namespace for the element
            element: Optional existing element to add members to (for subclass chaining)

        Returns:
            XML element representing this object
        """
        # ARObject.serialize() handles entire class hierarchy automatically
        return super().serialize(namespace, element)

    @classmethod
    def deserialize(cls, element: ET.Element) -> "EcucAbstractReferenceDef":
        """Create EcucAbstractReferenceDef from XML element.

        Args:
            element: XML element to deserialize from

        Returns:
            EcucAbstractReferenceDef instance
        """
        # ARObject.deserialize() handles entire class hierarchy automatically
        obj = super().deserialize(element)
        # Cast to EcucAbstractReferenceDef since parent returns ARObject
        return cast("EcucAbstractReferenceDef", obj)


class EcucAbstractReferenceDefBuilder:
    """Builder for EcucAbstractReferenceDef."""

    def __init__(self) -> None:
        """Initialize builder."""
        self._obj: EcucAbstractReferenceDef = EcucAbstractReferenceDef()

    def build(self) -> EcucAbstractReferenceDef:
        """Build and return EcucAbstractReferenceDef object.

        Returns:
            EcucAbstractReferenceDef instance
        """
        # TODO: Add validation
        return self._obj
