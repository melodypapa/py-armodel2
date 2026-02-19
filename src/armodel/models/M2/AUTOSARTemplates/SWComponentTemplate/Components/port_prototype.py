"""PortPrototype AUTOSAR element.

References:
  - AUTOSAR_CP_TPS_BSWModuleDescriptionTemplate.pdf (page 326)
  - AUTOSAR_CP_TPS_DiagnosticExtractTemplate.pdf (page 326)
  - AUTOSAR_CP_TPS_ECUConfiguration.pdf (page 304)
  - AUTOSAR_CP_TPS_ECUResourceTemplate.pdf (page 62)
  - AUTOSAR_CP_TPS_SoftwareComponentTemplate.pdf (page 66)
  - AUTOSAR_CP_TPS_SystemTemplate.pdf (page 2047)
  - AUTOSAR_CP_TPS_TimingExtensions.pdf (page 236)
  - AUTOSAR_FO_TPS_ARXMLSerializationRules.pdf (page 30)
  - AUTOSAR_FO_TPS_AbstractPlatformSpecification.pdf (page 48)
  - AUTOSAR_FO_TPS_FeatureModelExchangeFormat.pdf (page 76)
  - AUTOSAR_FO_TPS_GenericStructureTemplate.pdf (page 458)
  - AUTOSAR_FO_TPS_LogAndTraceExtract.pdf (page 33)
  - AUTOSAR_FO_TPS_SecurityExtractTemplate.pdf (page 65)
  - AUTOSAR_FO_TPS_StandardizationTemplate.pdf (page 201)

JSON Source: docs/json/packages/M2_AUTOSARTemplates_SWComponentTemplate_Components.classes.json"""

from __future__ import annotations
from typing import TYPE_CHECKING, Optional, Any
import xml.etree.ElementTree as ET

from armodel.models.M2.AUTOSARTemplates.GenericStructure.GeneralTemplateClasses.Identifiable.identifiable import (
    Identifiable,
)
from armodel.models.M2.AUTOSARTemplates.GenericStructure.GeneralTemplateClasses.ArObject.ar_object import ARObject
from armodel.models.M2.AUTOSARTemplates.GenericStructure.GeneralTemplateClasses.ArObject.ar_ref import ARRef
from armodel.models.M2.AUTOSARTemplates.SWComponentTemplate.ApplicationAttributes.client_server_annotation import (
    ClientServerAnnotation,
)
from armodel.models.M2.AUTOSARTemplates.SWComponentTemplate.ApplicationAttributes.delegated_port_annotation import (
    DelegatedPortAnnotation,
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

if TYPE_CHECKING:
    from armodel.models.M2.AUTOSARTemplates.SWComponentTemplate.ApplicationAttributes.io_hw_abstraction_server_annotation import (
        IoHwAbstractionServerAnnotation,
    )

from abc import ABC, abstractmethod


class PortPrototype(Identifiable, ABC):
    """AUTOSAR PortPrototype."""

    @property
    def is_abstract(self) -> bool:
        """Check if this class is abstract.

        Returns:
            True for abstract classes
        """
        return True

    client_servers: list[ClientServerAnnotation]
    delegated_port: Optional[DelegatedPortAnnotation]
    io_hw_abstraction_server_annotations: list[IoHwAbstractionServerAnnotation]
    mode_port_annotations: list[ModePortAnnotation]
    nv_data_port_annotations: list[NvDataPortAnnotation]
    parameter_ports: list[ParameterPortAnnotation]
    sender_receivers: list[Any]
    trigger_port_annotation_refs: list[ARRef]
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
        self.trigger_port_annotation_refs: list[ARRef] = []
    @classmethod
    def deserialize(cls, element: ET.Element) -> "PortPrototype":
        """Deserialize XML element to PortPrototype object.

        Args:
            element: XML element to deserialize from

        Returns:
            Deserialized PortPrototype object
        """
        # Create instance and initialize with default values
        obj = cls.__new__(cls)
        obj.__init__()

        # Parse client_servers (list)
        obj.client_servers = []
        for child in ARObject._find_all_child_elements(element, "CLIENT-SERVERS"):
            client_servers_value = ARObject._deserialize_by_tag(child, "ClientServerAnnotation")
            obj.client_servers.append(client_servers_value)

        # Parse delegated_port
        child = ARObject._find_child_element(element, "DELEGATED-PORT")
        if child is not None:
            delegated_port_value = ARObject._deserialize_by_tag(child, "DelegatedPortAnnotation")
            obj.delegated_port = delegated_port_value

        # Parse io_hw_abstraction_server_annotations (list)
        obj.io_hw_abstraction_server_annotations = []
        for child in ARObject._find_all_child_elements(element, "IO-HW-ABSTRACTION-SERVER-ANNOTATIONS"):
            io_hw_abstraction_server_annotations_value = ARObject._deserialize_by_tag(child, "IoHwAbstractionServerAnnotation")
            obj.io_hw_abstraction_server_annotations.append(io_hw_abstraction_server_annotations_value)

        # Parse mode_port_annotations (list)
        obj.mode_port_annotations = []
        for child in ARObject._find_all_child_elements(element, "MODE-PORT-ANNOTATIONS"):
            mode_port_annotations_value = ARObject._deserialize_by_tag(child, "ModePortAnnotation")
            obj.mode_port_annotations.append(mode_port_annotations_value)

        # Parse nv_data_port_annotations (list)
        obj.nv_data_port_annotations = []
        for child in ARObject._find_all_child_elements(element, "NV-DATA-PORT-ANNOTATIONS"):
            nv_data_port_annotations_value = ARObject._deserialize_by_tag(child, "NvDataPortAnnotation")
            obj.nv_data_port_annotations.append(nv_data_port_annotations_value)

        # Parse parameter_ports (list)
        obj.parameter_ports = []
        for child in ARObject._find_all_child_elements(element, "PARAMETER-PORTS"):
            parameter_ports_value = ARObject._deserialize_by_tag(child, "ParameterPortAnnotation")
            obj.parameter_ports.append(parameter_ports_value)

        # Parse sender_receivers (list)
        obj.sender_receivers = []
        for child in ARObject._find_all_child_elements(element, "SENDER-RECEIVERS"):
            sender_receivers_value = child.text
            obj.sender_receivers.append(sender_receivers_value)

        # Parse trigger_port_annotation_refs (list)
        obj.trigger_port_annotation_refs = []
        for child in ARObject._find_all_child_elements(element, "TRIGGER-PORT-ANNOTATIONS"):
            trigger_port_annotation_refs_value = ARObject._deserialize_by_tag(child, "TriggerPortAnnotation")
            obj.trigger_port_annotation_refs.append(trigger_port_annotation_refs_value)

        return obj



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
