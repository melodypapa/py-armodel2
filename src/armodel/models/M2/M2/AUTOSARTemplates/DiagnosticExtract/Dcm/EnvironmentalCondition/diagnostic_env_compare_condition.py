"""DiagnosticEnvCompareCondition AUTOSAR element."""

from typing import Optional
import xml.etree.ElementTree as ET
from armodel.serialization import XMLMember

from armodel.models.M2.AUTOSARTemplates.DiagnosticExtract.Dcm.EnvironmentalCondition.diagnostic_env_condition_formula_part import (
    DiagnosticEnvConditionFormulaPart,
)


class DiagnosticEnvCompareCondition(DiagnosticEnvConditionFormulaPart):
    """AUTOSAR DiagnosticEnvCompareCondition."""
    """Abstract base class - do not instantiate directly."""

    # XML member definitions for this class only (not inherited from parent classes)
    # Format: dict[str, XMLMember] for declarative metadata
    _xml_members: dict[str, "XMLMember"] = {
        "compare_type": XMLMember(
            xml_tag=None,
            is_attribute=False,
            multiplicity="0..1",
            element_class=DiagnosticCompareTypeEnum,
        ),  # compareType
    }

    def __init__(self) -> None:
        """Initialize DiagnosticEnvCompareCondition."""
        super().__init__()
        self.compare_type: Optional[DiagnosticCompareTypeEnum] = None


class DiagnosticEnvCompareConditionBuilder:
    """Builder for DiagnosticEnvCompareCondition."""

    def __init__(self) -> None:
        """Initialize builder."""
        self._obj: DiagnosticEnvCompareCondition = DiagnosticEnvCompareCondition()

    def build(self) -> DiagnosticEnvCompareCondition:
        """Build and return DiagnosticEnvCompareCondition object.

        Returns:
            DiagnosticEnvCompareCondition instance
        """
        # TODO: Add validation
        return self._obj
