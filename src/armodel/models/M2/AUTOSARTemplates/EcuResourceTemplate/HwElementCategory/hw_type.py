"""HwType AUTOSAR element.

References:
  - AUTOSAR_CP_TPS_ECUResourceTemplate.pdf (page 17)
  - AUTOSAR_CP_TPS_SoftwareComponentTemplate.pdf (page 991)

JSON Source: docs/json/packages/M2_AUTOSARTemplates_EcuResourceTemplate_HwElementCategory.classes.json"""

from typing import Optional
import xml.etree.ElementTree as ET
from armodel.serialization import XMLMember

from armodel.models.M2.AUTOSARTemplates.EcuResourceTemplate.hw_description_entity import (
    HwDescriptionEntity,
)


class HwType(HwDescriptionEntity):
    """AUTOSAR HwType."""

    # XML member definitions for this class only (not inherited from parent classes)
    # Format: dict[str, XMLMember] for declarative metadata
    _xml_members: dict[str, "XMLMember"] = {
    }

    def __init__(self) -> None:
        """Initialize HwType."""
        super().__init__()


class HwTypeBuilder:
    """Builder for HwType."""

    def __init__(self) -> None:
        """Initialize builder."""
        self._obj: HwType = HwType()

    def build(self) -> HwType:
        """Build and return HwType object.

        Returns:
            HwType instance
        """
        # TODO: Add validation
        return self._obj
