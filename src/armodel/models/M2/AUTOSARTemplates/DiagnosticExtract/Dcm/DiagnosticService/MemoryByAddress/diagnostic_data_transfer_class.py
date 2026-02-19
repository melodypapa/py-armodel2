"""DiagnosticDataTransferClass AUTOSAR element.

References:
  - AUTOSAR_CP_TPS_DiagnosticExtractTemplate.pdf (page 144)

JSON Source: docs/json/packages/M2_AUTOSARTemplates_DiagnosticExtract_Dcm_DiagnosticService_MemoryByAddress.classes.json"""

from __future__ import annotations
from typing import TYPE_CHECKING, Optional
import xml.etree.ElementTree as ET

from armodel.models.M2.AUTOSARTemplates.DiagnosticExtract.Dcm.DiagnosticService.CommonService.diagnostic_service_class import (
    DiagnosticServiceClass,
)
from armodel.models.M2.AUTOSARTemplates.GenericStructure.GeneralTemplateClasses.ArObject.ar_object import ARObject


class DiagnosticDataTransferClass(DiagnosticServiceClass):
    """AUTOSAR DiagnosticDataTransferClass."""

    @property
    def is_abstract(self) -> bool:
        """Check if this class is abstract.

        Returns:
            False for concrete classes
        """
        return False

    def __init__(self) -> None:
        """Initialize DiagnosticDataTransferClass."""
        super().__init__()
    def serialize(self) -> ET.Element:
        """Serialize DiagnosticDataTransferClass to XML element.

        Returns:
            xml.etree.ElementTree.Element representing this object
        """
        # Get XML tag name for this class
        tag = ARObject._get_xml_tag(self)
        elem = ET.Element(tag)

        # First, call parent's serialize to handle inherited attributes
        parent_elem = super(DiagnosticDataTransferClass, self).serialize()

        # Copy all attributes from parent element
        elem.attrib.update(parent_elem.attrib)

        # Copy all children from parent element
        for child in parent_elem:
            elem.append(child)

        return elem

    @classmethod
    def deserialize(cls, element: ET.Element) -> "DiagnosticDataTransferClass":
        """Deserialize XML element to DiagnosticDataTransferClass object.

        Args:
            element: XML element to deserialize from

        Returns:
            Deserialized DiagnosticDataTransferClass object
        """
        # Delegate to parent class to handle inherited attributes
        return super(DiagnosticDataTransferClass, cls).deserialize(element)



class DiagnosticDataTransferClassBuilder:
    """Builder for DiagnosticDataTransferClass."""

    def __init__(self) -> None:
        """Initialize builder."""
        self._obj: DiagnosticDataTransferClass = DiagnosticDataTransferClass()

    def build(self) -> DiagnosticDataTransferClass:
        """Build and return DiagnosticDataTransferClass object.

        Returns:
            DiagnosticDataTransferClass instance
        """
        # TODO: Add validation
        return self._obj
