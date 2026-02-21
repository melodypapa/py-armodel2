"""DiagnosticStopRoutine AUTOSAR element.

References:
  - AUTOSAR_CP_TPS_DiagnosticExtractTemplate.pdf (page 125)

JSON Source: docs/json/packages/M2_AUTOSARTemplates_DiagnosticExtract_CommonDiagnostics.classes.json"""

from __future__ import annotations
from typing import TYPE_CHECKING, Optional
import xml.etree.ElementTree as ET

from armodel.models.M2.AUTOSARTemplates.DiagnosticExtract.CommonDiagnostics.diagnostic_routine_subfunction import (
    DiagnosticRoutineSubfunction,
)
from armodel.models.M2.AUTOSARTemplates.GenericStructure.GeneralTemplateClasses.ArObject.ar_object import ARObject
from armodel.serialization import SerializationHelper
from armodel.models.M2.AUTOSARTemplates.DiagnosticExtract.CommonDiagnostics.diagnostic_parameter import (
    DiagnosticParameter,
)


class DiagnosticStopRoutine(DiagnosticRoutineSubfunction):
    """AUTOSAR DiagnosticStopRoutine."""

    @property
    def is_abstract(self) -> bool:
        """Check if this class is abstract.

        Returns:
            False for concrete classes
        """
        return False

    requests: list[DiagnosticParameter]
    responses: list[DiagnosticParameter]
    def __init__(self) -> None:
        """Initialize DiagnosticStopRoutine."""
        super().__init__()
        self.requests: list[DiagnosticParameter] = []
        self.responses: list[DiagnosticParameter] = []

    def serialize(self) -> ET.Element:
        """Serialize DiagnosticStopRoutine to XML element.

        Returns:
            xml.etree.ElementTree.Element representing this object
        """
        # Get XML tag name for this class
        tag = SerializationHelper.get_xml_tag(self.__class__)
        elem = ET.Element(tag)

        # First, call parent's serialize to handle inherited attributes
        parent_elem = super(DiagnosticStopRoutine, self).serialize()

        # Copy all attributes from parent element
        elem.attrib.update(parent_elem.attrib)

        # Copy text from parent element
        if parent_elem.text:
            elem.text = parent_elem.text

        # Copy all children from parent element
        for child in parent_elem:
            elem.append(child)

        # Serialize requests (list to container "REQUESTS")
        if self.requests:
            wrapper = ET.Element("REQUESTS")
            for item in self.requests:
                serialized = SerializationHelper.serialize_item(item, "DiagnosticParameter")
                if serialized is not None:
                    wrapper.append(serialized)
            if len(wrapper) > 0:
                elem.append(wrapper)

        # Serialize responses (list to container "RESPONSES")
        if self.responses:
            wrapper = ET.Element("RESPONSES")
            for item in self.responses:
                serialized = SerializationHelper.serialize_item(item, "DiagnosticParameter")
                if serialized is not None:
                    wrapper.append(serialized)
            if len(wrapper) > 0:
                elem.append(wrapper)

        return elem

    @classmethod
    def deserialize(cls, element: ET.Element) -> "DiagnosticStopRoutine":
        """Deserialize XML element to DiagnosticStopRoutine object.

        Args:
            element: XML element to deserialize from

        Returns:
            Deserialized DiagnosticStopRoutine object
        """
        # First, call parent's deserialize to handle inherited attributes
        obj = super(DiagnosticStopRoutine, cls).deserialize(element)

        # Parse requests (list from container "REQUESTS")
        obj.requests = []
        container = SerializationHelper.find_child_element(element, "REQUESTS")
        if container is not None:
            for child in container:
                # Deserialize each child element dynamically based on its tag
                child_value = SerializationHelper.deserialize_by_tag(child, None)
                if child_value is not None:
                    obj.requests.append(child_value)

        # Parse responses (list from container "RESPONSES")
        obj.responses = []
        container = SerializationHelper.find_child_element(element, "RESPONSES")
        if container is not None:
            for child in container:
                # Deserialize each child element dynamically based on its tag
                child_value = SerializationHelper.deserialize_by_tag(child, None)
                if child_value is not None:
                    obj.responses.append(child_value)

        return obj



class DiagnosticStopRoutineBuilder:
    """Builder for DiagnosticStopRoutine."""

    def __init__(self) -> None:
        """Initialize builder."""
        self._obj: DiagnosticStopRoutine = DiagnosticStopRoutine()

    def build(self) -> DiagnosticStopRoutine:
        """Build and return DiagnosticStopRoutine object.

        Returns:
            DiagnosticStopRoutine instance
        """
        # TODO: Add validation
        return self._obj
