"""SoftwareContext AUTOSAR element.

References:
  - AUTOSAR_CP_TPS_BSWModuleDescriptionTemplate.pdf (page 163)

JSON Source: docs/json/packages/M2_AUTOSARTemplates_CommonStructure_ResourceConsumption.classes.json"""

from __future__ import annotations
from typing import TYPE_CHECKING, Optional
import xml.etree.ElementTree as ET

from armodel.models.M2.AUTOSARTemplates.GenericStructure.GeneralTemplateClasses.ArObject.ar_object import ARObject
from armodel.models.M2.AUTOSARTemplates.GenericStructure.GeneralTemplateClasses.PrimitiveTypes import (
    String,
)


class SoftwareContext(ARObject):
    """AUTOSAR SoftwareContext."""

    @property
    def is_abstract(self) -> bool:
        """Check if this class is abstract.

        Returns:
            False for concrete classes
        """
        return False

    input: Optional[String]
    state: Optional[String]
    def __init__(self) -> None:
        """Initialize SoftwareContext."""
        super().__init__()
        self.input: Optional[String] = None
        self.state: Optional[String] = None


class SoftwareContextBuilder:
    """Builder for SoftwareContext."""

    def __init__(self) -> None:
        """Initialize builder."""
        self._obj: SoftwareContext = SoftwareContext()

    def build(self) -> SoftwareContext:
        """Build and return SoftwareContext object.

        Returns:
            SoftwareContext instance
        """
        # TODO: Add validation
        return self._obj
