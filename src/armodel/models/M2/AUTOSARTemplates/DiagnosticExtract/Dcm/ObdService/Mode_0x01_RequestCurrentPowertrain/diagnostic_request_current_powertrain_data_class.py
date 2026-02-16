"""DiagnosticRequestCurrentPowertrainDataClass AUTOSAR element."""

from typing import Optional, cast
import xml.etree.ElementTree as ET
from armodel.models.M2.AUTOSARTemplates.DiagnosticExtract.Dcm.DiagnosticService.CommonService.diagnostic_service_class import (
    DiagnosticServiceClass,
)


class DiagnosticRequestCurrentPowertrainDataClass(DiagnosticServiceClass):
    """AUTOSAR DiagnosticRequestCurrentPowertrainDataClass."""

    # XML member definitions for this class only (not inherited from parent classes)
    # Format: (member_name, xml_tag_name, is_attribute, is_list, element_class)
    _xml_members = [
    ]

    def __init__(self) -> None:
        """Initialize DiagnosticRequestCurrentPowertrainDataClass."""
        super().__init__()

    def serialize(self, namespace: str, element: Optional[ET.Element] = None) -> ET.Element:
        """Convert DiagnosticRequestCurrentPowertrainDataClass to XML element.

        Args:
            namespace: XML namespace for the element
            element: Optional existing element to add members to (for subclass chaining)

        Returns:
            XML element representing this object
        """
        # ARObject.serialize() handles entire class hierarchy automatically
        return super().serialize(namespace, element)

    @classmethod
    def deserialize(cls, element: ET.Element) -> "DiagnosticRequestCurrentPowertrainDataClass":
        """Create DiagnosticRequestCurrentPowertrainDataClass from XML element.

        Args:
            element: XML element to deserialize from

        Returns:
            DiagnosticRequestCurrentPowertrainDataClass instance
        """
        # ARObject.deserialize() handles entire class hierarchy automatically
        obj = super().deserialize(element)
        # Cast to DiagnosticRequestCurrentPowertrainDataClass since parent returns ARObject
        return cast("DiagnosticRequestCurrentPowertrainDataClass", obj)


class DiagnosticRequestCurrentPowertrainDataClassBuilder:
    """Builder for DiagnosticRequestCurrentPowertrainDataClass."""

    def __init__(self) -> None:
        """Initialize builder."""
        self._obj: DiagnosticRequestCurrentPowertrainDataClass = DiagnosticRequestCurrentPowertrainDataClass()

    def build(self) -> DiagnosticRequestCurrentPowertrainDataClass:
        """Build and return DiagnosticRequestCurrentPowertrainDataClass object.

        Returns:
            DiagnosticRequestCurrentPowertrainDataClass instance
        """
        # TODO: Add validation
        return self._obj
