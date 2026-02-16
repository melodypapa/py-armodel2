"""ReferenceCondition AUTOSAR element."""

from typing import Optional
import xml.etree.ElementTree as ET
from armodel.serialization import XMLMember

from armodel.models.M2.AUTOSARTemplates.CommonStructure.StandardizationTemplate.DataExchangePoint.Data.attribute_condition import (
    AttributeCondition,
)
from armodel.models.M2.AUTOSARTemplates.CommonStructure.StandardizationTemplate.DataExchangePoint.Data.reference_tailoring import (
    ReferenceTailoring,
)


class ReferenceCondition(AttributeCondition):
    """AUTOSAR ReferenceCondition."""

    # XML member definitions for this class only (not inherited from parent classes)
    # Format: dict[str, XMLMember] for declarative metadata
    _xml_members: dict[str, "XMLMember"] = {
        "reference": XMLMember(
            xml_tag=None,
            is_attribute=False,
            multiplicity="1",
            element_class=ReferenceTailoring,
        ),  # reference
    }

    def __init__(self) -> None:
        """Initialize ReferenceCondition."""
        super().__init__()
        self.reference: ReferenceTailoring = None


class ReferenceConditionBuilder:
    """Builder for ReferenceCondition."""

    def __init__(self) -> None:
        """Initialize builder."""
        self._obj: ReferenceCondition = ReferenceCondition()

    def build(self) -> ReferenceCondition:
        """Build and return ReferenceCondition object.

        Returns:
            ReferenceCondition instance
        """
        # TODO: Add validation
        return self._obj
