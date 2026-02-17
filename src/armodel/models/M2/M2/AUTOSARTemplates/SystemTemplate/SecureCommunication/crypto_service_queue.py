"""CryptoServiceQueue AUTOSAR element.

References:
  - AUTOSAR_CP_TPS_SystemTemplate.pdf (page 381)

JSON Source: docs/json/packages/M2_AUTOSARTemplates_SystemTemplate_SecureCommunication.classes.json"""

from __future__ import annotations
from typing import TYPE_CHECKING, Optional
import xml.etree.ElementTree as ET
from armodel.serialization import XMLMember

from armodel.models.M2.AUTOSARTemplates.GenericStructure.GeneralTemplateClasses.ARPackage.ar_element import (
    ARElement,
)
from armodel.models.M2.AUTOSARTemplates.GenericStructure.GeneralTemplateClasses.PrimitiveTypes import (
    PositiveInteger,
)


class CryptoServiceQueue(ARElement):
    """AUTOSAR CryptoServiceQueue."""

    # XML member definitions for this class only (not inherited from parent classes)
    # Format: dict[str, XMLMember] for declarative metadata
    _xml_members: dict[str, "XMLMember"] = {
        "queue_size": XMLMember(
            xml_tag=None,
            is_attribute=True,
            multiplicity="0..1",
        ),  # queueSize
    }

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
