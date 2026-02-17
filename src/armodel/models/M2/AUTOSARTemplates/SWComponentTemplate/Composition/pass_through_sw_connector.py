"""PassThroughSwConnector AUTOSAR element.

References:
  - AUTOSAR_CP_TPS_SoftwareComponentTemplate.pdf (page 83)
  - AUTOSAR_CP_TPS_SystemTemplate.pdf (page 2043)

JSON Source: docs/json/packages/M2_AUTOSARTemplates_SWComponentTemplate_Composition.classes.json"""

from __future__ import annotations
from typing import TYPE_CHECKING, Optional
import xml.etree.ElementTree as ET
from armodel.serialization import XMLMember

from armodel.models.M2.AUTOSARTemplates.SWComponentTemplate.Composition.sw_connector import (
    SwConnector,
)
from armodel.models.M2.AUTOSARTemplates.SWComponentTemplate.Components.abstract_provided_port_prototype import (
    AbstractProvidedPortPrototype,
)
from armodel.models.M2.AUTOSARTemplates.SWComponentTemplate.Components.abstract_required_port_prototype import (
    AbstractRequiredPortPrototype,
)


class PassThroughSwConnector(SwConnector):
    """AUTOSAR PassThroughSwConnector."""

    # XML member definitions for this class only (not inherited from parent classes)
    # Format: dict[str, XMLMember] for declarative metadata
    _xml_members: dict[str, "XMLMember"] = {
        "provided_outer": XMLMember(
            xml_tag=None,
            is_attribute=False,
            multiplicity="0..1",
            element_class=AbstractProvidedPortPrototype,
        ),  # providedOuter
        "required_outer": XMLMember(
            xml_tag=None,
            is_attribute=False,
            multiplicity="0..1",
            element_class=AbstractRequiredPortPrototype,
        ),  # requiredOuter
    }

    def __init__(self) -> None:
        """Initialize PassThroughSwConnector."""
        super().__init__()
        self.provided_outer: Optional[AbstractProvidedPortPrototype] = None
        self.required_outer: Optional[AbstractRequiredPortPrototype] = None


class PassThroughSwConnectorBuilder:
    """Builder for PassThroughSwConnector."""

    def __init__(self) -> None:
        """Initialize builder."""
        self._obj: PassThroughSwConnector = PassThroughSwConnector()

    def build(self) -> PassThroughSwConnector:
        """Build and return PassThroughSwConnector object.

        Returns:
            PassThroughSwConnector instance
        """
        # TODO: Add validation
        return self._obj
