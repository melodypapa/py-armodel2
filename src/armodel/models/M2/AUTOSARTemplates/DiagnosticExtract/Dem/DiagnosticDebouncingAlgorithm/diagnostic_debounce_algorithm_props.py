"""DiagnosticDebounceAlgorithmProps AUTOSAR element."""

from typing import Optional, cast
import xml.etree.ElementTree as ET
from armodel.models.M2.AUTOSARTemplates.GenericStructure.GeneralTemplateClasses.Identifiable.identifiable import (
    Identifiable,
)
from armodel.models.M2.AUTOSARTemplates.GenericStructure.GeneralTemplateClasses.PrimitiveTypes import (
    Boolean,
)


class DiagnosticDebounceAlgorithmProps(Identifiable):
    """AUTOSAR DiagnosticDebounceAlgorithmProps."""

    # XML member definitions for this class only (not inherited from parent classes)
    # Format: (member_name, xml_tag_name, is_attribute, is_list, element_class)
    _xml_members = [
        ("debounce", None, True, False, None),  # debounce
    ]

    def __init__(self) -> None:
        """Initialize DiagnosticDebounceAlgorithmProps."""
        super().__init__()
        self.debounce: Optional[Boolean] = None

    def serialize(self, namespace: str, element: Optional[ET.Element] = None) -> ET.Element:
        """Convert DiagnosticDebounceAlgorithmProps to XML element.

        Args:
            namespace: XML namespace for the element
            element: Optional existing element to add members to (for subclass chaining)

        Returns:
            XML element representing this object
        """
        # ARObject.serialize() handles entire class hierarchy automatically
        return super().serialize(namespace, element)

    @classmethod
    def deserialize(cls, element: ET.Element) -> "DiagnosticDebounceAlgorithmProps":
        """Create DiagnosticDebounceAlgorithmProps from XML element.

        Args:
            element: XML element to deserialize from

        Returns:
            DiagnosticDebounceAlgorithmProps instance
        """
        # ARObject.deserialize() handles entire class hierarchy automatically
        obj = super().deserialize(element)
        # Cast to DiagnosticDebounceAlgorithmProps since parent returns ARObject
        return cast("DiagnosticDebounceAlgorithmProps", obj)


class DiagnosticDebounceAlgorithmPropsBuilder:
    """Builder for DiagnosticDebounceAlgorithmProps."""

    def __init__(self) -> None:
        """Initialize builder."""
        self._obj: DiagnosticDebounceAlgorithmProps = DiagnosticDebounceAlgorithmProps()

    def build(self) -> DiagnosticDebounceAlgorithmProps:
        """Build and return DiagnosticDebounceAlgorithmProps object.

        Returns:
            DiagnosticDebounceAlgorithmProps instance
        """
        # TODO: Add validation
        return self._obj
