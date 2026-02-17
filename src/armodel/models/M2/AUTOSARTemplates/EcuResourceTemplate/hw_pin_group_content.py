"""HwPinGroupContent AUTOSAR element.

References:
  - AUTOSAR_CP_TPS_ECUResourceTemplate.pdf (page 20)

JSON Source: docs/json/packages/M2_AUTOSARTemplates_EcuResourceTemplate.classes.json"""

from __future__ import annotations
from typing import TYPE_CHECKING, Optional
import xml.etree.ElementTree as ET
from armodel.serialization import XMLMember

from armodel.models.M2.AUTOSARTemplates.GenericStructure.GeneralTemplateClasses.ArObject.ar_object import ARObject
from armodel.models.M2.AUTOSARTemplates.EcuResourceTemplate.hw_pin import (
    HwPin,
)
from armodel.models.M2.AUTOSARTemplates.EcuResourceTemplate.hw_pin_group import (
    HwPinGroup,
)


class HwPinGroupContent(ARObject):
    """AUTOSAR HwPinGroupContent."""

    # XML member definitions for this class only (not inherited from parent classes)
    # Format: dict[str, XMLMember] for declarative metadata
    _xml_members: dict[str, "XMLMember"] = {
        "hw_pin": XMLMember(
            xml_tag=None,
            is_attribute=False,
            multiplicity="0..1",
            element_class=HwPin,
        ),  # hwPin
        "hw_pin_group": XMLMember(
            xml_tag=None,
            is_attribute=False,
            multiplicity="0..1",
            element_class=HwPinGroup,
        ),  # hwPinGroup
    }

    def __init__(self) -> None:
        """Initialize HwPinGroupContent."""
        super().__init__()
        self.hw_pin: Optional[HwPin] = None
        self.hw_pin_group: Optional[HwPinGroup] = None


class HwPinGroupContentBuilder:
    """Builder for HwPinGroupContent."""

    def __init__(self) -> None:
        """Initialize builder."""
        self._obj: HwPinGroupContent = HwPinGroupContent()

    def build(self) -> HwPinGroupContent:
        """Build and return HwPinGroupContent object.

        Returns:
            HwPinGroupContent instance
        """
        # TODO: Add validation
        return self._obj
