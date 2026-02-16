"""AssemblySwConnector AUTOSAR element."""

from typing import Optional
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


class AssemblySwConnector(SwConnector):
    """AUTOSAR AssemblySwConnector."""

    # XML member definitions for this class only (not inherited from parent classes)
    # Format: dict[str, XMLMember] for declarative metadata
    _xml_members: dict[str, "XMLMember"] = {
        "provider_instance_ref": XMLMember(
            xml_tag=None,
            is_attribute=False,
            multiplicity="0..1",
            element_class=AbstractProvidedPortPrototype,
        ),  # providerInstanceRef
        "requester_instance_ref": XMLMember(
            xml_tag=None,
            is_attribute=False,
            multiplicity="0..1",
            element_class=AbstractRequiredPortPrototype,
        ),  # requesterInstanceRef
    }

    def __init__(self) -> None:
        """Initialize AssemblySwConnector."""
        super().__init__()
        self.provider_instance_ref: Optional[AbstractProvidedPortPrototype] = None
        self.requester_instance_ref: Optional[AbstractRequiredPortPrototype] = None


class AssemblySwConnectorBuilder:
    """Builder for AssemblySwConnector."""

    def __init__(self) -> None:
        """Initialize builder."""
        self._obj: AssemblySwConnector = AssemblySwConnector()

    def build(self) -> AssemblySwConnector:
        """Build and return AssemblySwConnector object.

        Returns:
            AssemblySwConnector instance
        """
        # TODO: Add validation
        return self._obj
