"""DiagnosticValueNeeds AUTOSAR element."""

from typing import Optional, cast
import xml.etree.ElementTree as ET
from armodel.models.M2.AUTOSARTemplates.CommonStructure.ServiceNeeds.diagnostic_capability_element import (
    DiagnosticCapabilityElement,
)
from armodel.models.M2.AUTOSARTemplates.GenericStructure.GeneralTemplateClasses.PrimitiveTypes import (
    Boolean,
    PositiveInteger,
)


class DiagnosticValueNeeds(DiagnosticCapabilityElement):
    """AUTOSAR DiagnosticValueNeeds."""

    # XML member definitions for this class only (not inherited from parent classes)
    # Format: (member_name, xml_tag_name, is_attribute, is_list, element_class)
    _xml_members = [
        ("data_length", None, True, False, None),  # dataLength
        ("diagnostic_value_access", None, False, False, DiagnosticValueAccessEnum),  # diagnosticValueAccess
        ("fixed_length", None, True, False, None),  # fixedLength
        ("processing_style", None, False, False, DiagnosticProcessingStyleEnum),  # processingStyle
    ]

    def __init__(self) -> None:
        """Initialize DiagnosticValueNeeds."""
        super().__init__()
        self.data_length: Optional[PositiveInteger] = None
        self.diagnostic_value_access: Optional[DiagnosticValueAccessEnum] = None
        self.fixed_length: Optional[Boolean] = None
        self.processing_style: Optional[DiagnosticProcessingStyleEnum] = None

    def serialize(self, namespace: str, element: Optional[ET.Element] = None) -> ET.Element:
        """Convert DiagnosticValueNeeds to XML element.

        Args:
            namespace: XML namespace for the element
            element: Optional existing element to add members to (for subclass chaining)

        Returns:
            XML element representing this object
        """
        # ARObject.serialize() handles entire class hierarchy automatically
        return super().serialize(namespace, element)

    @classmethod
    def deserialize(cls, element: ET.Element) -> "DiagnosticValueNeeds":
        """Create DiagnosticValueNeeds from XML element.

        Args:
            element: XML element to deserialize from

        Returns:
            DiagnosticValueNeeds instance
        """
        # ARObject.deserialize() handles entire class hierarchy automatically
        obj = super().deserialize(element)
        # Cast to DiagnosticValueNeeds since parent returns ARObject
        return cast("DiagnosticValueNeeds", obj)


class DiagnosticValueNeedsBuilder:
    """Builder for DiagnosticValueNeeds."""

    def __init__(self) -> None:
        """Initialize builder."""
        self._obj: DiagnosticValueNeeds = DiagnosticValueNeeds()

    def build(self) -> DiagnosticValueNeeds:
        """Build and return DiagnosticValueNeeds object.

        Returns:
            DiagnosticValueNeeds instance
        """
        # TODO: Add validation
        return self._obj
