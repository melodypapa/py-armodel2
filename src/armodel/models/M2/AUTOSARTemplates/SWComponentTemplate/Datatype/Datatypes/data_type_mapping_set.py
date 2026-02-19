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
from armodel.models.M2.AUTOSARTemplates.GenericStructure.GeneralTemplateClasses.ArObject.ar_object import ARObject
from armodel.models.M2.AUTOSARTemplates.SWComponentTemplate.Datatype.Datatypes.data_type_map import (
    DataTypeMap,
)
from armodel.models.M2.AUTOSARTemplates.CommonStructure.ModeDeclaration.mode_request_type_map import (
    ModeRequestTypeMap,
)


class DataTypeMappingSet(ARElement):
    """AUTOSAR DataTypeMappingSet."""

    @property
    def is_abstract(self) -> bool:
        """Check if this class is abstract.

        Returns:
            False for concrete classes
        """
        return False

    data_type_maps: list[DataTypeMap]
    mode_request_type_maps: list[ModeRequestTypeMap]
    def __init__(self) -> None:
        """Initialize DataTypeMappingSet."""
        super().__init__()
        self.data_type_maps: list[DataTypeMap] = []
        self.mode_request_type_maps: list[ModeRequestTypeMap] = []
    @classmethod
    def deserialize(cls, element: ET.Element) -> "DataTypeMappingSet":
        """Deserialize XML element to DataTypeMappingSet object.

        Args:
            element: XML element to deserialize from

        Returns:
            Deserialized DataTypeMappingSet object
        """
        # Create instance and initialize with default values
        obj = cls.__new__(cls)
        obj.__init__()

        # Parse data_type_maps (list)
        obj.data_type_maps = []
        for child in ARObject._find_all_child_elements(element, "DATA-TYPE-MAPS"):
            data_type_maps_value = ARObject._deserialize_by_tag(child, "DataTypeMap")
            obj.data_type_maps.append(data_type_maps_value)

        # Parse mode_request_type_maps (list)
        obj.mode_request_type_maps = []
        for child in ARObject._find_all_child_elements(element, "MODE-REQUEST-TYPE-MAPS"):
            mode_request_type_maps_value = ARObject._deserialize_by_tag(child, "ModeRequestTypeMap")
            obj.mode_request_type_maps.append(mode_request_type_maps_value)

        return obj



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
