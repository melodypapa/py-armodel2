"""IncludedDataTypeSet AUTOSAR element.

References:
  - AUTOSAR_CP_TPS_SoftwareComponentTemplate.pdf (page 600)

JSON Source: docs/json/packages/M2_AUTOSARTemplates_SWComponentTemplate_SwcInternalBehavior_IncludedDataTypes.classes.json"""

from __future__ import annotations
from typing import TYPE_CHECKING, Optional
import xml.etree.ElementTree as ET

from armodel.models.M2.AUTOSARTemplates.GenericStructure.GeneralTemplateClasses.ArObject.ar_object import ARObject
from armodel.models.M2.AUTOSARTemplates.GenericStructure.GeneralTemplateClasses.PrimitiveTypes import (
    Identifier,
)
from armodel.models.M2.AUTOSARTemplates.SWComponentTemplate.Datatype.Datatypes.autosar_data_type import (
    AutosarDataType,
)


class IncludedDataTypeSet(ARObject):
    """AUTOSAR IncludedDataTypeSet."""

    @property
    def is_abstract(self) -> bool:
        """Check if this class is abstract.

        Returns:
            False for concrete classes
        """
        return False

    data_types: list[AutosarDataType]
    literal_prefix: Optional[Identifier]
    def __init__(self) -> None:
        """Initialize IncludedDataTypeSet."""
        super().__init__()
        self.data_types: list[AutosarDataType] = []
        self.literal_prefix: Optional[Identifier] = None


class IncludedDataTypeSetBuilder:
    """Builder for IncludedDataTypeSet."""

    def __init__(self) -> None:
        """Initialize builder."""
        self._obj: IncludedDataTypeSet = IncludedDataTypeSet()

    def build(self) -> IncludedDataTypeSet:
        """Build and return IncludedDataTypeSet object.

        Returns:
            IncludedDataTypeSet instance
        """
        # TODO: Add validation
        return self._obj
