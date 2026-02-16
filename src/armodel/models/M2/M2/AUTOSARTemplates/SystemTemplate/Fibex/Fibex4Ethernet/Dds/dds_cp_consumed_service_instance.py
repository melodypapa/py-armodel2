"""DdsCpConsumedServiceInstance AUTOSAR element."""

from typing import Optional
import xml.etree.ElementTree as ET
from armodel.serialization import XMLMember

from armodel.models.M2.AUTOSARTemplates.SystemTemplate.Fibex.Fibex4Ethernet.Dds.dds_cp_service_instance import (
    DdsCpServiceInstance,
)
from armodel.models.M2.AUTOSARTemplates.GenericStructure.GeneralTemplateClasses.PrimitiveTypes import (
    AnyVersionString,
)
from armodel.models.M2.AUTOSARTemplates.SystemTemplate.Fibex.Fibex4Ethernet.EthernetTopology.application_endpoint import (
    ApplicationEndpoint,
)
from armodel.models.M2.AUTOSARTemplates.SystemTemplate.Fibex.Fibex4Ethernet.Dds.dds_cp_service_instance import (
    DdsCpServiceInstance,
)


class DdsCpConsumedServiceInstance(DdsCpServiceInstance):
    """AUTOSAR DdsCpConsumedServiceInstance."""

    # XML member definitions for this class only (not inherited from parent classes)
    # Format: dict[str, XMLMember] for declarative metadata
    _xml_members: dict[str, "XMLMember"] = {
        "consumed_ddses": XMLMember(
            xml_tag=None,
            is_attribute=False,
            multiplicity="*",
            element_class=DdsCpServiceInstance,
        ),  # consumedDdses
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
        "static_remote": XMLMember(
            xml_tag=None,
            is_attribute=False,
            multiplicity="0..1",
            element_class=ApplicationEndpoint,
        ),  # staticRemote
    }

    def __init__(self) -> None:
        """Initialize DdsCpConsumedServiceInstance."""
        super().__init__()
        self.consumed_ddses: list[DdsCpServiceInstance] = []
        self.local_unicast: Optional[ApplicationEndpoint] = None
        self.minor_version: Optional[AnyVersionString] = None
        self.static_remote: Optional[ApplicationEndpoint] = None


class DdsCpConsumedServiceInstanceBuilder:
    """Builder for DdsCpConsumedServiceInstance."""

    def __init__(self) -> None:
        """Initialize builder."""
        self._obj: DdsCpConsumedServiceInstance = DdsCpConsumedServiceInstance()

    def build(self) -> DdsCpConsumedServiceInstance:
        """Build and return DdsCpConsumedServiceInstance object.

        Returns:
            DdsCpConsumedServiceInstance instance
        """
        # TODO: Add validation
        return self._obj
