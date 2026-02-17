"""ReferenceValueSpecification AUTOSAR element.

References:
  - AUTOSAR_CP_TPS_SoftwareComponentTemplate.pdf (page 436)

JSON Source: docs/json/packages/M2_AUTOSARTemplates_CommonStructure_Constants.classes.json"""

from __future__ import annotations
from typing import TYPE_CHECKING, Optional
import xml.etree.ElementTree as ET

from armodel.models.M2.AUTOSARTemplates.CommonStructure.Constants.value_specification import (
    ValueSpecification,
)
from armodel.models.M2.AUTOSARTemplates.SWComponentTemplate.Datatype.DataPrototypes.data_prototype import (
    DataPrototype,
)


class ReferenceValueSpecification(ValueSpecification):
    """AUTOSAR ReferenceValueSpecification."""

    def __init__(self) -> None:
        """Initialize ReferenceValueSpecification."""
        super().__init__()
        self.reference_value: Optional[DataPrototype] = None


class ReferenceValueSpecificationBuilder:
    """Builder for ReferenceValueSpecification."""

    def __init__(self) -> None:
        """Initialize builder."""
        self._obj: ReferenceValueSpecification = ReferenceValueSpecification()

    def build(self) -> ReferenceValueSpecification:
        """Build and return ReferenceValueSpecification object.

        Returns:
            ReferenceValueSpecification instance
        """
        # TODO: Add validation
        return self._obj
