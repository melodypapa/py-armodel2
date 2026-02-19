"""SenderComSpec AUTOSAR element.

References:
  - AUTOSAR_CP_TPS_SoftwareComponentTemplate.pdf (page 178)
  - AUTOSAR_CP_TPS_SystemTemplate.pdf (page 2054)

JSON Source: docs/json/packages/M2_AUTOSARTemplates_SWComponentTemplate_Communication.classes.json"""

from __future__ import annotations
from typing import TYPE_CHECKING, Optional, Any
import xml.etree.ElementTree as ET

from armodel.models.M2.AUTOSARTemplates.SWComponentTemplate.Communication.p_port_com_spec import (
    PPortComSpec,
)
from armodel.models.M2.AUTOSARTemplates.GenericStructure.GeneralTemplateClasses.ArObject.ar_object import ARObject
from armodel.models.M2.AUTOSARTemplates.GenericStructure.GeneralTemplateClasses.ArObject.ar_ref import ARRef
from armodel.models.M2.AUTOSARTemplates.GenericStructure.GeneralTemplateClasses.PrimitiveTypes import (
    Boolean,
)
from armodel.models.M2.AUTOSARTemplates.SWComponentTemplate.Datatype.DataPrototypes.autosar_data_prototype import (
    AutosarDataPrototype,
)
from armodel.models.M2.AUTOSARTemplates.SWComponentTemplate.Communication.composite_network_representation import (
    CompositeNetworkRepresentation,
)
from armodel.models.M2.AUTOSARTemplates.SWComponentTemplate.Communication.transmission_com_spec_props import (
    TransmissionComSpecProps,
)

if TYPE_CHECKING:
    from armodel.models.M2.MSR.DataDictionary.DataDefProperties.sw_data_def_props import (
        SwDataDefProps,
    )

from abc import ABC, abstractmethod


class SenderComSpec(PPortComSpec, ABC):
    """AUTOSAR SenderComSpec."""

    @property
    def is_abstract(self) -> bool:
        """Check if this class is abstract.

        Returns:
            True for abstract classes
        """
        return True

    composite_networks: list[CompositeNetworkRepresentation]
    data_element_ref: Optional[ARRef]
    handle_out_of_range: Optional[Any]
    network: Optional[SwDataDefProps]
    transmission: Optional[Any]
    transmission_com_spec: Optional[TransmissionComSpecProps]
    uses_end_to_end: Optional[Boolean]
    def __init__(self) -> None:
        """Initialize SenderComSpec."""
        super().__init__()
        self.composite_networks: list[CompositeNetworkRepresentation] = []
        self.data_element_ref: Optional[ARRef] = None
        self.handle_out_of_range: Optional[Any] = None
        self.network: Optional[SwDataDefProps] = None
        self.transmission: Optional[Any] = None
        self.transmission_com_spec: Optional[TransmissionComSpecProps] = None
        self.uses_end_to_end: Optional[Boolean] = None
    @classmethod
    def deserialize(cls, element: ET.Element) -> "SenderComSpec":
        """Deserialize XML element to SenderComSpec object.

        Args:
            element: XML element to deserialize from

        Returns:
            Deserialized SenderComSpec object
        """
        # Create instance and initialize with default values
        obj = cls.__new__(cls)
        obj.__init__()

        # Parse composite_networks (list)
        obj.composite_networks = []
        for child in ARObject._find_all_child_elements(element, "COMPOSITE-NETWORKS"):
            composite_networks_value = ARObject._deserialize_by_tag(child, "CompositeNetworkRepresentation")
            obj.composite_networks.append(composite_networks_value)

        # Parse data_element_ref
        child = ARObject._find_child_element(element, "DATA-ELEMENT")
        if child is not None:
            data_element_ref_value = ARObject._deserialize_by_tag(child, "AutosarDataPrototype")
            obj.data_element_ref = data_element_ref_value

        # Parse handle_out_of_range
        child = ARObject._find_child_element(element, "HANDLE-OUT-OF-RANGE")
        if child is not None:
            handle_out_of_range_value = child.text
            obj.handle_out_of_range = handle_out_of_range_value

        # Parse network
        child = ARObject._find_child_element(element, "NETWORK")
        if child is not None:
            network_value = ARObject._deserialize_by_tag(child, "SwDataDefProps")
            obj.network = network_value

        # Parse transmission
        child = ARObject._find_child_element(element, "TRANSMISSION")
        if child is not None:
            transmission_value = child.text
            obj.transmission = transmission_value

        # Parse transmission_com_spec
        child = ARObject._find_child_element(element, "TRANSMISSION-COM-SPEC")
        if child is not None:
            transmission_com_spec_value = ARObject._deserialize_by_tag(child, "TransmissionComSpecProps")
            obj.transmission_com_spec = transmission_com_spec_value

        # Parse uses_end_to_end
        child = ARObject._find_child_element(element, "USES-END-TO-END")
        if child is not None:
            uses_end_to_end_value = child.text
            obj.uses_end_to_end = uses_end_to_end_value

        return obj



class SenderComSpecBuilder:
    """Builder for SenderComSpec."""

    def __init__(self) -> None:
        """Initialize builder."""
        self._obj: SenderComSpec = SenderComSpec()

    def build(self) -> SenderComSpec:
        """Build and return SenderComSpec object.

        Returns:
            SenderComSpec instance
        """
        # TODO: Add validation
        return self._obj
