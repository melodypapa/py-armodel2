"""BswModeSwitchAckRequest AUTOSAR element.

References:
  - AUTOSAR_CP_TPS_BSWModuleDescriptionTemplate.pdf (page 103)

JSON Source: docs/json/packages/M2_AUTOSARTemplates_BswModuleTemplate_BswBehavior.classes.json"""

from __future__ import annotations
from typing import TYPE_CHECKING, Optional
import xml.etree.ElementTree as ET

from armodel.models.M2.AUTOSARTemplates.GenericStructure.GeneralTemplateClasses.ArObject.ar_object import ARObject
from armodel.serialization import SerializationHelper
from armodel.models.M2.AUTOSARTemplates.GenericStructure.GeneralTemplateClasses.PrimitiveTypes import (
    TimeValue,
)


class BswModeSwitchAckRequest(ARObject):
    """AUTOSAR BswModeSwitchAckRequest."""

    @property
    def is_abstract(self) -> bool:
        """Check if this class is abstract.

        Returns:
            False for concrete classes
        """
        return False

    timeout: Optional[TimeValue]
    def __init__(self) -> None:
        """Initialize BswModeSwitchAckRequest."""
        super().__init__()
        self.timeout: Optional[TimeValue] = None

    def serialize(self) -> ET.Element:
        """Serialize BswModeSwitchAckRequest to XML element.

        Returns:
            xml.etree.ElementTree.Element representing this object
        """
        # Get XML tag name for this class
        tag = SerializationHelper.get_xml_tag(self.__class__)
        elem = ET.Element(tag)

        # First, call parent's serialize to handle inherited attributes
        parent_elem = super(BswModeSwitchAckRequest, self).serialize()

        # Copy all attributes from parent element
        elem.attrib.update(parent_elem.attrib)

        # Copy text from parent element
        if parent_elem.text:
            elem.text = parent_elem.text

        # Copy all children from parent element
        for child in parent_elem:
            elem.append(child)

        # Serialize timeout
        if self.timeout is not None:
            serialized = SerializationHelper.serialize_item(self.timeout, "TimeValue")
            if serialized is not None:
                # Wrap with correct tag
                wrapped = ET.Element("TIMEOUT")
                if hasattr(serialized, 'attrib'):
                    wrapped.attrib.update(serialized.attrib)
                    if serialized.text:
                        wrapped.text = serialized.text
                for child in serialized:
                    wrapped.append(child)
                elem.append(wrapped)

        return elem

    @classmethod
    def deserialize(cls, element: ET.Element) -> "BswModeSwitchAckRequest":
        """Deserialize XML element to BswModeSwitchAckRequest object.

        Args:
            element: XML element to deserialize from

        Returns:
            Deserialized BswModeSwitchAckRequest object
        """
        # First, call parent's deserialize to handle inherited attributes
        obj = super(BswModeSwitchAckRequest, cls).deserialize(element)

        # Parse timeout
        child = SerializationHelper.find_child_element(element, "TIMEOUT")
        if child is not None:
            timeout_value = child.text
            obj.timeout = timeout_value

        return obj



class BswModeSwitchAckRequestBuilder:
    """Builder for BswModeSwitchAckRequest."""

    def __init__(self) -> None:
        """Initialize builder."""
        self._obj: BswModeSwitchAckRequest = BswModeSwitchAckRequest()

    def build(self) -> BswModeSwitchAckRequest:
        """Build and return BswModeSwitchAckRequest object.

        Returns:
            BswModeSwitchAckRequest instance
        """
        # TODO: Add validation
        return self._obj
