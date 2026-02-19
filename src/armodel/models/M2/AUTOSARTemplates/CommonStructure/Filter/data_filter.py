"""DataFilter AUTOSAR element.

References:
  - AUTOSAR_CP_TPS_SoftwareComponentTemplate.pdf (page 182)
  - AUTOSAR_CP_TPS_SystemTemplate.pdf (page 394)

JSON Source: docs/json/packages/M2_AUTOSARTemplates_CommonStructure_Filter.classes.json"""

from __future__ import annotations
from typing import TYPE_CHECKING, Optional
import xml.etree.ElementTree as ET

from armodel.models.M2.AUTOSARTemplates.GenericStructure.GeneralTemplateClasses.ArObject.ar_object import ARObject
from armodel.models.M2.AUTOSARTemplates.CommonStructure.Filter import (
    DataFilterTypeEnum,
)
from armodel.models.M2.AUTOSARTemplates.GenericStructure.GeneralTemplateClasses.PrimitiveTypes import (
    PositiveInteger,
    UnlimitedInteger,
)


class DataFilter(ARObject):
    """AUTOSAR DataFilter."""

    @property
    def is_abstract(self) -> bool:
        """Check if this class is abstract.

        Returns:
            False for concrete classes
        """
        return False

    data_filter_type_enum: Optional[DataFilterTypeEnum]
    mask: Optional[UnlimitedInteger]
    max: Optional[UnlimitedInteger]
    min: Optional[UnlimitedInteger]
    offset: Optional[PositiveInteger]
    period: Optional[PositiveInteger]
    x: Optional[UnlimitedInteger]
    def __init__(self) -> None:
        """Initialize DataFilter."""
        super().__init__()
        self.data_filter_type_enum: Optional[DataFilterTypeEnum] = None
        self.mask: Optional[UnlimitedInteger] = None
        self.max: Optional[UnlimitedInteger] = None
        self.min: Optional[UnlimitedInteger] = None
        self.offset: Optional[PositiveInteger] = None
        self.period: Optional[PositiveInteger] = None
        self.x: Optional[UnlimitedInteger] = None

    def serialize(self) -> ET.Element:
        """Serialize DataFilter to XML element.

        Returns:
            xml.etree.ElementTree.Element representing this object
        """
        # Get XML tag name for this class
        tag = self._get_xml_tag()
        elem = ET.Element(tag)

        # Serialize data_filter_type_enum
        if self.data_filter_type_enum is not None:
            serialized = ARObject._serialize_item(self.data_filter_type_enum, "DataFilterTypeEnum")
            if serialized is not None:
                # Wrap with correct tag
                wrapped = ET.Element("DATA-FILTER-TYPE-ENUM")
                if hasattr(serialized, 'attrib'):
                    wrapped.attrib.update(serialized.attrib)
                    if serialized.text:
                        wrapped.text = serialized.text
                for child in serialized:
                    wrapped.append(child)
                elem.append(wrapped)

        # Serialize mask
        if self.mask is not None:
            serialized = ARObject._serialize_item(self.mask, "UnlimitedInteger")
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

        # Serialize max
        if self.max is not None:
            serialized = ARObject._serialize_item(self.max, "UnlimitedInteger")
            if serialized is not None:
                # Wrap with correct tag
                wrapped = ET.Element("MAX")
                if hasattr(serialized, 'attrib'):
                    wrapped.attrib.update(serialized.attrib)
                    if serialized.text:
                        wrapped.text = serialized.text
                for child in serialized:
                    wrapped.append(child)
                elem.append(wrapped)

        # Serialize min
        if self.min is not None:
            serialized = ARObject._serialize_item(self.min, "UnlimitedInteger")
            if serialized is not None:
                # Wrap with correct tag
                wrapped = ET.Element("MIN")
                if hasattr(serialized, 'attrib'):
                    wrapped.attrib.update(serialized.attrib)
                    if serialized.text:
                        wrapped.text = serialized.text
                for child in serialized:
                    wrapped.append(child)
                elem.append(wrapped)

        # Serialize offset
        if self.offset is not None:
            serialized = ARObject._serialize_item(self.offset, "PositiveInteger")
            if serialized is not None:
                # Wrap with correct tag
                wrapped = ET.Element("OFFSET")
                if hasattr(serialized, 'attrib'):
                    wrapped.attrib.update(serialized.attrib)
                    if serialized.text:
                        wrapped.text = serialized.text
                for child in serialized:
                    wrapped.append(child)
                elem.append(wrapped)

        # Serialize period
        if self.period is not None:
            serialized = ARObject._serialize_item(self.period, "PositiveInteger")
            if serialized is not None:
                # Wrap with correct tag
                wrapped = ET.Element("PERIOD")
                if hasattr(serialized, 'attrib'):
                    wrapped.attrib.update(serialized.attrib)
                    if serialized.text:
                        wrapped.text = serialized.text
                for child in serialized:
                    wrapped.append(child)
                elem.append(wrapped)

        # Serialize x
        if self.x is not None:
            serialized = ARObject._serialize_item(self.x, "UnlimitedInteger")
            if serialized is not None:
                # Wrap with correct tag
                wrapped = ET.Element("X")
                if hasattr(serialized, 'attrib'):
                    wrapped.attrib.update(serialized.attrib)
                    if serialized.text:
                        wrapped.text = serialized.text
                for child in serialized:
                    wrapped.append(child)
                elem.append(wrapped)

        return elem

    @classmethod
    def deserialize(cls, element: ET.Element) -> "DataFilter":
        """Deserialize XML element to DataFilter object.

        Args:
            element: XML element to deserialize from

        Returns:
            Deserialized DataFilter object
        """
        # Create instance and initialize with default values
        obj = cls.__new__(cls)
        obj.__init__()

        # Parse data_filter_type_enum
        child = ARObject._find_child_element(element, "DATA-FILTER-TYPE-ENUM")
        if child is not None:
            data_filter_type_enum_value = DataFilterTypeEnum.deserialize(child)
            obj.data_filter_type_enum = data_filter_type_enum_value

        # Parse mask
        child = ARObject._find_child_element(element, "MASK")
        if child is not None:
            mask_value = child.text
            obj.mask = mask_value

        # Parse max
        child = ARObject._find_child_element(element, "MAX")
        if child is not None:
            max_value = child.text
            obj.max = max_value

        # Parse min
        child = ARObject._find_child_element(element, "MIN")
        if child is not None:
            min_value = child.text
            obj.min = min_value

        # Parse offset
        child = ARObject._find_child_element(element, "OFFSET")
        if child is not None:
            offset_value = child.text
            obj.offset = offset_value

        # Parse period
        child = ARObject._find_child_element(element, "PERIOD")
        if child is not None:
            period_value = child.text
            obj.period = period_value

        # Parse x
        child = ARObject._find_child_element(element, "X")
        if child is not None:
            x_value = child.text
            obj.x = x_value

        return obj



class DataFilterBuilder:
    """Builder for DataFilter."""

    def __init__(self) -> None:
        """Initialize builder."""
        self._obj: DataFilter = DataFilter()

    def build(self) -> DataFilter:
        """Build and return DataFilter object.

        Returns:
            DataFilter instance
        """
        # TODO: Add validation
        return self._obj
