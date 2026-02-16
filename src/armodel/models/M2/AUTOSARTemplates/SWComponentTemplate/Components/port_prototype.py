"""PortPrototype AUTOSAR element."""

from typing import Optional, cast
import xml.etree.ElementTree as ET
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
    # Format: (member_name, xml_tag_name, is_attribute, is_list, element_class)
    _xml_members = [
        ("client_servers", None, False, True, ClientServerAnnotation),  # clientServers
        ("delegated_port", None, False, False, DelegatedPortAnnotation),  # delegatedPort
        ("io_hw_abstraction_server_annotations", None, False, True, IoHwAbstractionServerAnnotation),  # ioHwAbstractionServerAnnotations
        ("mode_port_annotations", None, False, True, ModePortAnnotation),  # modePortAnnotations
        ("nv_data_port_annotations", None, False, True, NvDataPortAnnotation),  # nvDataPortAnnotations
        ("parameter_ports", None, False, True, ParameterPortAnnotation),  # parameterPorts
        ("sender_receivers", None, False, True, any (SenderReceiver)),  # senderReceivers
        ("trigger_port_annotations", None, False, True, TriggerPortAnnotation),  # triggerPortAnnotations
    ]

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

    def serialize(self, namespace: str, element: Optional[ET.Element] = None) -> ET.Element:
        """Convert PortPrototype to XML element.

        Args:
            namespace: XML namespace for the element
            element: Optional existing element to add members to (for subclass chaining)

        Returns:
            XML element representing this object
        """
        # ARObject.serialize() handles entire class hierarchy automatically
        return super().serialize(namespace, element)

    @classmethod
    def deserialize(cls, element: ET.Element) -> "PortPrototype":
        """Create PortPrototype from XML element.

        Args:
            element: XML element to deserialize from

        Returns:
            PortPrototype instance
        """
        # ARObject.deserialize() handles entire class hierarchy automatically
        obj = super().deserialize(element)
        # Cast to PortPrototype since parent returns ARObject
        return cast("PortPrototype", obj)


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
