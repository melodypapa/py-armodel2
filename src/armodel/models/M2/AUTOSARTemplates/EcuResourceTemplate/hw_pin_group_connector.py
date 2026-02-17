"""HwPinGroupConnector AUTOSAR element.

References:
  - AUTOSAR_CP_TPS_ECUResourceTemplate.pdf (page 22)

JSON Source: docs/json/packages/M2_AUTOSARTemplates_EcuResourceTemplate.classes.json"""

from typing import Optional
import xml.etree.ElementTree as ET
from armodel.serialization import XMLMember

from armodel.models.M2.AUTOSARTemplates.GenericStructure.GeneralTemplateClasses.Identifiable.describable import (
    Describable,
)
from armodel.models.M2.AUTOSARTemplates.EcuResourceTemplate.hw_pin_connector import (
    HwPinConnector,
)
from armodel.models.M2.AUTOSARTemplates.EcuResourceTemplate.hw_pin_group import (
    HwPinGroup,
)


class HwPinGroupConnector(Describable):
    """AUTOSAR HwPinGroupConnector."""

    # XML member definitions for this class only (not inherited from parent classes)
    # Format: dict[str, XMLMember] for declarative metadata
    _xml_members: dict[str, "XMLMember"] = {
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
            element_class=HwPinGroup,
        ),  # hwPinGroups
    }

    def __init__(self) -> None:
        """Initialize HwPinGroupConnector."""
        super().__init__()
        self.hw_pins: list[HwPinConnector] = []
        self.hw_pin_groups: list[HwPinGroup] = []


class HwPinGroupConnectorBuilder:
    """Builder for HwPinGroupConnector."""

    def __init__(self) -> None:
        """Initialize builder."""
        self._obj: HwPinGroupConnector = HwPinGroupConnector()

    def build(self) -> HwPinGroupConnector:
        """Build and return HwPinGroupConnector object.

        Returns:
            HwPinGroupConnector instance
        """
        # TODO: Add validation
        return self._obj
