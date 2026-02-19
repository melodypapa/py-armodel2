"""CanClusterBusOffRecovery AUTOSAR element.

References:
  - AUTOSAR_CP_TPS_SystemTemplate.pdf (page 62)

JSON Source: docs/json/packages/M2_AUTOSARTemplates_SystemTemplate_Fibex_Fibex4Can_CanTopology.classes.json"""

from __future__ import annotations
from typing import TYPE_CHECKING, Optional
import xml.etree.ElementTree as ET

from armodel.models.M2.AUTOSARTemplates.GenericStructure.GeneralTemplateClasses.ArObject.ar_object import ARObject
from armodel.models.M2.AUTOSARTemplates.GenericStructure.GeneralTemplateClasses.PrimitiveTypes import (
    PositiveInteger,
    TimeValue,
)


class CanClusterBusOffRecovery(ARObject):
    """AUTOSAR CanClusterBusOffRecovery."""

    @property
    def is_abstract(self) -> bool:
        """Check if this class is abstract.

        Returns:
            False for concrete classes
        """
        return False

    bor_counter_l1_to: Optional[PositiveInteger]
    bor_time_l1: Optional[TimeValue]
    bor_time_l2: Optional[TimeValue]
    bor_time_tx: Optional[TimeValue]
    main_function: Optional[TimeValue]
    def __init__(self) -> None:
        """Initialize CanClusterBusOffRecovery."""
        super().__init__()
        self.bor_counter_l1_to: Optional[PositiveInteger] = None
        self.bor_time_l1: Optional[TimeValue] = None
        self.bor_time_l2: Optional[TimeValue] = None
        self.bor_time_tx: Optional[TimeValue] = None
        self.main_function: Optional[TimeValue] = None
    def serialize(self) -> ET.Element:
        """Serialize CanClusterBusOffRecovery to XML element.

        Returns:
            xml.etree.ElementTree.Element representing this object
        """
        # Get XML tag name for this class
        tag = self._get_xml_tag()
        elem = ET.Element(tag)

        # Serialize bor_counter_l1_to
        if self.bor_counter_l1_to is not None:
            serialized = ARObject._serialize_item(self.bor_counter_l1_to, "PositiveInteger")
            if serialized is not None:
                # Wrap with correct tag
                wrapped = ET.Element("BOR-COUNTER-L1-TO")
                if hasattr(serialized, 'attrib'):
                    wrapped.attrib.update(serialized.attrib)
                    if serialized.text:
                        wrapped.text = serialized.text
                for child in serialized:
                    wrapped.append(child)
                elem.append(wrapped)

        # Serialize bor_time_l1
        if self.bor_time_l1 is not None:
            serialized = ARObject._serialize_item(self.bor_time_l1, "TimeValue")
            if serialized is not None:
                # Wrap with correct tag
                wrapped = ET.Element("BOR-TIME-L1")
                if hasattr(serialized, 'attrib'):
                    wrapped.attrib.update(serialized.attrib)
                    if serialized.text:
                        wrapped.text = serialized.text
                for child in serialized:
                    wrapped.append(child)
                elem.append(wrapped)

        # Serialize bor_time_l2
        if self.bor_time_l2 is not None:
            serialized = ARObject._serialize_item(self.bor_time_l2, "TimeValue")
            if serialized is not None:
                # Wrap with correct tag
                wrapped = ET.Element("BOR-TIME-L2")
                if hasattr(serialized, 'attrib'):
                    wrapped.attrib.update(serialized.attrib)
                    if serialized.text:
                        wrapped.text = serialized.text
                for child in serialized:
                    wrapped.append(child)
                elem.append(wrapped)

        # Serialize bor_time_tx
        if self.bor_time_tx is not None:
            serialized = ARObject._serialize_item(self.bor_time_tx, "TimeValue")
            if serialized is not None:
                # Wrap with correct tag
                wrapped = ET.Element("BOR-TIME-TX")
                if hasattr(serialized, 'attrib'):
                    wrapped.attrib.update(serialized.attrib)
                    if serialized.text:
                        wrapped.text = serialized.text
                for child in serialized:
                    wrapped.append(child)
                elem.append(wrapped)

        # Serialize main_function
        if self.main_function is not None:
            serialized = ARObject._serialize_item(self.main_function, "TimeValue")
            if serialized is not None:
                # Wrap with correct tag
                wrapped = ET.Element("MAIN-FUNCTION")
                if hasattr(serialized, 'attrib'):
                    wrapped.attrib.update(serialized.attrib)
                    if serialized.text:
                        wrapped.text = serialized.text
                for child in serialized:
                    wrapped.append(child)
                elem.append(wrapped)

        return elem

    @classmethod
    def deserialize(cls, element: ET.Element) -> "CanClusterBusOffRecovery":
        """Deserialize XML element to CanClusterBusOffRecovery object.

        Args:
            element: XML element to deserialize from

        Returns:
            Deserialized CanClusterBusOffRecovery object
        """
        # Create instance and initialize with default values
        obj = cls.__new__(cls)
        obj.__init__()

        # Parse bor_counter_l1_to
        child = ARObject._find_child_element(element, "BOR-COUNTER-L1-TO")
        if child is not None:
            bor_counter_l1_to_value = child.text
            obj.bor_counter_l1_to = bor_counter_l1_to_value

        # Parse bor_time_l1
        child = ARObject._find_child_element(element, "BOR-TIME-L1")
        if child is not None:
            bor_time_l1_value = child.text
            obj.bor_time_l1 = bor_time_l1_value

        # Parse bor_time_l2
        child = ARObject._find_child_element(element, "BOR-TIME-L2")
        if child is not None:
            bor_time_l2_value = child.text
            obj.bor_time_l2 = bor_time_l2_value

        # Parse bor_time_tx
        child = ARObject._find_child_element(element, "BOR-TIME-TX")
        if child is not None:
            bor_time_tx_value = child.text
            obj.bor_time_tx = bor_time_tx_value

        # Parse main_function
        child = ARObject._find_child_element(element, "MAIN-FUNCTION")
        if child is not None:
            main_function_value = child.text
            obj.main_function = main_function_value

        return obj



class CanClusterBusOffRecoveryBuilder:
    """Builder for CanClusterBusOffRecovery."""

    def __init__(self) -> None:
        """Initialize builder."""
        self._obj: CanClusterBusOffRecovery = CanClusterBusOffRecovery()

    def build(self) -> CanClusterBusOffRecovery:
        """Build and return CanClusterBusOffRecovery object.

        Returns:
            CanClusterBusOffRecovery instance
        """
        # TODO: Add validation
        return self._obj
