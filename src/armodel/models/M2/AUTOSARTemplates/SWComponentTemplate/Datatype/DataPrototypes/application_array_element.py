"""ApplicationArrayElement AUTOSAR element.

References:
  - AUTOSAR_CP_TPS_SoftwareComponentTemplate.pdf (page 252)
  - AUTOSAR_FO_TPS_AbstractPlatformSpecification.pdf (page 43)

JSON Source: docs/json/packages/M2_AUTOSARTemplates_SWComponentTemplate_Datatype_DataPrototypes.classes.json"""

from __future__ import annotations
from typing import TYPE_CHECKING, Optional
import xml.etree.ElementTree as ET

from armodel.models.M2.AUTOSARTemplates.SWComponentTemplate.Datatype.DataPrototypes.application_composite_element_data_prototype import (
    ApplicationCompositeElementDataPrototype,
)
from armodel.models.M2.AUTOSARTemplates.CommonStructure.ImplementationDataTypes import (
    ArraySizeSemanticsEnum,
)
from armodel.models.M2.AUTOSARTemplates.SWComponentTemplate.Datatype.Datatypes import (
    ArraySizeHandlingEnum,
)
from armodel.models.M2.AUTOSARTemplates.GenericStructure.GeneralTemplateClasses.PrimitiveTypes import (
    PositiveInteger,
)

if TYPE_CHECKING:
    from armodel.models.M2.AUTOSARTemplates.SWComponentTemplate.Datatype.Datatypes.application_primitive_data_type import (
        ApplicationPrimitiveDataType,
    )



class ApplicationArrayElement(ApplicationCompositeElementDataPrototype):
    """AUTOSAR ApplicationArrayElement."""

    array_size_handling: Optional[ArraySizeHandlingEnum]
    array_size: Optional[ArraySizeSemanticsEnum]
    index_data_type: Optional[ApplicationPrimitiveDataType]
    max_number_of: Optional[PositiveInteger]
    def __init__(self) -> None:
        """Initialize ApplicationArrayElement."""
        super().__init__()
        self.array_size_handling: Optional[ArraySizeHandlingEnum] = None
        self.array_size: Optional[ArraySizeSemanticsEnum] = None
        self.index_data_type: Optional[ApplicationPrimitiveDataType] = None
        self.max_number_of: Optional[PositiveInteger] = None


class ApplicationArrayElementBuilder:
    """Builder for ApplicationArrayElement."""

    def __init__(self) -> None:
        """Initialize builder."""
        self._obj: ApplicationArrayElement = ApplicationArrayElement()

    def build(self) -> ApplicationArrayElement:
        """Build and return ApplicationArrayElement object.

        Returns:
            ApplicationArrayElement instance
        """
        # TODO: Add validation
        return self._obj
