"""PortPrototype AUTOSAR element."""

from typing import Optional
import xml.etree.ElementTree as ET
from armodel.serialization import XMLMember

from armodel.models.M2.AUTOSARTemplates.GenericStructure.GeneralTemplateClasses.Identifiable.identifiable import (
    Identifiable,
)
from armodel.models.M2.AUTOSARTemplates.SWComponentTemplate.ApplicationAttributes.client_server_annotation import (
    ClientServerAnnotation,
)
from armodel.models.M2.AUTOSARTemplates.SWComponentTemplate.ApplicationAttributes.delegated_port_annotation import (
    DelegatedPortAnnotation,
)
from armodel.models.M2.AUTOSARTemplates.SWComponentTemplate.ApplicationAttributes.io_hw_abstraction_server_annotation import (
    IoHwAbstractionServerAnnotation,
)
from armodel.models.M2.AUTOSARTemplates.SWComponentTemplate.ApplicationAttributes.mode_port_annotation import (
    ModePortAnnotation,
)
from armodel.models.M2.AUTOSARTemplates.SWComponentTemplate.ApplicationAttributes.nv_data_port_annotation import (
    NvDataPortAnnotation,
)
from armodel.models.M2.AUTOSARTemplates.SWComponentTemplate.ApplicationAttributes.parameter_port_annotation import (
    ParameterPortAnnotation,
)
from armodel.models.M2.AUTOSARTemplates.SWComponentTemplate.ApplicationAttributes.trigger_port_annotation import (
    TriggerPortAnnotation,
)


class PortPrototype(Identifiable):
    """AUTOSAR PortPrototype."""
    """Abstract base class - do not instantiate directly."""

    # XML member definitions for this class only (not inherited from parent classes)
    # Format: dict[str, XMLMember] for declarative metadata
    _xml_members: dict[str, "XMLMember"] = {
        "client_servers": XMLMember(
            xml_tag=None,
            is_attribute=False,
            multiplicity="*",
            element_class=ClientServerAnnotation,
        ),  # clientServers
        "delegated_port": XMLMember(
            xml_tag=None,
            is_attribute=False,
            multiplicity="0..1",
            element_class=DelegatedPortAnnotation,
        ),  # delegatedPort
        "io_hw_abstraction_server_annotations": XMLMember(
            xml_tag=None,
            is_attribute=False,
            multiplicity="*",
            element_class=IoHwAbstractionServerAnnotation,
        ),  # ioHwAbstractionServerAnnotations
        "mode_port_annotations": XMLMember(
            xml_tag=None,
            is_attribute=False,
            multiplicity="*",
            element_class=ModePortAnnotation,
        ),  # modePortAnnotations
        "nv_data_port_annotations": XMLMember(
            xml_tag=None,
            is_attribute=False,
            multiplicity="*",
            element_class=NvDataPortAnnotation,
        ),  # nvDataPortAnnotations
        "parameter_ports": XMLMember(
            xml_tag=None,
            is_attribute=False,
            multiplicity="*",
            element_class=ParameterPortAnnotation,
        ),  # parameterPorts
        "sender_receivers": XMLMember(
            xml_tag=None,
            is_attribute=False,
            multiplicity="*",
            element_class=any (SenderReceiver),
        ),  # senderReceivers
        "trigger_port_annotations": XMLMember(
            xml_tag=None,
            is_attribute=False,
            multiplicity="*",
            element_class=TriggerPortAnnotation,
        ),  # triggerPortAnnotations
    }

    def __init__(self) -> None:
        """Initialize PortPrototype."""
        super().__init__()
        self.client_servers: list[ClientServerAnnotation] = []
        self.delegated_port: Optional[DelegatedPortAnnotation] = None
        self.io_hw_abstraction_server_annotations: list[IoHwAbstractionServerAnnotation] = []
        self.mode_port_annotations: list[ModePortAnnotation] = []
        self.nv_data_port_annotations: list[NvDataPortAnnotation] = []
        self.parameter_ports: list[ParameterPortAnnotation] = []
        self.sender_receivers: list[Any] = []
        self.trigger_port_annotations: list[TriggerPortAnnotation] = []


class PortPrototypeBuilder:
    """Builder for PortPrototype."""

    def __init__(self) -> None:
        """Initialize builder."""
        self._obj: PortPrototype = PortPrototype()

    def build(self) -> PortPrototype:
        """Build and return PortPrototype object.

        Returns:
            PortPrototype instance
        """
        # TODO: Add validation
        return self._obj
