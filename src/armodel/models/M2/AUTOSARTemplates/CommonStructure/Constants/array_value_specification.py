"""ArrayValueSpecification AUTOSAR element.

References:
  - AUTOSAR_CP_TPS_BSWModuleDescriptionTemplate.pdf (page 303)
  - AUTOSAR_CP_TPS_SoftwareComponentTemplate.pdf (page 434)
  - AUTOSAR_CP_TPS_SystemTemplate.pdf (page 1999)

JSON Source: docs/json/packages/M2_AUTOSARTemplates_CommonStructure_Constants.classes.json"""

from __future__ import annotations
from typing import TYPE_CHECKING, Optional
import xml.etree.ElementTree as ET

from armodel.models.M2.AUTOSARTemplates.CommonStructure.Constants.composite_value_specification import (
    CompositeValueSpecification,
)
from armodel.models.M2.AUTOSARTemplates.GenericStructure.GeneralTemplateClasses.PrimitiveTypes import (
    PositiveInteger,
)

if TYPE_CHECKING:
    from armodel.models.M2.AUTOSARTemplates.CommonStructure.Constants.value_specification import (
        ValueSpecification,
    )



class ArrayValueSpecification(CompositeValueSpecification):
    """AUTOSAR ArrayValueSpecification."""

    elements: list[ValueSpecification]
    intended_partial: Optional[PositiveInteger]
    def __init__(self) -> None:
        """Initialize ArrayValueSpecification."""
        super().__init__()
        self.elements: list[ValueSpecification] = []
        self.intended_partial: Optional[PositiveInteger] = None


class ArrayValueSpecificationBuilder:
    """Builder for ArrayValueSpecification."""

    def __init__(self) -> None:
        """Initialize builder."""
        self._obj: ArrayValueSpecification = ArrayValueSpecification()

    def build(self) -> ArrayValueSpecification:
        """Build and return ArrayValueSpecification object.

        Returns:
            ArrayValueSpecification instance
        """
        # TODO: Add validation
        return self._obj
