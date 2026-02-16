"""DiagnosticCondition AUTOSAR element."""

from typing import Optional, cast
import xml.etree.ElementTree as ET
from armodel.models.M2.AUTOSARTemplates.DiagnosticExtract.CommonDiagnostics.diagnostic_common_element import (
    DiagnosticCommonElement,
)
from armodel.models.M2.AUTOSARTemplates.GenericStructure.GeneralTemplateClasses.PrimitiveTypes import (
    Boolean,
)


class DiagnosticCondition(DiagnosticCommonElement):
    """AUTOSAR DiagnosticCondition."""
    """Abstract base class - do not instantiate directly."""

    # XML member definitions for this class only (not inherited from parent classes)
    # Format: (member_name, xml_tag_name, is_attribute, is_list, element_class)
    _xml_members = [
        ("init_value", None, True, False, None),  # initValue
    ]

    def __init__(self) -> None:
        """Initialize DiagnosticCondition."""
        super().__init__()
        self.init_value: Optional[Boolean] = None

    def serialize(self, namespace: str, element: Optional[ET.Element] = None) -> ET.Element:
        """Convert DiagnosticCondition to XML element.

        Args:
            namespace: XML namespace for the element
            element: Optional existing element to add members to (for subclass chaining)

        Returns:
            XML element representing this object
        """
        # ARObject.serialize() handles entire class hierarchy automatically
        return super().serialize(namespace, element)

    @classmethod
    def deserialize(cls, element: ET.Element) -> "DiagnosticCondition":
        """Create DiagnosticCondition from XML element.

        Args:
            element: XML element to deserialize from

        Returns:
            DiagnosticCondition instance
        """
        # ARObject.deserialize() handles entire class hierarchy automatically
        obj = super().deserialize(element)
        # Cast to DiagnosticCondition since parent returns ARObject
        return cast("DiagnosticCondition", obj)


class DiagnosticConditionBuilder:
    """Builder for DiagnosticCondition."""

    def __init__(self) -> None:
        """Initialize builder."""
        self._obj: DiagnosticCondition = DiagnosticCondition()

    def build(self) -> DiagnosticCondition:
        """Build and return DiagnosticCondition object.

        Returns:
            DiagnosticCondition instance
        """
        # TODO: Add validation
        return self._obj
