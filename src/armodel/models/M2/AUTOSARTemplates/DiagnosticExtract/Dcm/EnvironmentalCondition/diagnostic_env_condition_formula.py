"""DiagnosticEnvConditionFormula AUTOSAR element."""

from typing import Optional, cast
import xml.etree.ElementTree as ET
from armodel.models.M2.AUTOSARTemplates.DiagnosticExtract.Dcm.EnvironmentalCondition.diagnostic_env_condition_formula_part import (
    DiagnosticEnvConditionFormulaPart,
)
from armodel.models.M2.AUTOSARTemplates.GenericStructure.GeneralTemplateClasses.PrimitiveTypes import (
    PositiveInteger,
)


class DiagnosticEnvConditionFormula(DiagnosticEnvConditionFormulaPart):
    """AUTOSAR DiagnosticEnvConditionFormula."""

    # XML member definitions for this class only (not inherited from parent classes)
    # Format: (member_name, xml_tag_name, is_attribute, is_list, element_class)
    _xml_members = [
        ("nrc_value", None, True, False, None),  # nrcValue
        ("op", None, False, False, DiagnosticLogicalOperatorEnum),  # op
    ]

    def __init__(self) -> None:
        """Initialize DiagnosticEnvConditionFormula."""
        super().__init__()
        self.nrc_value: Optional[PositiveInteger] = None
        self.op: Optional[DiagnosticLogicalOperatorEnum] = None

    def serialize(self, namespace: str, element: Optional[ET.Element] = None) -> ET.Element:
        """Convert DiagnosticEnvConditionFormula to XML element.

        Args:
            namespace: XML namespace for the element
            element: Optional existing element to add members to (for subclass chaining)

        Returns:
            XML element representing this object
        """
        # ARObject.serialize() handles entire class hierarchy automatically
        return super().serialize(namespace, element)

    @classmethod
    def deserialize(cls, element: ET.Element) -> "DiagnosticEnvConditionFormula":
        """Create DiagnosticEnvConditionFormula from XML element.

        Args:
            element: XML element to deserialize from

        Returns:
            DiagnosticEnvConditionFormula instance
        """
        # ARObject.deserialize() handles entire class hierarchy automatically
        obj = super().deserialize(element)
        # Cast to DiagnosticEnvConditionFormula since parent returns ARObject
        return cast("DiagnosticEnvConditionFormula", obj)


class DiagnosticEnvConditionFormulaBuilder:
    """Builder for DiagnosticEnvConditionFormula."""

    def __init__(self) -> None:
        """Initialize builder."""
        self._obj: DiagnosticEnvConditionFormula = DiagnosticEnvConditionFormula()

    def build(self) -> DiagnosticEnvConditionFormula:
        """Build and return DiagnosticEnvConditionFormula object.

        Returns:
            DiagnosticEnvConditionFormula instance
        """
        # TODO: Add validation
        return self._obj
