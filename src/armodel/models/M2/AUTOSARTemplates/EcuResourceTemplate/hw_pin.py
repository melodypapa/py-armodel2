"""HwPin AUTOSAR element.

References:
  - AUTOSAR_CP_TPS_ECUResourceTemplate.pdf (page 20)

JSON Source: docs/json/packages/M2_AUTOSARTemplates_EcuResourceTemplate.classes.json"""

from __future__ import annotations
from typing import TYPE_CHECKING, Optional
import xml.etree.ElementTree as ET
from armodel.serialization import XMLMember

from armodel.models.M2.AUTOSARTemplates.GenericStructure.GeneralTemplateClasses.Identifiable.identifiable import (
    Identifiable,
)
from armodel.models.M2.AUTOSARTemplates.GenericStructure.GeneralTemplateClasses.PrimitiveTypes import (
    Integer,
    String,
)


class HwPin(Identifiable):
    """AUTOSAR HwPin."""

    # XML member definitions for this class only (not inherited from parent classes)
    # Format: dict[str, XMLMember] for declarative metadata
    _xml_members: dict[str, "XMLMember"] = {
        "function_names": XMLMember(
            xml_tag=None,
            is_attribute=False,
            multiplicity="*",
        ),  # functionNames
        "packaging_pin": XMLMember(
            xml_tag=None,
            is_attribute=True,
            multiplicity="0..1",
        ),  # packagingPin
        "pin_number": XMLMember(
            xml_tag=None,
            is_attribute=True,
            multiplicity="0..1",
        ),  # pinNumber
    }

    def __init__(self) -> None:
        """Initialize HwPin."""
        super().__init__()
        self.function_names: list[String] = []
        self.packaging_pin: Optional[String] = None
        self.pin_number: Optional[Integer] = None


class HwPinBuilder:
    """Builder for HwPin."""

    def __init__(self) -> None:
        """Initialize builder."""
        self._obj: HwPin = HwPin()

    def build(self) -> HwPin:
        """Build and return HwPin object.

        Returns:
            HwPin instance
        """
        # TODO: Add validation
        return self._obj
