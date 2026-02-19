"""Baseline AUTOSAR element.

References:
  - AUTOSAR_FO_TPS_StandardizationTemplate.pdf (page 79)

JSON Source: docs/json/packages/M2_AUTOSARTemplates_CommonStructure_StandardizationTemplate_DataExchangePoint.classes.json"""

from __future__ import annotations
from typing import TYPE_CHECKING, Optional
import xml.etree.ElementTree as ET

from armodel.models.M2.AUTOSARTemplates.GenericStructure.GeneralTemplateClasses.ArObject.ar_object import ARObject
from armodel.models.M2.AUTOSARTemplates.GenericStructure.GeneralTemplateClasses.PrimitiveTypes import (
    String,
)
from armodel.models.M2.AUTOSARTemplates.GenericStructure.DocumentationOnM1.documentation import (
    Documentation,
)
from armodel.models.M2.AUTOSARTemplates.GenericStructure.GeneralTemplateClasses.SpecialDataDef.sdg_def import (
    SdgDef,
)


class Baseline(ARObject):
    """AUTOSAR Baseline."""

    @property
    def is_abstract(self) -> bool:
        """Check if this class is abstract.

        Returns:
            False for concrete classes
        """
        return False

    custom_sdg_defs: list[SdgDef]
    customs: list[Documentation]
    standards: list[String]
    def __init__(self) -> None:
        """Initialize Baseline."""
        super().__init__()
        self.custom_sdg_defs: list[SdgDef] = []
        self.customs: list[Documentation] = []
        self.standards: list[String] = []
    @classmethod
    def deserialize(cls, element: ET.Element) -> "Baseline":
        """Deserialize XML element to Baseline object.

        Args:
            element: XML element to deserialize from

        Returns:
            Deserialized Baseline object
        """
        # Create instance and initialize with default values
        obj = cls.__new__(cls)
        obj.__init__()

        # Parse custom_sdg_defs (list)
        obj.custom_sdg_defs = []
        for child in ARObject._find_all_child_elements(element, "CUSTOM-SDG-DEFS"):
            custom_sdg_defs_value = ARObject._deserialize_by_tag(child, "SdgDef")
            obj.custom_sdg_defs.append(custom_sdg_defs_value)

        # Parse customs (list)
        obj.customs = []
        for child in ARObject._find_all_child_elements(element, "CUSTOMS"):
            customs_value = ARObject._deserialize_by_tag(child, "Documentation")
            obj.customs.append(customs_value)

        # Parse standards (list)
        obj.standards = []
        for child in ARObject._find_all_child_elements(element, "STANDARDS"):
            standards_value = child.text
            obj.standards.append(standards_value)

        return obj



class BaselineBuilder:
    """Builder for Baseline."""

    def __init__(self) -> None:
        """Initialize builder."""
        self._obj: Baseline = Baseline()

    def build(self) -> Baseline:
        """Build and return Baseline object.

        Returns:
            Baseline instance
        """
        # TODO: Add validation
        return self._obj
