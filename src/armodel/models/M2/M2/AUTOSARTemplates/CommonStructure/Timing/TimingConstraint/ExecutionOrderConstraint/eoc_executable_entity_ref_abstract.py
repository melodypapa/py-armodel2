"""EOCExecutableEntityRefAbstract AUTOSAR element."""

from typing import Optional
import xml.etree.ElementTree as ET
from armodel.serialization import XMLMember

from armodel.models.M2.AUTOSARTemplates.GenericStructure.GeneralTemplateClasses.Identifiable.identifiable import (
    Identifiable,
)


class EOCExecutableEntityRefAbstract(Identifiable):
    """AUTOSAR EOCExecutableEntityRefAbstract."""
    """Abstract base class - do not instantiate directly."""

    # XML member definitions for this class only (not inherited from parent classes)
    # Format: dict[str, XMLMember] for declarative metadata
    _xml_members: dict[str, "XMLMember"] = {
        "direct_successors": XMLMember(
            xml_tag=None,
            is_attribute=False,
            multiplicity="*",
            element_class=any (EOCExecutableEntity),
        ),  # directSuccessors
    }

    def __init__(self) -> None:
        """Initialize EOCExecutableEntityRefAbstract."""
        super().__init__()
        self.direct_successors: list[Any] = []


class EOCExecutableEntityRefAbstractBuilder:
    """Builder for EOCExecutableEntityRefAbstract."""

    def __init__(self) -> None:
        """Initialize builder."""
        self._obj: EOCExecutableEntityRefAbstract = EOCExecutableEntityRefAbstract()

    def build(self) -> EOCExecutableEntityRefAbstract:
        """Build and return EOCExecutableEntityRefAbstract object.

        Returns:
            EOCExecutableEntityRefAbstract instance
        """
        # TODO: Add validation
        return self._obj
