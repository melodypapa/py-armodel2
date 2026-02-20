"""DdsDeadline AUTOSAR element.

References:
  - AUTOSAR_CP_TPS_SystemTemplate.pdf (page 532)

JSON Source: docs/json/packages/M2_AUTOSARTemplates_SystemTemplate_Fibex_Fibex4Ethernet_Dds.classes.json"""

from __future__ import annotations
from typing import TYPE_CHECKING, Optional
import xml.etree.ElementTree as ET

from armodel.models.M2.AUTOSARTemplates.GenericStructure.GeneralTemplateClasses.ArObject.ar_object import ARObject
from armodel.models.M2.AUTOSARTemplates.GenericStructure.GeneralTemplateClasses.PrimitiveTypes import (
    Float,
)


class DdsDeadline(ARObject):
    """AUTOSAR DdsDeadline."""

    @property
    def is_abstract(self) -> bool:
        """Check if this class is abstract.

        Returns:
            False for concrete classes
        """
        return False

    deadline_period: Optional[Float]
    def __init__(self) -> None:
        """Initialize DdsDeadline."""
        super().__init__()
        self.deadline_period: Optional[Float] = None

    def serialize(self) -> ET.Element:
        """Serialize DdsDeadline to XML element.

        Returns:
            xml.etree.ElementTree.Element representing this object
        """
        # Get XML tag name for this class
        tag = self._get_xml_tag()
        elem = ET.Element(tag)

        # Serialize deadline_period
        if self.deadline_period is not None:
            serialized = ARObject._serialize_item(self.deadline_period, "Float")
            if serialized is not None:
                # Wrap with correct tag
                wrapped = ET.Element("DEADLINE-PERIOD")
                if hasattr(serialized, 'attrib'):
                    wrapped.attrib.update(serialized.attrib)
                    if serialized.text:
                        wrapped.text = serialized.text
                for child in serialized:
                    wrapped.append(child)
                elem.append(wrapped)

        return elem

    @classmethod
    def deserialize(cls, element: ET.Element) -> "DdsDeadline":
        """Deserialize XML element to DdsDeadline object.

        Args:
            element: XML element to deserialize from

        Returns:
            Deserialized DdsDeadline object
        """
        # Create instance and initialize with default values
        obj = cls.__new__(cls)
        obj.__init__()

        # Parse deadline_period
        child = ARObject._find_child_element(element, "DEADLINE-PERIOD")
        if child is not None:
            deadline_period_value = child.text
            obj.deadline_period = deadline_period_value

        return obj



class DdsDeadlineBuilder:
    """Builder for DdsDeadline."""

    def __init__(self) -> None:
        """Initialize builder."""
        self._obj: DdsDeadline = DdsDeadline()

    def build(self) -> DdsDeadline:
        """Build and return DdsDeadline object.

        Returns:
            DdsDeadline instance
        """
        # TODO: Add validation
        return self._obj
