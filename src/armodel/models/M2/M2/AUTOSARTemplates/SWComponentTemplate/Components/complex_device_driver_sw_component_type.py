"""ComplexDeviceDriverSwComponentType AUTOSAR element."""

from typing import Optional
import xml.etree.ElementTree as ET
from armodel.serialization import XMLMember

from armodel.models.M2.AUTOSARTemplates.SWComponentTemplate.Components.atomic_sw_component_type import (
    AtomicSwComponentType,
)
from armodel.models.M2.AUTOSARTemplates.EcuResourceTemplate.hw_description_entity import (
    HwDescriptionEntity,
)


class ComplexDeviceDriverSwComponentType(AtomicSwComponentType):
    """AUTOSAR ComplexDeviceDriverSwComponentType."""

    # XML member definitions for this class only (not inherited from parent classes)
    # Format: dict[str, XMLMember] for declarative metadata
    _xml_members: dict[str, "XMLMember"] = {
        "hardwares": XMLMember(
            xml_tag=None,
            is_attribute=False,
            multiplicity="*",
            element_class=HwDescriptionEntity,
        ),  # hardwares
    }

    def __init__(self) -> None:
        """Initialize ComplexDeviceDriverSwComponentType."""
        super().__init__()
        self.hardwares: list[HwDescriptionEntity] = []


class ComplexDeviceDriverSwComponentTypeBuilder:
    """Builder for ComplexDeviceDriverSwComponentType."""

    def __init__(self) -> None:
        """Initialize builder."""
        self._obj: ComplexDeviceDriverSwComponentType = ComplexDeviceDriverSwComponentType()

    def build(self) -> ComplexDeviceDriverSwComponentType:
        """Build and return ComplexDeviceDriverSwComponentType object.

        Returns:
            ComplexDeviceDriverSwComponentType instance
        """
        # TODO: Add validation
        return self._obj
