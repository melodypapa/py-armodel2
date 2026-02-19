"""SdgAggregationWithVariation AUTOSAR element.

References:
  - AUTOSAR_FO_TPS_GenericStructureTemplate.pdf (page 101)

JSON Source: docs/json/packages/M2_AUTOSARTemplates_GenericStructure_GeneralTemplateClasses_SpecialDataDef.classes.json"""

from __future__ import annotations
from typing import TYPE_CHECKING, Optional
import xml.etree.ElementTree as ET

from armodel.models.M2.AUTOSARTemplates.GenericStructure.GeneralTemplateClasses.SpecialDataDef.sdg_element_with_gid import (
    SdgElementWithGid,
)
from armodel.models.M2.AUTOSARTemplates.GenericStructure.GeneralTemplateClasses.ArObject.ar_object import ARObject
from armodel.models.M2.AUTOSARTemplates.GenericStructure.GeneralTemplateClasses.SpecialDataDef.sdg_class import (
    SdgClass,
)


class SdgAggregationWithVariation(SdgElementWithGid):
    """AUTOSAR SdgAggregationWithVariation."""

    @property
    def is_abstract(self) -> bool:
        """Check if this class is abstract.

        Returns:
            False for concrete classes
        """
        return False

    sub_sdg: Optional[SdgClass]
    def __init__(self) -> None:
        """Initialize SdgAggregationWithVariation."""
        super().__init__()
        self.sub_sdg: Optional[SdgClass] = None
    @classmethod
    def deserialize(cls, element: ET.Element) -> "SdgAggregationWithVariation":
        """Deserialize XML element to SdgAggregationWithVariation object.

        Args:
            element: XML element to deserialize from

        Returns:
            Deserialized SdgAggregationWithVariation object
        """
        # Create instance and initialize with default values
        obj = cls.__new__(cls)
        obj.__init__()

        # Parse sub_sdg
        child = ARObject._find_child_element(element, "SUB-SDG")
        if child is not None:
            sub_sdg_value = ARObject._deserialize_by_tag(child, "SdgClass")
            obj.sub_sdg = sub_sdg_value

        return obj



class SdgAggregationWithVariationBuilder:
    """Builder for SdgAggregationWithVariation."""

    def __init__(self) -> None:
        """Initialize builder."""
        self._obj: SdgAggregationWithVariation = SdgAggregationWithVariation()

    def build(self) -> SdgAggregationWithVariation:
        """Build and return SdgAggregationWithVariation object.

        Returns:
            SdgAggregationWithVariation instance
        """
        # TODO: Add validation
        return self._obj
