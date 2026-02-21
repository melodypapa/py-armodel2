"""DiagnosticTransferExit AUTOSAR element.

References:
  - AUTOSAR_CP_TPS_DiagnosticExtractTemplate.pdf (page 142)

JSON Source: docs/json/packages/M2_AUTOSARTemplates_DiagnosticExtract_Dcm_DiagnosticService_MemoryByAddress.classes.json"""

from __future__ import annotations
from typing import TYPE_CHECKING, Optional
import xml.etree.ElementTree as ET

from armodel.models.M2.AUTOSARTemplates.DiagnosticExtract.Dcm.DiagnosticService.MemoryByAddress.diagnostic_memory_by_address import (
    DiagnosticMemoryByAddress,
)
from armodel.models.M2.AUTOSARTemplates.GenericStructure.GeneralTemplateClasses.ArObject.ar_object import ARObject
from armodel.serialization import SerializationHelper
from armodel.models.M2.AUTOSARTemplates.GenericStructure.GeneralTemplateClasses.ArObject.ar_ref import ARRef


class DiagnosticTransferExit(DiagnosticMemoryByAddress):
    """AUTOSAR DiagnosticTransferExit."""

    @property
    def is_abstract(self) -> bool:
        """Check if this class is abstract.

        Returns:
            False for concrete classes
        """
        return False

    transfer_exit_ref: Optional[ARRef]
    def __init__(self) -> None:
        """Initialize DiagnosticTransferExit."""
        super().__init__()
        self.transfer_exit_ref: Optional[ARRef] = None

    def serialize(self) -> ET.Element:
        """Serialize DiagnosticTransferExit to XML element.

        Returns:
            xml.etree.ElementTree.Element representing this object
        """
        # Get XML tag name for this class
        tag = SerializationHelper.get_xml_tag(self.__class__)
        elem = ET.Element(tag)

        # First, call parent's serialize to handle inherited attributes
        parent_elem = super(DiagnosticTransferExit, self).serialize()

        # Copy all attributes from parent element
        elem.attrib.update(parent_elem.attrib)

        # Copy text from parent element
        if parent_elem.text:
            elem.text = parent_elem.text

        # Copy all children from parent element
        for child in parent_elem:
            elem.append(child)

        # Serialize transfer_exit_ref
        if self.transfer_exit_ref is not None:
            serialized = SerializationHelper.serialize_item(self.transfer_exit_ref, "DiagnosticTransferExit")
            if serialized is not None:
                # Wrap with correct tag
                wrapped = ET.Element("TRANSFER-EXIT-REF")
                if hasattr(serialized, 'attrib'):
                    wrapped.attrib.update(serialized.attrib)
                    if serialized.text:
                        wrapped.text = serialized.text
                for child in serialized:
                    wrapped.append(child)
                elem.append(wrapped)

        return elem

    @classmethod
    def deserialize(cls, element: ET.Element) -> "DiagnosticTransferExit":
        """Deserialize XML element to DiagnosticTransferExit object.

        Args:
            element: XML element to deserialize from

        Returns:
            Deserialized DiagnosticTransferExit object
        """
        # First, call parent's deserialize to handle inherited attributes
        obj = super(DiagnosticTransferExit, cls).deserialize(element)

        # Parse transfer_exit_ref
        child = SerializationHelper.find_child_element(element, "TRANSFER-EXIT-REF")
        if child is not None:
            transfer_exit_ref_value = ARRef.deserialize(child)
            obj.transfer_exit_ref = transfer_exit_ref_value

        return obj



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
