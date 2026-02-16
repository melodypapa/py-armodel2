"""SwcToApplicationPartitionMapping AUTOSAR element."""

from typing import Optional
import xml.etree.ElementTree as ET
from armodel.serialization import XMLMember

from armodel.models.M2.AUTOSARTemplates.GenericStructure.GeneralTemplateClasses.Identifiable.identifiable import (
    Identifiable,
)
from armodel.models.M2.AUTOSARTemplates.SystemTemplate.SWmapping.application_partition import (
    ApplicationPartition,
)
from armodel.models.M2.AUTOSARTemplates.SWComponentTemplate.Composition.sw_component_prototype import (
    SwComponentPrototype,
)


class SwcToApplicationPartitionMapping(Identifiable):
    """AUTOSAR SwcToApplicationPartitionMapping."""

    # XML member definitions for this class only (not inherited from parent classes)
    # Format: dict[str, XMLMember] for declarative metadata
    _xml_members: dict[str, "XMLMember"] = {
        "application": XMLMember(
            xml_tag=None,
            is_attribute=False,
            multiplicity="0..1",
            element_class=ApplicationPartition,
        ),  # application
        "sw_component_prototype": XMLMember(
            xml_tag=None,
            is_attribute=False,
            multiplicity="0..1",
            element_class=SwComponentPrototype,
        ),  # swComponentPrototype
    }

    def __init__(self) -> None:
        """Initialize SwcToApplicationPartitionMapping."""
        super().__init__()
        self.application: Optional[ApplicationPartition] = None
        self.sw_component_prototype: Optional[SwComponentPrototype] = None


class SwcToApplicationPartitionMappingBuilder:
    """Builder for SwcToApplicationPartitionMapping."""

    def __init__(self) -> None:
        """Initialize builder."""
        self._obj: SwcToApplicationPartitionMapping = SwcToApplicationPartitionMapping()

    def build(self) -> SwcToApplicationPartitionMapping:
        """Build and return SwcToApplicationPartitionMapping object.

        Returns:
            SwcToApplicationPartitionMapping instance
        """
        # TODO: Add validation
        return self._obj
