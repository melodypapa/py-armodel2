"""DiagnosticResponseOnEvent AUTOSAR element.

References:
  - AUTOSAR_CP_TPS_DiagnosticExtractTemplate.pdf (page 132)

JSON Source: docs/json/packages/M2_AUTOSARTemplates_DiagnosticExtract_Dcm_DiagnosticService_ResponseOnEvent.classes.json"""

from __future__ import annotations
from typing import TYPE_CHECKING, Optional, Any
import xml.etree.ElementTree as ET

from armodel.models.M2.AUTOSARTemplates.DiagnosticExtract.Dcm.DiagnosticService.CommonService.diagnostic_service_instance import (
    DiagnosticServiceInstance,
)
from armodel.models.M2.AUTOSARTemplates.GenericStructure.GeneralTemplateClasses.ArObject.ar_object import ARObject
from armodel.models.M2.AUTOSARTemplates.GenericStructure.GeneralTemplateClasses.ArObject.ar_ref import ARRef
from armodel.models.M2.AUTOSARTemplates.DiagnosticExtract.Dcm.DiagnosticService.ResponseOnEvent.diagnostic_event_window import (
    DiagnosticEventWindow,
)


class DiagnosticResponseOnEvent(DiagnosticServiceInstance):
    """AUTOSAR DiagnosticResponseOnEvent."""

    @property
    def is_abstract(self) -> bool:
        """Check if this class is abstract.

        Returns:
            False for concrete classes
        """
        return False

    event_windows: list[DiagnosticEventWindow]
    response_on_ref: Optional[Any]
    def __init__(self) -> None:
        """Initialize DiagnosticResponseOnEvent."""
        super().__init__()
        self.event_windows: list[DiagnosticEventWindow] = []
        self.response_on_ref: Optional[Any] = None

    def serialize(self) -> ET.Element:
        """Serialize DiagnosticResponseOnEvent to XML element.

        Returns:
            xml.etree.ElementTree.Element representing this object
        """
        # Get XML tag name for this class
        tag = self._get_xml_tag()
        elem = ET.Element(tag)

        # First, call parent's serialize to handle inherited attributes
        parent_elem = super(DiagnosticResponseOnEvent, self).serialize()

        # Copy all attributes from parent element
        elem.attrib.update(parent_elem.attrib)

        # Copy all children from parent element
        for child in parent_elem:
            elem.append(child)

        # Serialize event_windows (list to container "EVENT-WINDOWS")
        if self.event_windows:
            wrapper = ET.Element("EVENT-WINDOWS")
            for item in self.event_windows:
                serialized = ARObject._serialize_item(item, "DiagnosticEventWindow")
                if serialized is not None:
                    wrapper.append(serialized)
            if len(wrapper) > 0:
                elem.append(wrapper)

        # Serialize response_on_ref
        if self.response_on_ref is not None:
            serialized = ARObject._serialize_item(self.response_on_ref, "Any")
            if serialized is not None:
                # Wrap with correct tag
                wrapped = ET.Element("RESPONSE-ON-REF")
                if hasattr(serialized, 'attrib'):
                    wrapped.attrib.update(serialized.attrib)
                    if serialized.text:
                        wrapped.text = serialized.text
                for child in serialized:
                    wrapped.append(child)
                elem.append(wrapped)

        return elem

    @classmethod
    def deserialize(cls, element: ET.Element) -> "DiagnosticResponseOnEvent":
        """Deserialize XML element to DiagnosticResponseOnEvent object.

        Args:
            element: XML element to deserialize from

        Returns:
            Deserialized DiagnosticResponseOnEvent object
        """
        # First, call parent's deserialize to handle inherited attributes
        obj = super(DiagnosticResponseOnEvent, cls).deserialize(element)

        # Parse event_windows (list from container "EVENT-WINDOWS")
        obj.event_windows = []
        container = ARObject._find_child_element(element, "EVENT-WINDOWS")
        if container is not None:
            for child in container:
                # Deserialize each child element dynamically based on its tag
                child_value = ARObject._deserialize_by_tag(child, None)
                if child_value is not None:
                    obj.event_windows.append(child_value)

        # Parse response_on_ref
        child = ARObject._find_child_element(element, "RESPONSE-ON-REF")
        if child is not None:
            response_on_ref_value = ARRef.deserialize(child)
            obj.response_on_ref = response_on_ref_value

        return obj



class DiagnosticResponseOnEventBuilder:
    """Builder for DiagnosticResponseOnEvent."""

    def __init__(self) -> None:
        """Initialize builder."""
        self._obj: DiagnosticResponseOnEvent = DiagnosticResponseOnEvent()

    def build(self) -> DiagnosticResponseOnEvent:
        """Build and return DiagnosticResponseOnEvent object.

        Returns:
            DiagnosticResponseOnEvent instance
        """
        # TODO: Add validation
        return self._obj
