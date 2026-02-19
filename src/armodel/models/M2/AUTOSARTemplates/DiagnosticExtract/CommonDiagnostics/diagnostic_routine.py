"""DiagnosticRoutine AUTOSAR element.

References:
  - AUTOSAR_CP_TPS_DiagnosticExtractTemplate.pdf (page 124)

JSON Source: docs/json/packages/M2_AUTOSARTemplates_DiagnosticExtract_CommonDiagnostics.classes.json"""

from __future__ import annotations
from typing import TYPE_CHECKING, Optional, Any
import xml.etree.ElementTree as ET

from armodel.models.M2.AUTOSARTemplates.DiagnosticExtract.CommonDiagnostics.diagnostic_common_element import (
    DiagnosticCommonElement,
)
from armodel.models.M2.AUTOSARTemplates.GenericStructure.GeneralTemplateClasses.ArObject.ar_object import ARObject
from armodel.models.M2.AUTOSARTemplates.GenericStructure.GeneralTemplateClasses.PrimitiveTypes import (
    PositiveInteger,
)
from armodel.models.M2.AUTOSARTemplates.DiagnosticExtract.CommonDiagnostics.diagnostic_start_routine import (
    DiagnosticStartRoutine,
)
from armodel.models.M2.AUTOSARTemplates.DiagnosticExtract.CommonDiagnostics.diagnostic_stop_routine import (
    DiagnosticStopRoutine,
)


class DiagnosticRoutine(DiagnosticCommonElement):
    """AUTOSAR DiagnosticRoutine."""

    @property
    def is_abstract(self) -> bool:
        """Check if this class is abstract.

        Returns:
            False for concrete classes
        """
        return False

    id: Optional[PositiveInteger]
    request_result: Optional[Any]
    routine_info: Optional[PositiveInteger]
    start: Optional[DiagnosticStartRoutine]
    stop: Optional[DiagnosticStopRoutine]
    def __init__(self) -> None:
        """Initialize DiagnosticRoutine."""
        super().__init__()
        self.id: Optional[PositiveInteger] = None
        self.request_result: Optional[Any] = None
        self.routine_info: Optional[PositiveInteger] = None
        self.start: Optional[DiagnosticStartRoutine] = None
        self.stop: Optional[DiagnosticStopRoutine] = None
    def serialize(self) -> ET.Element:
        """Serialize DiagnosticRoutine to XML element.

        Returns:
            xml.etree.ElementTree.Element representing this object
        """
        # Get XML tag name for this class
        tag = ARObject._get_xml_tag(self)
        elem = ET.Element(tag)

        # First, call parent's serialize to handle inherited attributes
        parent_elem = super(DiagnosticRoutine, self).serialize()

        # Copy all attributes from parent element
        elem.attrib.update(parent_elem.attrib)

        # Copy all children from parent element
        for child in parent_elem:
            elem.append(child)

        # Serialize id
        if self.id is not None:
            serialized = ARObject._serialize_item(self.id, "PositiveInteger")
            if serialized is not None:
                # Wrap with correct tag
                wrapped = ET.Element("ID")
                if hasattr(serialized, 'attrib'):
                    wrapped.attrib.update(serialized.attrib)
                    if serialized.text:
                        wrapped.text = serialized.text
                for child in serialized:
                    wrapped.append(child)
                elem.append(wrapped)

        # Serialize request_result
        if self.request_result is not None:
            serialized = ARObject._serialize_item(self.request_result, "Any")
            if serialized is not None:
                # Wrap with correct tag
                wrapped = ET.Element("REQUEST-RESULT")
                if hasattr(serialized, 'attrib'):
                    wrapped.attrib.update(serialized.attrib)
                    if serialized.text:
                        wrapped.text = serialized.text
                for child in serialized:
                    wrapped.append(child)
                elem.append(wrapped)

        # Serialize routine_info
        if self.routine_info is not None:
            serialized = ARObject._serialize_item(self.routine_info, "PositiveInteger")
            if serialized is not None:
                # Wrap with correct tag
                wrapped = ET.Element("ROUTINE-INFO")
                if hasattr(serialized, 'attrib'):
                    wrapped.attrib.update(serialized.attrib)
                    if serialized.text:
                        wrapped.text = serialized.text
                for child in serialized:
                    wrapped.append(child)
                elem.append(wrapped)

        # Serialize start
        if self.start is not None:
            serialized = ARObject._serialize_item(self.start, "DiagnosticStartRoutine")
            if serialized is not None:
                # Wrap with correct tag
                wrapped = ET.Element("START")
                if hasattr(serialized, 'attrib'):
                    wrapped.attrib.update(serialized.attrib)
                    if serialized.text:
                        wrapped.text = serialized.text
                for child in serialized:
                    wrapped.append(child)
                elem.append(wrapped)

        # Serialize stop
        if self.stop is not None:
            serialized = ARObject._serialize_item(self.stop, "DiagnosticStopRoutine")
            if serialized is not None:
                # Wrap with correct tag
                wrapped = ET.Element("STOP")
                if hasattr(serialized, 'attrib'):
                    wrapped.attrib.update(serialized.attrib)
                    if serialized.text:
                        wrapped.text = serialized.text
                for child in serialized:
                    wrapped.append(child)
                elem.append(wrapped)

        return elem

    @classmethod
    def deserialize(cls, element: ET.Element) -> "DiagnosticRoutine":
        """Deserialize XML element to DiagnosticRoutine object.

        Args:
            element: XML element to deserialize from

        Returns:
            Deserialized DiagnosticRoutine object
        """
        # First, call parent's deserialize to handle inherited attributes
        obj = super(DiagnosticRoutine, cls).deserialize(element)

        # Parse id
        child = ARObject._find_child_element(element, "ID")
        if child is not None:
            id_value = child.text
            obj.id = id_value

        # Parse request_result
        child = ARObject._find_child_element(element, "REQUEST-RESULT")
        if child is not None:
            request_result_value = child.text
            obj.request_result = request_result_value

        # Parse routine_info
        child = ARObject._find_child_element(element, "ROUTINE-INFO")
        if child is not None:
            routine_info_value = child.text
            obj.routine_info = routine_info_value

        # Parse start
        child = ARObject._find_child_element(element, "START")
        if child is not None:
            start_value = ARObject._deserialize_by_tag(child, "DiagnosticStartRoutine")
            obj.start = start_value

        # Parse stop
        child = ARObject._find_child_element(element, "STOP")
        if child is not None:
            stop_value = ARObject._deserialize_by_tag(child, "DiagnosticStopRoutine")
            obj.stop = stop_value

        return obj



class DiagnosticRoutineBuilder:
    """Builder for DiagnosticRoutine."""

    def __init__(self) -> None:
        """Initialize builder."""
        self._obj: DiagnosticRoutine = DiagnosticRoutine()

    def build(self) -> DiagnosticRoutine:
        """Build and return DiagnosticRoutine object.

        Returns:
            DiagnosticRoutine instance
        """
        # TODO: Add validation
        return self._obj
