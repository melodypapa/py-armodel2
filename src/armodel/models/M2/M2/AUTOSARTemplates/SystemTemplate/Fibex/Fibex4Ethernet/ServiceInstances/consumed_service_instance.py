"""ConsumedServiceInstance AUTOSAR element."""

from typing import Optional
import xml.etree.ElementTree as ET
from armodel.serialization import XMLMember

from armodel.models.M2.AUTOSARTemplates.SystemTemplate.Fibex.Fibex4Ethernet.ServiceInstances.abstract_service_instance import (
    AbstractServiceInstance,
)
from armodel.models.M2.AUTOSARTemplates.GenericStructure.GeneralTemplateClasses.PrimitiveTypes import (
    AnyServiceInstanceId,
    AnyVersionString,
    Boolean,
    PositiveInteger,
)
from armodel.models.M2.AUTOSARTemplates.SystemTemplate.Fibex.Fibex4Ethernet.EthernetTopology.application_endpoint import (
    ApplicationEndpoint,
)
from armodel.models.M2.AUTOSARTemplates.SystemTemplate.Fibex.Fibex4Ethernet.ServiceInstances.consumed_event_group import (
    ConsumedEventGroup,
)
from armodel.models.M2.AUTOSARTemplates.SystemTemplate.Fibex.Fibex4Ethernet.EthernetTopology.network_endpoint import (
    NetworkEndpoint,
)
from armodel.models.M2.AUTOSARTemplates.SystemTemplate.Fibex.Fibex4Ethernet.ServiceInstances.someip_sd_client_service_instance_config import (
    SomeipSdClientServiceInstanceConfig,
)
from armodel.models.M2.AUTOSARTemplates.SystemTemplate.Fibex.Fibex4Ethernet.ServiceInstances.someip_service_version import (
    SomeipServiceVersion,
)


class ConsumedServiceInstance(AbstractServiceInstance):
    """AUTOSAR ConsumedServiceInstance."""

    # XML member definitions for this class only (not inherited from parent classes)
    # Format: dict[str, XMLMember] for declarative metadata
    _xml_members: dict[str, "XMLMember"] = {
        "allowed_services": XMLMember(
            xml_tag=None,
            is_attribute=False,
            multiplicity="*",
            element_class=NetworkEndpoint,
        ),  # allowedServices
        "auto_require": XMLMember(
            xml_tag=None,
            is_attribute=True,
            multiplicity="0..1",
        ),  # autoRequire
        "blocklisteds": XMLMember(
            xml_tag=None,
            is_attribute=False,
            multiplicity="*",
            element_class=SomeipServiceVersion,
        ),  # blocklisteds
        "consumed_event_groups": XMLMember(
            xml_tag=None,
            is_attribute=False,
            multiplicity="*",
            element_class=ConsumedEventGroup,
        ),  # consumedEventGroups
        "event_multicast": XMLMember(
            xml_tag=None,
            is_attribute=False,
            multiplicity="0..1",
            element_class=ApplicationEndpoint,
        ),  # eventMulticast
        "instance": XMLMember(
            xml_tag=None,
            is_attribute=True,
            multiplicity="0..1",
        ),  # instance
        "local_unicast": XMLMember(
            xml_tag=None,
            is_attribute=False,
            multiplicity="1",
            element_class=ApplicationEndpoint,
        ),  # localUnicast
        "minor_version": XMLMember(
            xml_tag=None,
            is_attribute=True,
            multiplicity="0..1",
        ),  # minorVersion
        "provided_service": XMLMember(
            xml_tag=None,
            is_attribute=False,
            multiplicity="0..1",
            element_class=any (ProvidedService),
        ),  # providedService
        "remote_unicast": XMLMember(
            xml_tag=None,
            is_attribute=False,
            multiplicity="1",
            element_class=ApplicationEndpoint,
        ),  # remoteUnicast
        "sd_client_config": XMLMember(
            xml_tag=None,
            is_attribute=False,
            multiplicity="0..1",
            element_class=any (SdClientConfig),
        ),  # sdClientConfig
        "sd_client_timer": XMLMember(
            xml_tag=None,
            is_attribute=False,
            multiplicity="0..1",
            element_class=SomeipSdClientServiceInstanceConfig,
        ),  # sdClientTimer
        "service_identifier": XMLMember(
            xml_tag=None,
            is_attribute=True,
            multiplicity="0..1",
        ),  # serviceIdentifier
        "version_driven": XMLMember(
            xml_tag=None,
            is_attribute=False,
            multiplicity="0..1",
            element_class=any (ServiceVersion),
        ),  # versionDriven
    }

    def __init__(self) -> None:
        """Initialize ConsumedServiceInstance."""
        super().__init__()
        self.allowed_services: list[NetworkEndpoint] = []
        self.auto_require: Optional[Boolean] = None
        self.blocklisteds: list[SomeipServiceVersion] = []
        self.consumed_event_groups: list[ConsumedEventGroup] = []
        self.event_multicast: Optional[ApplicationEndpoint] = None
        self.instance: Optional[AnyServiceInstanceId] = None
        self.local_unicast: ApplicationEndpoint = None
        self.minor_version: Optional[AnyVersionString] = None
        self.provided_service: Optional[Any] = None
        self.remote_unicast: ApplicationEndpoint = None
        self.sd_client_config: Optional[Any] = None
        self.sd_client_timer: Optional[SomeipSdClientServiceInstanceConfig] = None
        self.service_identifier: Optional[PositiveInteger] = None
        self.version_driven: Optional[Any] = None


class ConsumedServiceInstanceBuilder:
    """Builder for ConsumedServiceInstance."""

    def __init__(self) -> None:
        """Initialize builder."""
        self._obj: ConsumedServiceInstance = ConsumedServiceInstance()

    def build(self) -> ConsumedServiceInstance:
        """Build and return ConsumedServiceInstance object.

        Returns:
            ConsumedServiceInstance instance
        """
        # TODO: Add validation
        return self._obj
