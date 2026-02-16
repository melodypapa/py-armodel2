"""SwGenericAxisParam AUTOSAR element."""

from typing import Optional, cast
import xml.etree.ElementTree as ET
from armodel.models.M2.AUTOSARTemplates.GenericStructure.GeneralTemplateClasses.ar_object import ARObject
from armodel.models.M2.MSR.DataDictionary.Axis.sw_generic_axis_param import (
    SwGenericAxisParam,
)


class SwGenericAxisParam(ARObject):
    """AUTOSAR SwGenericAxisParam."""

    # XML member definitions for this class only (not inherited from parent classes)
    # Format: (member_name, xml_tag_name, is_attribute, is_list, element_class)
    _xml_members = [
        ("sw_generic_axis_param", None, False, False, SwGenericAxisParam),  # swGenericAxisParam
    ]

    def __init__(self) -> None:
        """Initialize SwGenericAxisParam."""
        super().__init__()
        self.sw_generic_axis_param: Optional[SwGenericAxisParam] = None

    def serialize(self, namespace: str, element: Optional[ET.Element] = None) -> ET.Element:
        """Convert SwGenericAxisParam to XML element.

        Args:
            namespace: XML namespace for the element
            element: Optional existing element to add members to (for subclass chaining)

        Returns:
            XML element representing this object
        """
        # ARObject.serialize() handles entire class hierarchy automatically
        return super().serialize(namespace, element)

    @classmethod
    def deserialize(cls, element: ET.Element) -> "SwGenericAxisParam":
        """Create SwGenericAxisParam from XML element.

        Args:
            element: XML element to deserialize from

        Returns:
            SwGenericAxisParam instance
        """
        # ARObject.deserialize() handles entire class hierarchy automatically
        obj = super().deserialize(element)
        # Cast to SwGenericAxisParam since parent returns ARObject
        return cast("SwGenericAxisParam", obj)


class SwGenericAxisParamBuilder:
    """Builder for SwGenericAxisParam."""

    def __init__(self) -> None:
        """Initialize builder."""
        self._obj: SwGenericAxisParam = SwGenericAxisParam()

    def build(self) -> SwGenericAxisParam:
        """Build and return SwGenericAxisParam object.

        Returns:
            SwGenericAxisParam instance
        """
        # TODO: Add validation
        return self._obj
