"""ParameterSwComponentType AUTOSAR element.

References:
  - AUTOSAR_CP_TPS_SoftwareComponentTemplate.pdf (page 41)
  - AUTOSAR_CP_TPS_SystemTemplate.pdf (page 2043)

JSON Source: docs/json/packages/M2_AUTOSARTemplates_SWComponentTemplate_Components.classes.json"""

from __future__ import annotations
from typing import TYPE_CHECKING, Optional
import xml.etree.ElementTree as ET

from armodel.models.M2.AUTOSARTemplates.SWComponentTemplate.Components.sw_component_type import (
    SwComponentType,
)
from armodel.models.M2.AUTOSARTemplates.GenericStructure.GeneralTemplateClasses.ArObject.ar_object import ARObject
from armodel.models.M2.AUTOSARTemplates.GenericStructure.GeneralTemplateClasses.ArObject.ar_ref import ARRef
from armodel.models.M2.AUTOSARTemplates.CommonStructure.Constants.constant_specification import (
    ConstantSpecification,
)
from armodel.models.M2.AUTOSARTemplates.SWComponentTemplate.Datatype.Datatypes.data_type_mapping_set import (
    DataTypeMappingSet,
)
from armodel.models.M2.AUTOSARTemplates.SWComponentTemplate.SwcInternalBehavior.InstantiationDataDefProps.instantiation_data_def_props import (
    InstantiationDataDefProps,
)


class ParameterSwComponentType(SwComponentType):
    """AUTOSAR ParameterSwComponentType."""

    @property
    def is_abstract(self) -> bool:
        """Check if this class is abstract.

        Returns:
            False for concrete classes
        """
        return False

    constants: list[ConstantSpecification]
    data_type_refs: list[ARRef]
    instantiation_data_defs: list[InstantiationDataDefProps]
    def __init__(self) -> None:
        """Initialize ParameterSwComponentType."""
        super().__init__()
        self.constants: list[ConstantSpecification] = []
        self.data_type_refs: list[ARRef] = []
        self.instantiation_data_defs: list[InstantiationDataDefProps] = []
    @classmethod
    def deserialize(cls, element: ET.Element) -> "ParameterSwComponentType":
        """Deserialize XML element to ParameterSwComponentType object.

        Args:
            element: XML element to deserialize from

        Returns:
            Deserialized ParameterSwComponentType object
        """
        # Create instance and initialize with default values
        obj = cls.__new__(cls)
        obj.__init__()

        # Parse constants (list)
        obj.constants = []
        for child in ARObject._find_all_child_elements(element, "CONSTANTS"):
            constants_value = ARObject._deserialize_by_tag(child, "ConstantSpecification")
            obj.constants.append(constants_value)

        # Parse data_type_refs (list)
        obj.data_type_refs = []
        for child in ARObject._find_all_child_elements(element, "DATA-TYPES"):
            data_type_refs_value = ARObject._deserialize_by_tag(child, "DataTypeMappingSet")
            obj.data_type_refs.append(data_type_refs_value)

        # Parse instantiation_data_defs (list)
        obj.instantiation_data_defs = []
        for child in ARObject._find_all_child_elements(element, "INSTANTIATION-DATA-DEFS"):
            instantiation_data_defs_value = ARObject._deserialize_by_tag(child, "InstantiationDataDefProps")
            obj.instantiation_data_defs.append(instantiation_data_defs_value)

        return obj



class ParameterSwComponentTypeBuilder:
    """Builder for ParameterSwComponentType."""

    def __init__(self) -> None:
        """Initialize builder."""
        self._obj: ParameterSwComponentType = ParameterSwComponentType()

    def build(self) -> ParameterSwComponentType:
        """Build and return ParameterSwComponentType object.

        Returns:
            ParameterSwComponentType instance
        """
        # TODO: Add validation
        return self._obj
