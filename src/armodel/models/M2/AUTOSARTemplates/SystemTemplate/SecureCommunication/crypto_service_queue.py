"""CryptoServiceQueue AUTOSAR element.

References:
  - AUTOSAR_CP_TPS_SystemTemplate.pdf (page 381)

JSON Source: docs/json/packages/M2_AUTOSARTemplates_SystemTemplate_SecureCommunication.classes.json"""

from __future__ import annotations
from typing import TYPE_CHECKING, Optional
import xml.etree.ElementTree as ET

from armodel.models.M2.AUTOSARTemplates.GenericStructure.GeneralTemplateClasses.ARPackage.ar_element import (
    ARElement,
)
from armodel.models.M2.AUTOSARTemplates.GenericStructure.GeneralTemplateClasses.PrimitiveTypes import (
    PositiveInteger,
)


class CryptoServiceQueue(ARElement):
    """AUTOSAR CryptoServiceQueue."""

    @property
    def is_abstract(self) -> bool:
        """Check if this class is abstract.

        Returns:
            False for concrete classes
        """
        return False

    queue_size: Optional[PositiveInteger]
    def __init__(self) -> None:
        """Initialize CryptoServiceQueue."""
        super().__init__()
        self.queue_size: Optional[PositiveInteger] = None


class CryptoServiceQueueBuilder:
    """Builder for CryptoServiceQueue."""

    def __init__(self) -> None:
        """Initialize builder."""
        self._obj: CryptoServiceQueue = CryptoServiceQueue()

    def build(self) -> CryptoServiceQueue:
        """Build and return CryptoServiceQueue object.

        Returns:
            CryptoServiceQueue instance
        """
        # TODO: Add validation
        return self._obj
