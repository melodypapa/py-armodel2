"""DiagnosticReadDataByPeriodicID AUTOSAR element."""

from typing import Optional, cast
import xml.etree.ElementTree as ET
from armodel.models.M2.AUTOSARTemplates.DiagnosticExtract.Dcm.DiagnosticService.CommonService.diagnostic_service_instance import (
    DiagnosticServiceInstance,
)


class DiagnosticReadDataByPeriodicID(DiagnosticServiceInstance):
    """AUTOSAR DiagnosticReadDataByPeriodicID."""

    # XML member definitions for this class only (not inherited from parent classes)
    # Format: (member_name, xml_tag_name, is_attribute, is_list, element_class)
    _xml_members = [
        ("read_data_class", None, False, False, any (DiagnosticReadDataBy)),  # readDataClass
    ]

    def __init__(self) -> None:
        """Initialize DiagnosticReadDataByPeriodicID."""
        super().__init__()
        self.read_data_class: Optional[Any] = None

    def serialize(self, namespace: str, element: Optional[ET.Element] = None) -> ET.Element:
        """Convert DiagnosticReadDataByPeriodicID to XML element.

        Args:
            namespace: XML namespace for the element
            element: Optional existing element to add members to (for subclass chaining)

        Returns:
            XML element representing this object
        """
        # ARObject.serialize() handles entire class hierarchy automatically
        return super().serialize(namespace, element)

    @classmethod
    def deserialize(cls, element: ET.Element) -> "DiagnosticReadDataByPeriodicID":
        """Create DiagnosticReadDataByPeriodicID from XML element.

        Args:
            element: XML element to deserialize from

        Returns:
            DiagnosticReadDataByPeriodicID instance
        """
        # ARObject.deserialize() handles entire class hierarchy automatically
        obj = super().deserialize(element)
        # Cast to DiagnosticReadDataByPeriodicID since parent returns ARObject
        return cast("DiagnosticReadDataByPeriodicID", obj)


class DiagnosticReadDataByPeriodicIDBuilder:
    """Builder for DiagnosticReadDataByPeriodicID."""

    def __init__(self) -> None:
        """Initialize builder."""
        self._obj: DiagnosticReadDataByPeriodicID = DiagnosticReadDataByPeriodicID()

    def build(self) -> DiagnosticReadDataByPeriodicID:
        """Build and return DiagnosticReadDataByPeriodicID object.

        Returns:
            DiagnosticReadDataByPeriodicID instance
        """
        # TODO: Add validation
        return self._obj
