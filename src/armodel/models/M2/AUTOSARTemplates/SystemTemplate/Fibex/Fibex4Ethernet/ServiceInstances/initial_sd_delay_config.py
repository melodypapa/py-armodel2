"""InitialSdDelayConfig AUTOSAR element.

References:
  - AUTOSAR_CP_TPS_SystemTemplate.pdf (page 514)

JSON Source: docs/json/packages/M2_AUTOSARTemplates_SystemTemplate_Fibex_Fibex4Ethernet_ServiceInstances.classes.json"""

from __future__ import annotations
from typing import TYPE_CHECKING, Optional
import xml.etree.ElementTree as ET

from armodel.models.M2.AUTOSARTemplates.GenericStructure.GeneralTemplateClasses.ArObject.ar_object import ARObject
from armodel.serialization import SerializationHelper
from armodel.models.M2.AUTOSARTemplates.GenericStructure.GeneralTemplateClasses.PrimitiveTypes import (
    PositiveInteger,
    TimeValue,
)


class InitialSdDelayConfig(ARObject):
    """AUTOSAR InitialSdDelayConfig."""

    @property
    def is_abstract(self) -> bool:
        """Check if this class is abstract.

        Returns:
            False for concrete classes
        """
        return False

    initial_delay_max: Optional[TimeValue]
    initial_delay_min: Optional[TimeValue]
    initial: Optional[PositiveInteger]
    def __init__(self) -> None:
        """Initialize InitialSdDelayConfig."""
        super().__init__()
        self.initial_delay_max: Optional[TimeValue] = None
        self.initial_delay_min: Optional[TimeValue] = None
        self.initial: Optional[PositiveInteger] = None

    def serialize(self) -> ET.Element:
        """Serialize InitialSdDelayConfig to XML element.

        Returns:
            xml.etree.ElementTree.Element representing this object
        """
        # Get XML tag name for this class
        tag = SerializationHelper.get_xml_tag(self.__class__)
        elem = ET.Element(tag)

        # First, call parent's serialize to handle inherited attributes
        parent_elem = super(InitialSdDelayConfig, self).serialize()

        # Copy all attributes from parent element
        elem.attrib.update(parent_elem.attrib)

        # Copy text from parent element
        if parent_elem.text:
            elem.text = parent_elem.text

        # Copy all children from parent element
        for child in parent_elem:
            elem.append(child)

        # Serialize initial_delay_max
        if self.initial_delay_max is not None:
            serialized = SerializationHelper.serialize_item(self.initial_delay_max, "TimeValue")
            if serialized is not None:
                # Wrap with correct tag
                wrapped = ET.Element("INITIAL-DELAY-MAX")
                if hasattr(serialized, 'attrib'):
                    wrapped.attrib.update(serialized.attrib)
                    if serialized.text:
                        wrapped.text = serialized.text
                for child in serialized:
                    wrapped.append(child)
                elem.append(wrapped)

        # Serialize initial_delay_min
        if self.initial_delay_min is not None:
            serialized = SerializationHelper.serialize_item(self.initial_delay_min, "TimeValue")
            if serialized is not None:
                # Wrap with correct tag
                wrapped = ET.Element("INITIAL-DELAY-MIN")
                if hasattr(serialized, 'attrib'):
                    wrapped.attrib.update(serialized.attrib)
                    if serialized.text:
                        wrapped.text = serialized.text
                for child in serialized:
                    wrapped.append(child)
                elem.append(wrapped)

        # Serialize initial
        if self.initial is not None:
            serialized = SerializationHelper.serialize_item(self.initial, "PositiveInteger")
            if serialized is not None:
                # Wrap with correct tag
                wrapped = ET.Element("INITIAL")
                if hasattr(serialized, 'attrib'):
                    wrapped.attrib.update(serialized.attrib)
                    if serialized.text:
                        wrapped.text = serialized.text
                for child in serialized:
                    wrapped.append(child)
                elem.append(wrapped)

        return elem

    @classmethod
    def deserialize(cls, element: ET.Element) -> "InitialSdDelayConfig":
        """Deserialize XML element to InitialSdDelayConfig object.

        Args:
            element: XML element to deserialize from

        Returns:
            Deserialized InitialSdDelayConfig object
        """
        # First, call parent's deserialize to handle inherited attributes
        obj = super(InitialSdDelayConfig, cls).deserialize(element)

        # Parse initial_delay_max
        child = SerializationHelper.find_child_element(element, "INITIAL-DELAY-MAX")
        if child is not None:
            initial_delay_max_value = child.text
            obj.initial_delay_max = initial_delay_max_value

        # Parse initial_delay_min
        child = SerializationHelper.find_child_element(element, "INITIAL-DELAY-MIN")
        if child is not None:
            initial_delay_min_value = child.text
            obj.initial_delay_min = initial_delay_min_value

        # Parse initial
        child = SerializationHelper.find_child_element(element, "INITIAL")
        if child is not None:
            initial_value = child.text
            obj.initial = initial_value

        return obj



class InitialSdDelayConfigBuilder:
    """Builder for InitialSdDelayConfig."""

    def __init__(self) -> None:
        """Initialize builder."""
        self._obj: InitialSdDelayConfig = InitialSdDelayConfig()

    def build(self) -> InitialSdDelayConfig:
        """Build and return InitialSdDelayConfig object.

        Returns:
            InitialSdDelayConfig instance
        """
        # TODO: Add validation
        return self._obj
