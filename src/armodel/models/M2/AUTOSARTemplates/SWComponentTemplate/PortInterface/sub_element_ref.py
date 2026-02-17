"""SubElementRef AUTOSAR element.

References:
  - AUTOSAR_CP_TPS_SoftwareComponentTemplate.pdf (page 138)

JSON Source: docs/json/packages/M2_AUTOSARTemplates_SWComponentTemplate_PortInterface.classes.json"""

from __future__ import annotations
from typing import TYPE_CHECKING, Optional
import xml.etree.ElementTree as ET

from armodel.models.M2.AUTOSARTemplates.GenericStructure.GeneralTemplateClasses.ArObject.ar_object import ARObject


class SubElementRef(ARObject):
    """AUTOSAR SubElementRef."""
    """Abstract base class - do not instantiate directly."""

    def __init__(self) -> None:
        """Initialize SubElementRef."""
        super().__init__()


class SubElementRefBuilder:
    """Builder for SubElementRef."""

    def __init__(self) -> None:
        """Initialize builder."""
        self._obj: SubElementRef = SubElementRef()

    def build(self) -> SubElementRef:
        """Build and return SubElementRef object.

        Returns:
            SubElementRef instance
        """
        # TODO: Add validation
        return self._obj
