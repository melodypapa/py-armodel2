"""ARObject AUTOSAR element.

References:
  - AUTOSAR_FO_TPS_GenericStructureTemplate.pdf (page 191)

JSON Source: docs/json/packages/M2_AUTOSARTemplates_GenericStructure_GeneralTemplateClasses_ArObject.classes.json"""

from __future__ import annotations

from typing import TYPE_CHECKING, Optional

import xml.etree.ElementTree as ET

from armodel.serialization.decorators import xml_attribute
from armodel.serialization.serialization_helper import SerializationHelper

if TYPE_CHECKING:
    from armodel.models.M2.AUTOSARTemplates.GenericStructure.GeneralTemplateClasses.PrimitiveTypes import (
        DateTime,
        String,
    )


class ARObject:
    """AUTOSAR ARObject base class.

    This class provides the base serialization infrastructure for all AUTOSAR model classes.
    It only serializes checksum and timestamp attributes. Child classes must call
    super().serialize() and super().deserialize() to properly inherit these attributes.

    All serialization helper methods have been extracted to SerializationHelper class.
    """

    checksum: Optional["String"]
    timestamp: Optional["DateTime"]

    def __init__(self) -> None:
        """Initialize ARObject."""
        self._checksum: Optional["String"] = None
        self._timestamp: Optional["DateTime"] = None

    @property
    def checksum(self) -> Optional["String"]:
        """Checksum attribute."""
        return self._checksum

    @checksum.setter
    def checksum(self, value: Optional["String"]) -> None:
        """Set checksum attribute."""
        self._checksum = value

    @property
    @xml_attribute
    def timestamp(self) -> Optional["DateTime"]:
        """Timestamp attribute serialized as XML attribute 'T'."""
        return self._timestamp

    @timestamp.setter
    def timestamp(self, value: Optional["DateTime"]) -> None:
        """Set timestamp attribute."""
        self._timestamp = value

    def serialize(self) -> ET.Element:
        """Serialize object to XML element.

        Only serializes checksum and timestamp attributes.
        Child classes must call super().serialize() to inherit these attributes.

        Returns:
            xml.etree.ElementTree.Element representing this object
        """
        tag = SerializationHelper.get_xml_tag(self.__class__)
        elem = ET.Element(tag)

        # Serialize timestamp (XML attribute)
        if self._timestamp is not None:
            elem.set("T", str(self._timestamp))

        # Serialize checksum (child element)
        if self._checksum is not None:
            checksum_elem = ET.Element("CHECKSUM")
            checksum_elem.text = str(self._checksum)
            elem.append(checksum_elem)

        return elem

    @classmethod
    def deserialize(cls, element: ET.Element) -> ARObject:
        """Deserialize XML element to ARObject.

        Only deserializes checksum and timestamp attributes.
        Child classes must call super().deserialize() to inherit these attributes.

        Args:
            element: XML element to deserialize from

        Returns:
            Deserialized ARObject object
        """
        obj = cls.__new__(cls)
        obj.__init__()

        # Deserialize timestamp (XML attribute)
        timestamp_str = element.get("T")
        if timestamp_str is not None:
            obj.timestamp = timestamp_str

        # Deserialize checksum (child element)
        checksum_elem = SerializationHelper.find_child_element(element, "CHECKSUM")
        if checksum_elem is not None and checksum_elem.text:
            obj.checksum = checksum_elem.text

        return obj


class ARObjectBuilder:
    """Builder for ARObject."""

    def __init__(self) -> None:
        """Initialize builder."""
        self._obj: ARObject = ARObject()

    def build(self) -> ARObject:
        """Build and return ARObject object.

        Returns:
            ARObject instance
        """
        # TODO: Add validation
        return self._obj