"""DataTypeMap AUTOSAR element.

References:
  - AUTOSAR_CP_TPS_SoftwareComponentTemplate.pdf (page 232)
  - AUTOSAR_CP_TPS_SystemTemplate.pdf (page 2015)

JSON Source: docs/json/packages/M2_AUTOSARTemplates_SWComponentTemplate_Datatype_Datatypes.classes.json"""

from __future__ import annotations
from typing import TYPE_CHECKING, Optional
import xml.etree.ElementTree as ET

from armodel.models.M2.AUTOSARTemplates.GenericStructure.GeneralTemplateClasses.ArObject.ar_object import ARObject
from armodel.models.M2.AUTOSARTemplates.SWComponentTemplate.Datatype.Datatypes.application_data_type import (
    ApplicationDataType,
)

if TYPE_CHECKING:
    from armodel.models.M2.AUTOSARTemplates.CommonStructure.ImplementationDataTypes.abstract_implementation_data_type import (
        AbstractImplementationDataType,
    )



class DataTypeMap(ARObject):
    """AUTOSAR DataTypeMap."""

    application_data_type: Optional[ApplicationDataType]
    implementation: Optional[AbstractImplementationDataType]
    def __init__(self) -> None:
        """Initialize DataTypeMap."""
        super().__init__()
        self.application_data_type: Optional[ApplicationDataType] = None
        self.implementation: Optional[AbstractImplementationDataType] = None


class DataTypeMapBuilder:
    """Builder for DataTypeMap."""

    def __init__(self) -> None:
        """Initialize builder."""
        self._obj: DataTypeMap = DataTypeMap()

    def build(self) -> DataTypeMap:
        """Build and return DataTypeMap object.

        Returns:
            DataTypeMap instance
        """
        # TODO: Add validation
        return self._obj
