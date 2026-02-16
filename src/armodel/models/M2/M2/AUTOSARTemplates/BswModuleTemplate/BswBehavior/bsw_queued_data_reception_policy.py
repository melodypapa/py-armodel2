"""BswQueuedDataReceptionPolicy AUTOSAR element."""

from typing import Optional
import xml.etree.ElementTree as ET
from armodel.serialization import XMLMember

from armodel.models.M2.AUTOSARTemplates.GenericStructure.GeneralTemplateClasses.ar_object import ARObject
from armodel.models.M2.AUTOSARTemplates.GenericStructure.GeneralTemplateClasses.PrimitiveTypes import (
    PositiveInteger,
)


class BswQueuedDataReceptionPolicy(ARObject):
    """AUTOSAR BswQueuedDataReceptionPolicy."""

    # XML member definitions for this class only (not inherited from parent classes)
    # Format: dict[str, XMLMember] for declarative metadata
    _xml_members: dict[str, "XMLMember"] = {
        "queue_length": XMLMember(
            xml_tag=None,
            is_attribute=True,
            multiplicity="0..1",
        ),  # queueLength
    }

    def __init__(self) -> None:
        """Initialize BswQueuedDataReceptionPolicy."""
        super().__init__()
        self.queue_length: Optional[PositiveInteger] = None


class BswQueuedDataReceptionPolicyBuilder:
    """Builder for BswQueuedDataReceptionPolicy."""

    def __init__(self) -> None:
        """Initialize builder."""
        self._obj: BswQueuedDataReceptionPolicy = BswQueuedDataReceptionPolicy()

    def build(self) -> BswQueuedDataReceptionPolicy:
        """Build and return BswQueuedDataReceptionPolicy object.

        Returns:
            BswQueuedDataReceptionPolicy instance
        """
        # TODO: Add validation
        return self._obj
