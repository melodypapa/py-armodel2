"""SwComponentPrototype AUTOSAR element."""

from typing import Optional
import xml.etree.ElementTree as ET
from armodel.serialization import XMLMember

from armodel.models.M2.AUTOSARTemplates.GenericStructure.GeneralTemplateClasses.Identifiable.identifiable import (
    Identifiable,
)
from armodel.models.M2.AUTOSARTemplates.SWComponentTemplate.Components.sw_component_type import (
    SwComponentType,
)


class SwComponentPrototype(Identifiable):
    """AUTOSAR SwComponentPrototype."""

    # XML member definitions for this class only (not inherited from parent classes)
    # Format: dict[str, XMLMember] for declarative metadata
    _xml_members: dict[str, "XMLMember"] = {
        "type": XMLMember(
            xml_tag=None,
            is_attribute=False,
            multiplicity="0..1",
            element_class=SwComponentType,
        ),  # type
    }

    def __init__(self) -> None:
        """Initialize SwComponentPrototype."""
        super().__init__()
        self.type: Optional[SwComponentType] = None


class SwComponentPrototypeBuilder:
    """Builder for SwComponentPrototype."""

    def __init__(self) -> None:
        """Initialize builder."""
        self._obj: SwComponentPrototype = SwComponentPrototype()

    def build(self) -> SwComponentPrototype:
        """Build and return SwComponentPrototype object.

        Returns:
            SwComponentPrototype instance
        """
        # TODO: Add validation
        return self._obj
