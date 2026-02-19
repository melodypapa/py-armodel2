"""ParameterAccess AUTOSAR element.

References:
  - AUTOSAR_CP_TPS_BSWModuleDescriptionTemplate.pdf (page 325)
  - AUTOSAR_CP_TPS_SoftwareComponentTemplate.pdf (page 586)

JSON Source: docs/json/packages/M2_AUTOSARTemplates_SWComponentTemplate_SwcInternalBehavior_DataElements.classes.json"""

from __future__ import annotations
from typing import TYPE_CHECKING, Optional
import xml.etree.ElementTree as ET

from armodel.models.M2.AUTOSARTemplates.SWComponentTemplate.SwcInternalBehavior.AccessCount.abstract_access_point import (
    AbstractAccessPoint,
)
from armodel.models.M2.AUTOSARTemplates.GenericStructure.GeneralTemplateClasses.ArObject.ar_object import ARObject
from armodel.models.M2.AUTOSARTemplates.GenericStructure.GeneralTemplateClasses.ArObject.ar_ref import ARRef

if TYPE_CHECKING:
    from armodel.models.M2.AUTOSARTemplates.SWComponentTemplate.SwcInternalBehavior.DataElements.autosar_parameter_ref import (
        AutosarParameterRef,
    )
    from armodel.models.M2.MSR.DataDictionary.DataDefProperties.sw_data_def_props import (
        SwDataDefProps,
    )



class ParameterAccess(AbstractAccessPoint):
    """AUTOSAR ParameterAccess."""

    @property
    def is_abstract(self) -> bool:
        """Check if this class is abstract.

        Returns:
            False for concrete classes
        """
        return False

    accessed_parameter_ref: Optional[ARRef]
    sw_data_def: Optional[SwDataDefProps]
    def __init__(self) -> None:
        """Initialize ParameterAccess."""
        super().__init__()
        self.accessed_parameter_ref: Optional[ARRef] = None
        self.sw_data_def: Optional[SwDataDefProps] = None
    @classmethod
    def deserialize(cls, element: ET.Element) -> "ParameterAccess":
        """Deserialize XML element to ParameterAccess object.

        Args:
            element: XML element to deserialize from

        Returns:
            Deserialized ParameterAccess object
        """
        # First, call parent's deserialize to handle inherited attributes
        obj = super(ParameterAccess, cls).deserialize(element)

        # Parse accessed_parameter_ref
        child = ARObject._find_child_element(element, "ACCESSED-PARAMETER")
        if child is not None:
            accessed_parameter_ref_value = ARObject._deserialize_by_tag(child, "AutosarParameterRef")
            obj.accessed_parameter_ref = accessed_parameter_ref_value

        # Parse sw_data_def
        child = ARObject._find_child_element(element, "SW-DATA-DEF")
        if child is not None:
            sw_data_def_value = ARObject._deserialize_by_tag(child, "SwDataDefProps")
            obj.sw_data_def = sw_data_def_value

        return obj



class ParameterAccessBuilder:
    """Builder for ParameterAccess."""

    def __init__(self) -> None:
        """Initialize builder."""
        self._obj: ParameterAccess = ParameterAccess()

    def build(self) -> ParameterAccess:
        """Build and return ParameterAccess object.

        Returns:
            ParameterAccess instance
        """
        # TODO: Add validation
        return self._obj
