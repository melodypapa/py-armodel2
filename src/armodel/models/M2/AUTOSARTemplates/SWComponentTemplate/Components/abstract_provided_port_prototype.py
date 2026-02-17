"""AbstractProvidedPortPrototype AUTOSAR element.

References:
  - AUTOSAR_CP_TPS_SoftwareComponentTemplate.pdf (page 67)

JSON Source: docs/json/packages/M2_AUTOSARTemplates_SWComponentTemplate_Components.classes.json"""

from typing import Optional
import xml.etree.ElementTree as ET
from armodel.serialization import XMLMember

from armodel.models.M2.AUTOSARTemplates.SWComponentTemplate.Components.port_prototype import (
    PortPrototype,
)
from armodel.models.M2.AUTOSARTemplates.SWComponentTemplate.Communication.p_port_com_spec import (
    PPortComSpec,
)


class AbstractProvidedPortPrototype(PortPrototype):
    """AUTOSAR AbstractProvidedPortPrototype."""
    """Abstract base class - do not instantiate directly."""

    # XML member definitions for this class only (not inherited from parent classes)
    # Format: dict[str, XMLMember] for declarative metadata
    _xml_members: dict[str, "XMLMember"] = {
        "provided_coms": XMLMember(
            xml_tag=None,
            is_attribute=False,
            multiplicity="*",
            element_class=PPortComSpec,
        ),  # providedComs
    }

    def __init__(self) -> None:
        """Initialize AbstractProvidedPortPrototype."""
        super().__init__()
        self.provided_coms: list[PPortComSpec] = []


class AbstractProvidedPortPrototypeBuilder:
    """Builder for AbstractProvidedPortPrototype."""

    def __init__(self) -> None:
        """Initialize builder."""
        self._obj: AbstractProvidedPortPrototype = AbstractProvidedPortPrototype()

    def build(self) -> AbstractProvidedPortPrototype:
        """Build and return AbstractProvidedPortPrototype object.

        Returns:
            AbstractProvidedPortPrototype instance
        """
        # TODO: Add validation
        return self._obj
