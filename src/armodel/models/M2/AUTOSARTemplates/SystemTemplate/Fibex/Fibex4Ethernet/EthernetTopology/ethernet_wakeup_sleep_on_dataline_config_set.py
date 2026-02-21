"""EthernetWakeupSleepOnDatalineConfigSet AUTOSAR element.

References:
  - AUTOSAR_CP_TPS_SystemTemplate.pdf (page 159)

JSON Source: docs/json/packages/M2_AUTOSARTemplates_SystemTemplate_Fibex_Fibex4Ethernet_EthernetTopology.classes.json"""

from __future__ import annotations
from typing import TYPE_CHECKING, Optional, Any
import xml.etree.ElementTree as ET

from armodel.models.M2.AUTOSARTemplates.SystemTemplate.Fibex.FibexCore.fibex_element import (
    FibexElement,
)
from armodel.models.M2.AUTOSARTemplates.GenericStructure.GeneralTemplateClasses.ArObject.ar_object import ARObject
from armodel.serialization import SerializationHelper


class EthernetWakeupSleepOnDatalineConfigSet(FibexElement):
    """AUTOSAR EthernetWakeupSleepOnDatalineConfigSet."""

    @property
    def is_abstract(self) -> bool:
        """Check if this class is abstract.

        Returns:
            False for concrete classes
        """
        return False

    ethernets: list[Any]
    def __init__(self) -> None:
        """Initialize EthernetWakeupSleepOnDatalineConfigSet."""
        super().__init__()
        self.ethernets: list[Any] = []

    def serialize(self) -> ET.Element:
        """Serialize EthernetWakeupSleepOnDatalineConfigSet to XML element.

        Returns:
            xml.etree.ElementTree.Element representing this object
        """
        # Get XML tag name for this class
        tag = SerializationHelper.get_xml_tag(self.__class__)
        elem = ET.Element(tag)

        # First, call parent's serialize to handle inherited attributes
        parent_elem = super(EthernetWakeupSleepOnDatalineConfigSet, self).serialize()

        # Copy all attributes from parent element
        elem.attrib.update(parent_elem.attrib)

        # Copy text from parent element
        if parent_elem.text:
            elem.text = parent_elem.text

        # Copy all children from parent element
        for child in parent_elem:
            elem.append(child)

        # Serialize ethernets (list to container "ETHERNETS")
        if self.ethernets:
            wrapper = ET.Element("ETHERNETS")
            for item in self.ethernets:
                serialized = SerializationHelper.serialize_item(item, "Any")
                if serialized is not None:
                    wrapper.append(serialized)
            if len(wrapper) > 0:
                elem.append(wrapper)

        return elem

    @classmethod
    def deserialize(cls, element: ET.Element) -> "EthernetWakeupSleepOnDatalineConfigSet":
        """Deserialize XML element to EthernetWakeupSleepOnDatalineConfigSet object.

        Args:
            element: XML element to deserialize from

        Returns:
            Deserialized EthernetWakeupSleepOnDatalineConfigSet object
        """
        # First, call parent's deserialize to handle inherited attributes
        obj = super(EthernetWakeupSleepOnDatalineConfigSet, cls).deserialize(element)

        # Parse ethernets (list from container "ETHERNETS")
        obj.ethernets = []
        container = SerializationHelper.find_child_element(element, "ETHERNETS")
        if container is not None:
            for child in container:
                # Deserialize each child element dynamically based on its tag
                child_value = SerializationHelper.deserialize_by_tag(child, None)
                if child_value is not None:
                    obj.ethernets.append(child_value)

        return obj



class EthernetWakeupSleepOnDatalineConfigSetBuilder:
    """Builder for EthernetWakeupSleepOnDatalineConfigSet."""

    def __init__(self) -> None:
        """Initialize builder."""
        self._obj: EthernetWakeupSleepOnDatalineConfigSet = EthernetWakeupSleepOnDatalineConfigSet()

    def build(self) -> EthernetWakeupSleepOnDatalineConfigSet:
        """Build and return EthernetWakeupSleepOnDatalineConfigSet object.

        Returns:
            EthernetWakeupSleepOnDatalineConfigSet instance
        """
        # TODO: Add validation
        return self._obj
