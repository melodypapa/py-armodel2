"""SwcBswSynchronizedTrigger AUTOSAR element."""

from typing import Optional
import xml.etree.ElementTree as ET
from armodel.serialization import XMLMember

from armodel.models.M2.AUTOSARTemplates.GenericStructure.GeneralTemplateClasses.ar_object import ARObject
from armodel.models.M2.AUTOSARTemplates.CommonStructure.TriggerDeclaration.trigger import (
    Trigger,
)


class SwcBswSynchronizedTrigger(ARObject):
    """AUTOSAR SwcBswSynchronizedTrigger."""

    # XML member definitions for this class only (not inherited from parent classes)
    # Format: dict[str, XMLMember] for declarative metadata
    _xml_members: dict[str, "XMLMember"] = {
        "bsw_trigger": XMLMember(
            xml_tag=None,
            is_attribute=False,
            multiplicity="0..1",
            element_class=Trigger,
        ),  # bswTrigger
        "swc_trigger": XMLMember(
            xml_tag=None,
            is_attribute=False,
            multiplicity="0..1",
            element_class=Trigger,
        ),  # swcTrigger
    }

    def __init__(self) -> None:
        """Initialize SwcBswSynchronizedTrigger."""
        super().__init__()
        self.bsw_trigger: Optional[Trigger] = None
        self.swc_trigger: Optional[Trigger] = None


class SwcBswSynchronizedTriggerBuilder:
    """Builder for SwcBswSynchronizedTrigger."""

    def __init__(self) -> None:
        """Initialize builder."""
        self._obj: SwcBswSynchronizedTrigger = SwcBswSynchronizedTrigger()

    def build(self) -> SwcBswSynchronizedTrigger:
        """Build and return SwcBswSynchronizedTrigger object.

        Returns:
            SwcBswSynchronizedTrigger instance
        """
        # TODO: Add validation
        return self._obj
