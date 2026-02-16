"""CouplingPortAsynchronousTrafficShaper AUTOSAR element."""

from typing import Optional
import xml.etree.ElementTree as ET
from armodel.serialization import XMLMember

from armodel.models.M2.AUTOSARTemplates.GenericStructure.GeneralTemplateClasses.Identifiable.identifiable import (
    Identifiable,
)
from armodel.models.M2.AUTOSARTemplates.GenericStructure.GeneralTemplateClasses.PrimitiveTypes import (
    PositiveInteger,
)
from armodel.models.M2.AUTOSARTemplates.SystemTemplate.Fibex.Fibex4Ethernet.EthernetTopology.switch_asynchronous_traffic_shaper_group_entry import (
    SwitchAsynchronousTrafficShaperGroupEntry,
)


class CouplingPortAsynchronousTrafficShaper(Identifiable):
    """AUTOSAR CouplingPortAsynchronousTrafficShaper."""

    # XML member definitions for this class only (not inherited from parent classes)
    # Format: dict[str, XMLMember] for declarative metadata
    _xml_members: dict[str, "XMLMember"] = {
        "committed_burst": XMLMember(
            xml_tag=None,
            is_attribute=True,
            multiplicity="0..1",
        ),  # committedBurst
        "committed": XMLMember(
            xml_tag=None,
            is_attribute=True,
            multiplicity="0..1",
        ),  # committed
        "traffic_shaper": XMLMember(
            xml_tag=None,
            is_attribute=False,
            multiplicity="0..1",
            element_class=SwitchAsynchronousTrafficShaperGroupEntry,
        ),  # trafficShaper
    }

    def __init__(self) -> None:
        """Initialize CouplingPortAsynchronousTrafficShaper."""
        super().__init__()
        self.committed_burst: Optional[PositiveInteger] = None
        self.committed: Optional[PositiveInteger] = None
        self.traffic_shaper: Optional[SwitchAsynchronousTrafficShaperGroupEntry] = None


class CouplingPortAsynchronousTrafficShaperBuilder:
    """Builder for CouplingPortAsynchronousTrafficShaper."""

    def __init__(self) -> None:
        """Initialize builder."""
        self._obj: CouplingPortAsynchronousTrafficShaper = CouplingPortAsynchronousTrafficShaper()

    def build(self) -> CouplingPortAsynchronousTrafficShaper:
        """Build and return CouplingPortAsynchronousTrafficShaper object.

        Returns:
            CouplingPortAsynchronousTrafficShaper instance
        """
        # TODO: Add validation
        return self._obj
