"""ImplementationDataType AUTOSAR element.

References:
  - AUTOSAR_CP_TPS_BSWModuleDescriptionTemplate.pdf (page 320)
  - AUTOSAR_CP_TPS_DiagnosticExtractTemplate.pdf (page 230)
  - AUTOSAR_CP_TPS_ECUConfiguration.pdf (page 299)
  - AUTOSAR_CP_TPS_SoftwareComponentTemplate.pdf (page 268)
  - AUTOSAR_CP_TPS_SystemTemplate.pdf (page 2031)
  - AUTOSAR_FO_TPS_AbstractPlatformSpecification.pdf (page 47)
  - AUTOSAR_FO_TPS_GenericStructureTemplate.pdf (page 451)
  - AUTOSAR_FO_TPS_StandardizationTemplate.pdf (page 193)

JSON Source: docs/json/packages/M2_AUTOSARTemplates_CommonStructure_ImplementationDataTypes.classes.json"""

from __future__ import annotations
from typing import TYPE_CHECKING, Optional
import xml.etree.ElementTree as ET

from armodel.models.M2.AUTOSARTemplates.CommonStructure.ImplementationDataTypes.abstract_implementation_data_type import (
    AbstractImplementationDataType,
)
from armodel.models.M2.AUTOSARTemplates.GenericStructure.GeneralTemplateClasses.ArObject.ar_object import ARObject
from armodel.models.M2.AUTOSARTemplates.GenericStructure.GeneralTemplateClasses.PrimitiveTypes import (
    Boolean,
    NameToken,
    String,
)
from armodel.models.M2.AUTOSARTemplates.CommonStructure.ImplementationDataTypes.implementation_data_type_element import (
    ImplementationDataTypeElement,
)
from armodel.models.M2.AUTOSARTemplates.SWComponentTemplate.Components.symbol_props import (
    SymbolProps,
)


class ImplementationDataType(AbstractImplementationDataType):
    """AUTOSAR ImplementationDataType."""

    @property
    def is_abstract(self) -> bool:
        """Check if this class is abstract.

        Returns:
            False for concrete classes
        """
        return False

    dynamic_array_size_profile: Optional[String]
    is_struct_with_optional_element: Optional[Boolean]
    sub_elements: list[ImplementationDataTypeElement]
    symbol_props: Optional[SymbolProps]
    type_emitter: Optional[NameToken]
    def __init__(self) -> None:
        """Initialize ImplementationDataType."""
        super().__init__()
        self.dynamic_array_size_profile: Optional[String] = None
        self.is_struct_with_optional_element: Optional[Boolean] = None
        self.sub_elements: list[ImplementationDataTypeElement] = []
        self.symbol_props: Optional[SymbolProps] = None
        self.type_emitter: Optional[NameToken] = None
    @classmethod
    def deserialize(cls, element: ET.Element) -> "ImplementationDataType":
        """Deserialize XML element to ImplementationDataType object.

        Args:
            element: XML element to deserialize from

        Returns:
            Deserialized ImplementationDataType object
        """
        # Create instance and initialize with default values
        obj = cls.__new__(cls)
        obj.__init__()

        # Parse dynamic_array_size_profile
        child = ARObject._find_child_element(element, "DYNAMIC-ARRAY-SIZE-PROFILE")
        if child is not None:
            dynamic_array_size_profile_value = child.text
            obj.dynamic_array_size_profile = dynamic_array_size_profile_value

        # Parse is_struct_with_optional_element
        child = ARObject._find_child_element(element, "IS-STRUCT-WITH-OPTIONAL-ELEMENT")
        if child is not None:
            is_struct_with_optional_element_value = child.text
            obj.is_struct_with_optional_element = is_struct_with_optional_element_value

        # Parse sub_elements (list)
        obj.sub_elements = []
        for child in ARObject._find_all_child_elements(element, "SUB-ELEMENTS"):
            sub_elements_value = ARObject._deserialize_by_tag(child, "ImplementationDataTypeElement")
            obj.sub_elements.append(sub_elements_value)

        # Parse symbol_props
        child = ARObject._find_child_element(element, "SYMBOL-PROPS")
        if child is not None:
            symbol_props_value = ARObject._deserialize_by_tag(child, "SymbolProps")
            obj.symbol_props = symbol_props_value

        # Parse type_emitter
        child = ARObject._find_child_element(element, "TYPE-EMITTER")
        if child is not None:
            type_emitter_value = child.text
            obj.type_emitter = type_emitter_value

        return obj



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
