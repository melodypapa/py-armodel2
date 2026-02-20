"""SOMEIPTransformationISignalProps AUTOSAR element.

References:
  - AUTOSAR_CP_TPS_SystemTemplate.pdf (page 778)

JSON Source: docs/json/packages/M2_AUTOSARTemplates_SystemTemplate_Transformer.classes.json"""

from __future__ import annotations
from typing import TYPE_CHECKING, Optional
import xml.etree.ElementTree as ET
from armodel.serialization.decorators import atp_variant

from armodel.models.M2.AUTOSARTemplates.GenericStructure.GeneralTemplateClasses.ArObject.ar_object import ARObject
from armodel.models.M2.AUTOSARTemplates.GenericStructure.GeneralTemplateClasses.ArObject.ar_ref import ARRef
from armodel.models.M2.AUTOSARTemplates.SystemTemplate.Transformer import (
    SOMEIPMessageTypeEnum,
)
from armodel.models.M2.AUTOSARTemplates.GenericStructure.GeneralTemplateClasses.PrimitiveTypes import (
    Boolean,
    PositiveInteger,
)
from armodel.models.M2.AUTOSARTemplates.SystemTemplate.Transformer.tlv_data_id_definition_set import (
    TlvDataIdDefinitionSet,
)


@atp_variant()

class SOMEIPTransformationISignalProps(ARObject):
    """AUTOSAR SOMEIPTransformationISignalProps."""

    @property
    def is_abstract(self) -> bool:
        """Check if this class is abstract.

        Returns:
            False for concrete classes
        """
        return False

    implements: Optional[Boolean]
    interface_version: Optional[PositiveInteger]
    is_dynamic: Optional[Boolean]
    message_type: Optional[SOMEIPMessageTypeEnum]
    size_of_array: Optional[PositiveInteger]
    size_of_string: Optional[PositiveInteger]
    size_of_struct: Optional[PositiveInteger]
    size_of_union: Optional[PositiveInteger]
    tlv_data_id_refs: list[ARRef]
    def __init__(self) -> None:
        """Initialize SOMEIPTransformationISignalProps."""
        super().__init__()
        self.implements: Optional[Boolean] = None
        self.interface_version: Optional[PositiveInteger] = None
        self.is_dynamic: Optional[Boolean] = None
        self.message_type: Optional[SOMEIPMessageTypeEnum] = None
        self.size_of_array: Optional[PositiveInteger] = None
        self.size_of_string: Optional[PositiveInteger] = None
        self.size_of_struct: Optional[PositiveInteger] = None
        self.size_of_union: Optional[PositiveInteger] = None
        self.tlv_data_id_refs: list[ARRef] = []



class SOMEIPTransformationISignalPropsBuilder:
    """Builder for SOMEIPTransformationISignalProps."""

    def __init__(self) -> None:
        """Initialize builder."""
        self._obj: SOMEIPTransformationISignalProps = SOMEIPTransformationISignalProps()

    def build(self) -> SOMEIPTransformationISignalProps:
        """Build and return SOMEIPTransformationISignalProps object.

        Returns:
            SOMEIPTransformationISignalProps instance
        """
        # TODO: Add validation
        return self._obj
