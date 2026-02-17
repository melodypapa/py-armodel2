"""ModeRequestTypeMap AUTOSAR element.

References:
  - AUTOSAR_CP_TPS_BSWModuleDescriptionTemplate.pdf (page 44)
  - AUTOSAR_CP_TPS_SoftwareComponentTemplate.pdf (page 115)

JSON Source: docs/json/packages/M2_AUTOSARTemplates_CommonStructure_ModeDeclaration.classes.json"""

from __future__ import annotations
from typing import TYPE_CHECKING, Optional
import xml.etree.ElementTree as ET

from armodel.models.M2.AUTOSARTemplates.GenericStructure.GeneralTemplateClasses.ArObject.ar_object import ARObject
from armodel.models.M2.AUTOSARTemplates.CommonStructure.ModeDeclaration.mode_declaration_group import (
    ModeDeclarationGroup,
)

if TYPE_CHECKING:
    from armodel.models.M2.AUTOSARTemplates.CommonStructure.ImplementationDataTypes.abstract_implementation_data_type import (
        AbstractImplementationDataType,
    )



class ModeRequestTypeMap(ARObject):
    """AUTOSAR ModeRequestTypeMap."""

    implementation: Optional[AbstractImplementationDataType]
    mode_group: Optional[ModeDeclarationGroup]
    def __init__(self) -> None:
        """Initialize ModeRequestTypeMap."""
        super().__init__()
        self.implementation: Optional[AbstractImplementationDataType] = None
        self.mode_group: Optional[ModeDeclarationGroup] = None


class ModeRequestTypeMapBuilder:
    """Builder for ModeRequestTypeMap."""

    def __init__(self) -> None:
        """Initialize builder."""
        self._obj: ModeRequestTypeMap = ModeRequestTypeMap()

    def build(self) -> ModeRequestTypeMap:
        """Build and return ModeRequestTypeMap object.

        Returns:
            ModeRequestTypeMap instance
        """
        # TODO: Add validation
        return self._obj
