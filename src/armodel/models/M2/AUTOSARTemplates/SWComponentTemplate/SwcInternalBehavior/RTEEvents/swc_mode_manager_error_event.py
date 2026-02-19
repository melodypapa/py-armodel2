"""SwcModeManagerErrorEvent AUTOSAR element.

References:
  - AUTOSAR_CP_TPS_SoftwareComponentTemplate.pdf (page 637)

JSON Source: docs/json/packages/M2_AUTOSARTemplates_SWComponentTemplate_SwcInternalBehavior_RTEEvents.classes.json"""

from __future__ import annotations
from typing import TYPE_CHECKING, Optional
import xml.etree.ElementTree as ET

from armodel.models.M2.AUTOSARTemplates.SWComponentTemplate.SwcInternalBehavior.RTEEvents.rte_event import (
    RTEEvent,
)
from armodel.models.M2.AUTOSARTemplates.GenericStructure.GeneralTemplateClasses.ArObject.ar_object import ARObject
from armodel.models.M2.AUTOSARTemplates.GenericStructure.GeneralTemplateClasses.ArObject.ar_ref import ARRef
from armodel.models.M2.AUTOSARTemplates.CommonStructure.ModeDeclaration.mode_declaration_group import (
    ModeDeclarationGroup,
)


class SwcModeManagerErrorEvent(RTEEvent):
    """AUTOSAR SwcModeManagerErrorEvent."""

    @property
    def is_abstract(self) -> bool:
        """Check if this class is abstract.

        Returns:
            False for concrete classes
        """
        return False

    mode_group_ref: Optional[ARRef]
    def __init__(self) -> None:
        """Initialize SwcModeManagerErrorEvent."""
        super().__init__()
        self.mode_group_ref: Optional[ARRef] = None

    def serialize(self) -> ET.Element:
        """Serialize SwcModeManagerErrorEvent to XML element.

        Returns:
            xml.etree.ElementTree.Element representing this object
        """
        # Get XML tag name for this class
        tag = self._get_xml_tag()
        elem = ET.Element(tag)

        # First, call parent's serialize to handle inherited attributes
        parent_elem = super(SwcModeManagerErrorEvent, self).serialize()

        # Copy all attributes from parent element
        elem.attrib.update(parent_elem.attrib)

        # Copy all children from parent element
        for child in parent_elem:
            elem.append(child)

        # Serialize mode_group_ref
        if self.mode_group_ref is not None:
            serialized = ARObject._serialize_item(self.mode_group_ref, "ModeDeclarationGroup")
            if serialized is not None:
                # Wrap with correct tag
                wrapped = ET.Element("MODE-GROUP-REF")
                if hasattr(serialized, 'attrib'):
                    wrapped.attrib.update(serialized.attrib)
                    if serialized.text:
                        wrapped.text = serialized.text
                for child in serialized:
                    wrapped.append(child)
                elem.append(wrapped)

        return elem

    @classmethod
    def deserialize(cls, element: ET.Element) -> "SwcModeManagerErrorEvent":
        """Deserialize XML element to SwcModeManagerErrorEvent object.

        Args:
            element: XML element to deserialize from

        Returns:
            Deserialized SwcModeManagerErrorEvent object
        """
        # First, call parent's deserialize to handle inherited attributes
        obj = super(SwcModeManagerErrorEvent, cls).deserialize(element)

        # Parse mode_group_ref
        child = ARObject._find_child_element(element, "MODE-GROUP-REF")
        if child is not None:
            mode_group_ref_value = ARRef.deserialize(child)
            obj.mode_group_ref = mode_group_ref_value

        return obj



class SwcModeManagerErrorEventBuilder:
    """Builder for SwcModeManagerErrorEvent."""

    def __init__(self) -> None:
        """Initialize builder."""
        self._obj: SwcModeManagerErrorEvent = SwcModeManagerErrorEvent()

    def build(self) -> SwcModeManagerErrorEvent:
        """Build and return SwcModeManagerErrorEvent object.

        Returns:
            SwcModeManagerErrorEvent instance
        """
        # TODO: Add validation
        return self._obj
