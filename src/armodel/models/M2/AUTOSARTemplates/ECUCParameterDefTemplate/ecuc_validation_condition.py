"""EcucValidationCondition AUTOSAR element.

References:
  - AUTOSAR_CP_TPS_ECUConfiguration.pdf (page 103)

JSON Source: docs/json/packages/M2_AUTOSARTemplates_ECUCParameterDefTemplate.classes.json"""

from typing import Optional
import xml.etree.ElementTree as ET
from armodel.serialization import XMLMember

from armodel.models.M2.AUTOSARTemplates.GenericStructure.GeneralTemplateClasses.Identifiable.identifiable import (
    Identifiable,
)
from armodel.models.M2.AUTOSARTemplates.ECUCParameterDefTemplate.ecuc_condition_formula import (
    EcucConditionFormula,
)
from armodel.models.M2.AUTOSARTemplates.ECUCParameterDefTemplate.ecuc_query import (
    EcucQuery,
)


class EcucValidationCondition(Identifiable):
    """AUTOSAR EcucValidationCondition."""

    # XML member definitions for this class only (not inherited from parent classes)
    # Format: dict[str, XMLMember] for declarative metadata
    _xml_members: dict[str, "XMLMember"] = {
        "ecuc_queries": XMLMember(
            xml_tag=None,
            is_attribute=False,
            multiplicity="*",
            element_class=EcucQuery,
        ),  # ecucQueries
        "validation": XMLMember(
            xml_tag=None,
            is_attribute=False,
            multiplicity="0..1",
            element_class=EcucConditionFormula,
        ),  # validation
    }

    def __init__(self) -> None:
        """Initialize EcucValidationCondition."""
        super().__init__()
        self.ecuc_queries: list[EcucQuery] = []
        self.validation: Optional[EcucConditionFormula] = None


class EcucValidationConditionBuilder:
    """Builder for EcucValidationCondition."""

    def __init__(self) -> None:
        """Initialize builder."""
        self._obj: EcucValidationCondition = EcucValidationCondition()

    def build(self) -> EcucValidationCondition:
        """Build and return EcucValidationCondition object.

        Returns:
            EcucValidationCondition instance
        """
        # TODO: Add validation
        return self._obj
