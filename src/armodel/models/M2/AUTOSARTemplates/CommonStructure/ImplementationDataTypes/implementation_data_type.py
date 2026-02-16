"""ImplementationDataType AUTOSAR element."""

from typing import Optional, cast
import xml.etree.ElementTree as ET
from armodel.models.M2.AUTOSARTemplates.CommonStructure.ImplementationDataTypes.abstract_implementation_data_type import (
    AbstractImplementationDataType,
)
from armodel.models.M2.AUTOSARTemplates.GenericStructure.GeneralTemplateClasses.PrimitiveTypes import (
    NameToken,
    String,
)
from armodel.models.M2.AUTOSARTemplates.SWComponentTemplate.Components.symbol_props import (
    SymbolProps,
)


class ImplementationDataType(AbstractImplementationDataType):
    """AUTOSAR ImplementationDataType."""

    # XML member definitions for this class only (not inherited from parent classes)
    # Format: (member_name, xml_tag_name, is_attribute, is_list, element_class)
    _xml_members = [
        ("dynamic_array", None, True, False, None),  # dynamicArray
        ("sub_elements", None, False, True, any (ImplementationData)),  # subElements
        ("symbol_props", None, False, False, SymbolProps),  # symbolProps
        ("type_emitter", None, True, False, None),  # typeEmitter
    ]

    def __init__(self) -> None:
        """Initialize ImplementationDataType."""
        super().__init__()
        self.dynamic_array: Optional[String] = None
        self.sub_elements: list[Any] = []
        self.symbol_props: Optional[SymbolProps] = None
        self.type_emitter: Optional[NameToken] = None

    def serialize(self, namespace: str, element: Optional[ET.Element] = None) -> ET.Element:
        """Convert ImplementationDataType to XML element.

        Args:
            namespace: XML namespace for the element
            element: Optional existing element to add members to (for subclass chaining)

        Returns:
            XML element representing this object
        """
        # ARObject.serialize() handles entire class hierarchy automatically
        return super().serialize(namespace, element)

    @classmethod
    def deserialize(cls, element: ET.Element) -> "ImplementationDataType":
        """Create ImplementationDataType from XML element.

        Args:
            element: XML element to deserialize from

        Returns:
            ImplementationDataType instance
        """
        # ARObject.deserialize() handles entire class hierarchy automatically
        obj = super().deserialize(element)
        # Cast to ImplementationDataType since parent returns ARObject
        return cast("ImplementationDataType", obj)


class ImplementationDataTypeBuilder:
    """Builder for ImplementationDataType."""

    def __init__(self) -> None:
        """Initialize builder."""
        self._obj: ImplementationDataType = ImplementationDataType()

    def build(self) -> ImplementationDataType:
        """Build and return ImplementationDataType object.

        Returns:
            ImplementationDataType instance
        """
        # TODO: Add validation
        return self._obj
