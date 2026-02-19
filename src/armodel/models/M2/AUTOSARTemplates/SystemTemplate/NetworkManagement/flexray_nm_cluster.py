"""FlexrayNmCluster AUTOSAR element.

References:
  - AUTOSAR_CP_TPS_SystemTemplate.pdf (page 678)

JSON Source: docs/json/packages/M2_AUTOSARTemplates_SystemTemplate_NetworkManagement.classes.json"""

from __future__ import annotations
from typing import TYPE_CHECKING, Optional
import xml.etree.ElementTree as ET

from armodel.models.M2.AUTOSARTemplates.SystemTemplate.NetworkManagement.nm_cluster import (
    NmCluster,
)
from armodel.models.M2.AUTOSARTemplates.GenericStructure.GeneralTemplateClasses.ArObject.ar_object import ARObject
from armodel.models.M2.AUTOSARTemplates.GenericStructure.GeneralTemplateClasses.PrimitiveTypes import (
    Boolean,
    Integer,
    TimeValue,
)


class FlexrayNmCluster(NmCluster):
    """AUTOSAR FlexrayNmCluster."""

    @property
    def is_abstract(self) -> bool:
        """Check if this class is abstract.

        Returns:
            False for concrete classes
        """
        return False

    nm_car_wake_up: Optional[Boolean]
    nm_data_cycle: Optional[Integer]
    nm_main: Optional[TimeValue]
    nm_remote: Optional[TimeValue]
    nm_repeat: Optional[TimeValue]
    nm_repetition: Optional[Integer]
    nm_voting_cycle: Optional[Integer]
    def __init__(self) -> None:
        """Initialize FlexrayNmCluster."""
        super().__init__()
        self.nm_car_wake_up: Optional[Boolean] = None
        self.nm_data_cycle: Optional[Integer] = None
        self.nm_main: Optional[TimeValue] = None
        self.nm_remote: Optional[TimeValue] = None
        self.nm_repeat: Optional[TimeValue] = None
        self.nm_repetition: Optional[Integer] = None
        self.nm_voting_cycle: Optional[Integer] = None
    def serialize(self) -> ET.Element:
        """Serialize FlexrayNmCluster to XML element.

        Returns:
            xml.etree.ElementTree.Element representing this object
        """
        # Get XML tag name for this class
        tag = self._get_xml_tag()
        elem = ET.Element(tag)

        # First, call parent's serialize to handle inherited attributes
        parent_elem = super(FlexrayNmCluster, self).serialize()

        # Copy all attributes from parent element
        elem.attrib.update(parent_elem.attrib)

        # Copy all children from parent element
        for child in parent_elem:
            elem.append(child)

        # Serialize nm_car_wake_up
        if self.nm_car_wake_up is not None:
            serialized = ARObject._serialize_item(self.nm_car_wake_up, "Boolean")
            if serialized is not None:
                # Wrap with correct tag
                wrapped = ET.Element("NM-CAR-WAKE-UP")
                if hasattr(serialized, 'attrib'):
                    wrapped.attrib.update(serialized.attrib)
                    if serialized.text:
                        wrapped.text = serialized.text
                for child in serialized:
                    wrapped.append(child)
                elem.append(wrapped)

        # Serialize nm_data_cycle
        if self.nm_data_cycle is not None:
            serialized = ARObject._serialize_item(self.nm_data_cycle, "Integer")
            if serialized is not None:
                # Wrap with correct tag
                wrapped = ET.Element("NM-DATA-CYCLE")
                if hasattr(serialized, 'attrib'):
                    wrapped.attrib.update(serialized.attrib)
                    if serialized.text:
                        wrapped.text = serialized.text
                for child in serialized:
                    wrapped.append(child)
                elem.append(wrapped)

        # Serialize nm_main
        if self.nm_main is not None:
            serialized = ARObject._serialize_item(self.nm_main, "TimeValue")
            if serialized is not None:
                # Wrap with correct tag
                wrapped = ET.Element("NM-MAIN")
                if hasattr(serialized, 'attrib'):
                    wrapped.attrib.update(serialized.attrib)
                    if serialized.text:
                        wrapped.text = serialized.text
                for child in serialized:
                    wrapped.append(child)
                elem.append(wrapped)

        # Serialize nm_remote
        if self.nm_remote is not None:
            serialized = ARObject._serialize_item(self.nm_remote, "TimeValue")
            if serialized is not None:
                # Wrap with correct tag
                wrapped = ET.Element("NM-REMOTE")
                if hasattr(serialized, 'attrib'):
                    wrapped.attrib.update(serialized.attrib)
                    if serialized.text:
                        wrapped.text = serialized.text
                for child in serialized:
                    wrapped.append(child)
                elem.append(wrapped)

        # Serialize nm_repeat
        if self.nm_repeat is not None:
            serialized = ARObject._serialize_item(self.nm_repeat, "TimeValue")
            if serialized is not None:
                # Wrap with correct tag
                wrapped = ET.Element("NM-REPEAT")
                if hasattr(serialized, 'attrib'):
                    wrapped.attrib.update(serialized.attrib)
                    if serialized.text:
                        wrapped.text = serialized.text
                for child in serialized:
                    wrapped.append(child)
                elem.append(wrapped)

        # Serialize nm_repetition
        if self.nm_repetition is not None:
            serialized = ARObject._serialize_item(self.nm_repetition, "Integer")
            if serialized is not None:
                # Wrap with correct tag
                wrapped = ET.Element("NM-REPETITION")
                if hasattr(serialized, 'attrib'):
                    wrapped.attrib.update(serialized.attrib)
                    if serialized.text:
                        wrapped.text = serialized.text
                for child in serialized:
                    wrapped.append(child)
                elem.append(wrapped)

        # Serialize nm_voting_cycle
        if self.nm_voting_cycle is not None:
            serialized = ARObject._serialize_item(self.nm_voting_cycle, "Integer")
            if serialized is not None:
                # Wrap with correct tag
                wrapped = ET.Element("NM-VOTING-CYCLE")
                if hasattr(serialized, 'attrib'):
                    wrapped.attrib.update(serialized.attrib)
                    if serialized.text:
                        wrapped.text = serialized.text
                for child in serialized:
                    wrapped.append(child)
                elem.append(wrapped)

        return elem

    @classmethod
    def deserialize(cls, element: ET.Element) -> "FlexrayNmCluster":
        """Deserialize XML element to FlexrayNmCluster object.

        Args:
            element: XML element to deserialize from

        Returns:
            Deserialized FlexrayNmCluster object
        """
        # First, call parent's deserialize to handle inherited attributes
        obj = super(FlexrayNmCluster, cls).deserialize(element)

        # Parse nm_car_wake_up
        child = ARObject._find_child_element(element, "NM-CAR-WAKE-UP")
        if child is not None:
            nm_car_wake_up_value = child.text
            obj.nm_car_wake_up = nm_car_wake_up_value

        # Parse nm_data_cycle
        child = ARObject._find_child_element(element, "NM-DATA-CYCLE")
        if child is not None:
            nm_data_cycle_value = child.text
            obj.nm_data_cycle = nm_data_cycle_value

        # Parse nm_main
        child = ARObject._find_child_element(element, "NM-MAIN")
        if child is not None:
            nm_main_value = child.text
            obj.nm_main = nm_main_value

        # Parse nm_remote
        child = ARObject._find_child_element(element, "NM-REMOTE")
        if child is not None:
            nm_remote_value = child.text
            obj.nm_remote = nm_remote_value

        # Parse nm_repeat
        child = ARObject._find_child_element(element, "NM-REPEAT")
        if child is not None:
            nm_repeat_value = child.text
            obj.nm_repeat = nm_repeat_value

        # Parse nm_repetition
        child = ARObject._find_child_element(element, "NM-REPETITION")
        if child is not None:
            nm_repetition_value = child.text
            obj.nm_repetition = nm_repetition_value

        # Parse nm_voting_cycle
        child = ARObject._find_child_element(element, "NM-VOTING-CYCLE")
        if child is not None:
            nm_voting_cycle_value = child.text
            obj.nm_voting_cycle = nm_voting_cycle_value

        return obj



class FlexrayNmClusterBuilder:
    """Builder for FlexrayNmCluster."""

    def __init__(self) -> None:
        """Initialize builder."""
        self._obj: FlexrayNmCluster = FlexrayNmCluster()

    def build(self) -> FlexrayNmCluster:
        """Build and return FlexrayNmCluster object.

        Returns:
            FlexrayNmCluster instance
        """
        # TODO: Add validation
        return self._obj
