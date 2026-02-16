"""DiagnosticEnvDataCondition AUTOSAR element."""

from typing import Optional, cast
import xml.etree.ElementTree as ET
from armodel.models.M2.AUTOSARTemplates.DiagnosticExtract.Dcm.EnvironmentalCondition.diagnostic_env_compare_condition import (
    DiagnosticEnvCompareCondition,
)
from armodel.models.M2.AUTOSARTemplates.DiagnosticExtract.CommonDiagnostics.diagnostic_data_element import (
    DiagnosticDataElement,
)
from armodel.models.M2.AUTOSARTemplates.CommonStructure.Constants.value_specification import (
    ValueSpecification,
)


class DiagnosticEnvDataCondition(DiagnosticEnvCompareCondition):
    """AUTOSAR DiagnosticEnvDataCondition."""

    # XML member definitions for this class only (not inherited from parent classes)
    # Format: (member_name, xml_tag_name, is_attribute, is_list, element_class)
    _xml_members = [
        ("compare_value", None, False, False, ValueSpecification),  # compareValue
        ("data_element", None, False, False, DiagnosticDataElement),  # dataElement
    ]

    def __init__(self) -> None:
        """Initialize DiagnosticEnvDataCondition."""
        super().__init__()
        self.compare_value: Optional[ValueSpecification] = None
        self.data_element: Optional[DiagnosticDataElement] = None

    def serialize(self, namespace: str, element: Optional[ET.Element] = None) -> ET.Element:
        """Convert DiagnosticEnvDataCondition to XML element.

        Args:
            namespace: XML namespace for the element
            element: Optional existing element to add members to (for subclass chaining)

        Returns:
            XML element representing this object
        """
        # ARObject.serialize() handles entire class hierarchy automatically
        return super().serialize(namespace, element)

    @classmethod
    def deserialize(cls, element: ET.Element) -> "DiagnosticEnvDataCondition":
        """Create DiagnosticEnvDataCondition from XML element.

        Args:
            element: XML element to deserialize from

        Returns:
            DiagnosticEnvDataCondition instance
        """
        # ARObject.deserialize() handles entire class hierarchy automatically
        obj = super().deserialize(element)
        # Cast to DiagnosticEnvDataCondition since parent returns ARObject
        return cast("DiagnosticEnvDataCondition", obj)


class DiagnosticEnvDataConditionBuilder:
    """Builder for DiagnosticEnvDataCondition."""

    def __init__(self) -> None:
        """Initialize builder."""
        self._obj: DiagnosticEnvDataCondition = DiagnosticEnvDataCondition()

    def build(self) -> DiagnosticEnvDataCondition:
        """Build and return DiagnosticEnvDataCondition object.

        Returns:
            DiagnosticEnvDataCondition instance
        """
        # TODO: Add validation
        return self._obj
