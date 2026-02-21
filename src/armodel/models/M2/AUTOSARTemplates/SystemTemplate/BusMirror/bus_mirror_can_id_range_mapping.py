"""BusMirrorCanIdRangeMapping AUTOSAR element.

References:
  - AUTOSAR_CP_TPS_SystemTemplate.pdf (page 702)

JSON Source: docs/json/packages/M2_AUTOSARTemplates_SystemTemplate_BusMirror.classes.json"""

from __future__ import annotations
from typing import TYPE_CHECKING, Optional
import xml.etree.ElementTree as ET

from armodel.models.M2.AUTOSARTemplates.GenericStructure.GeneralTemplateClasses.ArObject.ar_object import ARObject
from armodel.serialization import SerializationHelper
from armodel.models.M2.AUTOSARTemplates.GenericStructure.GeneralTemplateClasses.PrimitiveTypes import (
    PositiveInteger,
)


class BusMirrorCanIdRangeMapping(ARObject):
    """AUTOSAR BusMirrorCanIdRangeMapping."""

    @property
    def is_abstract(self) -> bool:
        """Check if this class is abstract.

        Returns:
            False for concrete classes
        """
        return False

    destination_base: Optional[PositiveInteger]
    source_can_id_code: Optional[PositiveInteger]
    source_can_id: Optional[PositiveInteger]
    def __init__(self) -> None:
        """Initialize BusMirrorCanIdRangeMapping."""
        super().__init__()
        self.destination_base: Optional[PositiveInteger] = None
        self.source_can_id_code: Optional[PositiveInteger] = None
        self.source_can_id: Optional[PositiveInteger] = None

    def serialize(self) -> ET.Element:
        """Serialize BusMirrorCanIdRangeMapping to XML element.

        Returns:
            xml.etree.ElementTree.Element representing this object
        """
        # Get XML tag name for this class
        tag = SerializationHelper.get_xml_tag(self.__class__)
        elem = ET.Element(tag)

        # First, call parent's serialize to handle inherited attributes
        parent_elem = super(BusMirrorCanIdRangeMapping, self).serialize()

        # Copy all attributes from parent element
        elem.attrib.update(parent_elem.attrib)

        # Copy text from parent element
        if parent_elem.text:
            elem.text = parent_elem.text

        # Copy all children from parent element
        for child in parent_elem:
            elem.append(child)

        # Serialize destination_base
        if self.destination_base is not None:
            serialized = SerializationHelper.serialize_item(self.destination_base, "PositiveInteger")
            if serialized is not None:
                # Wrap with correct tag
                wrapped = ET.Element("DESTINATION-BASE")
                if hasattr(serialized, 'attrib'):
                    wrapped.attrib.update(serialized.attrib)
                    if serialized.text:
                        wrapped.text = serialized.text
                for child in serialized:
                    wrapped.append(child)
                elem.append(wrapped)

        # Serialize source_can_id_code
        if self.source_can_id_code is not None:
            serialized = SerializationHelper.serialize_item(self.source_can_id_code, "PositiveInteger")
            if serialized is not None:
                # Wrap with correct tag
                wrapped = ET.Element("SOURCE-CAN-ID-CODE")
                if hasattr(serialized, 'attrib'):
                    wrapped.attrib.update(serialized.attrib)
                    if serialized.text:
                        wrapped.text = serialized.text
                for child in serialized:
                    wrapped.append(child)
                elem.append(wrapped)

        # Serialize source_can_id
        if self.source_can_id is not None:
            serialized = SerializationHelper.serialize_item(self.source_can_id, "PositiveInteger")
            if serialized is not None:
                # Wrap with correct tag
                wrapped = ET.Element("SOURCE-CAN-ID")
                if hasattr(serialized, 'attrib'):
                    wrapped.attrib.update(serialized.attrib)
                    if serialized.text:
                        wrapped.text = serialized.text
                for child in serialized:
                    wrapped.append(child)
                elem.append(wrapped)

        return elem

    @classmethod
    def deserialize(cls, element: ET.Element) -> "BusMirrorCanIdRangeMapping":
        """Deserialize XML element to BusMirrorCanIdRangeMapping object.

        Args:
            element: XML element to deserialize from

        Returns:
            Deserialized BusMirrorCanIdRangeMapping object
        """
        # First, call parent's deserialize to handle inherited attributes
        obj = super(BusMirrorCanIdRangeMapping, cls).deserialize(element)

        # Parse destination_base
        child = SerializationHelper.find_child_element(element, "DESTINATION-BASE")
        if child is not None:
            destination_base_value = child.text
            obj.destination_base = destination_base_value

        # Parse source_can_id_code
        child = SerializationHelper.find_child_element(element, "SOURCE-CAN-ID-CODE")
        if child is not None:
            source_can_id_code_value = child.text
            obj.source_can_id_code = source_can_id_code_value

        # Parse source_can_id
        child = SerializationHelper.find_child_element(element, "SOURCE-CAN-ID")
        if child is not None:
            source_can_id_value = child.text
            obj.source_can_id = source_can_id_value

        return obj



class BusMirrorCanIdRangeMappingBuilder:
    """Builder for BusMirrorCanIdRangeMapping."""

    def __init__(self) -> None:
        """Initialize builder."""
        self._obj: BusMirrorCanIdRangeMapping = BusMirrorCanIdRangeMapping()

    def build(self) -> BusMirrorCanIdRangeMapping:
        """Build and return BusMirrorCanIdRangeMapping object.

        Returns:
            BusMirrorCanIdRangeMapping instance
        """
        # TODO: Add validation
        return self._obj
