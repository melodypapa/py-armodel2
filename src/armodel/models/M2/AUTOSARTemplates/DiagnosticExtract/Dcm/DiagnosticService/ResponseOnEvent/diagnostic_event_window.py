"""DiagnosticEventWindow AUTOSAR element.

References:
  - AUTOSAR_CP_TPS_DiagnosticExtractTemplate.pdf (page 133)

JSON Source: docs/json/packages/M2_AUTOSARTemplates_DiagnosticExtract_Dcm_DiagnosticService_ResponseOnEvent.classes.json"""

from __future__ import annotations
from typing import TYPE_CHECKING, Optional
import xml.etree.ElementTree as ET

from armodel.models.M2.AUTOSARTemplates.GenericStructure.GeneralTemplateClasses.ArObject.ar_object import ARObject
from armodel.serialization import SerializationHelper


class DiagnosticEventWindow(ARObject):
    """AUTOSAR DiagnosticEventWindow."""

    @property
    def is_abstract(self) -> bool:
        """Check if this class is abstract.

        Returns:
            False for concrete classes
        """
        return False

    event_window: Optional[DiagnosticEventWindow]
    def __init__(self) -> None:
        """Initialize DiagnosticEventWindow."""
        super().__init__()
        self.event_window: Optional[DiagnosticEventWindow] = None

    def serialize(self) -> ET.Element:
        """Serialize DiagnosticEventWindow to XML element.

        Returns:
            xml.etree.ElementTree.Element representing this object
        """
        # Get XML tag name for this class
        tag = SerializationHelper.get_xml_tag(self.__class__)
        elem = ET.Element(tag)

        # First, call parent's serialize to handle inherited attributes
        parent_elem = super(DiagnosticEventWindow, self).serialize()

        # Copy all attributes from parent element
        elem.attrib.update(parent_elem.attrib)

        # Copy text from parent element
        if parent_elem.text:
            elem.text = parent_elem.text

        # Copy all children from parent element
        for child in parent_elem:
            elem.append(child)

        # Serialize event_window
        if self.event_window is not None:
            serialized = SerializationHelper.serialize_item(self.event_window, "DiagnosticEventWindow")
            if serialized is not None:
                # Wrap with correct tag
                wrapped = ET.Element("EVENT-WINDOW")
                if hasattr(serialized, 'attrib'):
                    wrapped.attrib.update(serialized.attrib)
                    if serialized.text:
                        wrapped.text = serialized.text
                for child in serialized:
                    wrapped.append(child)
                elem.append(wrapped)

        return elem

    @classmethod
    def deserialize(cls, element: ET.Element) -> "DiagnosticEventWindow":
        """Deserialize XML element to DiagnosticEventWindow object.

        Args:
            element: XML element to deserialize from

        Returns:
            Deserialized DiagnosticEventWindow object
        """
        # First, call parent's deserialize to handle inherited attributes
        obj = super(DiagnosticEventWindow, cls).deserialize(element)

        # Parse event_window
        child = SerializationHelper.find_child_element(element, "EVENT-WINDOW")
        if child is not None:
            event_window_value = SerializationHelper.deserialize_by_tag(child, "DiagnosticEventWindow")
            obj.event_window = event_window_value

        return obj



class DiagnosticEventWindowBuilder:
    """Builder for DiagnosticEventWindow."""

    def __init__(self) -> None:
        """Initialize builder."""
        self._obj: DiagnosticEventWindow = DiagnosticEventWindow()

    def build(self) -> DiagnosticEventWindow:
        """Build and return DiagnosticEventWindow object.

        Returns:
            DiagnosticEventWindow instance
        """
        # TODO: Add validation
        return self._obj
