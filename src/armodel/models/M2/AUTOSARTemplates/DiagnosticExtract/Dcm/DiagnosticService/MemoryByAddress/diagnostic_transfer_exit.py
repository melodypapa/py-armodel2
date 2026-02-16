"""DiagnosticTransferExit AUTOSAR element."""

from typing import Optional, cast
import xml.etree.ElementTree as ET
from armodel.models.M2.AUTOSARTemplates.DiagnosticExtract.Dcm.DiagnosticService.MemoryByAddress.diagnostic_memory_by_address import (
    DiagnosticMemoryByAddress,
)
from armodel.models.M2.AUTOSARTemplates.DiagnosticExtract.Dcm.DiagnosticService.MemoryByAddress.diagnostic_transfer_exit import (
    DiagnosticTransferExit,
)


class DiagnosticTransferExit(DiagnosticMemoryByAddress):
    """AUTOSAR DiagnosticTransferExit."""

    # XML member definitions for this class only (not inherited from parent classes)
    # Format: (member_name, xml_tag_name, is_attribute, is_list, element_class)
    _xml_members = [
        ("transfer_exit", None, False, False, DiagnosticTransferExit),  # transferExit
    ]

    def __init__(self) -> None:
        """Initialize DiagnosticTransferExit."""
        super().__init__()
        self.transfer_exit: Optional[DiagnosticTransferExit] = None

    def serialize(self, namespace: str, element: Optional[ET.Element] = None) -> ET.Element:
        """Convert DiagnosticTransferExit to XML element.

        Args:
            namespace: XML namespace for the element
            element: Optional existing element to add members to (for subclass chaining)

        Returns:
            XML element representing this object
        """
        # ARObject.serialize() handles entire class hierarchy automatically
        return super().serialize(namespace, element)

    @classmethod
    def deserialize(cls, element: ET.Element) -> "DiagnosticTransferExit":
        """Create DiagnosticTransferExit from XML element.

        Args:
            element: XML element to deserialize from

        Returns:
            DiagnosticTransferExit instance
        """
        # ARObject.deserialize() handles entire class hierarchy automatically
        obj = super().deserialize(element)
        # Cast to DiagnosticTransferExit since parent returns ARObject
        return cast("DiagnosticTransferExit", obj)


class DiagnosticTransferExitBuilder:
    """Builder for DiagnosticTransferExit."""

    def __init__(self) -> None:
        """Initialize builder."""
        self._obj: DiagnosticTransferExit = DiagnosticTransferExit()

    def build(self) -> DiagnosticTransferExit:
        """Build and return DiagnosticTransferExit object.

        Returns:
            DiagnosticTransferExit instance
        """
        # TODO: Add validation
        return self._obj
