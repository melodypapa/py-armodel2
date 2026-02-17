"""ImplementationDataTypeElement AUTOSAR element.

References:
  - AUTOSAR_CP_TPS_BSWModuleDescriptionTemplate.pdf (page 321)
  - AUTOSAR_CP_TPS_SoftwareComponentTemplate.pdf (page 269)
  - AUTOSAR_CP_TPS_SystemTemplate.pdf (page 2032)
  - AUTOSAR_FO_TPS_GenericStructureTemplate.pdf (page 452)

JSON Source: docs/json/packages/M2_AUTOSARTemplates_CommonStructure_ImplementationDataTypes.classes.json"""

from __future__ import annotations
from typing import TYPE_CHECKING, Optional, Any
import xml.etree.ElementTree as ET

from armodel.models.M2.AUTOSARTemplates.CommonStructure.ImplementationDataTypes.abstract_implementation_data_type_element import (
    AbstractImplementationDataTypeElement,
)
from armodel.models.M2.AUTOSARTemplates.CommonStructure.ImplementationDataTypes import (
    ArrayImplPolicyEnum,
    ArraySizeSemanticsEnum,
)
from armodel.models.M2.AUTOSARTemplates.SWComponentTemplate.Datatype.Datatypes import (
    ArraySizeHandlingEnum,
)
from armodel.models.M2.AUTOSARTemplates.GenericStructure.GeneralTemplateClasses.PrimitiveTypes import (
    Boolean,
)
from armodel.models.M2.MSR.DataDictionary.DataDefProperties.sw_data_def_props import (
    SwDataDefProps,
)


class ImplementationDataTypeElement(AbstractImplementationDataTypeElement):
    """AUTOSAR ImplementationDataTypeElement."""

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
