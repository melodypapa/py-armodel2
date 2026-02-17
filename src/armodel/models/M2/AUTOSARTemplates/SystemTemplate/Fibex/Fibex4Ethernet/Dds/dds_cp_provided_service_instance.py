"""DdsCpProvidedServiceInstance AUTOSAR element."""

from typing import Optional
import xml.etree.ElementTree as ET
from armodel.serialization import XMLMember

from armodel.models.M2.AUTOSARTemplates.SystemTemplate.Fibex.Fibex4Ethernet.Dds.dds_cp_service_instance import (
    DdsCpServiceInstance,
)
from armodel.models.M2.AUTOSARTemplates.GenericStructure.GeneralTemplateClasses.PrimitiveTypes import (
    PositiveInteger,
)
from armodel.models.M2.AUTOSARTemplates.SystemTemplate.Fibex.Fibex4Ethernet.EthernetTopology.application_endpoint import (
    ApplicationEndpoint,
)


class DdsCpProvidedServiceInstance(DdsCpServiceInstance):
    """AUTOSAR DdsCpProvidedServiceInstance."""

    # XML member definitions for this class only (not inherited from parent classes)
    # Format: dict[str, XMLMember] for declarative metadata
    _xml_members: dict[str, "XMLMember"] = {
        "local_unicast": XMLMember(
            xml_tag=None,
            is_attribute=False,
            multiplicity="0..1",
            element_class=ApplicationEndpoint,
        ),  # localUnicast
        "minor_version": XMLMember(
            xml_tag=None,
            is_attribute=True,
            multiplicity="0..1",
        ),  # minorVersion
        "provided_ddses": XMLMember(
            xml_tag=None,
            is_attribute=False,
            multiplicity="*",
            element_class=DdsCpServiceInstance,
        ),  # providedDdses
        "static_remotes": XMLMember(
            xml_tag=None,
            is_attribute=False,
            multiplicity="*",
            element_class=ApplicationEndpoint,
        ),  # staticRemotes
    }

    def __init__(self) -> None:
        """Initialize DdsCpProvidedServiceInstance."""
        super().__init__()
        self.local_unicast: Optional[ApplicationEndpoint] = None
        self.minor_version: Optional[PositiveInteger] = None
        self.provided_ddses: list[DdsCpServiceInstance] = []
        self.static_remotes: list[ApplicationEndpoint] = []


class DdsCpProvidedServiceInstanceBuilder:
    """Builder for DdsCpProvidedServiceInstance."""

    def __init__(self) -> None:
        """Initialize builder."""
        self._obj: DdsCpProvidedServiceInstance = DdsCpProvidedServiceInstance()

    def build(self) -> DdsCpProvidedServiceInstance:
        """Build and return DdsCpProvidedServiceInstance object.

        Returns:
            DdsCpProvidedServiceInstance instance
        """
        # TODO: Add validation
        return self._obj
