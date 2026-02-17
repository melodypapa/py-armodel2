"""AggregationCondition AUTOSAR element.

References:
  - AUTOSAR_FO_TPS_StandardizationTemplate.pdf (page 102)

JSON Source: docs/json/packages/M2_AUTOSARTemplates_CommonStructure_StandardizationTemplate_DataExchangePoint_Data.classes.json"""

from typing import Optional
import xml.etree.ElementTree as ET
from armodel.serialization import XMLMember

from armodel.models.M2.AUTOSARTemplates.CommonStructure.StandardizationTemplate.DataExchangePoint.Data.attribute_condition import (
    AttributeCondition,
)
from armodel.models.M2.AUTOSARTemplates.CommonStructure.StandardizationTemplate.DataExchangePoint.Data.aggregation_tailoring import (
    AggregationTailoring,
)


class AggregationCondition(AttributeCondition):
    """AUTOSAR AggregationCondition."""

    # XML member definitions for this class only (not inherited from parent classes)
    # Format: dict[str, XMLMember] for declarative metadata
    _xml_members: dict[str, "XMLMember"] = {
        "aggregation": XMLMember(
            xml_tag=None,
            is_attribute=False,
            multiplicity="1",
            element_class=AggregationTailoring,
        ),  # aggregation
    }

    def __init__(self) -> None:
        """Initialize AggregationCondition."""
        super().__init__()
        self.aggregation: AggregationTailoring = None


class AggregationConditionBuilder:
    """Builder for AggregationCondition."""

    def __init__(self) -> None:
        """Initialize builder."""
        self._obj: AggregationCondition = AggregationCondition()

    def build(self) -> AggregationCondition:
        """Build and return AggregationCondition object.

        Returns:
            AggregationCondition instance
        """
        # TODO: Add validation
        return self._obj
