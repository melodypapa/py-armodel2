"""BswModeSwitchAckRequest AUTOSAR element.

References:
  - AUTOSAR_CP_TPS_BSWModuleDescriptionTemplate.pdf (page 103)

JSON Source: docs/json/packages/M2_AUTOSARTemplates_BswModuleTemplate_BswBehavior.classes.json"""

from __future__ import annotations
from typing import TYPE_CHECKING, Optional
import xml.etree.ElementTree as ET

from armodel.models.M2.AUTOSARTemplates.GenericStructure.GeneralTemplateClasses.ArObject.ar_object import ARObject
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
        tag = self._get_xml_tag()
        elem = ET.Element(tag)

        # Serialize timeout
        if self.timeout is not None:
            serialized = ARObject._serialize_item(self.timeout, "TimeValue")
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
        # Create instance and initialize with default values
        obj = cls.__new__(cls)
        obj.__init__()

        # Parse timeout
        child = ARObject._find_child_element(element, "TIMEOUT")
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
