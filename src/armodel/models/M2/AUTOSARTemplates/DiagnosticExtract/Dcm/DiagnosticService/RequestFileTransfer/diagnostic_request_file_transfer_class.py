"""DiagnosticRequestFileTransferClass AUTOSAR element.

References:
  - AUTOSAR_CP_TPS_DiagnosticExtractTemplate.pdf (page 147)

JSON Source: docs/json/packages/M2_AUTOSARTemplates_DiagnosticExtract_Dcm_DiagnosticService_RequestFileTransfer.classes.json"""

from __future__ import annotations
from typing import TYPE_CHECKING, Optional
import xml.etree.ElementTree as ET

from armodel.models.M2.AUTOSARTemplates.DiagnosticExtract.Dcm.DiagnosticService.CommonService.diagnostic_service_class import (
    DiagnosticServiceClass,
)
from armodel.models.M2.AUTOSARTemplates.GenericStructure.GeneralTemplateClasses.ArObject.ar_object import ARObject
from armodel.serialization import SerializationHelper


class DiagnosticRequestFileTransferClass(DiagnosticServiceClass):
    """AUTOSAR DiagnosticRequestFileTransferClass."""

    @property
    def is_abstract(self) -> bool:
        """Check if this class is abstract.

        Returns:
            False for concrete classes
        """
        return False

    def __init__(self) -> None:
        """Initialize DiagnosticRequestFileTransferClass."""
        super().__init__()

    def serialize(self) -> ET.Element:
        """Serialize DiagnosticRequestFileTransferClass to XML element.

        Returns:
            xml.etree.ElementTree.Element representing this object
        """
        # Get XML tag name for this class
        tag = SerializationHelper.get_xml_tag(self.__class__)
        elem = ET.Element(tag)

        # First, call parent's serialize to handle inherited attributes
        parent_elem = super(DiagnosticRequestFileTransferClass, self).serialize()

        # Copy all attributes from parent element
        elem.attrib.update(parent_elem.attrib)

        # Copy text from parent element
        if parent_elem.text:
            elem.text = parent_elem.text

        # Copy all children from parent element
        for child in parent_elem:
            elem.append(child)

        return elem

    @classmethod
    def deserialize(cls, element: ET.Element) -> "DiagnosticRequestFileTransferClass":
        """Deserialize XML element to DiagnosticRequestFileTransferClass object.

        Args:
            element: XML element to deserialize from

        Returns:
            Deserialized DiagnosticRequestFileTransferClass object
        """
        # Delegate to parent class to handle inherited attributes
        return super(DiagnosticRequestFileTransferClass, cls).deserialize(element)



class DiagnosticRequestFileTransferClassBuilder:
    """Builder for DiagnosticRequestFileTransferClass."""

    def __init__(self) -> None:
        """Initialize builder."""
        self._obj: DiagnosticRequestFileTransferClass = DiagnosticRequestFileTransferClass()

    def build(self) -> DiagnosticRequestFileTransferClass:
        """Build and return DiagnosticRequestFileTransferClass object.

        Returns:
            DiagnosticRequestFileTransferClass instance
        """
        # TODO: Add validation
        return self._obj
