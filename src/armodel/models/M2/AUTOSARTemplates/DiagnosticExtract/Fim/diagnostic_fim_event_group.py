"""DiagnosticFimEventGroup AUTOSAR element.

References:
  - AUTOSAR_CP_TPS_DiagnosticExtractTemplate.pdf (page 217)

JSON Source: docs/json/packages/M2_AUTOSARTemplates_DiagnosticExtract_Fim.classes.json"""

from __future__ import annotations
from typing import TYPE_CHECKING, Optional
import xml.etree.ElementTree as ET

from armodel.models.M2.AUTOSARTemplates.DiagnosticExtract.CommonDiagnostics.diagnostic_common_element import (
    DiagnosticCommonElement,
)
from armodel.models.M2.AUTOSARTemplates.GenericStructure.GeneralTemplateClasses.ArObject.ar_object import ARObject
from armodel.models.M2.AUTOSARTemplates.GenericStructure.GeneralTemplateClasses.ArObject.ar_ref import ARRef
from armodel.models.M2.AUTOSARTemplates.DiagnosticExtract.Dem.DiagnosticEvent.diagnostic_event import (
    DiagnosticEvent,
)


class DiagnosticFimEventGroup(DiagnosticCommonElement):
    """AUTOSAR DiagnosticFimEventGroup."""

    @property
    def is_abstract(self) -> bool:
        """Check if this class is abstract.

        Returns:
            False for concrete classes
        """
        return False

    event_refs: list[ARRef]
    def __init__(self) -> None:
        """Initialize DiagnosticFimEventGroup."""
        super().__init__()
        self.event_refs: list[ARRef] = []

    def serialize(self) -> ET.Element:
        """Serialize DiagnosticFimEventGroup to XML element.

        Returns:
            xml.etree.ElementTree.Element representing this object
        """
        # Get XML tag name for this class
        tag = self._get_xml_tag()
        elem = ET.Element(tag)

        # First, call parent's serialize to handle inherited attributes
        parent_elem = super(DiagnosticFimEventGroup, self).serialize()

        # Copy all attributes from parent element
        elem.attrib.update(parent_elem.attrib)

        # Copy text from parent element
        if parent_elem.text:
            elem.text = parent_elem.text

        # Copy all children from parent element
        for child in parent_elem:
            elem.append(child)

        # Serialize event_refs (list to container "EVENT-REFS")
        if self.event_refs:
            wrapper = ET.Element("EVENT-REFS")
            for item in self.event_refs:
                serialized = ARObject._serialize_item(item, "DiagnosticEvent")
                if serialized is not None:
                    child_elem = ET.Element("EVENT-REF")
                    if hasattr(serialized, 'attrib'):
                        child_elem.attrib.update(serialized.attrib)
                    if serialized.text:
                        child_elem.text = serialized.text
                    for child in serialized:
                        child_elem.append(child)
                    wrapper.append(child_elem)
            if len(wrapper) > 0:
                elem.append(wrapper)

        return elem

    @classmethod
    def deserialize(cls, element: ET.Element) -> "DiagnosticFimEventGroup":
        """Deserialize XML element to DiagnosticFimEventGroup object.

        Args:
            element: XML element to deserialize from

        Returns:
            Deserialized DiagnosticFimEventGroup object
        """
        # First, call parent's deserialize to handle inherited attributes
        obj = super(DiagnosticFimEventGroup, cls).deserialize(element)

        # Parse event_refs (list from container "EVENT-REFS")
        obj.event_refs = []
        container = ARObject._find_child_element(element, "EVENT-REFS")
        if container is not None:
            for child in container:
                # Check if child is a reference element (ends with -REF or -TREF)
                child_tag = ARObject._strip_namespace(child.tag)
                if child_tag.endswith("-REF") or child_tag.endswith("-TREF"):
                    # Use ARRef.deserialize() for reference elements
                    child_value = ARRef.deserialize(child)
                else:
                    # Deserialize each child element dynamically based on its tag
                    child_value = ARObject._deserialize_by_tag(child, None)
                if child_value is not None:
                    obj.event_refs.append(child_value)

        return obj



class DiagnosticFimEventGroupBuilder:
    """Builder for DiagnosticFimEventGroup."""

    def __init__(self) -> None:
        """Initialize builder."""
        self._obj: DiagnosticFimEventGroup = DiagnosticFimEventGroup()

    def build(self) -> DiagnosticFimEventGroup:
        """Build and return DiagnosticFimEventGroup object.

        Returns:
            DiagnosticFimEventGroup instance
        """
        # TODO: Add validation
        return self._obj
