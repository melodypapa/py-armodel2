"""ComplexDeviceDriverSwComponentType AUTOSAR element.

References:
  - AUTOSAR_CP_TPS_BSWModuleDescriptionTemplate.pdf (page 310)
  - AUTOSAR_CP_TPS_SoftwareComponentTemplate.pdf (page 648)
  - AUTOSAR_CP_TPS_SystemTemplate.pdf (page 2010)
  - AUTOSAR_CP_TPS_TimingExtensions.pdf (page 218)

JSON Source: docs/json/packages/M2_AUTOSARTemplates_SWComponentTemplate_Components.classes.json"""

from __future__ import annotations
from typing import TYPE_CHECKING, Optional
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
