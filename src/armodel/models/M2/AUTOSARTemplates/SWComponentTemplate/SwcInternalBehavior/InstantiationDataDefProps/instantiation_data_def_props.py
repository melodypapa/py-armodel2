"""InstantiationDataDefProps AUTOSAR element.

References:
  - AUTOSAR_CP_TPS_SoftwareComponentTemplate.pdf (page 588)

JSON Source: docs/json/packages/M2_AUTOSARTemplates_SWComponentTemplate_SwcInternalBehavior_InstantiationDataDefProps.classes.json"""

from __future__ import annotations
from typing import TYPE_CHECKING, Optional
import xml.etree.ElementTree as ET

from armodel.models.M2.AUTOSARTemplates.GenericStructure.GeneralTemplateClasses.ArObject.ar_object import ARObject
from armodel.models.M2.AUTOSARTemplates.GenericStructure.GeneralTemplateClasses.ArObject.ar_ref import ARRef
from armodel.models.M2.AUTOSARTemplates.SWComponentTemplate.SwcInternalBehavior.DataElements.autosar_parameter_ref import (
    AutosarParameterRef,
)
from armodel.models.M2.AUTOSARTemplates.SWComponentTemplate.SwcInternalBehavior.DataElements.autosar_variable_ref import (
    AutosarVariableRef,
)

if TYPE_CHECKING:
    from armodel.models.M2.MSR.DataDictionary.DataDefProperties.sw_data_def_props import (
        SwDataDefProps,
    )



class InstantiationDataDefProps(ARObject):
    """AUTOSAR InstantiationDataDefProps."""

    @property
    def is_abstract(self) -> bool:
        """Check if this class is abstract.

        Returns:
            False for concrete classes
        """
        return False

    parameter_ref: Optional[ARRef]
    sw_data_def: Optional[SwDataDefProps]
    variable_instance_ref: Optional[ARRef]
    def __init__(self) -> None:
        """Initialize InstantiationDataDefProps."""
        super().__init__()
        self.parameter_ref: Optional[ARRef] = None
        self.sw_data_def: Optional[SwDataDefProps] = None
        self.variable_instance_ref: Optional[ARRef] = None
    @classmethod
    def deserialize(cls, element: ET.Element) -> "InstantiationDataDefProps":
        """Deserialize XML element to InstantiationDataDefProps object.

        Args:
            element: XML element to deserialize from

        Returns:
            Deserialized InstantiationDataDefProps object
        """
        # Create instance and initialize with default values
        obj = cls.__new__(cls)
        obj.__init__()

        # Parse parameter_ref
        child = ARObject._find_child_element(element, "PARAMETER")
        if child is not None:
            parameter_ref_value = ARObject._deserialize_by_tag(child, "AutosarParameterRef")
            obj.parameter_ref = parameter_ref_value

        # Parse sw_data_def
        child = ARObject._find_child_element(element, "SW-DATA-DEF")
        if child is not None:
            sw_data_def_value = ARObject._deserialize_by_tag(child, "SwDataDefProps")
            obj.sw_data_def = sw_data_def_value

        # Parse variable_instance_ref
        child = ARObject._find_child_element(element, "VARIABLE-INSTANCE")
        if child is not None:
            variable_instance_ref_value = ARObject._deserialize_by_tag(child, "AutosarVariableRef")
            obj.variable_instance_ref = variable_instance_ref_value

        return obj



class InstantiationDataDefPropsBuilder:
    """Builder for InstantiationDataDefProps."""

    def __init__(self) -> None:
        """Initialize builder."""
        self._obj: InstantiationDataDefProps = InstantiationDataDefProps()

    def build(self) -> InstantiationDataDefProps:
        """Build and return InstantiationDataDefProps object.

        Returns:
            InstantiationDataDefProps instance
        """
        # TODO: Add validation
        return self._obj
