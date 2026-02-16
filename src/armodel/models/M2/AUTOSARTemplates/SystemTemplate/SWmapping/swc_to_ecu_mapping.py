"""SwcToEcuMapping AUTOSAR element."""

from typing import Optional, cast
import xml.etree.ElementTree as ET
from armodel.models.M2.AUTOSARTemplates.GenericStructure.GeneralTemplateClasses.Identifiable.identifiable import (
    Identifiable,
)
from armodel.models.M2.AUTOSARTemplates.SystemTemplate.Fibex.FibexCore.CoreTopology.ecu_instance import (
    EcuInstance,
)
from armodel.models.M2.AUTOSARTemplates.EcuResourceTemplate.hw_element import (
    HwElement,
)


class SwcToEcuMapping(Identifiable):
    """AUTOSAR SwcToEcuMapping."""

    # XML member definitions for this class only (not inherited from parent classes)
    # Format: (member_name, xml_tag_name, is_attribute, is_list, element_class)
    _xml_members = [
        ("components", None, False, True, any (SwComponent)),  # components
        ("controlled_hw", None, False, False, HwElement),  # controlledHw
        ("ecu_instance", None, False, False, EcuInstance),  # ecuInstance
        ("processing_unit", None, False, False, HwElement),  # processingUnit
    ]

    def __init__(self) -> None:
        """Initialize SwcToEcuMapping."""
        super().__init__()
        self.components: list[Any] = []
        self.controlled_hw: Optional[HwElement] = None
        self.ecu_instance: Optional[EcuInstance] = None
        self.processing_unit: Optional[HwElement] = None

    def serialize(self, namespace: str, element: Optional[ET.Element] = None) -> ET.Element:
        """Convert SwcToEcuMapping to XML element.

        Args:
            namespace: XML namespace for the element
            element: Optional existing element to add members to (for subclass chaining)

        Returns:
            XML element representing this object
        """
        # ARObject.serialize() handles entire class hierarchy automatically
        return super().serialize(namespace, element)

    @classmethod
    def deserialize(cls, element: ET.Element) -> "SwcToEcuMapping":
        """Create SwcToEcuMapping from XML element.

        Args:
            element: XML element to deserialize from

        Returns:
            SwcToEcuMapping instance
        """
        # ARObject.deserialize() handles entire class hierarchy automatically
        obj = super().deserialize(element)
        # Cast to SwcToEcuMapping since parent returns ARObject
        return cast("SwcToEcuMapping", obj)


class SwcToEcuMappingBuilder:
    """Builder for SwcToEcuMapping."""

    def __init__(self) -> None:
        """Initialize builder."""
        self._obj: SwcToEcuMapping = SwcToEcuMapping()

    def build(self) -> SwcToEcuMapping:
        """Build and return SwcToEcuMapping object.

        Returns:
            SwcToEcuMapping instance
        """
        # TODO: Add validation
        return self._obj
