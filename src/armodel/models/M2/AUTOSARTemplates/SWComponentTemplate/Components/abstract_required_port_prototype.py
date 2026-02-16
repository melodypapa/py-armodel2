"""AbstractRequiredPortPrototype AUTOSAR element."""

from typing import Optional
import xml.etree.ElementTree as ET
from armodel.serialization import XMLMember

from armodel.models.M2.AUTOSARTemplates.SWComponentTemplate.Components.port_prototype import (
    PortPrototype,
)
from armodel.models.M2.AUTOSARTemplates.SWComponentTemplate.Communication.r_port_com_spec import (
    RPortComSpec,
)


class AbstractRequiredPortPrototype(PortPrototype):
    """AUTOSAR AbstractRequiredPortPrototype."""
    """Abstract base class - do not instantiate directly."""

    # XML member definitions for this class only (not inherited from parent classes)
    # Format: dict[str, XMLMember] for declarative metadata
    _xml_members: dict[str, "XMLMember"] = {
        "required_coms": XMLMember(
            xml_tag=None,
            is_attribute=False,
            multiplicity="*",
            element_class=RPortComSpec,
        ),  # requiredComs
    }

    def __init__(self) -> None:
        """Initialize AbstractRequiredPortPrototype."""
        super().__init__()
        self.required_coms: list[RPortComSpec] = []


class AbstractRequiredPortPrototypeBuilder:
    """Builder for AbstractRequiredPortPrototype."""

    def __init__(self) -> None:
        """Initialize builder."""
        self._obj: AbstractRequiredPortPrototype = AbstractRequiredPortPrototype()

    def build(self) -> AbstractRequiredPortPrototype:
        """Build and return AbstractRequiredPortPrototype object.

        Returns:
            AbstractRequiredPortPrototype instance
        """
        # TODO: Add validation
        return self._obj
