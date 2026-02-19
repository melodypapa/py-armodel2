"""SwSystemconstantValueSet AUTOSAR element.

References:
  - AUTOSAR_CP_TPS_ECUConfiguration.pdf (page 313)
  - AUTOSAR_CP_TPS_SoftwareComponentTemplate.pdf (page 1007)
  - AUTOSAR_CP_TPS_SystemTemplate.pdf (page 2069)
  - AUTOSAR_CP_TPS_TimingExtensions.pdf (page 246)
  - AUTOSAR_FO_TPS_FeatureModelExchangeFormat.pdf (page 56)
  - AUTOSAR_FO_TPS_GenericStructureTemplate.pdf (page 258)

JSON Source: docs/json/packages/M2_AUTOSARTemplates_GenericStructure_VariantHandling.classes.json"""

from __future__ import annotations
from typing import TYPE_CHECKING, Optional
import xml.etree.ElementTree as ET

from armodel.models.M2.AUTOSARTemplates.GenericStructure.GeneralTemplateClasses.ARPackage.ar_element import (
    ARElement,
)
from armodel.models.M2.AUTOSARTemplates.GenericStructure.GeneralTemplateClasses.ArObject.ar_object import ARObject
from armodel.models.M2.AUTOSARTemplates.GenericStructure.VariantHandling.sw_systemconst_value import (
    SwSystemconstValue,
)


class SwSystemconstantValueSet(ARElement):
    """AUTOSAR SwSystemconstantValueSet."""

    @property
    def is_abstract(self) -> bool:
        """Check if this class is abstract.

        Returns:
            False for concrete classes
        """
        return False

    sws: list[SwSystemconstValue]
    def __init__(self) -> None:
        """Initialize SwSystemconstantValueSet."""
        super().__init__()
        self.sws: list[SwSystemconstValue] = []
    @classmethod
    def deserialize(cls, element: ET.Element) -> "SwSystemconstantValueSet":
        """Deserialize XML element to SwSystemconstantValueSet object.

        Args:
            element: XML element to deserialize from

        Returns:
            Deserialized SwSystemconstantValueSet object
        """
        # Create instance and initialize with default values
        obj = cls.__new__(cls)
        obj.__init__()

        # Parse sws (list)
        obj.sws = []
        for child in ARObject._find_all_child_elements(element, "SWS"):
            sws_value = ARObject._deserialize_by_tag(child, "SwSystemconstValue")
            obj.sws.append(sws_value)

        return obj



class SwSystemconstantValueSetBuilder:
    """Builder for SwSystemconstantValueSet."""

    def __init__(self) -> None:
        """Initialize builder."""
        self._obj: SwSystemconstantValueSet = SwSystemconstantValueSet()

    def build(self) -> SwSystemconstantValueSet:
        """Build and return SwSystemconstantValueSet object.

        Returns:
            SwSystemconstantValueSet instance
        """
        # TODO: Add validation
        return self._obj
