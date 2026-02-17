"""PRPortPrototype AUTOSAR element.

References:
  - AUTOSAR_CP_TPS_BSWModuleDescriptionTemplate.pdf (page 325)
  - AUTOSAR_CP_TPS_SoftwareComponentTemplate.pdf (page 68)
  - AUTOSAR_CP_TPS_SystemTemplate.pdf (page 2042)
  - AUTOSAR_FO_TPS_StandardizationTemplate.pdf (page 199)

JSON Source: docs/json/packages/M2_AUTOSARTemplates_SWComponentTemplate_Components.classes.json"""

from __future__ import annotations
from typing import TYPE_CHECKING, Optional
import xml.etree.ElementTree as ET
from armodel.serialization import XMLMember

from armodel.models.M2.AUTOSARTemplates.SWComponentTemplate.Components.abstract_required_port_prototype import (
    AbstractRequiredPortPrototype,
)
from armodel.models.M2.AUTOSARTemplates.SWComponentTemplate.PortInterface.port_interface import (
    PortInterface,
)


class PRPortPrototype(AbstractRequiredPortPrototype):
    """AUTOSAR PRPortPrototype."""

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
        """Initialize PRPortPrototype."""
        super().__init__()
        self.provided: Optional[PortInterface] = None


class PRPortPrototypeBuilder:
    """Builder for PRPortPrototype."""

    def __init__(self) -> None:
        """Initialize builder."""
        self._obj: PRPortPrototype = PRPortPrototype()

    def build(self) -> PRPortPrototype:
        """Build and return PRPortPrototype object.

        Returns:
            PRPortPrototype instance
        """
        # TODO: Add validation
        return self._obj
