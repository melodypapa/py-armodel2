"""ImplementationDataTypeElement AUTOSAR element.

References:
  - AUTOSAR_CP_TPS_BSWModuleDescriptionTemplate.pdf (page 321)
  - AUTOSAR_CP_TPS_SoftwareComponentTemplate.pdf (page 269)
  - AUTOSAR_CP_TPS_SystemTemplate.pdf (page 2032)
  - AUTOSAR_FO_TPS_GenericStructureTemplate.pdf (page 452)

JSON Source: docs/json/packages/M2_AUTOSARTemplates_CommonStructure_ImplementationDataTypes.classes.json"""

from typing import Optional
import xml.etree.ElementTree as ET
from armodel.serialization import XMLMember

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
    # Format: dict[str, XMLMember] for declarative metadata
    _xml_members: dict[str, "XMLMember"] = {
        "array_impl_policy_enum": XMLMember(
            xml_tag=None,
            is_attribute=False,
            multiplicity="0..1",
            element_class=ArrayImplPolicyEnum,
        ),  # arrayImplPolicyEnum
        "array_size": XMLMember(
            xml_tag=None,
            is_attribute=False,
            multiplicity="0..1",
            element_class=ArraySizeSemanticsEnum,
        ),  # arraySize
        "array_size_handling": XMLMember(
            xml_tag=None,
            is_attribute=False,
            multiplicity="0..1",
            element_class=ArraySizeHandlingEnum,
        ),  # arraySizeHandling
        "is_optional": XMLMember(
            xml_tag=None,
            is_attribute=True,
            multiplicity="0..1",
        ),  # isOptional
        "sub_elements": XMLMember(
            xml_tag=None,
            is_attribute=False,
            multiplicity="*",
            element_class=any (ImplementationData),
        ),  # subElements
        "sw_data_def": XMLMember(
            xml_tag=None,
            is_attribute=False,
            multiplicity="0..1",
            element_class=SwDataDefProps,
        ),  # swDataDef
    }

    def __init__(self) -> None:
        """Initialize ImplementationDataTypeElement."""
        super().__init__()
        self.array_impl_policy_enum: Optional[ArrayImplPolicyEnum] = None
        self.array_size: Optional[ArraySizeSemanticsEnum] = None
        self.array_size_handling: Optional[ArraySizeHandlingEnum] = None
        self.is_optional: Optional[Boolean] = None
        self.sub_elements: list[Any] = []
        self.sw_data_def: Optional[SwDataDefProps] = None


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
