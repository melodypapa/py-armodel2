"""CanControllerFdConfiguration AUTOSAR element.

References:
  - AUTOSAR_CP_TPS_SystemTemplate.pdf (page 66)

JSON Source: docs/json/packages/M2_AUTOSARTemplates_SystemTemplate_Fibex_Fibex4Can_CanTopology.classes.json"""

from __future__ import annotations
from typing import TYPE_CHECKING, Optional
import xml.etree.ElementTree as ET

from armodel.models.M2.AUTOSARTemplates.GenericStructure.GeneralTemplateClasses.ArObject.ar_object import ARObject
from armodel.models.M2.AUTOSARTemplates.GenericStructure.GeneralTemplateClasses.PrimitiveTypes import (
    Boolean,
    PositiveInteger,
)


class CanControllerFdConfiguration(ARObject):
    """AUTOSAR CanControllerFdConfiguration."""

    @property
    def is_abstract(self) -> bool:
        """Check if this class is abstract.

        Returns:
            False for concrete classes
        """
        return False

    padding_value: Optional[PositiveInteger]
    prop_seg: Optional[PositiveInteger]
    ssp_offset: Optional[PositiveInteger]
    sync_jump_width: Optional[PositiveInteger]
    time_seg1: Optional[PositiveInteger]
    time_seg2: Optional[PositiveInteger]
    tx_bit_rate_switch: Optional[Boolean]
    def __init__(self) -> None:
        """Initialize CanControllerFdConfiguration."""
        super().__init__()
        self.padding_value: Optional[PositiveInteger] = None
        self.prop_seg: Optional[PositiveInteger] = None
        self.ssp_offset: Optional[PositiveInteger] = None
        self.sync_jump_width: Optional[PositiveInteger] = None
        self.time_seg1: Optional[PositiveInteger] = None
        self.time_seg2: Optional[PositiveInteger] = None
        self.tx_bit_rate_switch: Optional[Boolean] = None
    def serialize(self) -> ET.Element:
        """Serialize CanControllerFdConfiguration to XML element.

        Returns:
            xml.etree.ElementTree.Element representing this object
        """
        # Get XML tag name for this class
        tag = self._get_xml_tag()
        elem = ET.Element(tag)

        # Serialize padding_value
        if self.padding_value is not None:
            serialized = ARObject._serialize_item(self.padding_value, "PositiveInteger")
            if serialized is not None:
                # Wrap with correct tag
                wrapped = ET.Element("PADDING-VALUE")
                if hasattr(serialized, 'attrib'):
                    wrapped.attrib.update(serialized.attrib)
                    if serialized.text:
                        wrapped.text = serialized.text
                for child in serialized:
                    wrapped.append(child)
                elem.append(wrapped)

        # Serialize prop_seg
        if self.prop_seg is not None:
            serialized = ARObject._serialize_item(self.prop_seg, "PositiveInteger")
            if serialized is not None:
                # Wrap with correct tag
                wrapped = ET.Element("PROP-SEG")
                if hasattr(serialized, 'attrib'):
                    wrapped.attrib.update(serialized.attrib)
                    if serialized.text:
                        wrapped.text = serialized.text
                for child in serialized:
                    wrapped.append(child)
                elem.append(wrapped)

        # Serialize ssp_offset
        if self.ssp_offset is not None:
            serialized = ARObject._serialize_item(self.ssp_offset, "PositiveInteger")
            if serialized is not None:
                # Wrap with correct tag
                wrapped = ET.Element("SSP-OFFSET")
                if hasattr(serialized, 'attrib'):
                    wrapped.attrib.update(serialized.attrib)
                    if serialized.text:
                        wrapped.text = serialized.text
                for child in serialized:
                    wrapped.append(child)
                elem.append(wrapped)

        # Serialize sync_jump_width
        if self.sync_jump_width is not None:
            serialized = ARObject._serialize_item(self.sync_jump_width, "PositiveInteger")
            if serialized is not None:
                # Wrap with correct tag
                wrapped = ET.Element("SYNC-JUMP-WIDTH")
                if hasattr(serialized, 'attrib'):
                    wrapped.attrib.update(serialized.attrib)
                    if serialized.text:
                        wrapped.text = serialized.text
                for child in serialized:
                    wrapped.append(child)
                elem.append(wrapped)

        # Serialize time_seg1
        if self.time_seg1 is not None:
            serialized = ARObject._serialize_item(self.time_seg1, "PositiveInteger")
            if serialized is not None:
                # Wrap with correct tag
                wrapped = ET.Element("TIME-SEG1")
                if hasattr(serialized, 'attrib'):
                    wrapped.attrib.update(serialized.attrib)
                    if serialized.text:
                        wrapped.text = serialized.text
                for child in serialized:
                    wrapped.append(child)
                elem.append(wrapped)

        # Serialize time_seg2
        if self.time_seg2 is not None:
            serialized = ARObject._serialize_item(self.time_seg2, "PositiveInteger")
            if serialized is not None:
                # Wrap with correct tag
                wrapped = ET.Element("TIME-SEG2")
                if hasattr(serialized, 'attrib'):
                    wrapped.attrib.update(serialized.attrib)
                    if serialized.text:
                        wrapped.text = serialized.text
                for child in serialized:
                    wrapped.append(child)
                elem.append(wrapped)

        # Serialize tx_bit_rate_switch
        if self.tx_bit_rate_switch is not None:
            serialized = ARObject._serialize_item(self.tx_bit_rate_switch, "Boolean")
            if serialized is not None:
                # Wrap with correct tag
                wrapped = ET.Element("TX-BIT-RATE-SWITCH")
                if hasattr(serialized, 'attrib'):
                    wrapped.attrib.update(serialized.attrib)
                    if serialized.text:
                        wrapped.text = serialized.text
                for child in serialized:
                    wrapped.append(child)
                elem.append(wrapped)

        return elem

    @classmethod
    def deserialize(cls, element: ET.Element) -> "CanControllerFdConfiguration":
        """Deserialize XML element to CanControllerFdConfiguration object.

        Args:
            element: XML element to deserialize from

        Returns:
            Deserialized CanControllerFdConfiguration object
        """
        # Create instance and initialize with default values
        obj = cls.__new__(cls)
        obj.__init__()

        # Parse padding_value
        child = ARObject._find_child_element(element, "PADDING-VALUE")
        if child is not None:
            padding_value_value = child.text
            obj.padding_value = padding_value_value

        # Parse prop_seg
        child = ARObject._find_child_element(element, "PROP-SEG")
        if child is not None:
            prop_seg_value = child.text
            obj.prop_seg = prop_seg_value

        # Parse ssp_offset
        child = ARObject._find_child_element(element, "SSP-OFFSET")
        if child is not None:
            ssp_offset_value = child.text
            obj.ssp_offset = ssp_offset_value

        # Parse sync_jump_width
        child = ARObject._find_child_element(element, "SYNC-JUMP-WIDTH")
        if child is not None:
            sync_jump_width_value = child.text
            obj.sync_jump_width = sync_jump_width_value

        # Parse time_seg1
        child = ARObject._find_child_element(element, "TIME-SEG1")
        if child is not None:
            time_seg1_value = child.text
            obj.time_seg1 = time_seg1_value

        # Parse time_seg2
        child = ARObject._find_child_element(element, "TIME-SEG2")
        if child is not None:
            time_seg2_value = child.text
            obj.time_seg2 = time_seg2_value

        # Parse tx_bit_rate_switch
        child = ARObject._find_child_element(element, "TX-BIT-RATE-SWITCH")
        if child is not None:
            tx_bit_rate_switch_value = child.text
            obj.tx_bit_rate_switch = tx_bit_rate_switch_value

        return obj



class CanControllerFdConfigurationBuilder:
    """Builder for CanControllerFdConfiguration."""

    def __init__(self) -> None:
        """Initialize builder."""
        self._obj: CanControllerFdConfiguration = CanControllerFdConfiguration()

    def build(self) -> CanControllerFdConfiguration:
        """Build and return CanControllerFdConfiguration object.

        Returns:
            CanControllerFdConfiguration instance
        """
        # TODO: Add validation
        return self._obj
