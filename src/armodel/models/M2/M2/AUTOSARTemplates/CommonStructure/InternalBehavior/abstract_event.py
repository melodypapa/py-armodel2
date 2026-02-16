"""AbstractEvent AUTOSAR element."""

from typing import Optional
import xml.etree.ElementTree as ET
from armodel.serialization import XMLMember

from armodel.models.M2.AUTOSARTemplates.GenericStructure.GeneralTemplateClasses.Identifiable.identifiable import (
    Identifiable,
)
from armodel.models.M2.AUTOSARTemplates.CommonStructure.InternalBehavior.executable_entity import (
    ExecutableEntity,
)


class AbstractEvent(Identifiable):
    """AUTOSAR AbstractEvent."""
    """Abstract base class - do not instantiate directly."""

    # XML member definitions for this class only (not inherited from parent classes)
    # Format: dict[str, XMLMember] for declarative metadata
    _xml_members: dict[str, "XMLMember"] = {
        "activation": XMLMember(
            xml_tag=None,
            is_attribute=False,
            multiplicity="0..1",
            element_class=ExecutableEntity,
        ),  # activation
    }

    def __init__(self) -> None:
        """Initialize AbstractEvent."""
        super().__init__()
        self.activation: Optional[ExecutableEntity] = None


class AbstractEventBuilder:
    """Builder for AbstractEvent."""

    def __init__(self) -> None:
        """Initialize builder."""
        self._obj: AbstractEvent = AbstractEvent()

    def build(self) -> AbstractEvent:
        """Build and return AbstractEvent object.

        Returns:
            AbstractEvent instance
        """
        # TODO: Add validation
        return self._obj
