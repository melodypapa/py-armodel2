"""SwTextProps AUTOSAR element."""

from typing import Optional, cast
import xml.etree.ElementTree as ET
from armodel.models.M2.AUTOSARTemplates.GenericStructure.GeneralTemplateClasses.ar_object import ARObject
from armodel.models.M2.AUTOSARTemplates.GenericStructure.GeneralTemplateClasses.PrimitiveTypes import (
    Integer,
)
from armodel.models.M2.MSR.AsamHdo.BaseTypes.sw_base_type import (
    SwBaseType,
)


class SwTextProps(ARObject):
    """AUTOSAR SwTextProps."""

    # XML member definitions for this class only (not inherited from parent classes)
    # Format: (member_name, xml_tag_name, is_attribute, is_list, element_class)
    _xml_members = [
        ("array_size", None, False, False, ArraySizeSemanticsEnum),  # arraySize
        ("base_type", None, False, False, SwBaseType),  # baseType
        ("sw_fill_character", None, True, False, None),  # swFillCharacter
        ("sw_max_text_size", None, True, False, None),  # swMaxTextSize
    ]

    def __init__(self) -> None:
        """Initialize SwTextProps."""
        super().__init__()
        self.array_size: Optional[ArraySizeSemanticsEnum] = None
        self.base_type: Optional[SwBaseType] = None
        self.sw_fill_character: Optional[Integer] = None
        self.sw_max_text_size: Optional[Integer] = None

    def serialize(self, namespace: str, element: Optional[ET.Element] = None) -> ET.Element:
        """Convert SwTextProps to XML element.

        Args:
            namespace: XML namespace for the element
            element: Optional existing element to add members to (for subclass chaining)

        Returns:
            XML element representing this object
        """
        # ARObject.serialize() handles entire class hierarchy automatically
        return super().serialize(namespace, element)

    @classmethod
    def deserialize(cls, element: ET.Element) -> "SwTextProps":
        """Create SwTextProps from XML element.

        Args:
            element: XML element to deserialize from

        Returns:
            SwTextProps instance
        """
        # ARObject.deserialize() handles entire class hierarchy automatically
        obj = super().deserialize(element)
        # Cast to SwTextProps since parent returns ARObject
        return cast("SwTextProps", obj)


class SwTextPropsBuilder:
    """Builder for SwTextProps."""

    def __init__(self) -> None:
        """Initialize builder."""
        self._obj: SwTextProps = SwTextProps()

    def build(self) -> SwTextProps:
        """Build and return SwTextProps object.

        Returns:
            SwTextProps instance
        """
        # TODO: Add validation
        return self._obj
