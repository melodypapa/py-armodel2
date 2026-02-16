"""EcuAbstractionSwComponentType AUTOSAR element."""

from typing import Optional, cast
import xml.etree.ElementTree as ET
from armodel.models.M2.AUTOSARTemplates.SWComponentTemplate.Components.atomic_sw_component_type import (
    AtomicSwComponentType,
)
from armodel.models.M2.AUTOSARTemplates.EcuResourceTemplate.hw_description_entity import (
    HwDescriptionEntity,
)


class EcuAbstractionSwComponentType(AtomicSwComponentType):
    """AUTOSAR EcuAbstractionSwComponentType."""

    # XML member definitions for this class only (not inherited from parent classes)
    # Format: (member_name, xml_tag_name, is_attribute, is_list, element_class)
    _xml_members = [
        ("hardwares", None, False, True, HwDescriptionEntity),  # hardwares
    ]

    def __init__(self) -> None:
        """Initialize EcuAbstractionSwComponentType."""
        super().__init__()
        self.hardwares: list[HwDescriptionEntity] = []

    def serialize(self, namespace: str, element: Optional[ET.Element] = None) -> ET.Element:
        """Convert EcuAbstractionSwComponentType to XML element.

        Args:
            namespace: XML namespace for the element
            element: Optional existing element to add members to (for subclass chaining)

        Returns:
            XML element representing this object
        """
        # ARObject.serialize() handles entire class hierarchy automatically
        return super().serialize(namespace, element)

    @classmethod
    def deserialize(cls, element: ET.Element) -> "EcuAbstractionSwComponentType":
        """Create EcuAbstractionSwComponentType from XML element.

        Args:
            element: XML element to deserialize from

        Returns:
            EcuAbstractionSwComponentType instance
        """
        # ARObject.deserialize() handles entire class hierarchy automatically
        obj = super().deserialize(element)
        # Cast to EcuAbstractionSwComponentType since parent returns ARObject
        return cast("EcuAbstractionSwComponentType", obj)


class EcuAbstractionSwComponentTypeBuilder:
    """Builder for EcuAbstractionSwComponentType."""

    def __init__(self) -> None:
        """Initialize builder."""
        self._obj: EcuAbstractionSwComponentType = EcuAbstractionSwComponentType()

    def build(self) -> EcuAbstractionSwComponentType:
        """Build and return EcuAbstractionSwComponentType object.

        Returns:
            EcuAbstractionSwComponentType instance
        """
        # TODO: Add validation
        return self._obj
