"""Referrable AUTOSAR element."""

from typing import Optional
import xml.etree.ElementTree as ET
from armodel.serialization import XMLMember

from armodel.models.M2.AUTOSARTemplates.GenericStructure.GeneralTemplateClasses.ar_object import ARObject
from armodel.models.M2.AUTOSARTemplates.GenericStructure.GeneralTemplateClasses.PrimitiveTypes import (
    Identifier,
)
from armodel.models.M2.AUTOSARTemplates.GenericStructure.GeneralTemplateClasses.Identifiable.short_name_fragment import (
    ShortNameFragment,
)


class Referrable(ARObject):
    """AUTOSAR Referrable."""
    """Abstract base class - do not instantiate directly."""

    # XML member definitions for this class only (not inherited from parent classes)
    # Format: dict[str, XMLMember] for declarative metadata
    _xml_members: dict[str, "XMLMember"] = {
        "short_name": XMLMember(
            xml_tag=None,
            is_attribute=True,
            multiplicity="1",
        ),  # shortName
        "short_name_fragments": XMLMember(
            xml_tag=None,
            is_attribute=False,
            multiplicity="*",
            element_class=ShortNameFragment,
        ),  # shortNameFragments
    }

    def __init__(self) -> None:
        """Initialize Referrable."""
        super().__init__()
        self.short_name: Identifier = None
        self.short_name_fragments: list[ShortNameFragment] = []


class ReferrableBuilder:
    """Builder for Referrable."""

    def __init__(self) -> None:
        """Initialize builder."""
        self._obj: Referrable = Referrable()

    def build(self) -> Referrable:
        """Build and return Referrable object.

        Returns:
            Referrable instance
        """
        # TODO: Add validation
        return self._obj
