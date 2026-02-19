"""SwSystemconstValue AUTOSAR element.

References:
  - AUTOSAR_CP_TPS_SystemTemplate.pdf (page 2068)
  - AUTOSAR_FO_TPS_FeatureModelExchangeFormat.pdf (page 80)
  - AUTOSAR_FO_TPS_GenericStructureTemplate.pdf (page 235)

JSON Source: docs/json/packages/M2_AUTOSARTemplates_GenericStructure_VariantHandling.classes.json"""

from __future__ import annotations
from typing import TYPE_CHECKING, Optional
import xml.etree.ElementTree as ET

from armodel.models.M2.AUTOSARTemplates.GenericStructure.GeneralTemplateClasses.ArObject.ar_object import ARObject
from armodel.models.M2.AUTOSARTemplates.GenericStructure.GeneralTemplateClasses.PrimitiveTypes import (
    Numerical,
)
from armodel.models.M2.MSR.Documentation.Annotation.annotation import (
    Annotation,
)
from armodel.models.M2.MSR.DataDictionary.SystemConstant.sw_systemconst import (
    SwSystemconst,
)


class SwSystemconstValue(ARObject):
    """AUTOSAR SwSystemconstValue."""

    @property
    def is_abstract(self) -> bool:
        """Check if this class is abstract.

        Returns:
            False for concrete classes
        """
        return False

    annotations: list[Annotation]
    sw_systemconst: SwSystemconst
    value: Numerical
    def __init__(self) -> None:
        """Initialize SwSystemconstValue."""
        super().__init__()
        self.annotations: list[Annotation] = []
        self.sw_systemconst: SwSystemconst = None
        self.value: Numerical = None
    @classmethod
    def deserialize(cls, element: ET.Element) -> "SwSystemconstValue":
        """Deserialize XML element to SwSystemconstValue object.

        Args:
            element: XML element to deserialize from

        Returns:
            Deserialized SwSystemconstValue object
        """
        # Create instance and initialize with default values
        obj = cls.__new__(cls)
        obj.__init__()

        # Parse annotations (list)
        obj.annotations = []
        for child in ARObject._find_all_child_elements(element, "ANNOTATIONS"):
            annotations_value = ARObject._deserialize_by_tag(child, "Annotation")
            obj.annotations.append(annotations_value)

        # Parse sw_systemconst
        child = ARObject._find_child_element(element, "SW-SYSTEMCONST")
        if child is not None:
            sw_systemconst_value = ARObject._deserialize_by_tag(child, "SwSystemconst")
            obj.sw_systemconst = sw_systemconst_value

        # Parse value
        child = ARObject._find_child_element(element, "VALUE")
        if child is not None:
            value_value = child.text
            obj.value = value_value

        return obj



class SwSystemconstValueBuilder:
    """Builder for SwSystemconstValue."""

    def __init__(self) -> None:
        """Initialize builder."""
        self._obj: SwSystemconstValue = SwSystemconstValue()

    def build(self) -> SwSystemconstValue:
        """Build and return SwSystemconstValue object.

        Returns:
            SwSystemconstValue instance
        """
        # TODO: Add validation
        return self._obj
