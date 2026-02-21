"""NmEcu AUTOSAR element.

References:
  - AUTOSAR_CP_TPS_SystemTemplate.pdf (page 674)

JSON Source: docs/json/packages/M2_AUTOSARTemplates_SystemTemplate_NetworkManagement.classes.json"""

from __future__ import annotations
from typing import TYPE_CHECKING, Optional, Any
import xml.etree.ElementTree as ET

from armodel.models.M2.AUTOSARTemplates.GenericStructure.GeneralTemplateClasses.Identifiable.identifiable import (
    Identifiable,
)
from armodel.models.M2.AUTOSARTemplates.GenericStructure.GeneralTemplateClasses.ArObject.ar_object import ARObject
from armodel.models.M2.AUTOSARTemplates.GenericStructure.GeneralTemplateClasses.ArObject.ar_ref import ARRef
from armodel.models.M2.AUTOSARTemplates.GenericStructure.GeneralTemplateClasses.PrimitiveTypes import (
    Boolean,
    TimeValue,
)
from armodel.models.M2.AUTOSARTemplates.SystemTemplate.NetworkManagement.busspecific_nm_ecu import (
    BusspecificNmEcu,
)
from armodel.models.M2.AUTOSARTemplates.SystemTemplate.Fibex.FibexCore.CoreTopology.ecu_instance import (
    EcuInstance,
)

if TYPE_CHECKING:
    from armodel.models.M2.AUTOSARTemplates.SystemTemplate.NetworkManagement.nm_coordinator import (
        NmCoordinator,
    )



