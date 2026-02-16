"""EcucAddInfoParamDef AUTOSAR element."""

from typing import Optional, cast
import xml.etree.ElementTree as ET
from armodel.models.M2.AUTOSARTemplates.ECUCParameterDefTemplate.ecuc_parameter_def import (
    EcucParameterDef,
)


class EcucAddInfoParamDef(EcucParameterDef):
    """AUTOSAR EcucAddInfoParamDef."""

    # XML member definitions for this class only (not inherited from parent classes)
    # Format: (member_name, xml_tag_name, is_attribute, is_list, element_class)
    _xml_members = [
    ]

    def __init__(self) -> None:
        """Initialize EcucAddInfoParamDef."""
        super().__init__()

    def serialize(self, namespace: str, element: Optional[ET.Element] = None) -> ET.Element:
        """Convert EcucAddInfoParamDef to XML element.

        Args:
            namespace: XML namespace for the element
            element: Optional existing element to add members to (for subclass chaining)

        Returns:
            XML element representing this object
        """
        # ARObject.serialize() handles entire class hierarchy automatically
        return super().serialize(namespace, element)

    @classmethod
    def deserialize(cls, element: ET.Element) -> "EcucAddInfoParamDef":
        """Create EcucAddInfoParamDef from XML element.

        Args:
            element: XML element to deserialize from

        Returns:
            EcucAddInfoParamDef instance
        """
        # ARObject.deserialize() handles entire class hierarchy automatically
        obj = super().deserialize(element)
        # Cast to EcucAddInfoParamDef since parent returns ARObject
        return cast("EcucAddInfoParamDef", obj)


class EcucAddInfoParamDefBuilder:
    """Builder for EcucAddInfoParamDef."""

    def __init__(self) -> None:
        """Initialize builder."""
        self._obj: EcucAddInfoParamDef = EcucAddInfoParamDef()

    def build(self) -> EcucAddInfoParamDef:
        """Build and return EcucAddInfoParamDef object.

        Returns:
            EcucAddInfoParamDef instance
        """
        # TODO: Add validation
        return self._obj
