"""SOMEIPTransformationDescription AUTOSAR element."""

from typing import Optional, cast
import xml.etree.ElementTree as ET
from armodel.models.M2.AUTOSARTemplates.SystemTemplate.Transformer.transformation_description import (
    TransformationDescription,
)
from armodel.models.M2.AUTOSARTemplates.GenericStructure.GeneralTemplateClasses.PrimitiveTypes import (
    PositiveInteger,
)


class SOMEIPTransformationDescription(TransformationDescription):
    """AUTOSAR SOMEIPTransformationDescription."""

    # XML member definitions for this class only (not inherited from parent classes)
    # Format: (member_name, xml_tag_name, is_attribute, is_list, element_class)
    _xml_members = [
        ("alignment", None, True, False, None),  # alignment
        ("byte_order", None, False, False, ByteOrderEnum),  # byteOrder
        ("interface_version", None, True, False, None),  # interfaceVersion
    ]

    def __init__(self) -> None:
        """Initialize SOMEIPTransformationDescription."""
        super().__init__()
        self.alignment: Optional[PositiveInteger] = None
        self.byte_order: Optional[ByteOrderEnum] = None
        self.interface_version: Optional[PositiveInteger] = None

    def serialize(self, namespace: str, element: Optional[ET.Element] = None) -> ET.Element:
        """Convert SOMEIPTransformationDescription to XML element.

        Args:
            namespace: XML namespace for the element
            element: Optional existing element to add members to (for subclass chaining)

        Returns:
            XML element representing this object
        """
        # ARObject.serialize() handles entire class hierarchy automatically
        return super().serialize(namespace, element)

    @classmethod
    def deserialize(cls, element: ET.Element) -> "SOMEIPTransformationDescription":
        """Create SOMEIPTransformationDescription from XML element.

        Args:
            element: XML element to deserialize from

        Returns:
            SOMEIPTransformationDescription instance
        """
        # ARObject.deserialize() handles entire class hierarchy automatically
        obj = super().deserialize(element)
        # Cast to SOMEIPTransformationDescription since parent returns ARObject
        return cast("SOMEIPTransformationDescription", obj)


class SOMEIPTransformationDescriptionBuilder:
    """Builder for SOMEIPTransformationDescription."""

    def __init__(self) -> None:
        """Initialize builder."""
        self._obj: SOMEIPTransformationDescription = SOMEIPTransformationDescription()

    def build(self) -> SOMEIPTransformationDescription:
        """Build and return SOMEIPTransformationDescription object.

        Returns:
            SOMEIPTransformationDescription instance
        """
        # TODO: Add validation
        return self._obj
