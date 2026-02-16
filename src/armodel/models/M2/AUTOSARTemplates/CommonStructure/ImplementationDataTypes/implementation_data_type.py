"""ImplementationDataType AUTOSAR element."""

from typing import Optional
import xml.etree.ElementTree as ET
from armodel.serialization import XMLMember

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
    # Format: dict[str, XMLMember] for declarative metadata
    _xml_members: dict[str, "XMLMember"] = {
        "dynamic_array": XMLMember(
            xml_tag=None,
            is_attribute=True,
            multiplicity="0..1",
        ),  # dynamicArray
        "sub_elements": XMLMember(
            xml_tag=None,
            is_attribute=False,
            multiplicity="*",
            element_class=any (ImplementationData),
        ),  # subElements
        "symbol_props": XMLMember(
            xml_tag=None,
            is_attribute=False,
            multiplicity="0..1",
            element_class=SymbolProps,
        ),  # symbolProps
        "type_emitter": XMLMember(
            xml_tag=None,
            is_attribute=True,
            multiplicity="0..1",
        ),  # typeEmitter
    }

    def __init__(self) -> None:
        """Initialize ImplementationDataType."""
        super().__init__()
        self.dynamic_array: Optional[String] = None
        self.sub_elements: list[Any] = []
        self.symbol_props: Optional[SymbolProps] = None
        self.type_emitter: Optional[NameToken] = None


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
