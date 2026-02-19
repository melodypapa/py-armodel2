"""SwitchAsynchronousTrafficShaperGroupEntry AUTOSAR element.

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
from armodel.models.M2.AUTOSARTemplates.GenericStructure.GeneralTemplateClasses.PrimitiveTypes import (
    PositiveInteger,
)


class SwitchAsynchronousTrafficShaperGroupEntry(Identifiable):
    """AUTOSAR SwitchAsynchronousTrafficShaperGroupEntry."""

    @property
    def is_abstract(self) -> bool:
        """Check if this class is abstract.

        Returns:
            False for concrete classes
        """
        return False

    maximum: Optional[PositiveInteger]
    def __init__(self) -> None:
        """Initialize SwitchAsynchronousTrafficShaperGroupEntry."""
        super().__init__()
        self.maximum: Optional[PositiveInteger] = None
    def serialize(self) -> ET.Element:
        """Serialize SwitchAsynchronousTrafficShaperGroupEntry to XML element.

        Returns:
            xml.etree.ElementTree.Element representing this object
        """
        # Get XML tag name for this class
        tag = ARObject._get_xml_tag(self)
        elem = ET.Element(tag)

        # First, call parent's serialize to handle inherited attributes
        parent_elem = super(SwitchAsynchronousTrafficShaperGroupEntry, self).serialize()

        # Copy all attributes from parent element
        elem.attrib.update(parent_elem.attrib)

        # Copy all children from parent element
        for child in parent_elem:
            elem.append(child)

        # Serialize maximum
        if self.maximum is not None:
            serialized = ARObject._serialize_item(self.maximum, "PositiveInteger")
            if serialized is not None:
                # Wrap with correct tag
                wrapped = ET.Element("MAXIMUM")
                if hasattr(serialized, 'attrib'):
                    wrapped.attrib.update(serialized.attrib)
                    if serialized.text:
                        wrapped.text = serialized.text
                for child in serialized:
                    wrapped.append(child)
                elem.append(wrapped)

        return elem

    @classmethod
    def deserialize(cls, element: ET.Element) -> "SwitchAsynchronousTrafficShaperGroupEntry":
        """Deserialize XML element to SwitchAsynchronousTrafficShaperGroupEntry object.

        Args:
            element: XML element to deserialize from

        Returns:
            Deserialized SwitchAsynchronousTrafficShaperGroupEntry object
        """
        # First, call parent's deserialize to handle inherited attributes
        obj = super(SwitchAsynchronousTrafficShaperGroupEntry, cls).deserialize(element)

        # Parse maximum
        child = ARObject._find_child_element(element, "MAXIMUM")
        if child is not None:
            maximum_value = child.text
            obj.maximum = maximum_value

        return obj



class SwitchAsynchronousTrafficShaperGroupEntryBuilder:
    """Builder for SwitchAsynchronousTrafficShaperGroupEntry."""

    def __init__(self) -> None:
        """Initialize builder."""
        self._obj: SwitchAsynchronousTrafficShaperGroupEntry = SwitchAsynchronousTrafficShaperGroupEntry()

    def build(self) -> SwitchAsynchronousTrafficShaperGroupEntry:
        """Build and return SwitchAsynchronousTrafficShaperGroupEntry object.

        Returns:
            SwitchAsynchronousTrafficShaperGroupEntry instance
        """
        # TODO: Add validation
        return self._obj
