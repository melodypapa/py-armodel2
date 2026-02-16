"""BusMirrorChannelMappingUserDefined AUTOSAR element."""

from typing import Optional
import xml.etree.ElementTree as ET
from armodel.serialization import XMLMember

from armodel.models.M2.AUTOSARTemplates.SystemTemplate.BusMirror.bus_mirror_channel_mapping import (
    BusMirrorChannelMapping,
)
from armodel.models.M2.AUTOSARTemplates.GenericStructure.GeneralTemplateClasses.PrimitiveTypes import (
    TimeValue,
)


class BusMirrorChannelMappingUserDefined(BusMirrorChannelMapping):
    """AUTOSAR BusMirrorChannelMappingUserDefined."""

    # XML member definitions for this class only (not inherited from parent classes)
    # Format: dict[str, XMLMember] for declarative metadata
    _xml_members: dict[str, "XMLMember"] = {
        "transmission": XMLMember(
            xml_tag=None,
            is_attribute=True,
            multiplicity="0..1",
        ),  # transmission
    }

    def __init__(self) -> None:
        """Initialize BusMirrorChannelMappingUserDefined."""
        super().__init__()
        self.transmission: Optional[TimeValue] = None


class BusMirrorChannelMappingUserDefinedBuilder:
    """Builder for BusMirrorChannelMappingUserDefined."""

    def __init__(self) -> None:
        """Initialize builder."""
        self._obj: BusMirrorChannelMappingUserDefined = BusMirrorChannelMappingUserDefined()

    def build(self) -> BusMirrorChannelMappingUserDefined:
        """Build and return BusMirrorChannelMappingUserDefined object.

        Returns:
            BusMirrorChannelMappingUserDefined instance
        """
        # TODO: Add validation
        return self._obj
