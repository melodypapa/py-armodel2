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
