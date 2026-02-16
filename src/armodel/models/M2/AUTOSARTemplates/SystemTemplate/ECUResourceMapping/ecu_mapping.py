"""ECUMapping AUTOSAR element."""

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
from armodel.models.M2.AUTOSARTemplates.SystemTemplate.ECUResourceMapping.hw_port_mapping import (
    HwPortMapping,
)


class ECUMapping(Identifiable):
    """AUTOSAR ECUMapping."""

    # XML member definitions for this class only (not inherited from parent classes)
    # Format: (member_name, xml_tag_name, is_attribute, is_list, element_class)
    _xml_members = [
        ("comm_controllers", None, False, True, any (Communication)),  # commControllers
        ("ecu", None, False, False, HwElement),  # ecu
        ("ecu_instance", None, False, False, EcuInstance),  # ecuInstance
        ("hw_port_mapping", None, False, False, HwPortMapping),  # hwPortMapping
    ]

    def __init__(self) -> None:
        """Initialize ECUMapping."""
        super().__init__()
        self.comm_controllers: list[Any] = []
        self.ecu: Optional[HwElement] = None
        self.ecu_instance: Optional[EcuInstance] = None
        self.hw_port_mapping: HwPortMapping = None

    def serialize(self, namespace: str, element: Optional[ET.Element] = None) -> ET.Element:
        """Convert ECUMapping to XML element.

        Args:
            namespace: XML namespace for the element
            element: Optional existing element to add members to (for subclass chaining)

        Returns:
            XML element representing this object
        """
        # ARObject.serialize() handles entire class hierarchy automatically
        return super().serialize(namespace, element)

    @classmethod
    def deserialize(cls, element: ET.Element) -> "ECUMapping":
        """Create ECUMapping from XML element.

        Args:
            element: XML element to deserialize from

        Returns:
            ECUMapping instance
        """
        # ARObject.deserialize() handles entire class hierarchy automatically
        obj = super().deserialize(element)
        # Cast to ECUMapping since parent returns ARObject
        return cast("ECUMapping", obj)


class ECUMappingBuilder:
    """Builder for ECUMapping."""

    def __init__(self) -> None:
        """Initialize builder."""
        self._obj: ECUMapping = ECUMapping()

    def build(self) -> ECUMapping:
        """Build and return ECUMapping object.

        Returns:
            ECUMapping instance
        """
        # TODO: Add validation
        return self._obj
