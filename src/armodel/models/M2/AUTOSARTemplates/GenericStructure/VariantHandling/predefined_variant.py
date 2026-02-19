"""PredefinedVariant AUTOSAR element.

References:
  - AUTOSAR_CP_TPS_ECUConfiguration.pdf (page 305)
  - AUTOSAR_FO_TPS_FeatureModelExchangeFormat.pdf (page 77)
  - AUTOSAR_FO_TPS_GenericStructureTemplate.pdf (page 257)

JSON Source: docs/json/packages/M2_AUTOSARTemplates_GenericStructure_VariantHandling.classes.json"""

from __future__ import annotations
from typing import TYPE_CHECKING, Optional, Any
import xml.etree.ElementTree as ET

from armodel.models.M2.AUTOSARTemplates.GenericStructure.GeneralTemplateClasses.ARPackage.ar_element import (
    ARElement,
)
from armodel.models.M2.AUTOSARTemplates.GenericStructure.GeneralTemplateClasses.ArObject.ar_object import ARObject
from armodel.models.M2.AUTOSARTemplates.GenericStructure.VariantHandling.sw_systemconstant_value_set import (
    SwSystemconstantValueSet,
)


class PredefinedVariant(ARElement):
    """AUTOSAR PredefinedVariant."""

    @property
    def is_abstract(self) -> bool:
        """Check if this class is abstract.

        Returns:
            False for concrete classes
        """
        return False

    included_variants: list[PredefinedVariant]
    post_build_variants: list[Any]
    sws: list[SwSystemconstantValueSet]
    def __init__(self) -> None:
        """Initialize PredefinedVariant."""
        super().__init__()
        self.included_variants: list[PredefinedVariant] = []
        self.post_build_variants: list[Any] = []
        self.sws: list[SwSystemconstantValueSet] = []
    @classmethod
    def deserialize(cls, element: ET.Element) -> "PredefinedVariant":
        """Deserialize XML element to PredefinedVariant object.

        Args:
            element: XML element to deserialize from

        Returns:
            Deserialized PredefinedVariant object
        """
        # First, call parent's deserialize to handle inherited attributes
        obj = super(PredefinedVariant, cls).deserialize(element)

        # Parse included_variants (list from container "INCLUDED-VARIANTS")
        obj.included_variants = []
        container = ARObject._find_child_element(element, "INCLUDED-VARIANTS")
        if container is not None:
            for child in container:
                # Deserialize each child element dynamically based on its tag
                child_value = ARObject._deserialize_by_tag(child, None)
                if child_value is not None:
                    obj.included_variants.append(child_value)

        # Parse post_build_variants (list from container "POST-BUILD-VARIANTS")
        obj.post_build_variants = []
        container = ARObject._find_child_element(element, "POST-BUILD-VARIANTS")
        if container is not None:
            for child in container:
                # Deserialize each child element dynamically based on its tag
                child_value = ARObject._deserialize_by_tag(child, None)
                if child_value is not None:
                    obj.post_build_variants.append(child_value)

        # Parse sws (list from container "SWS")
        obj.sws = []
        container = ARObject._find_child_element(element, "SWS")
        if container is not None:
            for child in container:
                # Deserialize each child element dynamically based on its tag
                child_value = ARObject._deserialize_by_tag(child, None)
                if child_value is not None:
                    obj.sws.append(child_value)

        return obj



class PredefinedVariantBuilder:
    """Builder for PredefinedVariant."""

    def __init__(self) -> None:
        """Initialize builder."""
        self._obj: PredefinedVariant = PredefinedVariant()

    def build(self) -> PredefinedVariant:
        """Build and return PredefinedVariant object.

        Returns:
            PredefinedVariant instance
        """
        # TODO: Add validation
        return self._obj
