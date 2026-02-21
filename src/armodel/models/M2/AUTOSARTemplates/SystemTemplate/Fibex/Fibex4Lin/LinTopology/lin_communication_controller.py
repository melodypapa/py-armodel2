"""LinCommunicationController AUTOSAR element.

References:
  - AUTOSAR_CP_TPS_SystemTemplate.pdf (page 93)

JSON Source: docs/json/packages/M2_AUTOSARTemplates_SystemTemplate_Fibex_Fibex4Lin_LinTopology.classes.json"""

from __future__ import annotations
from typing import TYPE_CHECKING, Optional
import xml.etree.ElementTree as ET
from armodel.serialization.decorators import atp_variant

from armodel.models.M2.AUTOSARTemplates.GenericStructure.GeneralTemplateClasses.ArObject.ar_object import ARObject
from armodel.serialization import SerializationHelper
from armodel.models.M2.AUTOSARTemplates.GenericStructure.GeneralTemplateClasses.PrimitiveTypes import (
    String,
)
from abc import ABC, abstractmethod


class LinCommunicationController(ARObject, ABC):
    """AUTOSAR LinCommunicationController."""

    @property
    def is_abstract(self) -> bool:
        """Check if this class is abstract.

        Returns:
            True for abstract classes
        """
        return True

    protocol_version: Optional[String]
    def __init__(self) -> None:
        """Initialize LinCommunicationController."""
        super().__init__()
        self.protocol_version: Optional[String] = None

    def serialize(self) -> ET.Element:
        """Serialize LinCommunicationController to XML element with atp_variant wrapper.

        Returns:
            xml.etree.ElementTree.Element representing this object
        """
        # Get XML tag name for this class
        tag = SerializationHelper.get_xml_tag(self.__class__)
        elem = ET.Element(tag)

        # Create inner element to hold attributes before wrapping
        inner_elem = ET.Element("INNER")

        # Serialize protocol_version
        if self.protocol_version is not None:
            serialized = SerializationHelper.serialize_item(self.protocol_version, "String")
            if serialized is not None:
                wrapped = ET.Element("PROTOCOL-VERSION")
                if hasattr(serialized, 'attrib'):
                    wrapped.attrib.update(serialized.attrib)
                    if serialized.text:
                        wrapped.text = serialized.text
                for child in serialized:
                    wrapped.append(child)
                inner_elem.append(wrapped)

        # Wrap inner element in atp_variant VARIANTS/CONDITIONAL structure
        wrapped = SerializationHelper.serialize_with_atp_variant(inner_elem, "LinCommunicationController")
        elem.append(wrapped)

        return elem

    @classmethod
    def deserialize(cls, element: ET.Element) -> "LinCommunicationController":
        """Deserialize XML element to LinCommunicationController object with atp_variant unwrapping.

        Args:
            element: XML element to deserialize from

        Returns:
            Deserialized LinCommunicationController object
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
        inner_elem = SerializationHelper.deserialize_from_atp_variant(element, "LinCommunicationController")
        if inner_elem is None:
            # No wrapper structure found, return object with default values
            return obj

        # Parse protocol_version
        child = SerializationHelper.find_child_element(inner_elem, "PROTOCOL-VERSION")
        if child is not None:
            protocol_version_value = child.text
            obj.protocol_version = protocol_version_value

        return obj



class LinCommunicationControllerBuilder:
    """Builder for LinCommunicationController."""

    def __init__(self) -> None:
        """Initialize builder."""
        self._obj: LinCommunicationController = LinCommunicationController()

    def build(self) -> LinCommunicationController:
        """Build and return LinCommunicationController object.

        Returns:
            LinCommunicationController instance
        """
        # TODO: Add validation
        return self._obj
