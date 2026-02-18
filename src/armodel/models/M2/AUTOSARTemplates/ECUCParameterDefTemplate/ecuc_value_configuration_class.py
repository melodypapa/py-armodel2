"""EcucValueConfigurationClass AUTOSAR element.

References:
  - AUTOSAR_CP_TPS_ECUConfiguration.pdf (page 52)

JSON Source: docs/json/packages/M2_AUTOSARTemplates_ECUCParameterDefTemplate.classes.json"""

from __future__ import annotations
from typing import TYPE_CHECKING, Optional
import xml.etree.ElementTree as ET

from armodel.models.M2.AUTOSARTemplates.ECUCParameterDefTemplate.ecuc_abstract_configuration_class import (
    EcucAbstractConfigurationClass,
)


class EcucValueConfigurationClass(EcucAbstractConfigurationClass):
    """AUTOSAR EcucValueConfigurationClass."""

    @property
    def is_abstract(self) -> bool:
        """Check if this class is abstract.

        Returns:
            False for concrete classes
        """
        return False

    def __init__(self) -> None:
        """Initialize EcucValueConfigurationClass."""
        super().__init__()


class EcucValueConfigurationClassBuilder:
    """Builder for EcucValueConfigurationClass."""

    def __init__(self) -> None:
        """Initialize builder."""
        self._obj: EcucValueConfigurationClass = EcucValueConfigurationClass()

    def build(self) -> EcucValueConfigurationClass:
        """Build and return EcucValueConfigurationClass object.

        Returns:
            EcucValueConfigurationClass instance
        """
        # TODO: Add validation
        return self._obj
