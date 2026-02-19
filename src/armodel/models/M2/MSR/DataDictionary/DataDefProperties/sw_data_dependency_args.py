"""SwDataDependencyArgs AUTOSAR element.

References:
  - AUTOSAR_CP_TPS_SoftwareComponentTemplate.pdf (page 374)

JSON Source: docs/json/packages/M2_MSR_DataDictionary_DataDefProperties.classes.json"""

from __future__ import annotations
from typing import TYPE_CHECKING, Optional
import xml.etree.ElementTree as ET

from armodel.models.M2.AUTOSARTemplates.GenericStructure.GeneralTemplateClasses.ArObject.ar_object import ARObject
from armodel.models.M2.AUTOSARTemplates.GenericStructure.GeneralTemplateClasses.ArObject.ar_ref import ARRef
from armodel.models.M2.MSR.DataDictionary.DatadictionaryProxies.sw_calprm_ref_proxy import (
    SwCalprmRefProxy,
)
from armodel.models.M2.MSR.DataDictionary.DatadictionaryProxies.sw_variable_ref_proxy import (
    SwVariableRefProxy,
)


class SwDataDependencyArgs(ARObject):
    """AUTOSAR SwDataDependencyArgs."""

    @property
    def is_abstract(self) -> bool:
        """Check if this class is abstract.

        Returns:
            False for concrete classes
        """
        return False

    sw_calprm_ref_proxy_ref: Optional[ARRef]
    sw_variable_ref_proxy_ref: Optional[ARRef]
    def __init__(self) -> None:
        """Initialize SwDataDependencyArgs."""
        super().__init__()
        self.sw_calprm_ref_proxy_ref: Optional[ARRef] = None
        self.sw_variable_ref_proxy_ref: Optional[ARRef] = None
    @classmethod
    def deserialize(cls, element: ET.Element) -> "SwDataDependencyArgs":
        """Deserialize XML element to SwDataDependencyArgs object.

        Args:
            element: XML element to deserialize from

        Returns:
            Deserialized SwDataDependencyArgs object
        """
        # Create instance and initialize with default values
        obj = cls.__new__(cls)
        obj.__init__()

        # Parse sw_calprm_ref_proxy_ref
        child = ARObject._find_child_element(element, "SW-CALPRM-REF-PROXY")
        if child is not None:
            sw_calprm_ref_proxy_ref_value = ARObject._deserialize_by_tag(child, "SwCalprmRefProxy")
            obj.sw_calprm_ref_proxy_ref = sw_calprm_ref_proxy_ref_value

        # Parse sw_variable_ref_proxy_ref
        child = ARObject._find_child_element(element, "SW-VARIABLE-REF-PROXY")
        if child is not None:
            sw_variable_ref_proxy_ref_value = ARObject._deserialize_by_tag(child, "SwVariableRefProxy")
            obj.sw_variable_ref_proxy_ref = sw_variable_ref_proxy_ref_value

        return obj



class SwDataDependencyArgsBuilder:
    """Builder for SwDataDependencyArgs."""

    def __init__(self) -> None:
        """Initialize builder."""
        self._obj: SwDataDependencyArgs = SwDataDependencyArgs()

    def build(self) -> SwDataDependencyArgs:
        """Build and return SwDataDependencyArgs object.

        Returns:
            SwDataDependencyArgs instance
        """
        # TODO: Add validation
        return self._obj