class NmEcu(Identifiable):
    """AUTOSAR NmEcu."""

    @property
    def is_abstract(self) -> bool:
        """Check if this class is abstract.

        Returns:
            False for concrete classes
        """
        return False

    bus_dependent_nm_ecus: list[BusspecificNmEcu]
    ecu_instance_ref: Optional[ARRef]
    nm_bus_synchronization: Optional[Any]
    nm_com_control_enabled: Optional[Boolean]
    nm_coordinator: Optional[NmCoordinator]
    nm_cycletime: Optional[TimeValue]
    nm_pdu_rx_indication: Optional[Any]
    nm_remote_sleep_ind: Optional[Any]
    nm_state_change: Optional[Boolean]
    nm_user_data_enabled: Optional[Boolean]
    def __init__(self) -> None:
        """Initialize NmEcu."""
        super().__init__()
        self.bus_dependent_nm_ecus: list[BusspecificNmEcu] = []
        self.ecu_instance_ref: Optional[ARRef] = None
        self.nm_bus_synchronization: Optional[Any] = None
        self.nm_com_control_enabled: Optional[Boolean] = None
        self.nm_coordinator: Optional[NmCoordinator] = None
        self.nm_cycletime: Optional[TimeValue] = None
        self.nm_pdu_rx_indication: Optional[Any] = None
        self.nm_remote_sleep_ind: Optional[Any] = None
        self.nm_state_change: Optional[Boolean] = None
        self.nm_user_data_enabled: Optional[Boolean] = None

    def serialize(self) -> ET.Element:
        """Serialize NmEcu to XML element.

        Returns:
            xml.etree.ElementTree.Element representing this object
        """
        # Get XML tag name for this class
        tag = self._get_xml_tag()
        elem = ET.Element(tag)

        # First, call parent's serialize to handle inherited attributes
        parent_elem = super(NmEcu, self).serialize()

        # Copy all attributes from parent element
        elem.attrib.update(parent_elem.attrib)

        # Copy text from parent element
        if parent_elem.text:
            elem.text = parent_elem.text

        # Copy all children from parent element
        for child in parent_elem:
            elem.append(child)

        # Serialize bus_dependent_nm_ecus (list to container "BUS-DEPENDENT-NM-ECUS")
        if self.bus_dependent_nm_ecus:
            wrapper = ET.Element("BUS-DEPENDENT-NM-ECUS")
            for item in self.bus_dependent_nm_ecus:
                serialized = ARObject._serialize_item(item, "BusspecificNmEcu")
                if serialized is not None:
                    wrapper.append(serialized)
            if len(wrapper) > 0:
                elem.append(wrapper)

        # Serialize ecu_instance_ref
        if self.ecu_instance_ref is not None:
            serialized = ARObject._serialize_item(self.ecu_instance_ref, "EcuInstance")
            if serialized is not None:
                # Wrap with correct tag
                wrapped = ET.Element("ECU-INSTANCE-REF")
                if hasattr(serialized, 'attrib'):
                    wrapped.attrib.update(serialized.attrib)
                    if serialized.text:
                        wrapped.text = serialized.text
                for child in serialized:
                    wrapped.append(child)
                elem.append(wrapped)

        # Serialize nm_bus_synchronization
        if self.nm_bus_synchronization is not None:
            serialized = ARObject._serialize_item(self.nm_bus_synchronization, "Any")
            if serialized is not None:
                # Wrap with correct tag
                wrapped = ET.Element("NM-BUS-SYNCHRONIZATION")
                if hasattr(serialized, 'attrib'):
                    wrapped.attrib.update(serialized.attrib)
                    if serialized.text:
                        wrapped.text = serialized.text
                for child in serialized:
                    wrapped.append(child)
                elem.append(wrapped)

        # Serialize nm_com_control_enabled
        if self.nm_com_control_enabled is not None:
            serialized = ARObject._serialize_item(self.nm_com_control_enabled, "Boolean")
            if serialized is not None:
                # Wrap with correct tag
                wrapped = ET.Element("NM-COM-CONTROL-ENABLED")
                if hasattr(serialized, 'attrib'):
                    wrapped.attrib.update(serialized.attrib)
                    if serialized.text:
                        wrapped.text = serialized.text
                for child in serialized:
                    wrapped.append(child)
                elem.append(wrapped)

        # Serialize nm_coordinator
        if self.nm_coordinator is not None:
            serialized = ARObject._serialize_item(self.nm_coordinator, "NmCoordinator")
            if serialized is not None:
                # Wrap with correct tag
                wrapped = ET.Element("NM-COORDINATOR")
                if hasattr(serialized, 'attrib'):
                    wrapped.attrib.update(serialized.attrib)
                    if serialized.text:
                        wrapped.text = serialized.text
                for child in serialized:
                    wrapped.append(child)
                elem.append(wrapped)

        # Serialize nm_cycletime
        if self.nm_cycletime is not None:
            serialized = ARObject._serialize_item(self.nm_cycletime, "TimeValue")
            if serialized is not None:
                # Wrap with correct tag
                wrapped = ET.Element("NM-CYCLETIME")
                if hasattr(serialized, 'attrib'):
                    wrapped.attrib.update(serialized.attrib)
                    if serialized.text:
                        wrapped.text = serialized.text
                for child in serialized:
                    wrapped.append(child)
                elem.append(wrapped)

        # Serialize nm_pdu_rx_indication
        if self.nm_pdu_rx_indication is not None:
            serialized = ARObject._serialize_item(self.nm_pdu_rx_indication, "Any")
            if serialized is not None:
                # Wrap with correct tag
                wrapped = ET.Element("NM-PDU-RX-INDICATION")
                if hasattr(serialized, 'attrib'):
                    wrapped.attrib.update(serialized.attrib)
                    if serialized.text:
                        wrapped.text = serialized.text
                for child in serialized:
                    wrapped.append(child)
                elem.append(wrapped)

        # Serialize nm_remote_sleep_ind
        if self.nm_remote_sleep_ind is not None:
            serialized = ARObject._serialize_item(self.nm_remote_sleep_ind, "Any")
            if serialized is not None:
                # Wrap with correct tag
                wrapped = ET.Element("NM-REMOTE-SLEEP-IND")
                if hasattr(serialized, 'attrib'):
                    wrapped.attrib.update(serialized.attrib)
                    if serialized.text:
                        wrapped.text = serialized.text
                for child in serialized:
                    wrapped.append(child)
                elem.append(wrapped)

        # Serialize nm_state_change
        if self.nm_state_change is not None:
            serialized = ARObject._serialize_item(self.nm_state_change, "Boolean")
            if serialized is not None:
                # Wrap with correct tag
                wrapped = ET.Element("NM-STATE-CHANGE")
                if hasattr(serialized, 'attrib'):
                    wrapped.attrib.update(serialized.attrib)
                    if serialized.text:
                        wrapped.text = serialized.text
                for child in serialized:
                    wrapped.append(child)
                elem.append(wrapped)

        # Serialize nm_user_data_enabled
        if self.nm_user_data_enabled is not None:
            serialized = ARObject._serialize_item(self.nm_user_data_enabled, "Boolean")
            if serialized is not None:
                # Wrap with correct tag
                wrapped = ET.Element("NM-USER-DATA-ENABLED")
                if hasattr(serialized, 'attrib'):
                    wrapped.attrib.update(serialized.attrib)
                    if serialized.text:
                        wrapped.text = serialized.text
                for child in serialized:
                    wrapped.append(child)
                elem.append(wrapped)

        return elem

    @classmethod
    def deserialize(cls, element: ET.Element) -> "NmEcu":
        """Deserialize XML element to NmEcu object.

        Args:
            element: XML element to deserialize from

        Returns:
            Deserialized NmEcu object
        """
        # First, call parent's deserialize to handle inherited attributes
        obj = super(NmEcu, cls).deserialize(element)

        # Parse bus_dependent_nm_ecus (list from container "BUS-DEPENDENT-NM-ECUS")
        obj.bus_dependent_nm_ecus = []
        container = ARObject._find_child_element(element, "BUS-DEPENDENT-NM-ECUS")
        if container is not None:
            for child in container:
                # Deserialize each child element dynamically based on its tag
                child_value = ARObject._deserialize_by_tag(child, None)
                if child_value is not None:
                    obj.bus_dependent_nm_ecus.append(child_value)

        # Parse ecu_instance_ref
        child = ARObject._find_child_element(element, "ECU-INSTANCE-REF")
        if child is not None:
            ecu_instance_ref_value = ARRef.deserialize(child)
            obj.ecu_instance_ref = ecu_instance_ref_value

        # Parse nm_bus_synchronization
        child = ARObject._find_child_element(element, "NM-BUS-SYNCHRONIZATION")
        if child is not None:
            nm_bus_synchronization_value = child.text
            obj.nm_bus_synchronization = nm_bus_synchronization_value

        # Parse nm_com_control_enabled
        child = ARObject._find_child_element(element, "NM-COM-CONTROL-ENABLED")
        if child is not None:
            nm_com_control_enabled_value = child.text
            obj.nm_com_control_enabled = nm_com_control_enabled_value

        # Parse nm_coordinator
        child = ARObject._find_child_element(element, "NM-COORDINATOR")
        if child is not None:
            nm_coordinator_value = ARObject._deserialize_by_tag(child, "NmCoordinator")
            obj.nm_coordinator = nm_coordinator_value

        # Parse nm_cycletime
        child = ARObject._find_child_element(element, "NM-CYCLETIME")
        if child is not None:
            nm_cycletime_value = child.text
            obj.nm_cycletime = nm_cycletime_value

        # Parse nm_pdu_rx_indication
        child = ARObject._find_child_element(element, "NM-PDU-RX-INDICATION")
        if child is not None:
            nm_pdu_rx_indication_value = child.text
            obj.nm_pdu_rx_indication = nm_pdu_rx_indication_value

        # Parse nm_remote_sleep_ind
        child = ARObject._find_child_element(element, "NM-REMOTE-SLEEP-IND")
        if child is not None:
            nm_remote_sleep_ind_value = child.text
            obj.nm_remote_sleep_ind = nm_remote_sleep_ind_value

        # Parse nm_state_change
        child = ARObject._find_child_element(element, "NM-STATE-CHANGE")
        if child is not None:
            nm_state_change_value = child.text
            obj.nm_state_change = nm_state_change_value

        # Parse nm_user_data_enabled
        child = ARObject._find_child_element(element, "NM-USER-DATA-ENABLED")
        if child is not None:
            nm_user_data_enabled_value = child.text
            obj.nm_user_data_enabled = nm_user_data_enabled_value

        return obj



class NmEcuBuilder:
    """Builder for NmEcu."""

    def __init__(self) -> None:
        """Initialize builder."""
        self._obj: NmEcu = NmEcu()

    def build(self) -> NmEcu:
        """Build and return NmEcu object.

        Returns:
            NmEcu instance
        """
        # TODO: Add validation
        return self._obj
