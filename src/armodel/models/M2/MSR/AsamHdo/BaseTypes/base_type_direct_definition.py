"""BaseTypeDirectDefinition AUTOSAR element.

References:
  - AUTOSAR_CP_TPS_DiagnosticExtractTemplate.pdf (page 302)
  - AUTOSAR_CP_TPS_SoftwareComponentTemplate.pdf (page 290)
  - AUTOSAR_CP_TPS_SystemTemplate.pdf (page 2002)
  - AUTOSAR_FO_TPS_LogAndTraceExtract.pdf (page 29)

JSON Source: docs/json/packages/M2_MSR_AsamHdo_BaseTypes.classes.json"""

from __future__ import annotations
from typing import TYPE_CHECKING, Optional
import xml.etree.ElementTree as ET

from armodel.models.M2.MSR.AsamHdo.BaseTypes.base_type_definition import (
    BaseTypeDefinition,
)
from armodel.models.M2.AUTOSARTemplates.GenericStructure.GeneralTemplateClasses.PrimitiveTypes import (
    ByteOrderEnum,
)
from armodel.models.M2.AUTOSARTemplates.GenericStructure.GeneralTemplateClasses.PrimitiveTypes import (
    NativeDeclarationString,
    PositiveInteger,
)
from armodel.models.M2.MSR.AsamHdo.BaseTypes import (
    BaseTypeEncodingString,
)


class BaseTypeDirectDefinition(BaseTypeDefinition):
    """AUTOSAR BaseTypeDirectDefinition."""

    base_type_encoding: Optional[BaseTypeEncodingString]
    base_type_size: Optional[PositiveInteger]
    byte_order: Optional[ByteOrderEnum]
    mem_alignment: Optional[PositiveInteger]
    native: Optional[NativeDeclarationString]
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
