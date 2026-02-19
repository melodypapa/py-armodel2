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
        # First, call parent's deserialize to handle inherited attributes
        obj = super(DataTypeMappingSet, cls).deserialize(element)

        # Parse data_type_maps (list from container "DATA-TYPE-MAPS")
        obj.data_type_maps = []
        container = ARObject._find_child_element(element, "DATA-TYPE-MAPS")
        if container is not None:
            for child in container:
                # Deserialize each child element dynamically based on its tag
                child_value = ARObject._deserialize_by_tag(child, None)
                if child_value is not None:
                    obj.data_type_maps.append(child_value)

        # Parse mode_request_type_maps (list from container "MODE-REQUEST-TYPE-MAPS")
        obj.mode_request_type_maps = []
        container = ARObject._find_child_element(element, "MODE-REQUEST-TYPE-MAPS")
        if container is not None:
            for child in container:
                # Deserialize each child element dynamically based on its tag
                child_value = ARObject._deserialize_by_tag(child, None)
                if child_value is not None:
                    obj.mode_request_type_maps.append(child_value)

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
