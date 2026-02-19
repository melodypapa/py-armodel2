"""SdgTailoring AUTOSAR element.

References:
  - AUTOSAR_FO_TPS_StandardizationTemplate.pdf (page 118)

JSON Source: docs/json/packages/M2_AUTOSARTemplates_CommonStructure_StandardizationTemplate_DataExchangePoint_Data.classes.json"""

from __future__ import annotations
from typing import TYPE_CHECKING, Optional
import xml.etree.ElementTree as ET

from armodel.models.M2.AUTOSARTemplates.CommonStructure.StandardizationTemplate.DataExchangePoint.Common.restriction_with_severity import (
    RestrictionWithSeverity,
)
from armodel.models.M2.AUTOSARTemplates.GenericStructure.GeneralTemplateClasses.ArObject.ar_object import ARObject
from armodel.models.M2.AUTOSARTemplates.GenericStructure.GeneralTemplateClasses.SpecialDataDef.sdg_class import (
    SdgClass,
)


class SdgTailoring(RestrictionWithSeverity):
    """AUTOSAR SdgTailoring."""

    @property
    def is_abstract(self) -> bool:
        """Check if this class is abstract.

        Returns:
            False for concrete classes
        """
        return False

    sdg_class: Optional[SdgClass]
    def __init__(self) -> None:
        """Initialize SdgTailoring."""
        super().__init__()
        self.sdg_class: Optional[SdgClass] = None
    @classmethod
    def deserialize(cls, element: ET.Element) -> "SdgTailoring":
        """Deserialize XML element to SdgTailoring object.

        Args:
            element: XML element to deserialize from

        Returns:
            Deserialized SdgTailoring object
        """
        # Create instance and initialize with default values
        obj = cls.__new__(cls)
        obj.__init__()

        # Parse sdg_class
        child = ARObject._find_child_element(element, "SDG-CLASS")
        if child is not None:
            sdg_class_value = ARObject._deserialize_by_tag(child, "SdgClass")
            obj.sdg_class = sdg_class_value

        return obj



class SdgTailoringBuilder:
    """Builder for SdgTailoring."""

    def __init__(self) -> None:
        """Initialize builder."""
        self._obj: SdgTailoring = SdgTailoring()

    def build(self) -> SdgTailoring:
        """Build and return SdgTailoring object.

        Returns:
            SdgTailoring instance
        """
        # TODO: Add validation
        return self._obj
