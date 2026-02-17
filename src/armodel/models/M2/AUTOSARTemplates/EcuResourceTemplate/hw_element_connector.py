"""HwElementConnector AUTOSAR element.

References:
  - AUTOSAR_CP_TPS_ECUResourceTemplate.pdf (page 21)

JSON Source: docs/json/packages/M2_AUTOSARTemplates_EcuResourceTemplate.classes.json"""

from __future__ import annotations
from typing import TYPE_CHECKING, Optional
import xml.etree.ElementTree as ET
from armodel.serialization import XMLMember

from armodel.models.M2.AUTOSARTemplates.GenericStructure.GeneralTemplateClasses.Identifiable.describable import (
    Describable,
)
from armodel.models.M2.AUTOSARTemplates.EcuResourceTemplate.hw_element import (
    HwElement,
)
from armodel.models.M2.AUTOSARTemplates.EcuResourceTemplate.hw_pin_connector import (
    HwPinConnector,
)
from armodel.models.M2.AUTOSARTemplates.EcuResourceTemplate.hw_pin_group_connector import (
    HwPinGroupConnector,
)


class HwElementConnector(Describable):
    """AUTOSAR HwElementConnector."""

    # XML member definitions for this class only (not inherited from parent classes)
    # Format: dict[str, XMLMember] for declarative metadata
    _xml_members: dict[str, "XMLMember"] = {
        "hw_elements": XMLMember(
            xml_tag=None,
            is_attribute=False,
            multiplicity="*",
            element_class=HwElement,
        ),  # hwElements
        "hw_pins": XMLMember(
            xml_tag=None,
            is_attribute=False,
            multiplicity="*",
            element_class=HwPinConnector,
        ),  # hwPins
        "hw_pin_groups": XMLMember(
            xml_tag=None,
            is_attribute=False,
            multiplicity="*",
            element_class=HwPinGroupConnector,
        ),  # hwPinGroups
    }

    def __init__(self) -> None:
        """Initialize HwElementConnector."""
        super().__init__()
        self.hw_elements: list[HwElement] = []
        self.hw_pins: list[HwPinConnector] = []
        self.hw_pin_groups: list[HwPinGroupConnector] = []


class HwElementConnectorBuilder:
    """Builder for HwElementConnector."""

    def __init__(self) -> None:
        """Initialize builder."""
        self._obj: HwElementConnector = HwElementConnector()

    def build(self) -> HwElementConnector:
        """Build and return HwElementConnector object.

        Returns:
            HwElementConnector instance
        """
        # TODO: Add validation
        return self._obj
