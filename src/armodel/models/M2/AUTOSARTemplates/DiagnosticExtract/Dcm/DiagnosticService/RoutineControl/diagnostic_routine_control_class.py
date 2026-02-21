"""DiagnosticRoutineControlClass AUTOSAR element.

References:
  - AUTOSAR_CP_TPS_DiagnosticExtractTemplate.pdf (page 125)

JSON Source: docs/json/packages/M2_AUTOSARTemplates_DiagnosticExtract_Dcm_DiagnosticService_RoutineControl.classes.json"""

from __future__ import annotations
from typing import TYPE_CHECKING, Optional
import xml.etree.ElementTree as ET

from armodel.models.M2.AUTOSARTemplates.DiagnosticExtract.Dcm.DiagnosticService.CommonService.diagnostic_service_class import (
    DiagnosticServiceClass,
)
from armodel.models.M2.AUTOSARTemplates.GenericStructure.GeneralTemplateClasses.ArObject.ar_object import ARObject
from armodel.serialization import SerializationHelper


class DiagnosticRoutineControlClass(DiagnosticServiceClass):
    """AUTOSAR DiagnosticRoutineControlClass."""

    @property
    def is_abstract(self) -> bool:
        """Check if this class is abstract.

        Returns:
            False for concrete classes
        """
        return False

    def __init__(self) -> None:
        """Initialize DiagnosticRoutineControlClass."""
        super().__init__()

    def serialize(self) -> ET.Element:
        """Serialize DiagnosticRoutineControlClass to XML element.

        Returns:
            xml.etree.ElementTree.Element representing this object
        """
        # Get XML tag name for this class
        tag = SerializationHelper.get_xml_tag(self.__class__)
        elem = ET.Element(tag)

        # First, call parent's serialize to handle inherited attributes
        parent_elem = super(DiagnosticRoutineControlClass, self).serialize()

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
    def deserialize(cls, element: ET.Element) -> "DiagnosticRoutineControlClass":
        """Deserialize XML element to DiagnosticRoutineControlClass object.

        Args:
            element: XML element to deserialize from

        Returns:
            Deserialized DiagnosticRoutineControlClass object
        """
        # Delegate to parent class to handle inherited attributes
        return super(DiagnosticRoutineControlClass, cls).deserialize(element)



class DiagnosticRoutineControlClassBuilder:
    """Builder for DiagnosticRoutineControlClass."""

    def __init__(self) -> None:
        """Initialize builder."""
        self._obj: DiagnosticRoutineControlClass = DiagnosticRoutineControlClass()

    def build(self) -> DiagnosticRoutineControlClass:
        """Build and return DiagnosticRoutineControlClass object.

        Returns:
            DiagnosticRoutineControlClass instance
        """
        # TODO: Add validation
        return self._obj
