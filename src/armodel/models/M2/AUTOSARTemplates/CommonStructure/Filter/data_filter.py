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
