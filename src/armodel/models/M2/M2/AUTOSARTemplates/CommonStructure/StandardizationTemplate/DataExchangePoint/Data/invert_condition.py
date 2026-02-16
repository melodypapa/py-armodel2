"""InvertCondition AUTOSAR element."""

from typing import Optional
import xml.etree.ElementTree as ET
from armodel.serialization import XMLMember

from armodel.models.M2.AUTOSARTemplates.CommonStructure.StandardizationTemplate.DataExchangePoint.Data.abstract_condition import (
    AbstractCondition,
)
from armodel.models.M2.AUTOSARTemplates.CommonStructure.StandardizationTemplate.DataExchangePoint.Data.abstract_condition import (
    AbstractCondition,
)


class InvertCondition(AbstractCondition):
    """AUTOSAR InvertCondition."""

    # XML member definitions for this class only (not inherited from parent classes)
    # Format: dict[str, XMLMember] for declarative metadata
    _xml_members: dict[str, "XMLMember"] = {
        "condition": XMLMember(
            xml_tag=None,
            is_attribute=False,
            multiplicity="1",
            element_class=AbstractCondition,
        ),  # condition
    }

    def __init__(self) -> None:
        """Initialize InvertCondition."""
        super().__init__()
        self.condition: AbstractCondition = None


class InvertConditionBuilder:
    """Builder for InvertCondition."""

    def __init__(self) -> None:
        """Initialize builder."""
        self._obj: InvertCondition = InvertCondition()

    def build(self) -> InvertCondition:
        """Build and return InvertCondition object.

        Returns:
            InvertCondition instance
        """
        # TODO: Add validation
        return self._obj
