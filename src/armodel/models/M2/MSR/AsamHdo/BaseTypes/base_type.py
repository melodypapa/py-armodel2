"""BaseType AUTOSAR element.

References:
  - AUTOSAR_CP_TPS_DiagnosticExtractTemplate.pdf (page 302)
  - AUTOSAR_CP_TPS_SoftwareComponentTemplate.pdf (page 291)
  - AUTOSAR_CP_TPS_SystemTemplate.pdf (page 2002)

JSON Source: docs/json/packages/M2_MSR_AsamHdo_BaseTypes.classes.json"""

from __future__ import annotations
from typing import TYPE_CHECKING, Optional
import xml.etree.ElementTree as ET

from armodel.models.M2.AUTOSARTemplates.GenericStructure.GeneralTemplateClasses.ARPackage.ar_element import (
    ARElement,
)
from armodel.models.M2.MSR.AsamHdo.BaseTypes.base_type_definition import (
    BaseTypeDefinition,
)


class BaseType(ARElement):
    """AUTOSAR BaseType."""
    """Abstract base class - do not instantiate directly."""

    base_type: BaseTypeDefinition
    def __init__(self) -> None:
        """Initialize BaseType."""
        super().__init__()
        self.base_type: BaseTypeDefinition = None


class BaseTypeBuilder:
    """Builder for BaseType."""

    def __init__(self) -> None:
        """Initialize builder."""
        self._obj: BaseType = BaseType()

    def build(self) -> BaseType:
        """Build and return BaseType object.

        Returns:
            BaseType instance
        """
        # TODO: Add validation
        return self._obj
