"""TlvDataIdDefinition AUTOSAR element.

References:
  - AUTOSAR_CP_TPS_SystemTemplate.pdf (page 830)

JSON Source: docs/json/packages/M2_AUTOSARTemplates_SystemTemplate_Transformer.classes.json"""

from __future__ import annotations
from typing import TYPE_CHECKING, Optional, Any
import xml.etree.ElementTree as ET

from armodel.models.M2.AUTOSARTemplates.GenericStructure.GeneralTemplateClasses.ArObject.ar_object import ARObject
from armodel.models.M2.AUTOSARTemplates.GenericStructure.GeneralTemplateClasses.PrimitiveTypes import (
    PositiveInteger,
)
from armodel.models.M2.AUTOSARTemplates.CommonStructure.ImplementationDataTypes.abstract_implementation_data_type import (
    AbstractImplementationDataType,
)
from armodel.models.M2.AUTOSARTemplates.SWComponentTemplate.PortInterface.argument_data_prototype import (
    ArgumentDataPrototype,
)


class TlvDataIdDefinition(ARObject):
    """AUTOSAR TlvDataIdDefinition."""

    id: Optional[PositiveInteger]
    tlv_argument: Optional[ArgumentDataPrototype]
    tlv: Optional[AbstractImplementationDataType]
    tlv_record: Optional[Any]
    def __init__(self) -> None:
        """Initialize TlvDataIdDefinition."""
        super().__init__()
        self.id: Optional[PositiveInteger] = None
        self.tlv_argument: Optional[ArgumentDataPrototype] = None
        self.tlv: Optional[AbstractImplementationDataType] = None
        self.tlv_record: Optional[Any] = None


class TlvDataIdDefinitionBuilder:
    """Builder for TlvDataIdDefinition."""

    def __init__(self) -> None:
        """Initialize builder."""
        self._obj: TlvDataIdDefinition = TlvDataIdDefinition()

    def build(self) -> TlvDataIdDefinition:
        """Build and return TlvDataIdDefinition object.

        Returns:
            TlvDataIdDefinition instance
        """
        # TODO: Add validation
        return self._obj
