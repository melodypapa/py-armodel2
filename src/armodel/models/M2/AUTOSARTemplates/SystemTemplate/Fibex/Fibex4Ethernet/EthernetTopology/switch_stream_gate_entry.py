"""SwitchStreamGateEntry AUTOSAR element.

References:
  - AUTOSAR_CP_TPS_SystemTemplate.pdf (page 142)

JSON Source: docs/json/packages/M2_AUTOSARTemplates_SystemTemplate_Fibex_Fibex4Ethernet_EthernetTopology.classes.json"""

from __future__ import annotations
from typing import TYPE_CHECKING, Optional
import xml.etree.ElementTree as ET

from armodel.models.M2.AUTOSARTemplates.GenericStructure.GeneralTemplateClasses.Identifiable.identifiable import (
    Identifiable,
)
from armodel.models.M2.AUTOSARTemplates.GenericStructure.GeneralTemplateClasses.ArObject.ar_object import ARObject
from armodel.serialization import SerializationHelper
from armodel.models.M2.AUTOSARTemplates.GenericStructure.GeneralTemplateClasses.PrimitiveTypes import (
    PositiveInteger,
)


class SwitchStreamGateEntry(Identifiable):
    """AUTOSAR SwitchStreamGateEntry."""

    @property
    def is_abstract(self) -> bool:
        """Check if this class is abstract.

        Returns:
            False for concrete classes
        """
        return False

    internal_priority: Optional[PositiveInteger]
    def __init__(self) -> None:
        """Initialize SwitchStreamGateEntry."""
        super().__init__()
        self.internal_priority: Optional[PositiveInteger] = None

    def serialize(self) -> ET.Element:
        """Serialize SwitchStreamGateEntry to XML element.

        Returns:
            xml.etree.ElementTree.Element representing this object
        """
        # Get XML tag name for this class
        tag = SerializationHelper.get_xml_tag(self.__class__)
        elem = ET.Element(tag)

        # First, call parent's serialize to handle inherited attributes
        parent_elem = super(SwitchStreamGateEntry, self).serialize()

        # Copy all attributes from parent element
        elem.attrib.update(parent_elem.attrib)

        # Copy text from parent element
        if parent_elem.text:
            elem.text = parent_elem.text

        # Copy all children from parent element
        for child in parent_elem:
            elem.append(child)

        # Serialize internal_priority
        if self.internal_priority is not None:
            serialized = SerializationHelper.serialize_item(self.internal_priority, "PositiveInteger")
            if serialized is not None:
                # Wrap with correct tag
                wrapped = ET.Element("INTERNAL-PRIORITY")
                if hasattr(serialized, 'attrib'):
                    wrapped.attrib.update(serialized.attrib)
                    if serialized.text:
                        wrapped.text = serialized.text
                for child in serialized:
                    wrapped.append(child)
                elem.append(wrapped)

        return elem

    @classmethod
    def deserialize(cls, element: ET.Element) -> "SwitchStreamGateEntry":
        """Deserialize XML element to SwitchStreamGateEntry object.

        Args:
            element: XML element to deserialize from

        Returns:
            Deserialized SwitchStreamGateEntry object
        """
        # First, call parent's deserialize to handle inherited attributes
        obj = super(SwitchStreamGateEntry, cls).deserialize(element)

        # Parse internal_priority
        child = SerializationHelper.find_child_element(element, "INTERNAL-PRIORITY")
        if child is not None:
            internal_priority_value = child.text
            obj.internal_priority = internal_priority_value

        return obj



class SwitchStreamGateEntryBuilder:
    """Builder for SwitchStreamGateEntry."""

    def __init__(self) -> None:
        """Initialize builder."""
        self._obj: SwitchStreamGateEntry = SwitchStreamGateEntry()

    def build(self) -> SwitchStreamGateEntry:
        """Build and return SwitchStreamGateEntry object.

        Returns:
            SwitchStreamGateEntry instance
        """
        # TODO: Add validation
        return self._obj
