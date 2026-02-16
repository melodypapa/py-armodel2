"""DiagnosticMeasurementIdentifier AUTOSAR element."""

from typing import Optional, cast
import xml.etree.ElementTree as ET
from armodel.models.M2.AUTOSARTemplates.DiagnosticExtract.CommonDiagnostics.diagnostic_common_element import (
    DiagnosticCommonElement,
)
from armodel.models.M2.AUTOSARTemplates.GenericStructure.GeneralTemplateClasses.PrimitiveTypes import (
    PositiveInteger,
)


class DiagnosticMeasurementIdentifier(DiagnosticCommonElement):
    """AUTOSAR DiagnosticMeasurementIdentifier."""

    # XML member definitions for this class only (not inherited from parent classes)
    # Format: (member_name, xml_tag_name, is_attribute, is_list, element_class)
    _xml_members = [
        ("obd_mid", None, True, False, None),  # obdMid
    ]

    def __init__(self) -> None:
        """Initialize DiagnosticMeasurementIdentifier."""
        super().__init__()
        self.obd_mid: Optional[PositiveInteger] = None

    def serialize(self, namespace: str, element: Optional[ET.Element] = None) -> ET.Element:
        """Convert DiagnosticMeasurementIdentifier to XML element.

        Args:
            namespace: XML namespace for the element
            element: Optional existing element to add members to (for subclass chaining)

        Returns:
            XML element representing this object
        """
        # ARObject.serialize() handles entire class hierarchy automatically
        return super().serialize(namespace, element)

    @classmethod
    def deserialize(cls, element: ET.Element) -> "DiagnosticMeasurementIdentifier":
        """Create DiagnosticMeasurementIdentifier from XML element.

        Args:
            element: XML element to deserialize from

        Returns:
            DiagnosticMeasurementIdentifier instance
        """
        # ARObject.deserialize() handles entire class hierarchy automatically
        obj = super().deserialize(element)
        # Cast to DiagnosticMeasurementIdentifier since parent returns ARObject
        return cast("DiagnosticMeasurementIdentifier", obj)


class DiagnosticMeasurementIdentifierBuilder:
    """Builder for DiagnosticMeasurementIdentifier."""

    def __init__(self) -> None:
        """Initialize builder."""
        self._obj: DiagnosticMeasurementIdentifier = DiagnosticMeasurementIdentifier()

    def build(self) -> DiagnosticMeasurementIdentifier:
        """Build and return DiagnosticMeasurementIdentifier object.

        Returns:
            DiagnosticMeasurementIdentifier instance
        """
        # TODO: Add validation
        return self._obj
