"""DiagnosticWriteDataByIdentifierClass AUTOSAR element.

References:
  - AUTOSAR_CP_TPS_DiagnosticExtractTemplate.pdf (page 113)

JSON Source: docs/json/packages/M2_AUTOSARTemplates_DiagnosticExtract_Dcm_DiagnosticService_DataByIdentifier.classes.json"""

from __future__ import annotations
from typing import TYPE_CHECKING, Optional
import xml.etree.ElementTree as ET

from armodel.models.M2.AUTOSARTemplates.DiagnosticExtract.Dcm.DiagnosticService.CommonService.diagnostic_service_class import (
    DiagnosticServiceClass,
)
from armodel.models.M2.AUTOSARTemplates.GenericStructure.GeneralTemplateClasses.ArObject.ar_object import ARObject
from armodel.serialization import SerializationHelper


class DiagnosticWriteDataByIdentifierClass(DiagnosticServiceClass):
    """AUTOSAR DiagnosticWriteDataByIdentifierClass."""

    @property
    def is_abstract(self) -> bool:
        """Check if this class is abstract.

        Returns:
            False for concrete classes
        """
        return False

    def __init__(self) -> None:
        """Initialize DiagnosticWriteDataByIdentifierClass."""
        super().__init__()

    def serialize(self) -> ET.Element:
        """Serialize DiagnosticWriteDataByIdentifierClass to XML element.

        Returns:
            xml.etree.ElementTree.Element representing this object
        """
        # Get XML tag name for this class
        tag = SerializationHelper.get_xml_tag(self.__class__)
        elem = ET.Element(tag)

        # First, call parent's serialize to handle inherited attributes
        parent_elem = super(DiagnosticWriteDataByIdentifierClass, self).serialize()

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
    def deserialize(cls, element: ET.Element) -> "DiagnosticWriteDataByIdentifierClass":
        """Deserialize XML element to DiagnosticWriteDataByIdentifierClass object.

        Args:
            element: XML element to deserialize from

        Returns:
            Deserialized DiagnosticWriteDataByIdentifierClass object
        """
        # Delegate to parent class to handle inherited attributes
        return super(DiagnosticWriteDataByIdentifierClass, cls).deserialize(element)



class DiagnosticWriteDataByIdentifierClassBuilder:
    """Builder for DiagnosticWriteDataByIdentifierClass."""

    def __init__(self) -> None:
        """Initialize builder."""
        self._obj: DiagnosticWriteDataByIdentifierClass = DiagnosticWriteDataByIdentifierClass()

    def build(self) -> DiagnosticWriteDataByIdentifierClass:
        """Build and return DiagnosticWriteDataByIdentifierClass object.

        Returns:
            DiagnosticWriteDataByIdentifierClass instance
        """
        # TODO: Add validation
        return self._obj
