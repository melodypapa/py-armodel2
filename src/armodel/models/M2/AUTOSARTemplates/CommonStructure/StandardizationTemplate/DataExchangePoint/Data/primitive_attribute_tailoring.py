"""PrimitiveAttributeTailoring AUTOSAR element.

References:
  - AUTOSAR_FO_TPS_StandardizationTemplate.pdf (page 111)

JSON Source: docs/json/packages/M2_AUTOSARTemplates_CommonStructure_StandardizationTemplate_DataExchangePoint_Data.classes.json"""

from __future__ import annotations
from typing import TYPE_CHECKING, Optional
import xml.etree.ElementTree as ET
from armodel.serialization import XMLMember

from armodel.models.M2.AUTOSARTemplates.CommonStructure.StandardizationTemplate.DataExchangePoint.Data.attribute_tailoring import (
    AttributeTailoring,
)
from armodel.models.M2.AUTOSARTemplates.CommonStructure.StandardizationTemplate.DataExchangePoint.Data import (
    DefaultValueApplicationStrategyEnum,
)
from armodel.models.M2.AUTOSARTemplates.CommonStructure.StandardizationTemplate.DataExchangePoint.Data.value_restriction_with_severity import (
    ValueRestrictionWithSeverity,
)


class PrimitiveAttributeTailoring(AttributeTailoring):
    """AUTOSAR PrimitiveAttributeTailoring."""

    # XML member definitions for this class only (not inherited from parent classes)
    # Format: dict[str, XMLMember] for declarative metadata
    _xml_members: dict[str, "XMLMember"] = {
        "default_value": XMLMember(
            xml_tag=None,
            is_attribute=False,
            multiplicity="0..1",
            element_class=DefaultValueApplicationStrategyEnum,
        ),  # defaultValue
        "sub_attributes": XMLMember(
            xml_tag=None,
            is_attribute=False,
            multiplicity="*",
            element_class=any (PrimitiveAttribute),
        ),  # subAttributes
        "value_restriction_with_severity": XMLMember(
            xml_tag=None,
            is_attribute=False,
            multiplicity="0..1",
            element_class=ValueRestrictionWithSeverity,
        ),  # valueRestrictionWithSeverity
    }

    def __init__(self) -> None:
        """Initialize PrimitiveAttributeTailoring."""
        super().__init__()
        self.default_value: Optional[DefaultValueApplicationStrategyEnum] = None
        self.sub_attributes: list[Any] = []
        self.value_restriction_with_severity: Optional[ValueRestrictionWithSeverity] = None


class PrimitiveAttributeTailoringBuilder:
    """Builder for PrimitiveAttributeTailoring."""

    def __init__(self) -> None:
        """Initialize builder."""
        self._obj: PrimitiveAttributeTailoring = PrimitiveAttributeTailoring()

    def build(self) -> PrimitiveAttributeTailoring:
        """Build and return PrimitiveAttributeTailoring object.

        Returns:
            PrimitiveAttributeTailoring instance
        """
        # TODO: Add validation
        return self._obj
