"""MacSecCipherSuiteConfig AUTOSAR element.

References:
  - AUTOSAR_CP_TPS_SystemTemplate.pdf (page 175)

JSON Source: docs/json/packages/M2_AUTOSARTemplates_SystemTemplate_SecureCommunication.classes.json"""

from __future__ import annotations
from typing import TYPE_CHECKING, Optional
import xml.etree.ElementTree as ET

from armodel.models.M2.AUTOSARTemplates.GenericStructure.GeneralTemplateClasses.ArObject.ar_object import ARObject
from armodel.models.M2.AUTOSARTemplates.GenericStructure.GeneralTemplateClasses.PrimitiveTypes import (
    PositiveInteger,
)


class MacSecCipherSuiteConfig(ARObject):
    """AUTOSAR MacSecCipherSuiteConfig."""

    @property
    def is_abstract(self) -> bool:
        """Check if this class is abstract.

        Returns:
            False for concrete classes
        """
        return False

    cipher_suite: Optional[PositiveInteger]
    def __init__(self) -> None:
        """Initialize MacSecCipherSuiteConfig."""
        super().__init__()
        self.cipher_suite: Optional[PositiveInteger] = None


class MacSecCipherSuiteConfigBuilder:
    """Builder for MacSecCipherSuiteConfig."""

    def __init__(self) -> None:
        """Initialize builder."""
        self._obj: MacSecCipherSuiteConfig = MacSecCipherSuiteConfig()

    def build(self) -> MacSecCipherSuiteConfig:
        """Build and return MacSecCipherSuiteConfig object.

        Returns:
            MacSecCipherSuiteConfig instance
        """
        # TODO: Add validation
        return self._obj
