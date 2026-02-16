"""DiagnosticIoControlNeeds AUTOSAR element."""

from typing import Optional, cast
import xml.etree.ElementTree as ET
from armodel.models.M2.AUTOSARTemplates.CommonStructure.ServiceNeeds.diagnostic_capability_element import (
    DiagnosticCapabilityElement,
)
from armodel.models.M2.AUTOSARTemplates.GenericStructure.GeneralTemplateClasses.PrimitiveTypes import (
    Boolean,
)
from armodel.models.M2.AUTOSARTemplates.CommonStructure.ServiceNeeds.diagnostic_value_needs import (
    DiagnosticValueNeeds,
)


class DiagnosticIoControlNeeds(DiagnosticCapabilityElement):
    """AUTOSAR DiagnosticIoControlNeeds."""

    # XML member definitions for this class only (not inherited from parent classes)
    # Format: (member_name, xml_tag_name, is_attribute, is_list, element_class)
    _xml_members = [
        ("current_value", None, False, False, DiagnosticValueNeeds),  # currentValue
        ("freeze_current", None, True, False, None),  # freezeCurrent
        ("reset_to_default", None, True, False, None),  # resetToDefault
        ("short_term", None, True, False, None),  # shortTerm
    ]

    def __init__(self) -> None:
        """Initialize DiagnosticIoControlNeeds."""
        super().__init__()
        self.current_value: Optional[DiagnosticValueNeeds] = None
        self.freeze_current: Optional[Boolean] = None
        self.reset_to_default: Optional[Boolean] = None
        self.short_term: Optional[Boolean] = None

    def serialize(self, namespace: str, element: Optional[ET.Element] = None) -> ET.Element:
        """Convert DiagnosticIoControlNeeds to XML element.

        Args:
            namespace: XML namespace for the element
            element: Optional existing element to add members to (for subclass chaining)

        Returns:
            XML element representing this object
        """
        # ARObject.serialize() handles entire class hierarchy automatically
        return super().serialize(namespace, element)

    @classmethod
    def deserialize(cls, element: ET.Element) -> "DiagnosticIoControlNeeds":
        """Create DiagnosticIoControlNeeds from XML element.

        Args:
            element: XML element to deserialize from

        Returns:
            DiagnosticIoControlNeeds instance
        """
        # ARObject.deserialize() handles entire class hierarchy automatically
        obj = super().deserialize(element)
        # Cast to DiagnosticIoControlNeeds since parent returns ARObject
        return cast("DiagnosticIoControlNeeds", obj)


class DiagnosticIoControlNeedsBuilder:
    """Builder for DiagnosticIoControlNeeds."""

    def __init__(self) -> None:
        """Initialize builder."""
        self._obj: DiagnosticIoControlNeeds = DiagnosticIoControlNeeds()

    def build(self) -> DiagnosticIoControlNeeds:
        """Build and return DiagnosticIoControlNeeds object.

        Returns:
            DiagnosticIoControlNeeds instance
        """
        # TODO: Add validation
        return self._obj
