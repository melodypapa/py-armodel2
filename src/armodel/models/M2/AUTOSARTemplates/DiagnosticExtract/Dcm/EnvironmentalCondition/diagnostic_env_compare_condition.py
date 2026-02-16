"""DiagnosticEnvCompareCondition AUTOSAR element."""

from typing import Optional, cast
import xml.etree.ElementTree as ET
from armodel.models.M2.AUTOSARTemplates.DiagnosticExtract.Dcm.EnvironmentalCondition.diagnostic_env_condition_formula_part import (
    DiagnosticEnvConditionFormulaPart,
)


class DiagnosticEnvCompareCondition(DiagnosticEnvConditionFormulaPart):
    """AUTOSAR DiagnosticEnvCompareCondition."""
    """Abstract base class - do not instantiate directly."""

    # XML member definitions for this class only (not inherited from parent classes)
    # Format: (member_name, xml_tag_name, is_attribute, is_list, element_class)
    _xml_members = [
        ("compare_type", None, False, False, DiagnosticCompareTypeEnum),  # compareType
    ]

    def __init__(self) -> None:
        """Initialize DiagnosticEnvCompareCondition."""
        super().__init__()
        self.compare_type: Optional[DiagnosticCompareTypeEnum] = None

    def serialize(self, namespace: str, element: Optional[ET.Element] = None) -> ET.Element:
        """Convert DiagnosticEnvCompareCondition to XML element.

        Args:
            namespace: XML namespace for the element
            element: Optional existing element to add members to (for subclass chaining)

        Returns:
            XML element representing this object
        """
        # ARObject.serialize() handles entire class hierarchy automatically
        return super().serialize(namespace, element)

    @classmethod
    def deserialize(cls, element: ET.Element) -> "DiagnosticEnvCompareCondition":
        """Create DiagnosticEnvCompareCondition from XML element.

        Args:
            element: XML element to deserialize from

        Returns:
            DiagnosticEnvCompareCondition instance
        """
        # ARObject.deserialize() handles entire class hierarchy automatically
        obj = super().deserialize(element)
        # Cast to DiagnosticEnvCompareCondition since parent returns ARObject
        return cast("DiagnosticEnvCompareCondition", obj)


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
