"""HwPinConnector AUTOSAR element.

References:
  - AUTOSAR_CP_TPS_ECUResourceTemplate.pdf (page 22)

JSON Source: docs/json/packages/M2_AUTOSARTemplates_EcuResourceTemplate.classes.json"""

from __future__ import annotations
from typing import TYPE_CHECKING, Optional
import xml.etree.ElementTree as ET
from armodel.serialization import XMLMember

from armodel.models.M2.AUTOSARTemplates.GenericStructure.GeneralTemplateClasses.Identifiable.describable import (
    Describable,
)
from armodel.models.M2.AUTOSARTemplates.EcuResourceTemplate.hw_pin import (
    HwPin,
)


class HwPinConnector(Describable):
    """AUTOSAR HwPinConnector."""

    # XML member definitions for this class only (not inherited from parent classes)
    # Format: dict[str, XMLMember] for declarative metadata
    _xml_members: dict[str, "XMLMember"] = {
        "hw_pins": XMLMember(
            xml_tag=None,
            is_attribute=False,
            multiplicity="*",
            element_class=HwPin,
        ),  # hwPins
    }

    def __init__(self) -> None:
        """Initialize HwPinConnector."""
        super().__init__()
        self.hw_pins: list[HwPin] = []


class HwPinConnectorBuilder:
    """Builder for HwPinConnector."""

    def __init__(self) -> None:
        """Initialize builder."""
        self._obj: HwPinConnector = HwPinConnector()

    def build(self) -> HwPinConnector:
        """Build and return HwPinConnector object.

        Returns:
            HwPinConnector instance
        """
        # TODO: Add validation
        return self._obj
