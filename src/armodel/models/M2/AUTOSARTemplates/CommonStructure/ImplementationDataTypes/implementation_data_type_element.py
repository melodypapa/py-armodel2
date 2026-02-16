"""ImplementationDataTypeElement AUTOSAR element."""

from typing import Optional, cast
import xml.etree.ElementTree as ET
from armodel.models.M2.AUTOSARTemplates.CommonStructure.ImplementationDataTypes.abstract_implementation_data_type_element import (
    AbstractImplementationDataTypeElement,
)
from armodel.models.M2.AUTOSARTemplates.GenericStructure.GeneralTemplateClasses.PrimitiveTypes import (
    Boolean,
)
from armodel.models.M2.MSR.DataDictionary.DataDefProperties.sw_data_def_props import (
    SwDataDefProps,
)


class ImplementationDataTypeElement(AbstractImplementationDataTypeElement):
    """AUTOSAR ImplementationDataTypeElement."""

    # XML member definitions for this class only (not inherited from parent classes)
    # Format: (member_name, xml_tag_name, is_attribute, is_list, element_class)
    _xml_members = [
        ("array_impl_policy_enum", None, False, False, ArrayImplPolicyEnum),  # arrayImplPolicyEnum
        ("array_size", None, False, False, ArraySizeSemanticsEnum),  # arraySize
        ("array_size_handling", None, False, False, ArraySizeHandlingEnum),  # arraySizeHandling
        ("is_optional", None, True, False, None),  # isOptional
        ("sub_elements", None, False, True, any (ImplementationData)),  # subElements
        ("sw_data_def", None, False, False, SwDataDefProps),  # swDataDef
    ]

    def __init__(self) -> None:
        """Initialize ImplementationDataTypeElement."""
        super().__init__()
        self.array_impl_policy_enum: Optional[ArrayImplPolicyEnum] = None
        self.array_size: Optional[ArraySizeSemanticsEnum] = None
        self.array_size_handling: Optional[ArraySizeHandlingEnum] = None
        self.is_optional: Optional[Boolean] = None
        self.sub_elements: list[Any] = []
        self.sw_data_def: Optional[SwDataDefProps] = None

    def serialize(self, namespace: str, element: Optional[ET.Element] = None) -> ET.Element:
        """Convert ImplementationDataTypeElement to XML element.

        Args:
            namespace: XML namespace for the element
            element: Optional existing element to add members to (for subclass chaining)

        Returns:
            XML element representing this object
        """
        # ARObject.serialize() handles entire class hierarchy automatically
        return super().serialize(namespace, element)

    @classmethod
    def deserialize(cls, element: ET.Element) -> "ImplementationDataTypeElement":
        """Create ImplementationDataTypeElement from XML element.

        Args:
            element: XML element to deserialize from

        Returns:
            ImplementationDataTypeElement instance
        """
        # ARObject.deserialize() handles entire class hierarchy automatically
        obj = super().deserialize(element)
        # Cast to ImplementationDataTypeElement since parent returns ARObject
        return cast("ImplementationDataTypeElement", obj)


class ImplementationDataTypeElementBuilder:
    """Builder for ImplementationDataTypeElement."""

    def __init__(self) -> None:
        """Initialize builder."""
        self._obj: ImplementationDataTypeElement = ImplementationDataTypeElement()

    def build(self) -> ImplementationDataTypeElement:
        """Build and return ImplementationDataTypeElement object.

        Returns:
            ImplementationDataTypeElement instance
        """
        # TODO: Add validation
        return self._obj
