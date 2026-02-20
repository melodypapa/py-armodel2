"""DiagnosticTransferExitClass AUTOSAR element.

References:
  - AUTOSAR_CP_TPS_DiagnosticExtractTemplate.pdf (page 143)

JSON Source: docs/json/packages/M2_AUTOSARTemplates_DiagnosticExtract_Dcm_DiagnosticService_MemoryByAddress.classes.json"""

from __future__ import annotations
from typing import TYPE_CHECKING, Optional
import xml.etree.ElementTree as ET

from armodel.models.M2.AUTOSARTemplates.DiagnosticExtract.Dcm.DiagnosticService.CommonService.diagnostic_service_class import (
    DiagnosticServiceClass,
)
from armodel.models.M2.AUTOSARTemplates.GenericStructure.GeneralTemplateClasses.ArObject.ar_object import ARObject


class DiagnosticTransferExitClass(DiagnosticServiceClass):
    """AUTOSAR DiagnosticTransferExitClass."""

    @property
    def is_abstract(self) -> bool:
        """Check if this class is abstract.

        Returns:
            False for concrete classes
        """
        return False

    def __init__(self) -> None:
        """Initialize DiagnosticTransferExitClass."""
        super().__init__()

    def serialize(self) -> ET.Element:
        """Serialize DiagnosticTransferExitClass to XML element.

        Returns:
            xml.etree.ElementTree.Element representing this object
        """
        # Get XML tag name for this class
        tag = self._get_xml_tag()
        elem = ET.Element(tag)

        # First, call parent's serialize to handle inherited attributes
        parent_elem = super(DiagnosticTransferExitClass, self).serialize()

        # Copy all attributes from parent element
        elem.attrib.update(parent_elem.attrib)

        # Copy all children from parent element
        for child in parent_elem:
            elem.append(child)

        return elem

    @classmethod
    def deserialize(cls, element: ET.Element) -> "DiagnosticTransferExitClass":
        """Deserialize XML element to DiagnosticTransferExitClass object.

        Args:
            element: XML element to deserialize from

        Returns:
            Deserialized DiagnosticTransferExitClass object
        """
        # Delegate to parent class to handle inherited attributes
        return super(DiagnosticTransferExitClass, cls).deserialize(element)



class DiagnosticTransferExitClassBuilder:
    """Builder for DiagnosticTransferExitClass."""

    def __init__(self) -> None:
        """Initialize builder."""
        self._obj: DiagnosticTransferExitClass = DiagnosticTransferExitClass()

    def build(self) -> DiagnosticTransferExitClass:
        """Build and return DiagnosticTransferExitClass object.

        Returns:
            DiagnosticTransferExitClass instance
        """
        # TODO: Add validation
        return self._obj
