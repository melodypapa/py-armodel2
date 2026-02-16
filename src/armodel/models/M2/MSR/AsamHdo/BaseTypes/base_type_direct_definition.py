"""BaseTypeDirectDefinition AUTOSAR element."""

from typing import Optional, cast
import xml.etree.ElementTree as ET
from armodel.models.M2.MSR.AsamHdo.BaseTypes.base_type_definition import (
    BaseTypeDefinition,
)
from armodel.models.M2.AUTOSARTemplates.GenericStructure.GeneralTemplateClasses.PrimitiveTypes import (
    BaseTypeEncodingString,
    NativeDeclarationString,
    PositiveInteger,
)


class BaseTypeDirectDefinition(BaseTypeDefinition):
    """AUTOSAR BaseTypeDirectDefinition."""

    # XML member definitions for this class only (not inherited from parent classes)
    # Format: (member_name, xml_tag_name, is_attribute, is_list, element_class)
    _xml_members = [
        ("base_type_encoding", None, True, False, None),  # baseTypeEncoding
        ("base_type_size", None, True, False, None),  # baseTypeSize
        ("byte_order", None, False, False, ByteOrderEnum),  # byteOrder
        ("mem_alignment", None, True, False, None),  # memAlignment
        ("native", None, True, False, None),  # native
    ]

    def __init__(self) -> None:
        """Initialize BaseTypeDirectDefinition."""
        super().__init__()
        self.base_type_encoding: Optional[BaseTypeEncodingString] = None
        self.base_type_size: Optional[PositiveInteger] = None
        self.byte_order: Optional[ByteOrderEnum] = None
        self.mem_alignment: Optional[PositiveInteger] = None
        self.native: Optional[NativeDeclarationString] = None

    def serialize(self, namespace: str, element: Optional[ET.Element] = None) -> ET.Element:
        """Convert BaseTypeDirectDefinition to XML element.

        Args:
            namespace: XML namespace for the element
            element: Optional existing element to add members to (for subclass chaining)

        Returns:
            XML element representing this object
        """
        # ARObject.serialize() handles entire class hierarchy automatically
        return super().serialize(namespace, element)

    @classmethod
    def deserialize(cls, element: ET.Element) -> "BaseTypeDirectDefinition":
        """Create BaseTypeDirectDefinition from XML element.

        Args:
            element: XML element to deserialize from

        Returns:
            BaseTypeDirectDefinition instance
        """
        # ARObject.deserialize() handles entire class hierarchy automatically
        obj = super().deserialize(element)
        # Cast to BaseTypeDirectDefinition since parent returns ARObject
        return cast("BaseTypeDirectDefinition", obj)


class BaseTypeDirectDefinitionBuilder:
    """Builder for BaseTypeDirectDefinition."""

    def __init__(self) -> None:
        """Initialize builder."""
        self._obj: BaseTypeDirectDefinition = BaseTypeDirectDefinition()

    def build(self) -> BaseTypeDirectDefinition:
        """Build and return BaseTypeDirectDefinition object.

        Returns:
            BaseTypeDirectDefinition instance
        """
        # TODO: Add validation
        return self._obj
