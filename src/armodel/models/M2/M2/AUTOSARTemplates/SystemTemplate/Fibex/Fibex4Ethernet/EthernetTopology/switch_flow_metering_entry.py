"""SwitchFlowMeteringEntry AUTOSAR element."""

from typing import Optional
import xml.etree.ElementTree as ET
from armodel.serialization import XMLMember

from armodel.models.M2.AUTOSARTemplates.GenericStructure.GeneralTemplateClasses.Identifiable.identifiable import (
    Identifiable,
)
from armodel.models.M2.AUTOSARTemplates.GenericStructure.GeneralTemplateClasses.PrimitiveTypes import (
    Boolean,
    PositiveInteger,
)


class SwitchFlowMeteringEntry(Identifiable):
    """AUTOSAR SwitchFlowMeteringEntry."""

    # XML member definitions for this class only (not inherited from parent classes)
    # Format: dict[str, XMLMember] for declarative metadata
    _xml_members: dict[str, "XMLMember"] = {
        "color_mode": XMLMember(
            xml_tag=None,
            is_attribute=False,
            multiplicity="0..1",
            element_class=FlowMeteringColorModeEnum,
        ),  # colorMode
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
        "coupling_flag": XMLMember(
            xml_tag=None,
            is_attribute=True,
            multiplicity="0..1",
        ),  # couplingFlag
        "excess_burst": XMLMember(
            xml_tag=None,
            is_attribute=True,
            multiplicity="0..1",
        ),  # excessBurst
        "excess": XMLMember(
            xml_tag=None,
            is_attribute=True,
            multiplicity="0..1",
        ),  # excess
    }

    def __init__(self) -> None:
        """Initialize SwitchFlowMeteringEntry."""
        super().__init__()
        self.color_mode: Optional[FlowMeteringColorModeEnum] = None
        self.committed_burst: Optional[PositiveInteger] = None
        self.committed: Optional[PositiveInteger] = None
        self.coupling_flag: Optional[Boolean] = None
        self.excess_burst: Optional[PositiveInteger] = None
        self.excess: Optional[PositiveInteger] = None


class SwitchFlowMeteringEntryBuilder:
    """Builder for SwitchFlowMeteringEntry."""

    def __init__(self) -> None:
        """Initialize builder."""
        self._obj: SwitchFlowMeteringEntry = SwitchFlowMeteringEntry()

    def build(self) -> SwitchFlowMeteringEntry:
        """Build and return SwitchFlowMeteringEntry object.

        Returns:
            SwitchFlowMeteringEntry instance
        """
        # TODO: Add validation
        return self._obj
