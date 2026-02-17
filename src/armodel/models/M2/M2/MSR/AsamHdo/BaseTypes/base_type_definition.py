"""BaseTypeDefinition AUTOSAR element.

References:
  - AUTOSAR_CP_TPS_SoftwareComponentTemplate.pdf (page 290)

JSON Source: docs/json/packages/M2_MSR_AsamHdo_BaseTypes.classes.json"""

from __future__ import annotations
from typing import TYPE_CHECKING, Optional
import xml.etree.ElementTree as ET

from armodel.models.M2.AUTOSARTemplates.GenericStructure.GeneralTemplateClasses.ArObject.ar_object import ARObject


class BaseTypeDefinition(ARObject):
    """AUTOSAR BaseTypeDefinition."""
    """Abstract base class - do not instantiate directly."""

    def __init__(self) -> None:
        """Initialize BaseTypeDefinition."""
        super().__init__()


class BaseTypeDefinitionBuilder:
    """Builder for BaseTypeDefinition."""

    def __init__(self) -> None:
        """Initialize builder."""
        self._obj: BaseTypeDefinition = BaseTypeDefinition()

    def build(self) -> BaseTypeDefinition:
        """Build and return BaseTypeDefinition object.

        Returns:
            BaseTypeDefinition instance
        """
        # TODO: Add validation
        return self._obj
