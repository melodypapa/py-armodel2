"""CommunicationBufferLocking AUTOSAR element.

References:
  - AUTOSAR_CP_TPS_SoftwareComponentTemplate.pdf (page 595)

JSON Source: docs/json/packages/M2_AUTOSARTemplates_SWComponentTemplate_SwcInternalBehavior_PortAPIOptions.classes.json"""

from __future__ import annotations
from typing import TYPE_CHECKING, Optional
import xml.etree.ElementTree as ET
from armodel.serialization import XMLMember

from armodel.models.M2.AUTOSARTemplates.SWComponentTemplate.SwcInternalBehavior.PortAPIOptions.swc_supported_feature import (
    SwcSupportedFeature,
)
from armodel.models.M2.AUTOSARTemplates.SWComponentTemplate.SwcInternalBehavior.PortAPIOptions import (
    SupportBufferLockingEnum,
)


class CommunicationBufferLocking(SwcSupportedFeature):
    """AUTOSAR CommunicationBufferLocking."""

    # XML member definitions for this class only (not inherited from parent classes)
    # Format: dict[str, XMLMember] for declarative metadata
    _xml_members: dict[str, "XMLMember"] = {
        "support_buffer_locking": XMLMember(
            xml_tag=None,
            is_attribute=False,
            multiplicity="0..1",
            element_class=SupportBufferLockingEnum,
        ),  # supportBufferLocking
    }

    def __init__(self) -> None:
        """Initialize CommunicationBufferLocking."""
        super().__init__()
        self.support_buffer_locking: Optional[SupportBufferLockingEnum] = None


class CommunicationBufferLockingBuilder:
    """Builder for CommunicationBufferLocking."""

    def __init__(self) -> None:
        """Initialize builder."""
        self._obj: CommunicationBufferLocking = CommunicationBufferLocking()

    def build(self) -> CommunicationBufferLocking:
        """Build and return CommunicationBufferLocking object.

        Returns:
            CommunicationBufferLocking instance
        """
        # TODO: Add validation
        return self._obj
