"""LimitValueVariationPoint AUTOSAR element.

References:
  - AUTOSAR_FO_TPS_GenericStructureTemplate.pdf (page 241)

JSON Source: docs/json/packages/M2_AUTOSARTemplates_GenericStructure_VariantHandling_AttributeValueVariationPoints.classes.json"""

from __future__ import annotations
from typing import TYPE_CHECKING, Optional
import xml.etree.ElementTree as ET

from armodel.models.M2.AUTOSARTemplates.GenericStructure.GeneralTemplateClasses.ArObject.ar_object import ARObject
from armodel.serialization import SerializationHelper
from armodel.models.M2.AUTOSARTemplates.GenericStructure.GeneralTemplateClasses.PrimitiveTypes import (
    IntervalTypeEnum,
)


class LimitValueVariationPoint(ARObject):
    """AUTOSAR LimitValueVariationPoint."""

    @property
    def is_abstract(self) -> bool:
        """Check if this class is abstract.

        Returns:
            False for concrete classes
        """
        return False

    interval_type_enum: Optional[IntervalTypeEnum]
    def __init__(self) -> None:
        """Initialize LimitValueVariationPoint."""
        super().__init__()
        self.interval_type_enum: Optional[IntervalTypeEnum] = None

    def serialize(self) -> ET.Element:
        """Serialize LimitValueVariationPoint to XML element.

        Returns:
            xml.etree.ElementTree.Element representing this object
        """
        # Get XML tag name for this class
        tag = SerializationHelper.get_xml_tag(self.__class__)
        elem = ET.Element(tag)

        # First, call parent's serialize to handle inherited attributes
        parent_elem = super(LimitValueVariationPoint, self).serialize()

        # Copy all attributes from parent element
        elem.attrib.update(parent_elem.attrib)

        # Copy text from parent element
        if parent_elem.text:
            elem.text = parent_elem.text

        # Copy all children from parent element
        for child in parent_elem:
            elem.append(child)

        # Serialize interval_type_enum
        if self.interval_type_enum is not None:
            serialized = SerializationHelper.serialize_item(self.interval_type_enum, "IntervalTypeEnum")
            if serialized is not None:
                # Wrap with correct tag
                wrapped = ET.Element("INTERVAL-TYPE-ENUM")
                if hasattr(serialized, 'attrib'):
                    wrapped.attrib.update(serialized.attrib)
                    if serialized.text:
                        wrapped.text = serialized.text
                for child in serialized:
                    wrapped.append(child)
                elem.append(wrapped)

        return elem

    @classmethod
    def deserialize(cls, element: ET.Element) -> "LimitValueVariationPoint":
        """Deserialize XML element to LimitValueVariationPoint object.

        Args:
            element: XML element to deserialize from

        Returns:
            Deserialized LimitValueVariationPoint object
        """
        # First, call parent's deserialize to handle inherited attributes
        obj = super(LimitValueVariationPoint, cls).deserialize(element)

        # Parse interval_type_enum
        child = SerializationHelper.find_child_element(element, "INTERVAL-TYPE-ENUM")
        if child is not None:
            interval_type_enum_value = IntervalTypeEnum.deserialize(child)
            obj.interval_type_enum = interval_type_enum_value

        return obj



class LimitValueVariationPointBuilder:
    """Builder for LimitValueVariationPoint."""

    def __init__(self) -> None:
        """Initialize builder."""
        self._obj: LimitValueVariationPoint = LimitValueVariationPoint()

    def build(self) -> LimitValueVariationPoint:
        """Build and return LimitValueVariationPoint object.

        Returns:
            LimitValueVariationPoint instance
        """
        # TODO: Add validation
        return self._obj
