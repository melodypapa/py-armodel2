"""LinCommunicationConnector AUTOSAR element."""

from typing import Optional
import xml.etree.ElementTree as ET
from armodel.serialization import XMLMember

from armodel.models.M2.AUTOSARTemplates.SystemTemplate.Fibex.FibexCore.CoreTopology.communication_connector import (
    CommunicationConnector,
)
from armodel.models.M2.AUTOSARTemplates.GenericStructure.GeneralTemplateClasses.PrimitiveTypes import (
    Boolean,
    Integer,
)
from armodel.models.M2.AUTOSARTemplates.SystemTemplate.Fibex.Fibex4Lin.LinTopology.lin_configurable_frame import (
    LinConfigurableFrame,
)
from armodel.models.M2.AUTOSARTemplates.SystemTemplate.Fibex.Fibex4Lin.LinTopology.lin_ordered_configurable_frame import (
    LinOrderedConfigurableFrame,
)


class LinCommunicationConnector(CommunicationConnector):
    """AUTOSAR LinCommunicationConnector."""

    # XML member definitions for this class only (not inherited from parent classes)
    # Format: dict[str, XMLMember] for declarative metadata
    _xml_members: dict[str, "XMLMember"] = {
        "initial_nad": XMLMember(
            xml_tag=None,
            is_attribute=True,
            multiplicity="0..1",
        ),  # initialNad
        "lin_configurable_frames": XMLMember(
            xml_tag=None,
            is_attribute=False,
            multiplicity="*",
            element_class=LinConfigurableFrame,
        ),  # linConfigurableFrames
        "lin_ordereds": XMLMember(
            xml_tag=None,
            is_attribute=False,
            multiplicity="*",
            element_class=LinOrderedConfigurableFrame,
        ),  # linOrdereds
        "schedule": XMLMember(
            xml_tag=None,
            is_attribute=True,
            multiplicity="0..1",
        ),  # schedule
    }

    def __init__(self) -> None:
        """Initialize LinCommunicationConnector."""
        super().__init__()
        self.initial_nad: Optional[Integer] = None
        self.lin_configurable_frames: list[LinConfigurableFrame] = []
        self.lin_ordereds: list[LinOrderedConfigurableFrame] = []
        self.schedule: Optional[Boolean] = None


class LinCommunicationConnectorBuilder:
    """Builder for LinCommunicationConnector."""

    def __init__(self) -> None:
        """Initialize builder."""
        self._obj: LinCommunicationConnector = LinCommunicationConnector()

    def build(self) -> LinCommunicationConnector:
        """Build and return LinCommunicationConnector object.

        Returns:
            LinCommunicationConnector instance
        """
        # TODO: Add validation
        return self._obj
