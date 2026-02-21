"""RequestResponseDelay AUTOSAR element.

References:
  - AUTOSAR_CP_TPS_SystemTemplate.pdf (page 515)

JSON Source: docs/json/packages/M2_AUTOSARTemplates_SystemTemplate_Fibex_Fibex4Ethernet_ServiceInstances.classes.json"""

from __future__ import annotations
from typing import TYPE_CHECKING, Optional
import xml.etree.ElementTree as ET

from armodel.models.M2.AUTOSARTemplates.GenericStructure.GeneralTemplateClasses.ArObject.ar_object import ARObject
from armodel.serialization import SerializationHelper
from armodel.models.M2.AUTOSARTemplates.GenericStructure.GeneralTemplateClasses.PrimitiveTypes import (
    TimeValue,
)


class RequestResponseDelay(ARObject):
    """AUTOSAR RequestResponseDelay."""

    @property
    def is_abstract(self) -> bool:
        """Check if this class is abstract.

        Returns:
            False for concrete classes
        """
        return False

    max_value: Optional[TimeValue]
    min_value: Optional[TimeValue]
    def __init__(self) -> None:
        """Initialize RequestResponseDelay."""
        super().__init__()
        self.max_value: Optional[TimeValue] = None
        self.min_value: Optional[TimeValue] = None

    def serialize(self) -> ET.Element:
        """Serialize RequestResponseDelay to XML element.

        Returns:
            xml.etree.ElementTree.Element representing this object
        """
        # Get XML tag name for this class
        tag = SerializationHelper.get_xml_tag(self.__class__)
        elem = ET.Element(tag)

        # First, call parent's serialize to handle inherited attributes
        parent_elem = super(RequestResponseDelay, self).serialize()

        # Copy all attributes from parent element
        elem.attrib.update(parent_elem.attrib)

        # Copy text from parent element
        if parent_elem.text:
            elem.text = parent_elem.text

        # Copy all children from parent element
        for child in parent_elem:
            elem.append(child)

        # Serialize max_value
        if self.max_value is not None:
            serialized = SerializationHelper.serialize_item(self.max_value, "TimeValue")
            if serialized is not None:
                # Wrap with correct tag
                wrapped = ET.Element("MAX-VALUE")
                if hasattr(serialized, 'attrib'):
                    wrapped.attrib.update(serialized.attrib)
                    if serialized.text:
                        wrapped.text = serialized.text
                for child in serialized:
                    wrapped.append(child)
                elem.append(wrapped)

        # Serialize min_value
        if self.min_value is not None:
            serialized = SerializationHelper.serialize_item(self.min_value, "TimeValue")
            if serialized is not None:
                # Wrap with correct tag
                wrapped = ET.Element("MIN-VALUE")
                if hasattr(serialized, 'attrib'):
                    wrapped.attrib.update(serialized.attrib)
                    if serialized.text:
                        wrapped.text = serialized.text
                for child in serialized:
                    wrapped.append(child)
                elem.append(wrapped)

        return elem

    @classmethod
    def deserialize(cls, element: ET.Element) -> "RequestResponseDelay":
        """Deserialize XML element to RequestResponseDelay object.

        Args:
            element: XML element to deserialize from

        Returns:
            Deserialized RequestResponseDelay object
        """
        # First, call parent's deserialize to handle inherited attributes
        obj = super(RequestResponseDelay, cls).deserialize(element)

        # Parse max_value
        child = SerializationHelper.find_child_element(element, "MAX-VALUE")
        if child is not None:
            max_value_value = child.text
            obj.max_value = max_value_value

        # Parse min_value
        child = SerializationHelper.find_child_element(element, "MIN-VALUE")
        if child is not None:
            min_value_value = child.text
            obj.min_value = min_value_value

        return obj



class RequestResponseDelayBuilder:
    """Builder for RequestResponseDelay."""

    def __init__(self) -> None:
        """Initialize builder."""
        self._obj: RequestResponseDelay = RequestResponseDelay()

    def build(self) -> RequestResponseDelay:
        """Build and return RequestResponseDelay object.

        Returns:
            RequestResponseDelay instance
        """
        # TODO: Add validation
        return self._obj
