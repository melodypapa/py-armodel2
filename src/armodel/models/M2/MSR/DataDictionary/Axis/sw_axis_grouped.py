"""SwAxisGrouped AUTOSAR element."""

from typing import Optional, cast
import xml.etree.ElementTree as ET
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
    # Format: (member_name, xml_tag_name, is_attribute, is_list, element_class)
    _xml_members = [
        ("shared_axis_type", None, False, False, ApplicationPrimitiveDataType),  # sharedAxisType
        ("sw_axis_index", None, True, False, None),  # swAxisIndex
        ("sw_calprm_ref_proxy", None, False, False, SwCalprmRefProxy),  # swCalprmRefProxy
    ]

    def __init__(self) -> None:
        """Initialize SwAxisGrouped."""
        super().__init__()
        self.shared_axis_type: Optional[ApplicationPrimitiveDataType] = None
        self.sw_axis_index: Optional[AxisIndexType] = None
        self.sw_calprm_ref_proxy: SwCalprmRefProxy = None

    def serialize(self, namespace: str, element: Optional[ET.Element] = None) -> ET.Element:
        """Convert SwAxisGrouped to XML element.

        Args:
            namespace: XML namespace for the element
            element: Optional existing element to add members to (for subclass chaining)

        Returns:
            XML element representing this object
        """
        # ARObject.serialize() handles entire class hierarchy automatically
        return super().serialize(namespace, element)

    @classmethod
    def deserialize(cls, element: ET.Element) -> "SwAxisGrouped":
        """Create SwAxisGrouped from XML element.

        Args:
            element: XML element to deserialize from

        Returns:
            SwAxisGrouped instance
        """
        # ARObject.deserialize() handles entire class hierarchy automatically
        obj = super().deserialize(element)
        # Cast to SwAxisGrouped since parent returns ARObject
        return cast("SwAxisGrouped", obj)


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
