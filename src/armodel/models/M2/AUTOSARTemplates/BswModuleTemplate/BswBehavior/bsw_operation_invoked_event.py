"""BswOperationInvokedEvent AUTOSAR element.

References:
  - AUTOSAR_CP_TPS_BSWModuleDescriptionTemplate.pdf (page 97)

JSON Source: docs/json/packages/M2_AUTOSARTemplates_BswModuleTemplate_BswBehavior.classes.json"""

from __future__ import annotations
from typing import TYPE_CHECKING, Optional
import xml.etree.ElementTree as ET

from armodel.models.M2.AUTOSARTemplates.BswModuleTemplate.BswBehavior.bsw_event import (
    BswEvent,
)
from armodel.models.M2.AUTOSARTemplates.GenericStructure.GeneralTemplateClasses.ArObject.ar_object import ARObject
from armodel.models.M2.AUTOSARTemplates.BswModuleTemplate.BswInterfaces.bsw_module_client_server_entry import (
    BswModuleClientServerEntry,
)


class BswOperationInvokedEvent(BswEvent):
    """AUTOSAR BswOperationInvokedEvent."""

    @property
    def is_abstract(self) -> bool:
        """Check if this class is abstract.

        Returns:
            False for concrete classes
        """
        return False

    entry: Optional[BswModuleClientServerEntry]
    def __init__(self) -> None:
        """Initialize BswOperationInvokedEvent."""
        super().__init__()
        self.entry: Optional[BswModuleClientServerEntry] = None
    def serialize(self) -> ET.Element:
        """Serialize BswOperationInvokedEvent to XML element.

        Returns:
            xml.etree.ElementTree.Element representing this object
        """
        # Get XML tag name for this class
        tag = ARObject._get_xml_tag(self)
        elem = ET.Element(tag)

        # First, call parent's serialize to handle inherited attributes
        parent_elem = super(BswOperationInvokedEvent, self).serialize()

        # Copy all attributes from parent element
        elem.attrib.update(parent_elem.attrib)

        # Copy all children from parent element
        for child in parent_elem:
            elem.append(child)

        # Serialize entry
        if self.entry is not None:
            serialized = ARObject._serialize_item(self.entry, "BswModuleClientServerEntry")
            if serialized is not None:
                # Wrap with correct tag
                wrapped = ET.Element("ENTRY")
                if hasattr(serialized, 'attrib'):
                    wrapped.attrib.update(serialized.attrib)
                    if serialized.text:
                        wrapped.text = serialized.text
                for child in serialized:
                    wrapped.append(child)
                elem.append(wrapped)

        return elem

    @classmethod
    def deserialize(cls, element: ET.Element) -> "BswOperationInvokedEvent":
        """Deserialize XML element to BswOperationInvokedEvent object.

        Args:
            element: XML element to deserialize from

        Returns:
            Deserialized BswOperationInvokedEvent object
        """
        # First, call parent's deserialize to handle inherited attributes
        obj = super(BswOperationInvokedEvent, cls).deserialize(element)

        # Parse entry
        child = ARObject._find_child_element(element, "ENTRY")
        if child is not None:
            entry_value = ARObject._deserialize_by_tag(child, "BswModuleClientServerEntry")
            obj.entry = entry_value

        return obj



class BswOperationInvokedEventBuilder:
    """Builder for BswOperationInvokedEvent."""

    def __init__(self) -> None:
        """Initialize builder."""
        self._obj: BswOperationInvokedEvent = BswOperationInvokedEvent()

    def build(self) -> BswOperationInvokedEvent:
        """Build and return BswOperationInvokedEvent object.

        Returns:
            BswOperationInvokedEvent instance
        """
        # TODO: Add validation
        return self._obj
