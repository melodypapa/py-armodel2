"""DataFormatElementScope AUTOSAR element.

References:
  - AUTOSAR_FO_TPS_StandardizationTemplate.pdf (page 91)

JSON Source: docs/json/packages/M2_AUTOSARTemplates_CommonStructure_StandardizationTemplate_DataExchangePoint_Data.classes.json"""

from __future__ import annotations
from typing import TYPE_CHECKING, Optional
import xml.etree.ElementTree as ET

from armodel.models.M2.AUTOSARTemplates.CommonStructure.StandardizationTemplate.DataExchangePoint.Common.spec_element_scope import (
    SpecElementScope,
)
from armodel.models.M2.AUTOSARTemplates.GenericStructure.GeneralTemplateClasses.ArObject.ar_object import ARObject
from abc import ABC, abstractmethod


class DataFormatElementScope(SpecElementScope, ABC):
    """AUTOSAR DataFormatElementScope."""

    @property
    def is_abstract(self) -> bool:
        """Check if this class is abstract.

        Returns:
            True for abstract classes
        """
        return True

    def __init__(self) -> None:
        """Initialize DataFormatElementScope."""
        super().__init__()
    @classmethod
    def deserialize(cls, element: ET.Element) -> "DataFormatElementScope":
        """Deserialize XML element to DataFormatElementScope object.

        Args:
            element: XML element to deserialize from

        Returns:
            Deserialized DataFormatElementScope object
        """
        # Create instance and initialize with default values
        obj = cls.__new__(cls)
        obj.__init__()

        return obj



class DataFormatElementScopeBuilder:
    """Builder for DataFormatElementScope."""

    def __init__(self) -> None:
        """Initialize builder."""
        self._obj: DataFormatElementScope = DataFormatElementScope()

    def build(self) -> DataFormatElementScope:
        """Build and return DataFormatElementScope object.

        Returns:
            DataFormatElementScope instance
        """
        # TODO: Add validation
        return self._obj
