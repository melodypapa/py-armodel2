"""PPortPrototype AUTOSAR element."""

from typing import Optional
import xml.etree.ElementTree as ET
from armodel.serialization import XMLMember

from armodel.models.M2.AUTOSARTemplates.SWComponentTemplate.Components.abstract_provided_port_prototype import (
    AbstractProvidedPortPrototype,
)
from armodel.models.M2.AUTOSARTemplates.SWComponentTemplate.PortInterface.port_interface import (
    PortInterface,
)


class PPortPrototype(AbstractProvidedPortPrototype):
    """AUTOSAR PPortPrototype."""

    # XML member definitions for this class only (not inherited from parent classes)
    # Format: dict[str, XMLMember] for declarative metadata
    _xml_members: dict[str, "XMLMember"] = {
        "provided": XMLMember(
            xml_tag=None,
            is_attribute=False,
            multiplicity="0..1",
            element_class=PortInterface,
        ),  # provided
    }

    def __init__(self) -> None:
        """Initialize PPortPrototype."""
        super().__init__()
        self.provided: Optional[PortInterface] = None


class PPortPrototypeBuilder:
    """Builder for PPortPrototype."""

    def __init__(self) -> None:
        """Initialize builder."""
        self._obj: PPortPrototype = PPortPrototype()

    def build(self) -> PPortPrototype:
        """Build and return PPortPrototype object.

        Returns:
            PPortPrototype instance
        """
        # TODO: Add validation
        return self._obj
