"""SwCalprmAxisTypeProps AUTOSAR element.

References:
  - AUTOSAR_CP_TPS_SoftwareComponentTemplate.pdf (page 353)

JSON Source: docs/json/packages/M2_MSR_DataDictionary_CalibrationParameter.classes.json"""

from __future__ import annotations
from typing import TYPE_CHECKING, Optional
import xml.etree.ElementTree as ET

from armodel.models.M2.AUTOSARTemplates.GenericStructure.GeneralTemplateClasses.ArObject.ar_object import ARObject
from armodel.models.M2.AUTOSARTemplates.GenericStructure.GeneralTemplateClasses.PrimitiveTypes import (
    MonotonyEnum,
)
from armodel.models.M2.AUTOSARTemplates.GenericStructure.GeneralTemplateClasses.PrimitiveTypes import (
    Float,
)
from abc import ABC, abstractmethod


class SwCalprmAxisTypeProps(ARObject, ABC):
    """AUTOSAR SwCalprmAxisTypeProps."""

    @property
    def is_abstract(self) -> bool:
        """Check if this class is abstract.

        Returns:
            True for abstract classes
        """
        return True

    max_gradient: Optional[Float]
    monotony: Optional[MonotonyEnum]
    def __init__(self) -> None:
        """Initialize SwCalprmAxisTypeProps."""
        super().__init__()
        self.max_gradient: Optional[Float] = None
        self.monotony: Optional[MonotonyEnum] = None


class SwCalprmAxisTypePropsBuilder:
    """Builder for SwCalprmAxisTypeProps."""

    def __init__(self) -> None:
        """Initialize builder."""
        self._obj: SwCalprmAxisTypeProps = SwCalprmAxisTypeProps()

    def build(self) -> SwCalprmAxisTypeProps:
        """Build and return SwCalprmAxisTypeProps object.

        Returns:
            SwCalprmAxisTypeProps instance
        """
        # TODO: Add validation
        return self._obj
