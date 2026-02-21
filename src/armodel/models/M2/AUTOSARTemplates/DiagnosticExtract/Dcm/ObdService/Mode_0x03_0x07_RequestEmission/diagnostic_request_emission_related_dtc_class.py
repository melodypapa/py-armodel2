"""DiagnosticRequestEmissionRelatedDTCClass AUTOSAR element.

References:
  - AUTOSAR_CP_TPS_DiagnosticExtractTemplate.pdf (page 154)

JSON Source: docs/json/packages/M2_AUTOSARTemplates_DiagnosticExtract_Dcm_ObdService_Mode_0x03_0x07_RequestEmission.classes.json"""

from __future__ import annotations
from typing import TYPE_CHECKING, Optional
import xml.etree.ElementTree as ET

from armodel.models.M2.AUTOSARTemplates.DiagnosticExtract.Dcm.DiagnosticService.CommonService.diagnostic_service_class import (
    DiagnosticServiceClass,
)
from armodel.models.M2.AUTOSARTemplates.GenericStructure.GeneralTemplateClasses.ArObject.ar_object import ARObject


class DiagnosticRequestEmissionRelatedDTCClass(DiagnosticServiceClass):
    """AUTOSAR DiagnosticRequestEmissionRelatedDTCClass."""

    @property
    def is_abstract(self) -> bool:
        """Check if this class is abstract.

        Returns:
            False for concrete classes
        """
        return False

    def __init__(self) -> None:
        """Initialize DiagnosticRequestEmissionRelatedDTCClass."""
        super().__init__()

    def serialize(self) -> ET.Element:
        """Serialize DiagnosticRequestEmissionRelatedDTCClass to XML element.

        Returns:
            xml.etree.ElementTree.Element representing this object
        """
        # Get XML tag name for this class
        tag = self._get_xml_tag()
        elem = ET.Element(tag)

        # First, call parent's serialize to handle inherited attributes
        parent_elem = super(DiagnosticRequestEmissionRelatedDTCClass, self).serialize()

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
    def deserialize(cls, element: ET.Element) -> "DiagnosticRequestEmissionRelatedDTCClass":
        """Deserialize XML element to DiagnosticRequestEmissionRelatedDTCClass object.

        Args:
            element: XML element to deserialize from

        Returns:
            Deserialized DiagnosticRequestEmissionRelatedDTCClass object
        """
        # Delegate to parent class to handle inherited attributes
        return super(DiagnosticRequestEmissionRelatedDTCClass, cls).deserialize(element)



class DiagnosticRequestEmissionRelatedDTCClassBuilder:
    """Builder for DiagnosticRequestEmissionRelatedDTCClass."""

    def __init__(self) -> None:
        """Initialize builder."""
        self._obj: DiagnosticRequestEmissionRelatedDTCClass = DiagnosticRequestEmissionRelatedDTCClass()

    def build(self) -> DiagnosticRequestEmissionRelatedDTCClass:
        """Build and return DiagnosticRequestEmissionRelatedDTCClass object.

        Returns:
            DiagnosticRequestEmissionRelatedDTCClass instance
        """
        # TODO: Add validation
        return self._obj
