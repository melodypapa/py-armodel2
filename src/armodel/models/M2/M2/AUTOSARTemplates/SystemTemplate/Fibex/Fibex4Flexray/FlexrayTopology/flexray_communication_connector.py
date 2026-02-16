"""FlexrayCommunicationConnector AUTOSAR element."""

from typing import Optional
import xml.etree.ElementTree as ET
from armodel.serialization import XMLMember

from armodel.models.M2.AUTOSARTemplates.SystemTemplate.Fibex.FibexCore.CoreTopology.communication_connector import (
    CommunicationConnector,
)
from armodel.models.M2.AUTOSARTemplates.GenericStructure.GeneralTemplateClasses.PrimitiveTypes import (
    Boolean,
    Float,
)


class FlexrayCommunicationConnector(CommunicationConnector):
    """AUTOSAR FlexrayCommunicationConnector."""

    # XML member definitions for this class only (not inherited from parent classes)
    # Format: dict[str, XMLMember] for declarative metadata
    _xml_members: dict[str, "XMLMember"] = {
        "nm_ready_sleep": XMLMember(
            xml_tag=None,
            is_attribute=True,
            multiplicity="0..1",
        ),  # nmReadySleep
        "wake_up": XMLMember(
            xml_tag=None,
            is_attribute=True,
            multiplicity="0..1",
        ),  # wakeUp
    }

    def __init__(self) -> None:
        """Initialize FlexrayCommunicationConnector."""
        super().__init__()
        self.nm_ready_sleep: Optional[Float] = None
        self.wake_up: Optional[Boolean] = None


class FlexrayCommunicationConnectorBuilder:
    """Builder for FlexrayCommunicationConnector."""

    def __init__(self) -> None:
        """Initialize builder."""
        self._obj: FlexrayCommunicationConnector = FlexrayCommunicationConnector()

    def build(self) -> FlexrayCommunicationConnector:
        """Build and return FlexrayCommunicationConnector object.

        Returns:
            FlexrayCommunicationConnector instance
        """
        # TODO: Add validation
        return self._obj
