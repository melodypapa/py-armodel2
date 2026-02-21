"""ConditionalChangeNad AUTOSAR element.

References:
  - AUTOSAR_CP_TPS_SystemTemplate.pdf (page 438)

JSON Source: docs/json/packages/M2_AUTOSARTemplates_SystemTemplate_Fibex_Fibex4Lin_LinCommunication.classes.json"""

from __future__ import annotations
from typing import TYPE_CHECKING, Optional
import xml.etree.ElementTree as ET

from armodel.models.M2.AUTOSARTemplates.SystemTemplate.Fibex.Fibex4Lin.LinCommunication.lin_configuration_entry import (
    LinConfigurationEntry,
)
from armodel.models.M2.AUTOSARTemplates.GenericStructure.GeneralTemplateClasses.ArObject.ar_object import ARObject
from armodel.serialization import SerializationHelper
from armodel.models.M2.AUTOSARTemplates.GenericStructure.GeneralTemplateClasses.PrimitiveTypes import (
    Integer,
    PositiveInteger,
)


class ConditionalChangeNad(LinConfigurationEntry):
    """AUTOSAR ConditionalChangeNad."""

    @property
    def is_abstract(self) -> bool:
        """Check if this class is abstract.

        Returns:
            False for concrete classes
        """
        return False

    byte: Optional[Integer]
    id: Optional[PositiveInteger]
    invert: Optional[Integer]
    mask: Optional[Integer]
    new_nad: Optional[Integer]
    def __init__(self) -> None:
        """Initialize ConditionalChangeNad."""
        super().__init__()
        self.byte: Optional[Integer] = None
        self.id: Optional[PositiveInteger] = None
        self.invert: Optional[Integer] = None
        self.mask: Optional[Integer] = None
        self.new_nad: Optional[Integer] = None

    def serialize(self) -> ET.Element:
        """Serialize ConditionalChangeNad to XML element.

        Returns:
            xml.etree.ElementTree.Element representing this object
        """
        # Get XML tag name for this class
        tag = SerializationHelper.get_xml_tag(self.__class__)
        elem = ET.Element(tag)

        # First, call parent's serialize to handle inherited attributes
        parent_elem = super(ConditionalChangeNad, self).serialize()

        # Copy all attributes from parent element
        elem.attrib.update(parent_elem.attrib)

        # Copy text from parent element
        if parent_elem.text:
            elem.text = parent_elem.text

        # Copy all children from parent element
        for child in parent_elem:
            elem.append(child)

        # Serialize byte
        if self.byte is not None:
            serialized = SerializationHelper.serialize_item(self.byte, "Integer")
            if serialized is not None:
                # Wrap with correct tag
                wrapped = ET.Element("BYTE")
                if hasattr(serialized, 'attrib'):
                    wrapped.attrib.update(serialized.attrib)
                    if serialized.text:
                        wrapped.text = serialized.text
                for child in serialized:
                    wrapped.append(child)
                elem.append(wrapped)

        # Serialize id
        if self.id is not None:
            serialized = SerializationHelper.serialize_item(self.id, "PositiveInteger")
            if serialized is not None:
                # Wrap with correct tag
                wrapped = ET.Element("ID")
                if hasattr(serialized, 'attrib'):
                    wrapped.attrib.update(serialized.attrib)
                    if serialized.text:
                        wrapped.text = serialized.text
                for child in serialized:
                    wrapped.append(child)
                elem.append(wrapped)

        # Serialize invert
        if self.invert is not None:
            serialized = SerializationHelper.serialize_item(self.invert, "Integer")
            if serialized is not None:
                # Wrap with correct tag
                wrapped = ET.Element("INVERT")
                if hasattr(serialized, 'attrib'):
                    wrapped.attrib.update(serialized.attrib)
                    if serialized.text:
                        wrapped.text = serialized.text
                for child in serialized:
                    wrapped.append(child)
                elem.append(wrapped)

        # Serialize mask
        if self.mask is not None:
            serialized = SerializationHelper.serialize_item(self.mask, "Integer")
            if serialized is not None:
                # Wrap with correct tag
                wrapped = ET.Element("MASK")
                if hasattr(serialized, 'attrib'):
                    wrapped.attrib.update(serialized.attrib)
                    if serialized.text:
                        wrapped.text = serialized.text
                for child in serialized:
                    wrapped.append(child)
                elem.append(wrapped)

        # Serialize new_nad
        if self.new_nad is not None:
            serialized = SerializationHelper.serialize_item(self.new_nad, "Integer")
            if serialized is not None:
                # Wrap with correct tag
                wrapped = ET.Element("NEW-NAD")
                if hasattr(serialized, 'attrib'):
                    wrapped.attrib.update(serialized.attrib)
                    if serialized.text:
                        wrapped.text = serialized.text
                for child in serialized:
                    wrapped.append(child)
                elem.append(wrapped)

        return elem

    @classmethod
    def deserialize(cls, element: ET.Element) -> "ConditionalChangeNad":
        """Deserialize XML element to ConditionalChangeNad object.

        Args:
            element: XML element to deserialize from

        Returns:
            Deserialized ConditionalChangeNad object
        """
        # First, call parent's deserialize to handle inherited attributes
        obj = super(ConditionalChangeNad, cls).deserialize(element)

        # Parse byte
        child = SerializationHelper.find_child_element(element, "BYTE")
        if child is not None:
            byte_value = child.text
            obj.byte = byte_value

        # Parse id
        child = SerializationHelper.find_child_element(element, "ID")
        if child is not None:
            id_value = child.text
            obj.id = id_value

        # Parse invert
        child = SerializationHelper.find_child_element(element, "INVERT")
        if child is not None:
            invert_value = child.text
            obj.invert = invert_value

        # Parse mask
        child = SerializationHelper.find_child_element(element, "MASK")
        if child is not None:
            mask_value = child.text
            obj.mask = mask_value

        # Parse new_nad
        child = SerializationHelper.find_child_element(element, "NEW-NAD")
        if child is not None:
            new_nad_value = child.text
            obj.new_nad = new_nad_value

        return obj



class ConditionalChangeNadBuilder:
    """Builder for ConditionalChangeNad."""

    def __init__(self) -> None:
        """Initialize builder."""
        self._obj: ConditionalChangeNad = ConditionalChangeNad()

    def build(self) -> ConditionalChangeNad:
        """Build and return ConditionalChangeNad object.

        Returns:
            ConditionalChangeNad instance
        """
        # TODO: Add validation
        return self._obj
