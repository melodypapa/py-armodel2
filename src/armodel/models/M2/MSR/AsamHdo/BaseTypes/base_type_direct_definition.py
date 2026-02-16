"""BaseTypeDirectDefinition AUTOSAR element."""

from typing import Optional
import xml.etree.ElementTree as ET
from armodel.serialization import XMLMember

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
    # Format: dict[str, XMLMember] for declarative metadata
    _xml_members: dict[str, "XMLMember"] = {
        "base_type_encoding": XMLMember(
            xml_tag=None,
            is_attribute=True,
            multiplicity="0..1",
        ),  # baseTypeEncoding
        "base_type_size": XMLMember(
            xml_tag=None,
            is_attribute=True,
            multiplicity="0..1",
        ),  # baseTypeSize
        "byte_order": XMLMember(
            xml_tag=None,
            is_attribute=False,
            multiplicity="0..1",
            element_class=ByteOrderEnum,
        ),  # byteOrder
        "mem_alignment": XMLMember(
            xml_tag=None,
            is_attribute=True,
            multiplicity="0..1",
        ),  # memAlignment
        "native": XMLMember(
            xml_tag=None,
            is_attribute=True,
            multiplicity="0..1",
        ),  # native
    }

    def __init__(self) -> None:
        """Initialize BaseTypeDirectDefinition."""
        super().__init__()
        self.base_type_encoding: Optional[BaseTypeEncodingString] = None
        self.base_type_size: Optional[PositiveInteger] = None
        self.byte_order: Optional[ByteOrderEnum] = None
        self.mem_alignment: Optional[PositiveInteger] = None
        self.native: Optional[NativeDeclarationString] = None


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
