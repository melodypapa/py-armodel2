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
        # First, call parent's deserialize to handle inherited attributes
        obj = super(ParameterSwComponentType, cls).deserialize(element)

        # Parse constants (list from container "CONSTANTS")
        obj.constants = []
        container = ARObject._find_child_element(element, "CONSTANTS")
        if container is not None:
            for child in container:
                # Deserialize each child element dynamically based on its tag
                child_value = ARObject._deserialize_by_tag(child, None)
                if child_value is not None:
                    obj.constants.append(child_value)

        # Parse data_type_refs (list from container "DATA-TYPES")
        obj.data_type_refs = []
        container = ARObject._find_child_element(element, "DATA-TYPES")
        if container is not None:
            for child in container:
                # Deserialize each child element dynamically based on its tag
                child_value = ARObject._deserialize_by_tag(child, None)
                if child_value is not None:
                    obj.data_type_refs.append(child_value)

        # Parse instantiation_data_defs (list from container "INSTANTIATION-DATA-DEFS")
        obj.instantiation_data_defs = []
        container = ARObject._find_child_element(element, "INSTANTIATION-DATA-DEFS")
        if container is not None:
            for child in container:
                # Deserialize each child element dynamically based on its tag
                child_value = ARObject._deserialize_by_tag(child, None)
                if child_value is not None:
                    obj.instantiation_data_defs.append(child_value)

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
