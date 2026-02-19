"""McSwEmulationMethodSupport AUTOSAR element.

References:
  - AUTOSAR_CP_TPS_BSWModuleDescriptionTemplate.pdf (page 180)

JSON Source: docs/json/packages/M2_AUTOSARTemplates_CommonStructure_MeasurementCalibrationSupport.classes.json"""

from __future__ import annotations
from typing import TYPE_CHECKING, Optional
import xml.etree.ElementTree as ET

from armodel.models.M2.AUTOSARTemplates.GenericStructure.GeneralTemplateClasses.ArObject.ar_object import ARObject
from armodel.models.M2.AUTOSARTemplates.GenericStructure.GeneralTemplateClasses.ArObject.ar_ref import ARRef
from armodel.models.M2.AUTOSARTemplates.GenericStructure.GeneralTemplateClasses.PrimitiveTypes import (
    Identifier,
)
from armodel.models.M2.AUTOSARTemplates.CommonStructure.MeasurementCalibrationSupport.mc_parameter_element_group import (
    McParameterElementGroup,
)
from armodel.models.M2.AUTOSARTemplates.SWComponentTemplate.Datatype.DataPrototypes.variable_data_prototype import (
    VariableDataPrototype,
)


class McSwEmulationMethodSupport(ARObject):
    """AUTOSAR McSwEmulationMethodSupport."""

    @property
    def is_abstract(self) -> bool:
        """Check if this class is abstract.

        Returns:
            False for concrete classes
        """
        return False

    base_reference_ref: Optional[ARRef]
    category: Optional[Identifier]
    element_groups: list[McParameterElementGroup]
    reference_table_ref: Optional[ARRef]
    short_label: Optional[Identifier]
    def __init__(self) -> None:
        """Initialize McSwEmulationMethodSupport."""
        super().__init__()
        self.base_reference_ref: Optional[ARRef] = None
        self.category: Optional[Identifier] = None
        self.element_groups: list[McParameterElementGroup] = []
        self.reference_table_ref: Optional[ARRef] = None
        self.short_label: Optional[Identifier] = None
    @classmethod
    def deserialize(cls, element: ET.Element) -> "McSwEmulationMethodSupport":
        """Deserialize XML element to McSwEmulationMethodSupport object.

        Args:
            element: XML element to deserialize from

        Returns:
            Deserialized McSwEmulationMethodSupport object
        """
        # Create instance and initialize with default values
        obj = cls.__new__(cls)
        obj.__init__()

        # Parse base_reference_ref
        child = ARObject._find_child_element(element, "BASE-REFERENCE")
        if child is not None:
            base_reference_ref_value = ARObject._deserialize_by_tag(child, "VariableDataPrototype")
            obj.base_reference_ref = base_reference_ref_value

        # Parse category
        child = ARObject._find_child_element(element, "CATEGORY")
        if child is not None:
            category_value = ARObject._deserialize_by_tag(child, "Identifier")
            obj.category = category_value

        # Parse element_groups (list from container "ELEMENT-GROUPS")
        obj.element_groups = []
        container = ARObject._find_child_element(element, "ELEMENT-GROUPS")
        if container is not None:
            for child in container:
                # Deserialize each child element dynamically based on its tag
                child_value = ARObject._deserialize_by_tag(child, None)
                if child_value is not None:
                    obj.element_groups.append(child_value)

        # Parse reference_table_ref
        child = ARObject._find_child_element(element, "REFERENCE-TABLE")
        if child is not None:
            reference_table_ref_value = ARObject._deserialize_by_tag(child, "VariableDataPrototype")
            obj.reference_table_ref = reference_table_ref_value

        # Parse short_label
        child = ARObject._find_child_element(element, "SHORT-LABEL")
        if child is not None:
            short_label_value = ARObject._deserialize_by_tag(child, "Identifier")
            obj.short_label = short_label_value

        return obj



class McSwEmulationMethodSupportBuilder:
    """Builder for McSwEmulationMethodSupport."""

    def __init__(self) -> None:
        """Initialize builder."""
        self._obj: McSwEmulationMethodSupport = McSwEmulationMethodSupport()

    def build(self) -> McSwEmulationMethodSupport:
        """Build and return McSwEmulationMethodSupport object.

        Returns:
            McSwEmulationMethodSupport instance
        """
        # TODO: Add validation
        return self._obj
