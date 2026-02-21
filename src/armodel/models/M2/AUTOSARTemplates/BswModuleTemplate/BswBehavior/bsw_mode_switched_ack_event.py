"""BswModeSwitchedAckEvent AUTOSAR element.

References:
  - AUTOSAR_CP_TPS_BSWModuleDescriptionTemplate.pdf (page 95)

JSON Source: docs/json/packages/M2_AUTOSARTemplates_BswModuleTemplate_BswBehavior.classes.json"""

from __future__ import annotations
from typing import TYPE_CHECKING, Optional
import xml.etree.ElementTree as ET

from armodel.models.M2.AUTOSARTemplates.BswModuleTemplate.BswBehavior.bsw_schedule_event import (
    BswScheduleEvent,
)
from armodel.models.M2.AUTOSARTemplates.GenericStructure.GeneralTemplateClasses.ArObject.ar_object import ARObject
from armodel.serialization import SerializationHelper
from armodel.models.M2.AUTOSARTemplates.GenericStructure.GeneralTemplateClasses.ArObject.ar_ref import ARRef
from armodel.models.M2.AUTOSARTemplates.CommonStructure.ModeDeclaration.mode_declaration_group import (
    ModeDeclarationGroup,
)


class BswModeSwitchedAckEvent(BswScheduleEvent):
    """AUTOSAR BswModeSwitchedAckEvent."""

    @property
    def is_abstract(self) -> bool:
        """Check if this class is abstract.

        Returns:
            False for concrete classes
        """
        return False

    mode_group_ref: Optional[ARRef]
    def __init__(self) -> None:
        """Initialize BswModeSwitchedAckEvent."""
        super().__init__()
        self.mode_group_ref: Optional[ARRef] = None

    def serialize(self) -> ET.Element:
        """Serialize BswModeSwitchedAckEvent to XML element.

        Returns:
            xml.etree.ElementTree.Element representing this object
        """
        # Get XML tag name for this class
        tag = SerializationHelper.get_xml_tag(self.__class__)
        elem = ET.Element(tag)

        # First, call parent's serialize to handle inherited attributes
        parent_elem = super(BswModeSwitchedAckEvent, self).serialize()

        # Copy all attributes from parent element
        elem.attrib.update(parent_elem.attrib)

        # Copy text from parent element
        if parent_elem.text:
            elem.text = parent_elem.text

        # Copy all children from parent element
        for child in parent_elem:
            elem.append(child)

        # Serialize mode_group_ref
        if self.mode_group_ref is not None:
            serialized = SerializationHelper.serialize_item(self.mode_group_ref, "ModeDeclarationGroup")
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
    def deserialize(cls, element: ET.Element) -> "BswModeSwitchedAckEvent":
        """Deserialize XML element to BswModeSwitchedAckEvent object.

        Args:
            element: XML element to deserialize from

        Returns:
            Deserialized BswModeSwitchedAckEvent object
        """
        # First, call parent's deserialize to handle inherited attributes
        obj = super(BswModeSwitchedAckEvent, cls).deserialize(element)

        # Parse mode_group_ref
        child = SerializationHelper.find_child_element(element, "MODE-GROUP-REF")
        if child is not None:
            mode_group_ref_value = ARRef.deserialize(child)
            obj.mode_group_ref = mode_group_ref_value

        return obj



class BswModeSwitchedAckEventBuilder:
    """Builder for BswModeSwitchedAckEvent."""

    def __init__(self) -> None:
        """Initialize builder."""
        self._obj: BswModeSwitchedAckEvent = BswModeSwitchedAckEvent()

    def build(self) -> BswModeSwitchedAckEvent:
        """Build and return BswModeSwitchedAckEvent object.

        Returns:
            BswModeSwitchedAckEvent instance
        """
        # TODO: Add validation
        return self._obj
