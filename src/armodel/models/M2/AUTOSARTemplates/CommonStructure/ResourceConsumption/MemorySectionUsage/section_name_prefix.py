"""SectionNamePrefix AUTOSAR element.

References:
  - AUTOSAR_CP_TPS_BSWModuleDescriptionTemplate.pdf (page 147)
  - AUTOSAR_CP_TPS_SoftwareComponentTemplate.pdf (page 412)

JSON Source: docs/json/packages/M2_AUTOSARTemplates_CommonStructure_ResourceConsumption_MemorySectionUsage.classes.json"""

from typing import Optional
import xml.etree.ElementTree as ET
from armodel.serialization import XMLMember

from armodel.models.M2.AUTOSARTemplates.CommonStructure.Implementation.implementation_props import (
    ImplementationProps,
)
from armodel.models.M2.AUTOSARTemplates.CommonStructure.Implementation.dependency_on_artifact import (
    DependencyOnArtifact,
)


class SectionNamePrefix(ImplementationProps):
    """AUTOSAR SectionNamePrefix."""

    # XML member definitions for this class only (not inherited from parent classes)
    # Format: dict[str, XMLMember] for declarative metadata
    _xml_members: dict[str, "XMLMember"] = {
        "implemented_in": XMLMember(
            xml_tag=None,
            is_attribute=False,
            multiplicity="0..1",
            element_class=DependencyOnArtifact,
        ),  # implementedIn
    }

    def __init__(self) -> None:
        """Initialize SectionNamePrefix."""
        super().__init__()
        self.implemented_in: Optional[DependencyOnArtifact] = None


class SectionNamePrefixBuilder:
    """Builder for SectionNamePrefix."""

    def __init__(self) -> None:
        """Initialize builder."""
        self._obj: SectionNamePrefix = SectionNamePrefix()

    def build(self) -> SectionNamePrefix:
        """Build and return SectionNamePrefix object.

        Returns:
            SectionNamePrefix instance
        """
        # TODO: Add validation
        return self._obj
