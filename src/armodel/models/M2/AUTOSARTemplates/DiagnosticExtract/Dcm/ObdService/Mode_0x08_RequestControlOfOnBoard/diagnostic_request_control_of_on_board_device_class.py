"""DiagnosticRequestControlOfOnBoardDeviceClass AUTOSAR element.

References:
  - AUTOSAR_CP_TPS_DiagnosticExtractTemplate.pdf (page 158)

JSON Source: docs/json/packages/M2_AUTOSARTemplates_DiagnosticExtract_Dcm_ObdService_Mode_0x08_RequestControlOfOnBoard.classes.json"""

from __future__ import annotations
from typing import TYPE_CHECKING, Optional
import xml.etree.ElementTree as ET

from armodel.models.M2.AUTOSARTemplates.DiagnosticExtract.Dcm.DiagnosticService.CommonService.diagnostic_service_class import (
    DiagnosticServiceClass,
)
from armodel.models.M2.AUTOSARTemplates.GenericStructure.GeneralTemplateClasses.ArObject.ar_object import ARObject


class DiagnosticRequestControlOfOnBoardDeviceClass(DiagnosticServiceClass):
    """AUTOSAR DiagnosticRequestControlOfOnBoardDeviceClass."""

    @property
    def is_abstract(self) -> bool:
        """Check if this class is abstract.

        Returns:
            False for concrete classes
        """
        return False

    def __init__(self) -> None:
        """Initialize DiagnosticRequestControlOfOnBoardDeviceClass."""
        super().__init__()

    def serialize(self) -> ET.Element:
        """Serialize DiagnosticRequestControlOfOnBoardDeviceClass to XML element.

        Returns:
            xml.etree.ElementTree.Element representing this object
        """
        # Get XML tag name for this class
        tag = self._get_xml_tag()
        elem = ET.Element(tag)

        # First, call parent's serialize to handle inherited attributes
        parent_elem = super(DiagnosticRequestControlOfOnBoardDeviceClass, self).serialize()

        # Copy all attributes from parent element
        elem.attrib.update(parent_elem.attrib)

        # Copy all children from parent element
        for child in parent_elem:
            elem.append(child)

        return elem

    @classmethod
    def deserialize(cls, element: ET.Element) -> "DiagnosticRequestControlOfOnBoardDeviceClass":
        """Deserialize XML element to DiagnosticRequestControlOfOnBoardDeviceClass object.

        Args:
            element: XML element to deserialize from

        Returns:
            Deserialized DiagnosticRequestControlOfOnBoardDeviceClass object
        """
        # Delegate to parent class to handle inherited attributes
        return super(DiagnosticRequestControlOfOnBoardDeviceClass, cls).deserialize(element)



class DiagnosticRequestControlOfOnBoardDeviceClassBuilder:
    """Builder for DiagnosticRequestControlOfOnBoardDeviceClass."""

    def __init__(self) -> None:
        """Initialize builder."""
        self._obj: DiagnosticRequestControlOfOnBoardDeviceClass = DiagnosticRequestControlOfOnBoardDeviceClass()

    def build(self) -> DiagnosticRequestControlOfOnBoardDeviceClass:
        """Build and return DiagnosticRequestControlOfOnBoardDeviceClass object.

        Returns:
            DiagnosticRequestControlOfOnBoardDeviceClass instance
        """
        # TODO: Add validation
        return self._obj
