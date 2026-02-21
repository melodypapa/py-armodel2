"""TtcanCluster AUTOSAR element.

References:
  - AUTOSAR_CP_TPS_SystemTemplate.pdf (page 76)

JSON Source: docs/json/packages/M2_AUTOSARTemplates_SystemTemplate_Fibex_Fibex4Ttcan_TtcanTopology.classes.json"""

from __future__ import annotations
from typing import TYPE_CHECKING, Optional
import xml.etree.ElementTree as ET
from armodel.serialization.decorators import atp_variant

from armodel.models.M2.AUTOSARTemplates.GenericStructure.GeneralTemplateClasses.ArObject.ar_object import ARObject
from armodel.serialization import SerializationHelper
from armodel.models.M2.AUTOSARTemplates.GenericStructure.GeneralTemplateClasses.PrimitiveTypes import (
    Boolean,
    Integer,
    TimeValue,
)


@atp_variant()

class TtcanCluster(ARObject):
    """AUTOSAR TtcanCluster."""

    @property
    def is_abstract(self) -> bool:
        """Check if this class is abstract.

        Returns:
            False for concrete classes
        """
        return False

    basic_cycle_length: Optional[Integer]
    ntu: Optional[TimeValue]
    operation_mode: Optional[Boolean]
    def __init__(self) -> None:
        """Initialize TtcanCluster."""
        super().__init__()
        self.basic_cycle_length: Optional[Integer] = None
        self.ntu: Optional[TimeValue] = None
        self.operation_mode: Optional[Boolean] = None

    def serialize(self) -> ET.Element:
        """Serialize TtcanCluster to XML element with atp_variant wrapper.

        Returns:
            xml.etree.ElementTree.Element representing this object
        """
        # Get XML tag name for this class
        tag = SerializationHelper.get_xml_tag(self.__class__)
        elem = ET.Element(tag)

        # Create inner element to hold attributes before wrapping
        inner_elem = ET.Element("INNER")

        # Serialize basic_cycle_length
        if self.basic_cycle_length is not None:
            serialized = SerializationHelper.serialize_item(self.basic_cycle_length, "Integer")
            if serialized is not None:
                wrapped = ET.Element("BASIC-CYCLE-LENGTH")
                if hasattr(serialized, 'attrib'):
                    wrapped.attrib.update(serialized.attrib)
                    if serialized.text:
                        wrapped.text = serialized.text
                for child in serialized:
                    wrapped.append(child)
                inner_elem.append(wrapped)

        # Serialize ntu
        if self.ntu is not None:
            serialized = SerializationHelper.serialize_item(self.ntu, "TimeValue")
            if serialized is not None:
                wrapped = ET.Element("NTU")
                if hasattr(serialized, 'attrib'):
                    wrapped.attrib.update(serialized.attrib)
                    if serialized.text:
                        wrapped.text = serialized.text
                for child in serialized:
                    wrapped.append(child)
                inner_elem.append(wrapped)

        # Serialize operation_mode
        if self.operation_mode is not None:
            serialized = SerializationHelper.serialize_item(self.operation_mode, "Boolean")
            if serialized is not None:
                wrapped = ET.Element("OPERATION-MODE")
                if hasattr(serialized, 'attrib'):
                    wrapped.attrib.update(serialized.attrib)
                    if serialized.text:
                        wrapped.text = serialized.text
                for child in serialized:
                    wrapped.append(child)
                inner_elem.append(wrapped)

        # Wrap inner element in atp_variant VARIANTS/CONDITIONAL structure
        wrapped = SerializationHelper.serialize_with_atp_variant(inner_elem, "TtcanCluster")
        elem.append(wrapped)

        return elem

    @classmethod
    def deserialize(cls, element: ET.Element) -> "TtcanCluster":
        """Deserialize XML element to TtcanCluster object with atp_variant unwrapping.

        Args:
            element: XML element to deserialize from

        Returns:
            Deserialized TtcanCluster object
        """
        # Create instance and initialize with default values
        obj = cls.__new__(cls)
        obj.__init__()

        # Handle ARObject inherited attributes (checksum and timestamp)
        # Parse timestamp (XML attribute 'T')
        timestamp_value = element.get("T")
        if timestamp_value is not None:
            obj.timestamp = timestamp_value

        # Parse checksum (child element)
        checksum_elem = SerializationHelper.find_child_element(element, "CHECKSUM")
        if checksum_elem is not None:
            checksum_value = checksum_elem.text
            if checksum_value is not None:
                obj.checksum = checksum_value

        # Unwrap atp_variant VARIANTS/CONDITIONAL structure
        inner_elem = SerializationHelper.deserialize_from_atp_variant(element, "TtcanCluster")
        if inner_elem is None:
            # No wrapper structure found, return object with default values
            return obj

        # Parse basic_cycle_length
        child = SerializationHelper.find_child_element(inner_elem, "BASIC-CYCLE-LENGTH")
        if child is not None:
            basic_cycle_length_value = child.text
            obj.basic_cycle_length = basic_cycle_length_value

        # Parse ntu
        child = SerializationHelper.find_child_element(inner_elem, "NTU")
        if child is not None:
            ntu_value = child.text
            obj.ntu = ntu_value

        # Parse operation_mode
        child = SerializationHelper.find_child_element(inner_elem, "OPERATION-MODE")
        if child is not None:
            operation_mode_value = child.text
            obj.operation_mode = operation_mode_value

        return obj



class TtcanClusterBuilder:
    """Builder for TtcanCluster."""

    def __init__(self) -> None:
        """Initialize builder."""
        self._obj: TtcanCluster = TtcanCluster()

    def build(self) -> TtcanCluster:
        """Build and return TtcanCluster object.

        Returns:
            TtcanCluster instance
        """
        # TODO: Add validation
        return self._obj
