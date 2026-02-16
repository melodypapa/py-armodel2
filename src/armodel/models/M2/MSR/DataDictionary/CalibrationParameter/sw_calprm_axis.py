"""SwCalprmAxis AUTOSAR element."""

from typing import Optional, cast
import xml.etree.ElementTree as ET
from armodel.models.M2.AUTOSARTemplates.GenericStructure.GeneralTemplateClasses.ar_object import ARObject
from armodel.models.M2.AUTOSARTemplates.GenericStructure.GeneralTemplateClasses.PrimitiveTypes import (
    AxisIndexType,
    DisplayFormatString,
)
from armodel.models.M2.MSR.DataDictionary.CalibrationParameter.sw_calprm_axis_type_props import (
    SwCalprmAxisTypeProps,
)


class SwCalprmAxis(ARObject):
    """AUTOSAR SwCalprmAxis."""

    # XML member definitions for this class only (not inherited from parent classes)
    # Format: (member_name, xml_tag_name, is_attribute, is_list, element_class)
    _xml_members = [
        ("category", None, False, False, CalprmAxisCategoryEnum),  # category
        ("display_format_string", None, True, False, None),  # displayFormatString
        ("sw_axis_index", None, True, False, None),  # swAxisIndex
        ("sw_calibration_access", None, False, False, SwCalibrationAccessEnum),  # swCalibrationAccess
        ("sw_calprm_axis", None, False, False, SwCalprmAxisTypeProps),  # swCalprmAxis
    ]

    def __init__(self) -> None:
        """Initialize SwCalprmAxis."""
        super().__init__()
        self.category: Optional[CalprmAxisCategoryEnum] = None
        self.display_format_string: Optional[DisplayFormatString] = None
        self.sw_axis_index: Optional[AxisIndexType] = None
        self.sw_calibration_access: Optional[SwCalibrationAccessEnum] = None
        self.sw_calprm_axis: Optional[SwCalprmAxisTypeProps] = None

    def serialize(self, namespace: str, element: Optional[ET.Element] = None) -> ET.Element:
        """Convert SwCalprmAxis to XML element.

        Args:
            namespace: XML namespace for the element
            element: Optional existing element to add members to (for subclass chaining)

        Returns:
            XML element representing this object
        """
        # ARObject.serialize() handles entire class hierarchy automatically
        return super().serialize(namespace, element)

    @classmethod
    def deserialize(cls, element: ET.Element) -> "SwCalprmAxis":
        """Create SwCalprmAxis from XML element.

        Args:
            element: XML element to deserialize from

        Returns:
            SwCalprmAxis instance
        """
        # ARObject.deserialize() handles entire class hierarchy automatically
        obj = super().deserialize(element)
        # Cast to SwCalprmAxis since parent returns ARObject
        return cast("SwCalprmAxis", obj)


class SwCalprmAxisBuilder:
    """Builder for SwCalprmAxis."""

    def __init__(self) -> None:
        """Initialize builder."""
        self._obj: SwCalprmAxis = SwCalprmAxis()

    def build(self) -> SwCalprmAxis:
        """Build and return SwCalprmAxis object.

        Returns:
            SwCalprmAxis instance
        """
        # TODO: Add validation
        return self._obj
