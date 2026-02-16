"""SwAxisType AUTOSAR element."""

from typing import Optional, cast
import xml.etree.ElementTree as ET
from armodel.models.M2.AUTOSARTemplates.GenericStructure.GeneralTemplateClasses.ARPackage.ar_element import (
    ARElement,
)
from armodel.models.M2.MSR.Documentation.BlockElements.documentation_block import (
    DocumentationBlock,
)
from armodel.models.M2.MSR.DataDictionary.Axis.sw_generic_axis_param import (
    SwGenericAxisParam,
)


class SwAxisType(ARElement):
    """AUTOSAR SwAxisType."""

    # XML member definitions for this class only (not inherited from parent classes)
    # Format: (member_name, xml_tag_name, is_attribute, is_list, element_class)
    _xml_members = [
        ("sw_generic_axis", None, False, False, DocumentationBlock),  # swGenericAxis
        ("sw_generic_axis_params", None, False, True, SwGenericAxisParam),  # swGenericAxisParams
    ]

    def __init__(self) -> None:
        """Initialize SwAxisType."""
        super().__init__()
        self.sw_generic_axis: Optional[DocumentationBlock] = None
        self.sw_generic_axis_params: list[SwGenericAxisParam] = []

    def serialize(self, namespace: str, element: Optional[ET.Element] = None) -> ET.Element:
        """Convert SwAxisType to XML element.

        Args:
            namespace: XML namespace for the element
            element: Optional existing element to add members to (for subclass chaining)

        Returns:
            XML element representing this object
        """
        # ARObject.serialize() handles entire class hierarchy automatically
        return super().serialize(namespace, element)

    @classmethod
    def deserialize(cls, element: ET.Element) -> "SwAxisType":
        """Create SwAxisType from XML element.

        Args:
            element: XML element to deserialize from

        Returns:
            SwAxisType instance
        """
        # ARObject.deserialize() handles entire class hierarchy automatically
        obj = super().deserialize(element)
        # Cast to SwAxisType since parent returns ARObject
        return cast("SwAxisType", obj)


class SwAxisTypeBuilder:
    """Builder for SwAxisType."""

    def __init__(self) -> None:
        """Initialize builder."""
        self._obj: SwAxisType = SwAxisType()

    def build(self) -> SwAxisType:
        """Build and return SwAxisType object.

        Returns:
            SwAxisType instance
        """
        # TODO: Add validation
        return self._obj
