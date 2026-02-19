"""FMFeatureMapAssertion AUTOSAR element.

References:
  - AUTOSAR_FO_TPS_FeatureModelExchangeFormat.pdf (page 55)

JSON Source: docs/json/packages/M2_AUTOSARTemplates_FeatureModelTemplate.classes.json"""

from __future__ import annotations
from typing import TYPE_CHECKING, Optional, Any
import xml.etree.ElementTree as ET

from armodel.models.M2.AUTOSARTemplates.GenericStructure.GeneralTemplateClasses.Identifiable.identifiable import (
    Identifiable,
)
from armodel.models.M2.AUTOSARTemplates.GenericStructure.GeneralTemplateClasses.ArObject.ar_object import ARObject


class FMFeatureMapAssertion(Identifiable):
    """AUTOSAR FMFeatureMapAssertion."""

    @property
    def is_abstract(self) -> bool:
        """Check if this class is abstract.

        Returns:
            False for concrete classes
        """
        return False

    fm_syscond_and_sw_systemconsts: Optional[Any]
    def __init__(self) -> None:
        """Initialize FMFeatureMapAssertion."""
        super().__init__()
        self.fm_syscond_and_sw_systemconsts: Optional[Any] = None
    @classmethod
    def deserialize(cls, element: ET.Element) -> "FMFeatureMapAssertion":
        """Deserialize XML element to FMFeatureMapAssertion object.

        Args:
            element: XML element to deserialize from

        Returns:
            Deserialized FMFeatureMapAssertion object
        """
        # First, call parent's deserialize to handle inherited attributes
        obj = super(FMFeatureMapAssertion, cls).deserialize(element)

        # Parse fm_syscond_and_sw_systemconsts
        child = ARObject._find_child_element(element, "FM-SYSCOND-AND-SW-SYSTEMCONSTS")
        if child is not None:
            fm_syscond_and_sw_systemconsts_value = child.text
            obj.fm_syscond_and_sw_systemconsts = fm_syscond_and_sw_systemconsts_value

        return obj



class FMFeatureMapAssertionBuilder:
    """Builder for FMFeatureMapAssertion."""

    def __init__(self) -> None:
        """Initialize builder."""
        self._obj: FMFeatureMapAssertion = FMFeatureMapAssertion()

    def build(self) -> FMFeatureMapAssertion:
        """Build and return FMFeatureMapAssertion object.

        Returns:
            FMFeatureMapAssertion instance
        """
        # TODO: Add validation
        return self._obj
