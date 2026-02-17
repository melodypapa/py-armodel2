"""AbstractGlobalTimeDomainProps AUTOSAR element.

References:
  - AUTOSAR_CP_TPS_SystemTemplate.pdf (page 859)

JSON Source: docs/json/packages/M2_AUTOSARTemplates_SystemTemplate_GlobalTime.classes.json"""

from __future__ import annotations
from typing import TYPE_CHECKING, Optional
import xml.etree.ElementTree as ET

from armodel.models.M2.AUTOSARTemplates.GenericStructure.GeneralTemplateClasses.ArObject.ar_object import ARObject


class AbstractGlobalTimeDomainProps(ARObject):
    """AUTOSAR AbstractGlobalTimeDomainProps."""
    """Abstract base class - do not instantiate directly."""

    def __init__(self) -> None:
        """Initialize AbstractGlobalTimeDomainProps."""
        super().__init__()


class AbstractGlobalTimeDomainPropsBuilder:
    """Builder for AbstractGlobalTimeDomainProps."""

    def __init__(self) -> None:
        """Initialize builder."""
        self._obj: AbstractGlobalTimeDomainProps = AbstractGlobalTimeDomainProps()

    def build(self) -> AbstractGlobalTimeDomainProps:
        """Build and return AbstractGlobalTimeDomainProps object.

        Returns:
            AbstractGlobalTimeDomainProps instance
        """
        # TODO: Add validation
        return self._obj
