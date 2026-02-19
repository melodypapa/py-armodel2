"""DiagnosticRequestVehicleInfoClass AUTOSAR element.

References:
  - AUTOSAR_CP_TPS_DiagnosticExtractTemplate.pdf (page 160)

JSON Source: docs/json/packages/M2_AUTOSARTemplates_DiagnosticExtract_Dcm_ObdService_Mode_0x09_RequestVehicleInformation.classes.json"""

from __future__ import annotations
from typing import TYPE_CHECKING, Optional
import xml.etree.ElementTree as ET

from armodel.models.M2.AUTOSARTemplates.DiagnosticExtract.Dcm.DiagnosticService.CommonService.diagnostic_service_class import (
    DiagnosticServiceClass,
)
from armodel.models.M2.AUTOSARTemplates.GenericStructure.GeneralTemplateClasses.ArObject.ar_object import ARObject


class DiagnosticRequestVehicleInfoClass(DiagnosticServiceClass):
    """AUTOSAR DiagnosticRequestVehicleInfoClass."""

    @property
    def is_abstract(self) -> bool:
        """Check if this class is abstract.

        Returns:
            False for concrete classes
        """
        return False

    def __init__(self) -> None:
        """Initialize DiagnosticRequestVehicleInfoClass."""
        super().__init__()

    def serialize(self) -> ET.Element:
        """Serialize DiagnosticRequestVehicleInfoClass to XML element.

        Returns:
            xml.etree.ElementTree.Element representing this object
        """
        # Get XML tag name for this class
        tag = self._get_xml_tag()
        elem = ET.Element(tag)

        # First, call parent's serialize to handle inherited attributes
        parent_elem = super(DiagnosticRequestVehicleInfoClass, self).serialize()

        # Copy all attributes from parent element
        elem.attrib.update(parent_elem.attrib)

        # Copy all children from parent element
        for child in parent_elem:
            elem.append(child)

        return elem

    @classmethod
    def deserialize(cls, element: ET.Element) -> "DiagnosticRequestVehicleInfoClass":
        """Deserialize XML element to DiagnosticRequestVehicleInfoClass object.

        Args:
            element: XML element to deserialize from

        Returns:
            Deserialized DiagnosticRequestVehicleInfoClass object
        """
        # Delegate to parent class to handle inherited attributes
        return super(DiagnosticRequestVehicleInfoClass, cls).deserialize(element)



class DiagnosticRequestVehicleInfoClassBuilder:
    """Builder for DiagnosticRequestVehicleInfoClass."""

    def __init__(self) -> None:
        """Initialize builder."""
        self._obj: DiagnosticRequestVehicleInfoClass = DiagnosticRequestVehicleInfoClass()

    def build(self) -> DiagnosticRequestVehicleInfoClass:
        """Build and return DiagnosticRequestVehicleInfoClass object.

        Returns:
            DiagnosticRequestVehicleInfoClass instance
        """
        # TODO: Add validation
        return self._obj
