"""DataFormatElementReference AUTOSAR element.

References:
  - AUTOSAR_FO_TPS_StandardizationTemplate.pdf (page 91)

JSON Source: docs/json/packages/M2_AUTOSARTemplates_CommonStructure_StandardizationTemplate_DataExchangePoint_Common.classes.json"""

from __future__ import annotations
from typing import TYPE_CHECKING, Optional
import xml.etree.ElementTree as ET

from armodel.models.M2.AUTOSARTemplates.CommonStructure.StandardizationTemplate.DataExchangePoint.Common.spec_element_reference import (
    SpecElementReference,
)
from armodel.models.M2.AUTOSARTemplates.GenericStructure.GeneralTemplateClasses.ArObject.ar_object import ARObject
from abc import ABC, abstractmethod


class DataFormatElementReference(SpecElementReference, ABC):
    """AUTOSAR DataFormatElementReference."""

    @property
    def is_abstract(self) -> bool:
        """Check if this class is abstract.

        Returns:
            True for abstract classes
        """
        return True

    def __init__(self) -> None:
        """Initialize DataFormatElementReference."""
        super().__init__()
    @classmethod
    def deserialize(cls, element: ET.Element) -> "DataFormatElementReference":
        """Deserialize XML element to DataFormatElementReference object.

        Args:
            element: XML element to deserialize from

        Returns:
            Deserialized DataFormatElementReference object
        """
        # Create instance and initialize with default values
        obj = cls.__new__(cls)
        obj.__init__()

        return obj



class DataFormatElementReferenceBuilder:
    """Builder for DataFormatElementReference."""

    def __init__(self) -> None:
        """Initialize builder."""
        self._obj: DataFormatElementReference = DataFormatElementReference()

    def build(self) -> DataFormatElementReference:
        """Build and return DataFormatElementReference object.

        Returns:
            DataFormatElementReference instance
        """
        # TODO: Add validation
        return self._obj
