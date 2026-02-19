"""InternalBehavior AUTOSAR element.

References:
  - AUTOSAR_CP_TPS_BSWModuleDescriptionTemplate.pdf (page 64)
  - AUTOSAR_CP_TPS_DiagnosticExtractTemplate.pdf (page 319)
  - AUTOSAR_CP_TPS_SoftwareComponentTemplate.pdf (page 516)
  - AUTOSAR_CP_TPS_SystemTemplate.pdf (page 2033)
  - AUTOSAR_CP_TPS_TimingExtensions.pdf (page 231)
  - AUTOSAR_FO_TPS_GenericStructureTemplate.pdf (page 453)

JSON Source: docs/json/packages/M2_AUTOSARTemplates_CommonStructure_InternalBehavior.classes.json"""

from __future__ import annotations
from typing import TYPE_CHECKING, Optional
import xml.etree.ElementTree as ET

from armodel.models.M2.AUTOSARTemplates.GenericStructure.GeneralTemplateClasses.Identifiable.identifiable import (
    Identifiable,
)
from armodel.models.M2.AUTOSARTemplates.GenericStructure.GeneralTemplateClasses.ArObject.ar_object import ARObject
from armodel.models.M2.AUTOSARTemplates.GenericStructure.GeneralTemplateClasses.ArObject.ar_ref import ARRef
from armodel.models.M2.AUTOSARTemplates.CommonStructure.Constants.constant_specification import (
    ConstantSpecification,
)
from armodel.models.M2.AUTOSARTemplates.SWComponentTemplate.Datatype.Datatypes.data_type_mapping_set import (
    DataTypeMappingSet,
)
from armodel.models.M2.AUTOSARTemplates.CommonStructure.InternalBehavior.exclusive_area import (
    ExclusiveArea,
)
from armodel.models.M2.AUTOSARTemplates.CommonStructure.InternalBehavior.exclusive_area_nesting_order import (
    ExclusiveAreaNestingOrder,
)
from armodel.models.M2.AUTOSARTemplates.SWComponentTemplate.Datatype.DataPrototypes.parameter_data_prototype import (
    ParameterDataPrototype,
)
from armodel.models.M2.AUTOSARTemplates.SWComponentTemplate.Datatype.DataPrototypes.variable_data_prototype import (
    VariableDataPrototype,
)
from abc import ABC, abstractmethod


class InternalBehavior(Identifiable, ABC):
    """AUTOSAR InternalBehavior."""

    @property
    def is_abstract(self) -> bool:
        """Check if this class is abstract.

        Returns:
            True for abstract classes
        """
        return True

    constants: list[ParameterDataPrototype]
    constant_values: list[ConstantSpecification]
    data_type_refs: list[ARRef]
    exclusive_areas: list[ExclusiveArea]
    exclusive_area_nestings: list[ExclusiveAreaNestingOrder]
    static_memorie_refs: list[ARRef]
    def __init__(self) -> None:
        """Initialize InternalBehavior."""
        super().__init__()
        self.constants: list[ParameterDataPrototype] = []
        self.constant_values: list[ConstantSpecification] = []
        self.data_type_refs: list[ARRef] = []
        self.exclusive_areas: list[ExclusiveArea] = []
        self.exclusive_area_nestings: list[ExclusiveAreaNestingOrder] = []
        self.static_memorie_refs: list[ARRef] = []
    @classmethod
    def deserialize(cls, element: ET.Element) -> "InternalBehavior":
        """Deserialize XML element to InternalBehavior object.

        Args:
            element: XML element to deserialize from

        Returns:
            Deserialized InternalBehavior object
        """
        # Create instance and initialize with default values
        obj = cls.__new__(cls)
        obj.__init__()

        # Parse constants (list)
        obj.constants = []
        for child in ARObject._find_all_child_elements(element, "CONSTANTS"):
            constants_value = ARObject._deserialize_by_tag(child, "ParameterDataPrototype")
            obj.constants.append(constants_value)

        # Parse constant_values (list)
        obj.constant_values = []
        for child in ARObject._find_all_child_elements(element, "CONSTANT-VALUES"):
            constant_values_value = ARObject._deserialize_by_tag(child, "ConstantSpecification")
            obj.constant_values.append(constant_values_value)

        # Parse data_type_refs (list)
        obj.data_type_refs = []
        for child in ARObject._find_all_child_elements(element, "DATA-TYPES"):
            data_type_refs_value = ARObject._deserialize_by_tag(child, "DataTypeMappingSet")
            obj.data_type_refs.append(data_type_refs_value)

        # Parse exclusive_areas (list)
        obj.exclusive_areas = []
        for child in ARObject._find_all_child_elements(element, "EXCLUSIVE-AREAS"):
            exclusive_areas_value = ARObject._deserialize_by_tag(child, "ExclusiveArea")
            obj.exclusive_areas.append(exclusive_areas_value)

        # Parse exclusive_area_nestings (list)
        obj.exclusive_area_nestings = []
        for child in ARObject._find_all_child_elements(element, "EXCLUSIVE-AREA-NESTINGS"):
            exclusive_area_nestings_value = ARObject._deserialize_by_tag(child, "ExclusiveAreaNestingOrder")
            obj.exclusive_area_nestings.append(exclusive_area_nestings_value)

        # Parse static_memorie_refs (list)
        obj.static_memorie_refs = []
        for child in ARObject._find_all_child_elements(element, "STATIC-MEMORIES"):
            static_memorie_refs_value = ARObject._deserialize_by_tag(child, "VariableDataPrototype")
            obj.static_memorie_refs.append(static_memorie_refs_value)

        return obj



class InternalBehaviorBuilder:
    """Builder for InternalBehavior."""

    def __init__(self) -> None:
        """Initialize builder."""
        self._obj: InternalBehavior = InternalBehavior()

    def build(self) -> InternalBehavior:
        """Build and return InternalBehavior object.

        Returns:
            InternalBehavior instance
        """
        # TODO: Add validation
        return self._obj
