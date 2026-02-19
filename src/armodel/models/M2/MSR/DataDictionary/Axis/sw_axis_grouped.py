"""SwAxisGrouped AUTOSAR element.

References:
  - AUTOSAR_CP_TPS_SoftwareComponentTemplate.pdf (page 357)

JSON Source: docs/json/packages/M2_MSR_DataDictionary_Axis.classes.json"""

from __future__ import annotations
from typing import TYPE_CHECKING, Optional
import xml.etree.ElementTree as ET

from armodel.models.M2.MSR.DataDictionary.CalibrationParameter.sw_calprm_axis_type_props import (
    SwCalprmAxisTypeProps,
)
from armodel.models.M2.AUTOSARTemplates.GenericStructure.GeneralTemplateClasses.ArObject.ar_object import ARObject
from armodel.models.M2.AUTOSARTemplates.GenericStructure.GeneralTemplateClasses.ArObject.ar_ref import ARRef
from armodel.models.M2.MSR.DataDictionary.RecordLayout import (
    AxisIndexType,
)
from armodel.models.M2.MSR.DataDictionary.DatadictionaryProxies.sw_calprm_ref_proxy import (
    SwCalprmRefProxy,
)

if TYPE_CHECKING:
    from armodel.models.M2.AUTOSARTemplates.SWComponentTemplate.Datatype.Datatypes.application_primitive_data_type import (
        ApplicationPrimitiveDataType,
    )



class SwAxisGrouped(SwCalprmAxisTypeProps):
    """AUTOSAR SwAxisGrouped."""

    @property
    def is_abstract(self) -> bool:
        """Check if this class is abstract.

        Returns:
            False for concrete classes
        """
        return False

    shared_axis_type: Optional[ApplicationPrimitiveDataType]
    sw_axis_index: Optional[AxisIndexType]
    sw_calprm_ref_proxy_ref: ARRef
    def __init__(self) -> None:
        """Initialize SwAxisGrouped."""
        super().__init__()
        self.shared_axis_type: Optional[ApplicationPrimitiveDataType] = None
        self.sw_axis_index: Optional[AxisIndexType] = None
        self.sw_calprm_ref_proxy_ref: ARRef = None
    @classmethod
    def deserialize(cls, element: ET.Element) -> "SwAxisGrouped":
        """Deserialize XML element to SwAxisGrouped object.

        Args:
            element: XML element to deserialize from

        Returns:
            Deserialized SwAxisGrouped object
        """
        # Create instance and initialize with default values
        obj = cls.__new__(cls)
        obj.__init__()

        # Parse shared_axis_type
        child = ARObject._find_child_element(element, "SHARED-AXIS-TYPE")
        if child is not None:
            shared_axis_type_value = ARObject._deserialize_by_tag(child, "ApplicationPrimitiveDataType")
            obj.shared_axis_type = shared_axis_type_value

        # Parse sw_axis_index
        child = ARObject._find_child_element(element, "SW-AXIS-INDEX")
        if child is not None:
            sw_axis_index_value = child.text
            obj.sw_axis_index = sw_axis_index_value

        # Parse sw_calprm_ref_proxy_ref
        child = ARObject._find_child_element(element, "SW-CALPRM-REF-PROXY")
        if child is not None:
            sw_calprm_ref_proxy_ref_value = ARObject._deserialize_by_tag(child, "SwCalprmRefProxy")
            obj.sw_calprm_ref_proxy_ref = sw_calprm_ref_proxy_ref_value

        return obj



class SwAxisGroupedBuilder:
    """Builder for SwAxisGrouped."""

    def __init__(self) -> None:
        """Initialize builder."""
        self._obj: SwAxisGrouped = SwAxisGrouped()

    def build(self) -> SwAxisGrouped:
        """Build and return SwAxisGrouped object.

        Returns:
            SwAxisGrouped instance
        """
        # TODO: Add validation
        return self._obj
