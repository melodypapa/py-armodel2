"""SOMEIPTransformationProps AUTOSAR element."""

from typing import Optional, cast
import xml.etree.ElementTree as ET
from armodel.models.M2.AUTOSARTemplates.SystemTemplate.Transformer.transformation_props import (
    TransformationProps,
)
from armodel.models.M2.AUTOSARTemplates.GenericStructure.GeneralTemplateClasses.PrimitiveTypes import (
    PositiveInteger,
)


class SOMEIPTransformationProps(TransformationProps):
    """AUTOSAR SOMEIPTransformationProps."""

    # XML member definitions for this class only (not inherited from parent classes)
    # Format: (member_name, xml_tag_name, is_attribute, is_list, element_class)
    _xml_members = [
        ("alignment", None, True, False, None),  # alignment
        ("size_of_array", None, True, False, None),  # sizeOfArray
        ("size_of_string", None, True, False, None),  # sizeOfString
        ("size_of_struct", None, True, False, None),  # sizeOfStruct
        ("size_of_union", None, True, False, None),  # sizeOfUnion
    ]

    def __init__(self) -> None:
        """Initialize SOMEIPTransformationProps."""
        super().__init__()
        self.alignment: Optional[PositiveInteger] = None
        self.size_of_array: Optional[PositiveInteger] = None
        self.size_of_string: Optional[PositiveInteger] = None
        self.size_of_struct: Optional[PositiveInteger] = None
        self.size_of_union: Optional[PositiveInteger] = None

    def serialize(self, namespace: str, element: Optional[ET.Element] = None) -> ET.Element:
        """Convert SOMEIPTransformationProps to XML element.

        Args:
            namespace: XML namespace for the element
            element: Optional existing element to add members to (for subclass chaining)

        Returns:
            XML element representing this object
        """
        # ARObject.serialize() handles entire class hierarchy automatically
        return super().serialize(namespace, element)

    @classmethod
    def deserialize(cls, element: ET.Element) -> "SOMEIPTransformationProps":
        """Create SOMEIPTransformationProps from XML element.

        Args:
            element: XML element to deserialize from

        Returns:
            SOMEIPTransformationProps instance
        """
        # ARObject.deserialize() handles entire class hierarchy automatically
        obj = super().deserialize(element)
        # Cast to SOMEIPTransformationProps since parent returns ARObject
        return cast("SOMEIPTransformationProps", obj)


class SOMEIPTransformationPropsBuilder:
    """Builder for SOMEIPTransformationProps."""

    def __init__(self) -> None:
        """Initialize builder."""
        self._obj: SOMEIPTransformationProps = SOMEIPTransformationProps()

    def build(self) -> SOMEIPTransformationProps:
        """Build and return SOMEIPTransformationProps object.

        Returns:
            SOMEIPTransformationProps instance
        """
        # TODO: Add validation
        return self._obj
