"""DiagnosticClearDiagnosticInformation AUTOSAR element.

References:
  - AUTOSAR_CP_TPS_DiagnosticExtractTemplate.pdf (page 137)

JSON Source: docs/json/packages/M2_AUTOSARTemplates_DiagnosticExtract_Dcm_DiagnosticService_ClearDiagnosticInfo.classes.json"""

from __future__ import annotations
from typing import TYPE_CHECKING, Optional, Any
import xml.etree.ElementTree as ET

from armodel.models.M2.AUTOSARTemplates.DiagnosticExtract.Dcm.DiagnosticService.CommonService.diagnostic_service_instance import (
    DiagnosticServiceInstance,
)
from armodel.models.M2.AUTOSARTemplates.GenericStructure.GeneralTemplateClasses.ArObject.ar_object import ARObject


class DiagnosticClearDiagnosticInformation(DiagnosticServiceInstance):
    """AUTOSAR DiagnosticClearDiagnosticInformation."""

    @property
    def is_abstract(self) -> bool:
        """Check if this class is abstract.

        Returns:
            False for concrete classes
        """
        return False

    clear_diagnostic: Optional[Any]
    def __init__(self) -> None:
        """Initialize DiagnosticClearDiagnosticInformation."""
        super().__init__()
        self.clear_diagnostic: Optional[Any] = None
    def serialize(self) -> ET.Element:
        """Serialize DiagnosticClearDiagnosticInformation to XML element.

        Returns:
            xml.etree.ElementTree.Element representing this object
        """
        # Get XML tag name for this class
        tag = ARObject._get_xml_tag(self)
        elem = ET.Element(tag)

        # First, call parent's serialize to handle inherited attributes
        parent_elem = super(DiagnosticClearDiagnosticInformation, self).serialize()

        # Copy all attributes from parent element
        elem.attrib.update(parent_elem.attrib)

        # Copy all children from parent element
        for child in parent_elem:
            elem.append(child)

        # Serialize clear_diagnostic
        if self.clear_diagnostic is not None:
            serialized = ARObject._serialize_item(self.clear_diagnostic, "Any")
            if serialized is not None:
                # Wrap with correct tag
                wrapped = ET.Element("CLEAR-DIAGNOSTIC")
                if hasattr(serialized, 'attrib'):
                    wrapped.attrib.update(serialized.attrib)
                    if serialized.text:
                        wrapped.text = serialized.text
                for child in serialized:
                    wrapped.append(child)
                elem.append(wrapped)

        return elem

    @classmethod
    def deserialize(cls, element: ET.Element) -> "DiagnosticClearDiagnosticInformation":
        """Deserialize XML element to DiagnosticClearDiagnosticInformation object.

        Args:
            element: XML element to deserialize from

        Returns:
            Deserialized DiagnosticClearDiagnosticInformation object
        """
        # First, call parent's deserialize to handle inherited attributes
        obj = super(DiagnosticClearDiagnosticInformation, cls).deserialize(element)

        # Parse clear_diagnostic
        child = ARObject._find_child_element(element, "CLEAR-DIAGNOSTIC")
        if child is not None:
            clear_diagnostic_value = child.text
            obj.clear_diagnostic = clear_diagnostic_value

        return obj



class DiagnosticClearDiagnosticInformationBuilder:
    """Builder for DiagnosticClearDiagnosticInformation."""

    def __init__(self) -> None:
        """Initialize builder."""
        self._obj: DiagnosticClearDiagnosticInformation = DiagnosticClearDiagnosticInformation()

    def build(self) -> DiagnosticClearDiagnosticInformation:
        """Build and return DiagnosticClearDiagnosticInformation object.

        Returns:
            DiagnosticClearDiagnosticInformation instance
        """
        # TODO: Add validation
        return self._obj
