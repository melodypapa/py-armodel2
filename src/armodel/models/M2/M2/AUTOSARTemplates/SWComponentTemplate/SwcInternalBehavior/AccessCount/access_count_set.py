"""AccessCountSet AUTOSAR element."""

from typing import Optional
import xml.etree.ElementTree as ET
from armodel.serialization import XMLMember

from armodel.models.M2.AUTOSARTemplates.GenericStructure.GeneralTemplateClasses.ar_object import ARObject
from armodel.models.M2.AUTOSARTemplates.GenericStructure.GeneralTemplateClasses.PrimitiveTypes import (
    NameToken,
)
from armodel.models.M2.AUTOSARTemplates.SWComponentTemplate.SwcInternalBehavior.AccessCount.access_count import (
    AccessCount,
)


class AccessCountSet(ARObject):
    """AUTOSAR AccessCountSet."""

    # XML member definitions for this class only (not inherited from parent classes)
    # Format: dict[str, XMLMember] for declarative metadata
    _xml_members: dict[str, "XMLMember"] = {
        "access_counts": XMLMember(
            xml_tag=None,
            is_attribute=False,
            multiplicity="*",
            element_class=AccessCount,
        ),  # accessCounts
        "count_profile": XMLMember(
            xml_tag=None,
            is_attribute=True,
            multiplicity="0..1",
        ),  # countProfile
    }

    def __init__(self) -> None:
        """Initialize AccessCountSet."""
        super().__init__()
        self.access_counts: list[AccessCount] = []
        self.count_profile: Optional[NameToken] = None


class AccessCountSetBuilder:
    """Builder for AccessCountSet."""

    def __init__(self) -> None:
        """Initialize builder."""
        self._obj: AccessCountSet = AccessCountSet()

    def build(self) -> AccessCountSet:
        """Build and return AccessCountSet object.

        Returns:
            AccessCountSet instance
        """
        # TODO: Add validation
        return self._obj
