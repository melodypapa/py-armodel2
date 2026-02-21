"""EcucAbstractStringParamDef AUTOSAR element.

References:
  - AUTOSAR_CP_TPS_ECUConfiguration.pdf (page 63)
  - AUTOSAR_FO_TPS_StandardizationTemplate.pdf (page 183)

JSON Source: docs/json/packages/M2_AUTOSARTemplates_ECUCParameterDefTemplate.classes.json"""

from __future__ import annotations
from typing import TYPE_CHECKING, Optional
import xml.etree.ElementTree as ET
from armodel.serialization.decorators import atp_variant

from armodel.models.M2.AUTOSARTemplates.GenericStructure.GeneralTemplateClasses.ArObject.ar_object import ARObject
from armodel.serialization import SerializationHelper
from armodel.models.M2.AUTOSARTemplates.GenericStructure.GeneralTemplateClasses.PrimitiveTypes import (
    PositiveInteger,
    RegularExpression,
    VerbatimString,
)
from abc import ABC, abstractmethod


class EcucAbstractStringParamDef(ARObject, ABC):
    """AUTOSAR EcucAbstractStringParamDef."""

    @property
    def is_abstract(self) -> bool:
        """Check if this class is abstract.

        Returns:
            True for abstract classes
        """
        return True

    default_value: Optional[VerbatimString]
    max_length: Optional[PositiveInteger]
    min_length: Optional[PositiveInteger]
    regular: Optional[RegularExpression]
    def __init__(self) -> None:
        """Initialize EcucAbstractStringParamDef."""
        super().__init__()
        self.default_value: Optional[VerbatimString] = None
        self.max_length: Optional[PositiveInteger] = None
        self.min_length: Optional[PositiveInteger] = None
        self.regular: Optional[RegularExpression] = None

    def serialize(self) -> ET.Element:
        """Serialize EcucAbstractStringParamDef to XML element with atp_variant wrapper.

        Returns:
            xml.etree.ElementTree.Element representing this object
        """
        # Get XML tag name for this class
        tag = SerializationHelper.get_xml_tag(self.__class__)
        elem = ET.Element(tag)

        # Create inner element to hold attributes before wrapping
        inner_elem = ET.Element("INNER")

        # Serialize default_value
        if self.default_value is not None:
            serialized = SerializationHelper.serialize_item(self.default_value, "VerbatimString")
            if serialized is not None:
                wrapped = ET.Element("DEFAULT-VALUE")
                if hasattr(serialized, 'attrib'):
                    wrapped.attrib.update(serialized.attrib)
                    if serialized.text:
                        wrapped.text = serialized.text
                for child in serialized:
                    wrapped.append(child)
                inner_elem.append(wrapped)

        # Serialize max_length
        if self.max_length is not None:
            serialized = SerializationHelper.serialize_item(self.max_length, "PositiveInteger")
            if serialized is not None:
                wrapped = ET.Element("MAX-LENGTH")
                if hasattr(serialized, 'attrib'):
                    wrapped.attrib.update(serialized.attrib)
                    if serialized.text:
                        wrapped.text = serialized.text
                for child in serialized:
                    wrapped.append(child)
                inner_elem.append(wrapped)

        # Serialize min_length
        if self.min_length is not None:
            serialized = SerializationHelper.serialize_item(self.min_length, "PositiveInteger")
            if serialized is not None:
                wrapped = ET.Element("MIN-LENGTH")
                if hasattr(serialized, 'attrib'):
                    wrapped.attrib.update(serialized.attrib)
                    if serialized.text:
                        wrapped.text = serialized.text
                for child in serialized:
                    wrapped.append(child)
                inner_elem.append(wrapped)

        # Serialize regular
        if self.regular is not None:
            serialized = SerializationHelper.serialize_item(self.regular, "RegularExpression")
            if serialized is not None:
                wrapped = ET.Element("REGULAR")
                if hasattr(serialized, 'attrib'):
                    wrapped.attrib.update(serialized.attrib)
                    if serialized.text:
                        wrapped.text = serialized.text
                for child in serialized:
                    wrapped.append(child)
                inner_elem.append(wrapped)

        # Wrap inner element in atp_variant VARIANTS/CONDITIONAL structure
        wrapped = SerializationHelper.serialize_with_atp_variant(inner_elem, "EcucAbstractStringParamDef")
        elem.append(wrapped)

        return elem

    @classmethod
    def deserialize(cls, element: ET.Element) -> "EcucAbstractStringParamDef":
        """Deserialize XML element to EcucAbstractStringParamDef object with atp_variant unwrapping.

        Args:
            element: XML element to deserialize from

        Returns:
            Deserialized EcucAbstractStringParamDef object
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
        inner_elem = SerializationHelper.deserialize_from_atp_variant(element, "EcucAbstractStringParamDef")
        if inner_elem is None:
            # No wrapper structure found, return object with default values
            return obj

        # Parse default_value
        child = SerializationHelper.find_child_element(inner_elem, "DEFAULT-VALUE")
        if child is not None:
            default_value_value = SerializationHelper.deserialize_by_tag(child, "VerbatimString")
            obj.default_value = default_value_value

        # Parse max_length
        child = SerializationHelper.find_child_element(inner_elem, "MAX-LENGTH")
        if child is not None:
            max_length_value = child.text
            obj.max_length = max_length_value

        # Parse min_length
        child = SerializationHelper.find_child_element(inner_elem, "MIN-LENGTH")
        if child is not None:
            min_length_value = child.text
            obj.min_length = min_length_value

        # Parse regular
        child = SerializationHelper.find_child_element(inner_elem, "REGULAR")
        if child is not None:
            regular_value = child.text
            obj.regular = regular_value

        return obj



class EcucAbstractStringParamDefBuilder:
    """Builder for EcucAbstractStringParamDef."""

    def __init__(self) -> None:
        """Initialize builder."""
        self._obj: EcucAbstractStringParamDef = EcucAbstractStringParamDef()

    def build(self) -> EcucAbstractStringParamDef:
        """Build and return EcucAbstractStringParamDef object.

        Returns:
            EcucAbstractStringParamDef instance
        """
        # TODO: Add validation
        return self._obj
