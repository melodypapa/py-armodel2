"""EcuTiming AUTOSAR element."""

from typing import Optional
import xml.etree.ElementTree as ET
from armodel.serialization import XMLMember

from armodel.models.M2.AUTOSARTemplates.CommonStructure.Timing.TimingExtensions.timing_extension import (
    TimingExtension,
)
from armodel.models.M2.AUTOSARTemplates.ECUCDescriptionTemplate.ecuc_value_collection import (
    EcucValueCollection,
)


class EcuTiming(TimingExtension):
    """AUTOSAR EcuTiming."""

    # XML member definitions for this class only (not inherited from parent classes)
    # Format: dict[str, XMLMember] for declarative metadata
    _xml_members: dict[str, "XMLMember"] = {
        "ecu": XMLMember(
            xml_tag=None,
            is_attribute=False,
            multiplicity="0..1",
            element_class=EcucValueCollection,
        ),  # ecu
    }

    def __init__(self) -> None:
        """Initialize EcuTiming."""
        super().__init__()
        self.ecu: Optional[EcucValueCollection] = None


class EcuTimingBuilder:
    """Builder for EcuTiming."""

    def __init__(self) -> None:
        """Initialize builder."""
        self._obj: EcuTiming = EcuTiming()

    def build(self) -> EcuTiming:
        """Build and return EcuTiming object.

        Returns:
            EcuTiming instance
        """
        # TODO: Add validation
        return self._obj
