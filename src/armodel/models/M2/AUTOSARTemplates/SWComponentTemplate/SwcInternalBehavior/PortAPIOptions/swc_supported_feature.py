"""SwcSupportedFeature AUTOSAR element.

References:
  - AUTOSAR_CP_TPS_SoftwareComponentTemplate.pdf (page 594)

JSON Source: docs/json/packages/M2_AUTOSARTemplates_SWComponentTemplate_SwcInternalBehavior_PortAPIOptions.classes.json"""

from __future__ import annotations
from typing import TYPE_CHECKING, Optional
import xml.etree.ElementTree as ET

from armodel.models.M2.AUTOSARTemplates.GenericStructure.GeneralTemplateClasses.ArObject.ar_object import ARObject
from abc import ABC, abstractmethod


class SwcSupportedFeature(ARObject, ABC):
    """AUTOSAR SwcSupportedFeature."""

    @property
    def is_abstract(self) -> bool:
        """Check if this class is abstract.

        Returns:
            True for abstract classes
        """
        return True

    def __init__(self) -> None:
        """Initialize SwcSupportedFeature."""
        super().__init__()


class SwcSupportedFeatureBuilder:
    """Builder for SwcSupportedFeature."""

    def __init__(self) -> None:
        """Initialize builder."""
        self._obj: SwcSupportedFeature = SwcSupportedFeature()

    def build(self) -> SwcSupportedFeature:
        """Build and return SwcSupportedFeature object.

        Returns:
            SwcSupportedFeature instance
        """
        # TODO: Add validation
        return self._obj
