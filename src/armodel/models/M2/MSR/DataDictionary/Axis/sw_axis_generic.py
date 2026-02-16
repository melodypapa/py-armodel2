"""SwAxisGeneric AUTOSAR element."""

from typing import Optional, cast
import xml.etree.ElementTree as ET
from armodel.models.M2.AUTOSARTemplates.GenericStructure.GeneralTemplateClasses.ar_object import ARObject
from armodel.models.M2.MSR.DataDictionary.Axis.sw_axis_type import (
    SwAxisType,
)
from armodel.models.M2.MSR.DataDictionary.Axis.sw_generic_axis_param import (
    SwGenericAxisParam,
)


class SwAxisGeneric(ARObject):
    """AUTOSAR SwAxisGeneric."""

    # XML member definitions for this class only (not inherited from parent classes)
    # Format: (member_name, xml_tag_name, is_attribute, is_list, element_class)
    _xml_members = [
        ("sw_axis_type", None, False, False, SwAxisType),  # swAxisType
        ("sw_generic_axis_params", None, False, True, SwGenericAxisParam),  # swGenericAxisParams
    ]

    def __init__(self) -> None:
        """Initialize SwAxisGeneric."""
        super().__init__()
        self.sw_axis_type: Optional[SwAxisType] = None
        self.sw_generic_axis_params: list[SwGenericAxisParam] = []

    def serialize(self, namespace: str, element: Optional[ET.Element] = None) -> ET.Element:
        """Convert SwAxisGeneric to XML element.

        Args:
            namespace: XML namespace for the element
            element: Optional existing element to add members to (for subclass chaining)

        Returns:
            XML element representing this object
        """
        # ARObject.serialize() handles entire class hierarchy automatically
        return super().serialize(namespace, element)

    @classmethod
    def deserialize(cls, element: ET.Element) -> "SwAxisGeneric":
        """Create SwAxisGeneric from XML element.

        Args:
            element: XML element to deserialize from

        Returns:
            SwAxisGeneric instance
        """
        # ARObject.deserialize() handles entire class hierarchy automatically
        obj = super().deserialize(element)
        # Cast to SwAxisGeneric since parent returns ARObject
        return cast("SwAxisGeneric", obj)


class SwAxisGenericBuilder:
    """Builder for SwAxisGeneric."""

    def __init__(self) -> None:
        """Initialize builder."""
        self._obj: SwAxisGeneric = SwAxisGeneric()

    def build(self) -> SwAxisGeneric:
        """Build and return SwAxisGeneric object.

        Returns:
            SwAxisGeneric instance
        """
        # TODO: Add validation
        return self._obj
