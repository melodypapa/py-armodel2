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
