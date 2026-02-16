"""IEEE1722TpAcfBusPart AUTOSAR element."""

from typing import Optional
import xml.etree.ElementTree as ET
from armodel.serialization import XMLMember

from armodel.models.M2.AUTOSARTemplates.GenericStructure.GeneralTemplateClasses.Identifiable.identifiable import (
    Identifiable,
)


class IEEE1722TpAcfBusPart(Identifiable):
    """AUTOSAR IEEE1722TpAcfBusPart."""
    """Abstract base class - do not instantiate directly."""

    # XML member definitions for this class only (not inherited from parent classes)
    # Format: dict[str, XMLMember] for declarative metadata
    _xml_members: dict[str, "XMLMember"] = {
        "collection_trigger": XMLMember(
            xml_tag=None,
            is_attribute=False,
            multiplicity="0..1",
            element_class=PduCollectionTriggerEnum,
        ),  # collectionTrigger
    }

    def __init__(self) -> None:
        """Initialize IEEE1722TpAcfBusPart."""
        super().__init__()
        self.collection_trigger: Optional[PduCollectionTriggerEnum] = None


class IEEE1722TpAcfBusPartBuilder:
    """Builder for IEEE1722TpAcfBusPart."""

    def __init__(self) -> None:
        """Initialize builder."""
        self._obj: IEEE1722TpAcfBusPart = IEEE1722TpAcfBusPart()

    def build(self) -> IEEE1722TpAcfBusPart:
        """Build and return IEEE1722TpAcfBusPart object.

        Returns:
            IEEE1722TpAcfBusPart instance
        """
        # TODO: Add validation
        return self._obj
