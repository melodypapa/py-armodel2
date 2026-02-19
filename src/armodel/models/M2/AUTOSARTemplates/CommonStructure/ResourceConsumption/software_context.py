"""SoftwareContext AUTOSAR element.

References:
  - AUTOSAR_CP_TPS_BSWModuleDescriptionTemplate.pdf (page 163)

JSON Source: docs/json/packages/M2_AUTOSARTemplates_CommonStructure_ResourceConsumption.classes.json"""

from __future__ import annotations
from typing import TYPE_CHECKING, Optional
import xml.etree.ElementTree as ET

from armodel.models.M2.AUTOSARTemplates.GenericStructure.GeneralTemplateClasses.ArObject.ar_object import ARObject
from armodel.models.M2.AUTOSARTemplates.GenericStructure.GeneralTemplateClasses.PrimitiveTypes import (
    String,
)


class SoftwareContext(ARObject):
    """AUTOSAR SoftwareContext."""

    @property
    def is_abstract(self) -> bool:
        """Check if this class is abstract.

        Returns:
            False for concrete classes
        """
        return False

    input: Optional[String]
    state: Optional[String]
    def __init__(self) -> None:
        """Initialize SoftwareContext."""
        super().__init__()
        self.input: Optional[String] = None
        self.state: Optional[String] = None
    def serialize(self) -> ET.Element:
        """Serialize SoftwareContext to XML element.

        Returns:
            xml.etree.ElementTree.Element representing this object
        """
        # Get XML tag name for this class
        tag = self._get_xml_tag()
        elem = ET.Element(tag)

        # Serialize input
        if self.input is not None:
            serialized = ARObject._serialize_item(self.input, "String")
            if serialized is not None:
                # Wrap with correct tag
                wrapped = ET.Element("INPUT")
                if hasattr(serialized, 'attrib'):
                    wrapped.attrib.update(serialized.attrib)
                    if serialized.text:
                        wrapped.text = serialized.text
                for child in serialized:
                    wrapped.append(child)
                elem.append(wrapped)

        # Serialize state
        if self.state is not None:
            serialized = ARObject._serialize_item(self.state, "String")
            if serialized is not None:
                # Wrap with correct tag
                wrapped = ET.Element("STATE")
                if hasattr(serialized, 'attrib'):
                    wrapped.attrib.update(serialized.attrib)
                    if serialized.text:
                        wrapped.text = serialized.text
                for child in serialized:
                    wrapped.append(child)
                elem.append(wrapped)

        return elem

    @classmethod
    def deserialize(cls, element: ET.Element) -> "SoftwareContext":
        """Deserialize XML element to SoftwareContext object.

        Args:
            element: XML element to deserialize from

        Returns:
            Deserialized SoftwareContext object
        """
        # Create instance and initialize with default values
        obj = cls.__new__(cls)
        obj.__init__()

        # Parse input
        child = ARObject._find_child_element(element, "INPUT")
        if child is not None:
            input_value = child.text
            obj.input = input_value

        # Parse state
        child = ARObject._find_child_element(element, "STATE")
        if child is not None:
            state_value = child.text
            obj.state = state_value

        return obj



class SoftwareContextBuilder:
    """Builder for SoftwareContext."""

    def __init__(self) -> None:
        """Initialize builder."""
        self._obj: SoftwareContext = SoftwareContext()

    def build(self) -> SoftwareContext:
        """Build and return SoftwareContext object.

        Returns:
            SoftwareContext instance
        """
        # TODO: Add validation
        return self._obj
