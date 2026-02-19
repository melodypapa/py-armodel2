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
    @classmethod
    def deserialize(cls, element: ET.Element) -> "SwCalprmAxisTypeProps":
        """Deserialize XML element to SwCalprmAxisTypeProps object.

        Args:
            element: XML element to deserialize from

        Returns:
            Deserialized SwCalprmAxisTypeProps object
        """
        # Create instance and initialize with default values
        obj = cls.__new__(cls)
        obj.__init__()

        # Parse max_gradient
        child = ARObject._find_child_element(element, "MAX-GRADIENT")
        if child is not None:
            max_gradient_value = child.text
            obj.max_gradient = max_gradient_value

        # Parse monotony
        child = ARObject._find_child_element(element, "MONOTONY")
        if child is not None:
            monotony_value = child.text
            obj.monotony = monotony_value

        return obj



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
