"""SwAxisGrouped AUTOSAR element."""

from typing import Optional
import xml.etree.ElementTree as ET
from armodel.serialization import XMLMember

from armodel.models.M2.MSR.DataDictionary.CalibrationParameter.sw_calprm_axis_type_props import (
    SwCalprmAxisTypeProps,
)
from armodel.models.M2.AUTOSARTemplates.GenericStructure.GeneralTemplateClasses.PrimitiveTypes import (
    AxisIndexType,
)
from armodel.models.M2.AUTOSARTemplates.SWComponentTemplate.Datatype.Datatypes.application_primitive_data_type import (
    ApplicationPrimitiveDataType,
)
from armodel.models.M2.MSR.DataDictionary.DatadictionaryProxies.sw_calprm_ref_proxy import (
    SwCalprmRefProxy,
)


class SwAxisGrouped(SwCalprmAxisTypeProps):
    """AUTOSAR SwAxisGrouped."""

    # XML member definitions for this class only (not inherited from parent classes)
    # Format: dict[str, XMLMember] for declarative metadata
    _xml_members: dict[str, "XMLMember"] = {
        "shared_axis_type": XMLMember(
            xml_tag=None,
            is_attribute=False,
            multiplicity="0..1",
            element_class=ApplicationPrimitiveDataType,
        ),  # sharedAxisType
        "sw_axis_index": XMLMember(
            xml_tag=None,
            is_attribute=True,
            multiplicity="0..1",
        ),  # swAxisIndex
        "sw_calprm_ref_proxy": XMLMember(
            xml_tag=None,
            is_attribute=False,
            multiplicity="1",
            element_class=SwCalprmRefProxy,
        ),  # swCalprmRefProxy
    }

    def __init__(self) -> None:
        """Initialize SwAxisGrouped."""
        super().__init__()
        self.shared_axis_type: Optional[ApplicationPrimitiveDataType] = None
        self.sw_axis_index: Optional[AxisIndexType] = None
        self.sw_calprm_ref_proxy: SwCalprmRefProxy = None


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
