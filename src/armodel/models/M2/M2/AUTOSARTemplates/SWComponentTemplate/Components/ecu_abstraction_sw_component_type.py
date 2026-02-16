"""EcuAbstractionSwComponentType AUTOSAR element."""

from typing import Optional
import xml.etree.ElementTree as ET
from armodel.serialization import XMLMember

from armodel.models.M2.AUTOSARTemplates.SWComponentTemplate.Components.atomic_sw_component_type import (
    AtomicSwComponentType,
)
from armodel.models.M2.AUTOSARTemplates.EcuResourceTemplate.hw_description_entity import (
    HwDescriptionEntity,
)


class EcuAbstractionSwComponentType(AtomicSwComponentType):
    """AUTOSAR EcuAbstractionSwComponentType."""

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
        """Initialize EcuAbstractionSwComponentType."""
        super().__init__()
        self.hardwares: list[HwDescriptionEntity] = []


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
