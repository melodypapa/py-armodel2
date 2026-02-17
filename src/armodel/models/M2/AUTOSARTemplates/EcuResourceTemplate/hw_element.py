"""HwElement AUTOSAR element."""

from typing import Optional
import xml.etree.ElementTree as ET
from armodel.serialization import XMLMember

from armodel.models.M2.AUTOSARTemplates.EcuResourceTemplate.hw_description_entity import (
    HwDescriptionEntity,
)
from armodel.models.M2.AUTOSARTemplates.EcuResourceTemplate.hw_element_connector import (
    HwElementConnector,
)
from armodel.models.M2.AUTOSARTemplates.EcuResourceTemplate.hw_pin_group import (
    HwPinGroup,
)


class HwElement(HwDescriptionEntity):
    """AUTOSAR HwElement."""

    # XML member definitions for this class only (not inherited from parent classes)
    # Format: dict[str, XMLMember] for declarative metadata
    _xml_members: dict[str, "XMLMember"] = {
        "hw_elements": XMLMember(
            xml_tag=None,
            is_attribute=False,
            multiplicity="*",
            element_class=HwElementConnector,
        ),  # hwElements
        "hw_pin_groups": XMLMember(
            xml_tag=None,
            is_attribute=False,
            multiplicity="*",
            element_class=HwPinGroup,
        ),  # hwPinGroups
        "nested_elements": XMLMember(
            xml_tag=None,
            is_attribute=False,
            multiplicity="*",
            element_class=HwElement,
        ),  # nestedElements
    }

    def __init__(self) -> None:
        """Initialize HwElement."""
        super().__init__()
        self.hw_elements: list[HwElementConnector] = []
        self.hw_pin_groups: list[HwPinGroup] = []
        self.nested_elements: list[HwElement] = []


class HwElementBuilder:
    """Builder for HwElement."""

    def __init__(self) -> None:
        """Initialize builder."""
        self._obj: HwElement = HwElement()

    def build(self) -> HwElement:
        """Build and return HwElement object.

        Returns:
            HwElement instance
        """
        # TODO: Add validation
        return self._obj
