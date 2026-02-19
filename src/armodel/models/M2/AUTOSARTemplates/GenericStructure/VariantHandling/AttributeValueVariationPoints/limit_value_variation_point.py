"""LimitValueVariationPoint AUTOSAR element.

References:
  - AUTOSAR_FO_TPS_GenericStructureTemplate.pdf (page 241)

JSON Source: docs/json/packages/M2_AUTOSARTemplates_GenericStructure_VariantHandling_AttributeValueVariationPoints.classes.json"""

from __future__ import annotations
from typing import TYPE_CHECKING, Optional
import xml.etree.ElementTree as ET

from armodel.models.M2.AUTOSARTemplates.GenericStructure.GeneralTemplateClasses.ArObject.ar_object import ARObject
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
        tag = ARObject._get_xml_tag(self)
        elem = ET.Element(tag)

        # Serialize interval_type_enum
        if self.interval_type_enum is not None:
            serialized = ARObject._serialize_item(self.interval_type_enum, "IntervalTypeEnum")
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
        # Create instance and initialize with default values
        obj = cls.__new__(cls)
        obj.__init__()

        # Parse interval_type_enum
        child = ARObject._find_child_element(element, "INTERVAL-TYPE-ENUM")
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
