"""LinPhysicalChannel AUTOSAR element."""

from typing import Optional
import xml.etree.ElementTree as ET
from armodel.serialization import XMLMember

from armodel.models.M2.AUTOSARTemplates.SystemTemplate.Fibex.FibexCore.CoreTopology.physical_channel import (
    PhysicalChannel,
)
from armodel.models.M2.AUTOSARTemplates.GenericStructure.GeneralTemplateClasses.PrimitiveTypes import (
    TimeValue,
)
from armodel.models.M2.AUTOSARTemplates.SystemTemplate.Fibex.Fibex4Lin.LinCommunication.lin_schedule_table import (
    LinScheduleTable,
)


class LinPhysicalChannel(PhysicalChannel):
    """AUTOSAR LinPhysicalChannel."""

    # XML member definitions for this class only (not inherited from parent classes)
    # Format: dict[str, XMLMember] for declarative metadata
    _xml_members: dict[str, "XMLMember"] = {
        "bus_idle_timeout": XMLMember(
            xml_tag=None,
            is_attribute=True,
            multiplicity="0..1",
        ),  # busIdleTimeout
        "schedule_tables": XMLMember(
            xml_tag=None,
            is_attribute=False,
            multiplicity="*",
            element_class=LinScheduleTable,
        ),  # scheduleTables
    }

    def __init__(self) -> None:
        """Initialize LinPhysicalChannel."""
        super().__init__()
        self.bus_idle_timeout: Optional[TimeValue] = None
        self.schedule_tables: list[LinScheduleTable] = []


class LinPhysicalChannelBuilder:
    """Builder for LinPhysicalChannel."""

    def __init__(self) -> None:
        """Initialize builder."""
        self._obj: LinPhysicalChannel = LinPhysicalChannel()

    def build(self) -> LinPhysicalChannel:
        """Build and return LinPhysicalChannel object.

        Returns:
            LinPhysicalChannel instance
        """
        # TODO: Add validation
        return self._obj
