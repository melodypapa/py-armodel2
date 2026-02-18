"""BufferProperties AUTOSAR element.

References:
  - AUTOSAR_CP_TPS_SoftwareComponentTemplate.pdf (page 199)
  - AUTOSAR_CP_TPS_SystemTemplate.pdf (page 767)

JSON Source: docs/json/packages/M2_AUTOSARTemplates_SystemTemplate_Transformer.classes.json"""

from __future__ import annotations
from typing import TYPE_CHECKING, Optional
import xml.etree.ElementTree as ET

from armodel.models.M2.AUTOSARTemplates.GenericStructure.GeneralTemplateClasses.ArObject.ar_object import ARObject
from armodel.models.M2.AUTOSARTemplates.GenericStructure.GeneralTemplateClasses.PrimitiveTypes import (
    Boolean,
    Integer,
)


class BufferProperties(ARObject):
    """AUTOSAR BufferProperties."""

    @property
    def is_abstract(self) -> bool:
        """Check if this class is abstract.

        Returns:
            False for concrete classes
        """
        return False

    header_length: Optional[Integer]
    in_place: Optional[Boolean]
    def __init__(self) -> None:
        """Initialize BufferProperties."""
        super().__init__()
        self.header_length: Optional[Integer] = None
        self.in_place: Optional[Boolean] = None


class BufferPropertiesBuilder:
    """Builder for BufferProperties."""

    def __init__(self) -> None:
        """Initialize builder."""
        self._obj: BufferProperties = BufferProperties()

    def build(self) -> BufferProperties:
        """Build and return BufferProperties object.

        Returns:
            BufferProperties instance
        """
        # TODO: Add validation
        return self._obj
