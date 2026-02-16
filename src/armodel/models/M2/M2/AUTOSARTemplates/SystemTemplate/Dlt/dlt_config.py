"""DltConfig AUTOSAR element."""

from typing import Optional
import xml.etree.ElementTree as ET
from armodel.serialization import XMLMember

from armodel.models.M2.AUTOSARTemplates.GenericStructure.GeneralTemplateClasses.ar_object import ARObject
from armodel.models.M2.AUTOSARTemplates.GenericStructure.GeneralTemplateClasses.PrimitiveTypes import (
    Boolean,
)
from armodel.models.M2.AUTOSARTemplates.LogAndTraceExtract.dlt_ecu import (
    DltEcu,
)
from armodel.models.M2.AUTOSARTemplates.SystemTemplate.Dlt.dlt_log_channel import (
    DltLogChannel,
)


class DltConfig(ARObject):
    """AUTOSAR DltConfig."""

    # XML member definitions for this class only (not inherited from parent classes)
    # Format: dict[str, XMLMember] for declarative metadata
    _xml_members: dict[str, "XMLMember"] = {
        "dlt_ecu": XMLMember(
            xml_tag=None,
            is_attribute=False,
            multiplicity="0..1",
            element_class=DltEcu,
        ),  # dltEcu
        "dlt_log_channels": XMLMember(
            xml_tag=None,
            is_attribute=False,
            multiplicity="*",
            element_class=DltLogChannel,
        ),  # dltLogChannels
        "session_id": XMLMember(
            xml_tag=None,
            is_attribute=True,
            multiplicity="0..1",
        ),  # sessionId
        "timestamp": XMLMember(
            xml_tag=None,
            is_attribute=True,
            multiplicity="0..1",
        ),  # timestamp
    }

    def __init__(self) -> None:
        """Initialize DltConfig."""
        super().__init__()
        self.dlt_ecu: Optional[DltEcu] = None
        self.dlt_log_channels: list[DltLogChannel] = []
        self.session_id: Optional[Boolean] = None
        self.timestamp: Optional[Boolean] = None


class DltConfigBuilder:
    """Builder for DltConfig."""

    def __init__(self) -> None:
        """Initialize builder."""
        self._obj: DltConfig = DltConfig()

    def build(self) -> DltConfig:
        """Build and return DltConfig object.

        Returns:
            DltConfig instance
        """
        # TODO: Add validation
        return self._obj
