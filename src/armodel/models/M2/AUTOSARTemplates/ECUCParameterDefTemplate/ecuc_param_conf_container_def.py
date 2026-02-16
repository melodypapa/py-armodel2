"""EcucParamConfContainerDef AUTOSAR element."""

from typing import Optional, cast
import xml.etree.ElementTree as ET
from armodel.models.M2.AUTOSARTemplates.ECUCParameterDefTemplate.ecuc_container_def import (
    EcucContainerDef,
)
from armodel.models.M2.AUTOSARTemplates.ECUCParameterDefTemplate.ecuc_parameter_def import (
    EcucParameterDef,
)


class EcucParamConfContainerDef(EcucContainerDef):
    """AUTOSAR EcucParamConfContainerDef."""

    # XML member definitions for this class only (not inherited from parent classes)
    # Format: (member_name, xml_tag_name, is_attribute, is_list, element_class)
    _xml_members = [
        ("parameters", None, False, True, EcucParameterDef),  # parameters
        ("references", None, False, True, any (EcucAbstractReference)),  # references
        ("sub_containers", None, False, True, EcucContainerDef),  # subContainers
    ]

    def __init__(self) -> None:
        """Initialize EcucParamConfContainerDef."""
        super().__init__()
        self.parameters: list[EcucParameterDef] = []
        self.references: list[Any] = []
        self.sub_containers: list[EcucContainerDef] = []

    def serialize(self, namespace: str, element: Optional[ET.Element] = None) -> ET.Element:
        """Convert EcucParamConfContainerDef to XML element.

        Args:
            namespace: XML namespace for the element
            element: Optional existing element to add members to (for subclass chaining)

        Returns:
            XML element representing this object
        """
        # ARObject.serialize() handles entire class hierarchy automatically
        return super().serialize(namespace, element)

    @classmethod
    def deserialize(cls, element: ET.Element) -> "EcucParamConfContainerDef":
        """Create EcucParamConfContainerDef from XML element.

        Args:
            element: XML element to deserialize from

        Returns:
            EcucParamConfContainerDef instance
        """
        # ARObject.deserialize() handles entire class hierarchy automatically
        obj = super().deserialize(element)
        # Cast to EcucParamConfContainerDef since parent returns ARObject
        return cast("EcucParamConfContainerDef", obj)


class EcucParamConfContainerDefBuilder:
    """Builder for EcucParamConfContainerDef."""

    def __init__(self) -> None:
        """Initialize builder."""
        self._obj: EcucParamConfContainerDef = EcucParamConfContainerDef()

    def build(self) -> EcucParamConfContainerDef:
        """Build and return EcucParamConfContainerDef object.

        Returns:
            EcucParamConfContainerDef instance
        """
        # TODO: Add validation
        return self._obj
