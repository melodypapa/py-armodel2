"""DiagnosticDataTransfer AUTOSAR element.

References:
  - AUTOSAR_CP_TPS_DiagnosticExtractTemplate.pdf (page 143)

JSON Source: docs/json/packages/M2_AUTOSARTemplates_DiagnosticExtract_Dcm_DiagnosticService_MemoryByAddress.classes.json"""

from __future__ import annotations
from typing import TYPE_CHECKING, Optional
import xml.etree.ElementTree as ET

from armodel.models.M2.AUTOSARTemplates.DiagnosticExtract.Dcm.DiagnosticService.MemoryByAddress.diagnostic_memory_by_address import (
    DiagnosticMemoryByAddress,
)
from armodel.models.M2.AUTOSARTemplates.GenericStructure.GeneralTemplateClasses.ArObject.ar_object import ARObject
from armodel.models.M2.AUTOSARTemplates.GenericStructure.GeneralTemplateClasses.ArObject.ar_ref import ARRef


class DiagnosticDataTransfer(DiagnosticMemoryByAddress):
    """AUTOSAR DiagnosticDataTransfer."""

    @property
    def is_abstract(self) -> bool:
        """Check if this class is abstract.

        Returns:
            False for concrete classes
        """
        return False

    data_transfer_ref: Optional[ARRef]
    def __init__(self) -> None:
        """Initialize DiagnosticDataTransfer."""
        super().__init__()
        self.data_transfer_ref: Optional[ARRef] = None

    def serialize(self) -> ET.Element:
        """Serialize DiagnosticDataTransfer to XML element.

        Returns:
            xml.etree.ElementTree.Element representing this object
        """
        # Get XML tag name for this class
        tag = self._get_xml_tag()
        elem = ET.Element(tag)

        # First, call parent's serialize to handle inherited attributes
        parent_elem = super(DiagnosticDataTransfer, self).serialize()

        # Copy all attributes from parent element
        elem.attrib.update(parent_elem.attrib)

        # Copy text from parent element
        if parent_elem.text:
            elem.text = parent_elem.text

        # Copy all children from parent element
        for child in parent_elem:
            elem.append(child)

        # Serialize data_transfer_ref
        if self.data_transfer_ref is not None:
            serialized = ARObject._serialize_item(self.data_transfer_ref, "DiagnosticDataTransfer")
            if serialized is not None:
                # Wrap with correct tag
                wrapped = ET.Element("DATA-TRANSFER-REF")
                if hasattr(serialized, 'attrib'):
                    wrapped.attrib.update(serialized.attrib)
                    if serialized.text:
                        wrapped.text = serialized.text
                for child in serialized:
                    wrapped.append(child)
                elem.append(wrapped)

        return elem

    @classmethod
    def deserialize(cls, element: ET.Element) -> "DiagnosticDataTransfer":
        """Deserialize XML element to DiagnosticDataTransfer object.

        Args:
            element: XML element to deserialize from

        Returns:
            Deserialized DiagnosticDataTransfer object
        """
        # First, call parent's deserialize to handle inherited attributes
        obj = super(DiagnosticDataTransfer, cls).deserialize(element)

        # Parse data_transfer_ref
        child = ARObject._find_child_element(element, "DATA-TRANSFER-REF")
        if child is not None:
            data_transfer_ref_value = ARRef.deserialize(child)
            obj.data_transfer_ref = data_transfer_ref_value

        return obj



class DiagnosticDataTransferBuilder:
    """Builder for DiagnosticDataTransfer."""

    def __init__(self) -> None:
        """Initialize builder."""
        self._obj: DiagnosticDataTransfer = DiagnosticDataTransfer()

    def build(self) -> DiagnosticDataTransfer:
        """Build and return DiagnosticDataTransfer object.

        Returns:
            DiagnosticDataTransfer instance
        """
        # TODO: Add validation
        return self._obj
