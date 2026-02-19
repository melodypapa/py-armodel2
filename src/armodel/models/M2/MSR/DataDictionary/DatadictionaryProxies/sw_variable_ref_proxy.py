"""SwVariableRefProxy AUTOSAR element.

References:
  - AUTOSAR_CP_TPS_SoftwareComponentTemplate.pdf (page 370)

JSON Source: docs/json/packages/M2_MSR_DataDictionary_DatadictionaryProxies.classes.json"""

from __future__ import annotations
from typing import TYPE_CHECKING, Optional
import xml.etree.ElementTree as ET

from armodel.models.M2.AUTOSARTemplates.GenericStructure.GeneralTemplateClasses.ArObject.ar_object import ARObject
from armodel.models.M2.AUTOSARTemplates.GenericStructure.GeneralTemplateClasses.ArObject.ar_ref import ARRef
from armodel.models.M2.AUTOSARTemplates.SWComponentTemplate.SwcInternalBehavior.DataElements.autosar_variable_ref import (
    AutosarVariableRef,
)

if TYPE_CHECKING:
    from armodel.models.M2.AUTOSARTemplates.CommonStructure.MeasurementCalibrationSupport.mc_data_instance import (
        McDataInstance,
    )



class SwVariableRefProxy(ARObject):
    """AUTOSAR SwVariableRefProxy."""

    @property
    def is_abstract(self) -> bool:
        """Check if this class is abstract.

        Returns:
            False for concrete classes
        """
        return False

    autosar_variable_ref: Optional[ARRef]
    mc_data_instance: Optional[McDataInstance]
    def __init__(self) -> None:
        """Initialize SwVariableRefProxy."""
        super().__init__()
        self.autosar_variable_ref: Optional[ARRef] = None
        self.mc_data_instance: Optional[McDataInstance] = None
    @classmethod
    def deserialize(cls, element: ET.Element) -> "SwVariableRefProxy":
        """Deserialize XML element to SwVariableRefProxy object.

        Args:
            element: XML element to deserialize from

        Returns:
            Deserialized SwVariableRefProxy object
        """
        # Create instance and initialize with default values
        obj = cls.__new__(cls)
        obj.__init__()

        # Parse autosar_variable_ref
        child = ARObject._find_child_element(element, "AUTOSAR-VARIABLE-REF")
        if child is not None:
            autosar_variable_ref_value = ARObject._deserialize_by_tag(child, "AutosarVariableRef")
            obj.autosar_variable_ref = autosar_variable_ref_value

        # Parse mc_data_instance
        child = ARObject._find_child_element(element, "MC-DATA-INSTANCE")
        if child is not None:
            mc_data_instance_value = ARObject._deserialize_by_tag(child, "McDataInstance")
            obj.mc_data_instance = mc_data_instance_value

        return obj



class SwVariableRefProxyBuilder:
    """Builder for SwVariableRefProxy."""

    def __init__(self) -> None:
        """Initialize builder."""
        self._obj: SwVariableRefProxy = SwVariableRefProxy()

    def build(self) -> SwVariableRefProxy:
        """Build and return SwVariableRefProxy object.

        Returns:
            SwVariableRefProxy instance
        """
        # TODO: Add validation
        return self._obj
