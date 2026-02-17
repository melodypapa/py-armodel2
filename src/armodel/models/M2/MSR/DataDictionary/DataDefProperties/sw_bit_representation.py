"""SwBitRepresentation AUTOSAR element.

References:
  - AUTOSAR_CP_TPS_SoftwareComponentTemplate.pdf (page 333)

JSON Source: docs/json/packages/M2_MSR_DataDictionary_DataDefProperties.classes.json"""

from __future__ import annotations
from typing import TYPE_CHECKING, Optional
import xml.etree.ElementTree as ET

from armodel.models.M2.AUTOSARTemplates.GenericStructure.GeneralTemplateClasses.ArObject.ar_object import ARObject
from armodel.models.M2.AUTOSARTemplates.GenericStructure.GeneralTemplateClasses.PrimitiveTypes import (
    Integer,
)


class SwBitRepresentation(ARObject):
    """AUTOSAR SwBitRepresentation."""

    def __init__(self) -> None:
        """Initialize SwBitRepresentation."""
        super().__init__()
        self.bit_position: Optional[Integer] = None
        self.number_of_bits: Optional[Integer] = None


class SwBitRepresentationBuilder:
    """Builder for SwBitRepresentation."""

    def __init__(self) -> None:
        """Initialize builder."""
        self._obj: SwBitRepresentation = SwBitRepresentation()

    def build(self) -> SwBitRepresentation:
        """Build and return SwBitRepresentation object.

        Returns:
            SwBitRepresentation instance
        """
        # TODO: Add validation
        return self._obj
