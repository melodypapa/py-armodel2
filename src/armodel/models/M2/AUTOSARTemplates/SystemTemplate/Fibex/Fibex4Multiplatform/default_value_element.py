"""DefaultValueElement AUTOSAR element.

References:
  - AUTOSAR_CP_TPS_SystemTemplate.pdf (page 841)

JSON Source: docs/json/packages/M2_AUTOSARTemplates_SystemTemplate_Fibex_Fibex4Multiplatform.classes.json"""

from __future__ import annotations
from typing import TYPE_CHECKING, Optional
import xml.etree.ElementTree as ET

from armodel.models.M2.AUTOSARTemplates.GenericStructure.GeneralTemplateClasses.ArObject.ar_object import ARObject
from armodel.models.M2.AUTOSARTemplates.GenericStructure.GeneralTemplateClasses.PrimitiveTypes import (
    Integer,
)


class DefaultValueElement(ARObject):
    """AUTOSAR DefaultValueElement."""

    element_byte_value: Optional[Integer]
    element_position: Optional[Integer]
    def __init__(self) -> None:
        """Initialize DefaultValueElement."""
        super().__init__()
        self.element_byte_value: Optional[Integer] = None
        self.element_position: Optional[Integer] = None


class DefaultValueElementBuilder:
    """Builder for DefaultValueElement."""

    def __init__(self) -> None:
        """Initialize builder."""
        self._obj: DefaultValueElement = DefaultValueElement()

    def build(self) -> DefaultValueElement:
        """Build and return DefaultValueElement object.

        Returns:
            DefaultValueElement instance
        """
        # TODO: Add validation
        return self._obj
