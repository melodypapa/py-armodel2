"""EcuAbstractionSwComponentType AUTOSAR element.

References:
  - AUTOSAR_CP_TPS_BSWModuleDescriptionTemplate.pdf (page 313)
  - AUTOSAR_CP_TPS_SoftwareComponentTemplate.pdf (page 647)
  - AUTOSAR_CP_TPS_SystemTemplate.pdf (page 2020)
  - AUTOSAR_CP_TPS_TimingExtensions.pdf (page 222)

JSON Source: docs/json/packages/M2_AUTOSARTemplates_SWComponentTemplate_Components.classes.json"""

from __future__ import annotations
from typing import TYPE_CHECKING, Optional
import xml.etree.ElementTree as ET

from armodel.models.M2.AUTOSARTemplates.SWComponentTemplate.Components.atomic_sw_component_type import (
    AtomicSwComponentType,
)
from armodel.models.M2.AUTOSARTemplates.GenericStructure.GeneralTemplateClasses.ArObject.ar_object import ARObject
from armodel.models.M2.AUTOSARTemplates.EcuResourceTemplate.hw_description_entity import (
    HwDescriptionEntity,
)


class EcuAbstractionSwComponentType(AtomicSwComponentType):
    """AUTOSAR EcuAbstractionSwComponentType."""

    @property
    def is_abstract(self) -> bool:
        """Check if this class is abstract.

        Returns:
            False for concrete classes
        """
        return False

    hardwares: list[HwDescriptionEntity]
    def __init__(self) -> None:
        """Initialize EcuAbstractionSwComponentType."""
        super().__init__()
        self.hardwares: list[HwDescriptionEntity] = []
    @classmethod
    def deserialize(cls, element: ET.Element) -> "EcuAbstractionSwComponentType":
        """Deserialize XML element to EcuAbstractionSwComponentType object.

        Args:
            element: XML element to deserialize from

        Returns:
            Deserialized EcuAbstractionSwComponentType object
        """
        # First, call parent's deserialize to handle inherited attributes
        obj = super(EcuAbstractionSwComponentType, cls).deserialize(element)

        # Parse hardwares (list from container "HARDWARES")
        obj.hardwares = []
        container = ARObject._find_child_element(element, "HARDWARES")
        if container is not None:
            for child in container:
                # Deserialize each child element dynamically based on its tag
                child_value = ARObject._deserialize_by_tag(child, None)
                if child_value is not None:
                    obj.hardwares.append(child_value)

        return obj



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
