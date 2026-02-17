"""HwDescriptionEntity AUTOSAR element.

References:
  - AUTOSAR_CP_TPS_ECUResourceTemplate.pdf (page 15)
  - AUTOSAR_CP_TPS_SoftwareComponentTemplate.pdf (page 990)

JSON Source: docs/json/packages/M2_AUTOSARTemplates_EcuResourceTemplate.classes.json"""

from __future__ import annotations
from typing import TYPE_CHECKING, Optional
import xml.etree.ElementTree as ET
from armodel.serialization import XMLMember

from armodel.models.M2.AUTOSARTemplates.GenericStructure.GeneralTemplateClasses.Identifiable.referrable import (
    Referrable,
)
from armodel.models.M2.AUTOSARTemplates.EcuResourceTemplate.HwElementCategory.hw_attribute_value import (
    HwAttributeValue,
)
from armodel.models.M2.AUTOSARTemplates.EcuResourceTemplate.HwElementCategory.hw_category import (
    HwCategory,
)
from armodel.models.M2.AUTOSARTemplates.EcuResourceTemplate.HwElementCategory.hw_type import (
    HwType,
)


class HwDescriptionEntity(Referrable):
    """AUTOSAR HwDescriptionEntity."""
    """Abstract base class - do not instantiate directly."""

    # XML member definitions for this class only (not inherited from parent classes)
    # Format: dict[str, XMLMember] for declarative metadata
    _xml_members: dict[str, "XMLMember"] = {
        "hw_attributes": XMLMember(
            xml_tag=None,
            is_attribute=False,
            multiplicity="*",
            element_class=HwAttributeValue,
        ),  # hwAttributes
        "hw_categories": XMLMember(
            xml_tag=None,
            is_attribute=False,
            multiplicity="*",
            element_class=HwCategory,
        ),  # hwCategories
        "hw_type": XMLMember(
            xml_tag=None,
            is_attribute=False,
            multiplicity="0..1",
            element_class=HwType,
        ),  # hwType
    }

    def __init__(self) -> None:
        """Initialize HwDescriptionEntity."""
        super().__init__()
        self.hw_attributes: list[HwAttributeValue] = []
        self.hw_categories: list[HwCategory] = []
        self.hw_type: Optional[HwType] = None


class HwDescriptionEntityBuilder:
    """Builder for HwDescriptionEntity."""

    def __init__(self) -> None:
        """Initialize builder."""
        self._obj: HwDescriptionEntity = HwDescriptionEntity()

    def build(self) -> HwDescriptionEntity:
        """Build and return HwDescriptionEntity object.

        Returns:
            HwDescriptionEntity instance
        """
        # TODO: Add validation
        return self._obj
