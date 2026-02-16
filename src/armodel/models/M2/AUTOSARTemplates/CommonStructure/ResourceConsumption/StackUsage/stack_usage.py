"""StackUsage AUTOSAR element."""

from typing import Optional, cast
import xml.etree.ElementTree as ET
from armodel.models.M2.AUTOSARTemplates.GenericStructure.GeneralTemplateClasses.Identifiable.identifiable import (
    Identifiable,
)
from armodel.models.M2.AUTOSARTemplates.CommonStructure.InternalBehavior.executable_entity import (
    ExecutableEntity,
)
from armodel.models.M2.AUTOSARTemplates.CommonStructure.ResourceConsumption.hardware_configuration import (
    HardwareConfiguration,
)
from armodel.models.M2.AUTOSARTemplates.EcuResourceTemplate.hw_element import (
    HwElement,
)
from armodel.models.M2.AUTOSARTemplates.CommonStructure.ResourceConsumption.software_context import (
    SoftwareContext,
)


class StackUsage(Identifiable):
    """AUTOSAR StackUsage."""
    """Abstract base class - do not instantiate directly."""

    # XML member definitions for this class only (not inherited from parent classes)
    # Format: (member_name, xml_tag_name, is_attribute, is_list, element_class)
    _xml_members = [
        ("executable_entity", None, False, False, ExecutableEntity),  # executableEntity
        ("hardware", None, False, False, HardwareConfiguration),  # hardware
        ("hw_element", None, False, False, HwElement),  # hwElement
        ("software_context", None, False, False, SoftwareContext),  # softwareContext
    ]

    def __init__(self) -> None:
        """Initialize StackUsage."""
        super().__init__()
        self.executable_entity: Optional[ExecutableEntity] = None
        self.hardware: Optional[HardwareConfiguration] = None
        self.hw_element: Optional[HwElement] = None
        self.software_context: Optional[SoftwareContext] = None

    def serialize(self, namespace: str, element: Optional[ET.Element] = None) -> ET.Element:
        """Convert StackUsage to XML element.

        Args:
            namespace: XML namespace for the element
            element: Optional existing element to add members to (for subclass chaining)

        Returns:
            XML element representing this object
        """
        # ARObject.serialize() handles entire class hierarchy automatically
        return super().serialize(namespace, element)

    @classmethod
    def deserialize(cls, element: ET.Element) -> "StackUsage":
        """Create StackUsage from XML element.

        Args:
            element: XML element to deserialize from

        Returns:
            StackUsage instance
        """
        # ARObject.deserialize() handles entire class hierarchy automatically
        obj = super().deserialize(element)
        # Cast to StackUsage since parent returns ARObject
        return cast("StackUsage", obj)


class StackUsageBuilder:
    """Builder for StackUsage."""

    def __init__(self) -> None:
        """Initialize builder."""
        self._obj: StackUsage = StackUsage()

    def build(self) -> StackUsage:
        """Build and return StackUsage object.

        Returns:
            StackUsage instance
        """
        # TODO: Add validation
        return self._obj
