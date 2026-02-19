"""DiagnosticRoutineControl AUTOSAR element.

References:
  - AUTOSAR_CP_TPS_DiagnosticExtractTemplate.pdf (page 125)

JSON Source: docs/json/packages/M2_AUTOSARTemplates_DiagnosticExtract_Dcm_DiagnosticService_RoutineControl.classes.json"""

from __future__ import annotations
from typing import TYPE_CHECKING, Optional
import xml.etree.ElementTree as ET

from armodel.models.M2.AUTOSARTemplates.DiagnosticExtract.Dcm.DiagnosticService.CommonService.diagnostic_service_instance import (
    DiagnosticServiceInstance,
)
from armodel.models.M2.AUTOSARTemplates.GenericStructure.GeneralTemplateClasses.ArObject.ar_object import ARObject
from armodel.models.M2.AUTOSARTemplates.DiagnosticExtract.CommonDiagnostics.diagnostic_routine import (
    DiagnosticRoutine,
)


class DiagnosticRoutineControl(DiagnosticServiceInstance):
    """AUTOSAR DiagnosticRoutineControl."""

    @property
    def is_abstract(self) -> bool:
        """Check if this class is abstract.

        Returns:
            False for concrete classes
        """
        return False

    routine: Optional[DiagnosticRoutine]
    routine_control: Optional[DiagnosticRoutine]
    def __init__(self) -> None:
        """Initialize DiagnosticRoutineControl."""
        super().__init__()
        self.routine: Optional[DiagnosticRoutine] = None
        self.routine_control: Optional[DiagnosticRoutine] = None
    def serialize(self) -> ET.Element:
        """Serialize DiagnosticRoutineControl to XML element.

        Returns:
            xml.etree.ElementTree.Element representing this object
        """
        # Get XML tag name for this class
        tag = self._get_xml_tag()
        elem = ET.Element(tag)

        # First, call parent's serialize to handle inherited attributes
        parent_elem = super(DiagnosticRoutineControl, self).serialize()

        # Copy all attributes from parent element
        elem.attrib.update(parent_elem.attrib)

        # Copy all children from parent element
        for child in parent_elem:
            elem.append(child)

        # Serialize routine
        if self.routine is not None:
            serialized = ARObject._serialize_item(self.routine, "DiagnosticRoutine")
            if serialized is not None:
                # Wrap with correct tag
                wrapped = ET.Element("ROUTINE")
                if hasattr(serialized, 'attrib'):
                    wrapped.attrib.update(serialized.attrib)
                    if serialized.text:
                        wrapped.text = serialized.text
                for child in serialized:
                    wrapped.append(child)
                elem.append(wrapped)

        # Serialize routine_control
        if self.routine_control is not None:
            serialized = ARObject._serialize_item(self.routine_control, "DiagnosticRoutine")
            if serialized is not None:
                # Wrap with correct tag
                wrapped = ET.Element("ROUTINE-CONTROL")
                if hasattr(serialized, 'attrib'):
                    wrapped.attrib.update(serialized.attrib)
                    if serialized.text:
                        wrapped.text = serialized.text
                for child in serialized:
                    wrapped.append(child)
                elem.append(wrapped)

        return elem

    @classmethod
    def deserialize(cls, element: ET.Element) -> "DiagnosticRoutineControl":
        """Deserialize XML element to DiagnosticRoutineControl object.

        Args:
            element: XML element to deserialize from

        Returns:
            Deserialized DiagnosticRoutineControl object
        """
        # First, call parent's deserialize to handle inherited attributes
        obj = super(DiagnosticRoutineControl, cls).deserialize(element)

        # Parse routine
        child = ARObject._find_child_element(element, "ROUTINE")
        if child is not None:
            routine_value = ARObject._deserialize_by_tag(child, "DiagnosticRoutine")
            obj.routine = routine_value

        # Parse routine_control
        child = ARObject._find_child_element(element, "ROUTINE-CONTROL")
        if child is not None:
            routine_control_value = ARObject._deserialize_by_tag(child, "DiagnosticRoutine")
            obj.routine_control = routine_control_value

        return obj



class DiagnosticRoutineControlBuilder:
    """Builder for DiagnosticRoutineControl."""

    def __init__(self) -> None:
        """Initialize builder."""
        self._obj: DiagnosticRoutineControl = DiagnosticRoutineControl()

    def build(self) -> DiagnosticRoutineControl:
        """Build and return DiagnosticRoutineControl object.

        Returns:
            DiagnosticRoutineControl instance
        """
        # TODO: Add validation
        return self._obj
