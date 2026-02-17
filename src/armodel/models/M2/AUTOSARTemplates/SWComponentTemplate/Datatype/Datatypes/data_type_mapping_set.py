"""DataTypeMappingSet AUTOSAR element.

References:
  - AUTOSAR_CP_TPS_BSWModuleDescriptionTemplate.pdf (page 311)
  - AUTOSAR_CP_TPS_SoftwareComponentTemplate.pdf (page 234)
  - AUTOSAR_CP_TPS_SystemTemplate.pdf (page 2015)
  - AUTOSAR_FO_TPS_StandardizationTemplate.pdf (page 180)

JSON Source: docs/json/packages/M2_AUTOSARTemplates_SWComponentTemplate_Datatype_Datatypes.classes.json"""

from __future__ import annotations
from typing import TYPE_CHECKING, Optional
import xml.etree.ElementTree as ET

from armodel.models.M2.AUTOSARTemplates.GenericStructure.GeneralTemplateClasses.ARPackage.ar_element import (
    ARElement,
)
from armodel.models.M2.AUTOSARTemplates.SWComponentTemplate.Datatype.Datatypes.data_type_map import (
    DataTypeMap,
)
from armodel.models.M2.AUTOSARTemplates.CommonStructure.ModeDeclaration.mode_request_type_map import (
    ModeRequestTypeMap,
)


class DataTypeMappingSet(ARElement):
    """AUTOSAR DataTypeMappingSet."""

    data_type_maps: list[DataTypeMap]
    mode_request_type_maps: list[ModeRequestTypeMap]
    def __init__(self) -> None:
        """Initialize DataTypeMappingSet."""
        super().__init__()
        self.data_type_maps: list[DataTypeMap] = []
        self.mode_request_type_maps: list[ModeRequestTypeMap] = []


class DataTypeMappingSetBuilder:
    """Builder for DataTypeMappingSet."""

    def __init__(self) -> None:
        """Initialize builder."""
        self._obj: DataTypeMappingSet = DataTypeMappingSet()

    def build(self) -> DataTypeMappingSet:
        """Build and return DataTypeMappingSet object.

        Returns:
            DataTypeMappingSet instance
        """
        # TODO: Add validation
        return self._obj
