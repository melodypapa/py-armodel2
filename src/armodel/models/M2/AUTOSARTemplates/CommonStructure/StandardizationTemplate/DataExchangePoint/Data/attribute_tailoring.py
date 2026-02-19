"""AttributeTailoring AUTOSAR element.

References:
  - AUTOSAR_FO_TPS_StandardizationTemplate.pdf (page 109)

JSON Source: docs/json/packages/M2_AUTOSARTemplates_CommonStructure_StandardizationTemplate_DataExchangePoint_Data.classes.json"""

from __future__ import annotations
from typing import TYPE_CHECKING, Optional, Any
import xml.etree.ElementTree as ET

from armodel.models.M2.AUTOSARTemplates.CommonStructure.StandardizationTemplate.DataExchangePoint.Data.data_format_element_scope import (
    DataFormatElementScope,
)
from armodel.models.M2.AUTOSARTemplates.GenericStructure.GeneralTemplateClasses.ArObject.ar_object import ARObject
from armodel.models.M2.AUTOSARTemplates.CommonStructure.StandardizationTemplate.DataExchangePoint.Data.variation_restriction_with_severity import (
    VariationRestrictionWithSeverity,
)
from abc import ABC, abstractmethod


class AttributeTailoring(DataFormatElementScope, ABC):
    """AUTOSAR AttributeTailoring."""

    @property
    def is_abstract(self) -> bool:
        """Check if this class is abstract.

        Returns:
            True for abstract classes
        """
        return True

    multiplicity: Optional[Any]
    variation: Optional[VariationRestrictionWithSeverity]
    def __init__(self) -> None:
        """Initialize AttributeTailoring."""
        super().__init__()
        self.multiplicity: Optional[Any] = None
        self.variation: Optional[VariationRestrictionWithSeverity] = None
    @classmethod
    def deserialize(cls, element: ET.Element) -> "AttributeTailoring":
        """Deserialize XML element to AttributeTailoring object.

        Args:
            element: XML element to deserialize from

        Returns:
            Deserialized AttributeTailoring object
        """
        # Create instance and initialize with default values
        obj = cls.__new__(cls)
        obj.__init__()

        # Parse multiplicity
        child = ARObject._find_child_element(element, "MULTIPLICITY")
        if child is not None:
            multiplicity_value = child.text
            obj.multiplicity = multiplicity_value

        # Parse variation
        child = ARObject._find_child_element(element, "VARIATION")
        if child is not None:
            variation_value = ARObject._deserialize_by_tag(child, "VariationRestrictionWithSeverity")
            obj.variation = variation_value

        return obj



class AttributeTailoringBuilder:
    """Builder for AttributeTailoring."""

    def __init__(self) -> None:
        """Initialize builder."""
        self._obj: AttributeTailoring = AttributeTailoring()

    def build(self) -> AttributeTailoring:
        """Build and return AttributeTailoring object.

        Returns:
            AttributeTailoring instance
        """
        # TODO: Add validation
        return self._obj
