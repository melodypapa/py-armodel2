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

    def serialize(self) -> ET.Element:
        """Serialize SenderComSpec to XML element.

        Returns:
            xml.etree.ElementTree.Element representing this object
        """
        # Get XML tag name for this class
        tag = self._get_xml_tag()
        elem = ET.Element(tag)

        # First, call parent's serialize to handle inherited attributes
        parent_elem = super(SenderComSpec, self).serialize()

        # Copy all attributes from parent element
        elem.attrib.update(parent_elem.attrib)

        # Copy text from parent element
        if parent_elem.text:
            elem.text = parent_elem.text

        # Copy all children from parent element
        for child in parent_elem:
            elem.append(child)

        # Serialize composite_networks (list to container "COMPOSITE-NETWORKS")
        if self.composite_networks:
            wrapper = ET.Element("COMPOSITE-NETWORKS")
            for item in self.composite_networks:
                serialized = ARObject._serialize_item(item, "CompositeNetworkRepresentation")
                if serialized is not None:
                    wrapper.append(serialized)
            if len(wrapper) > 0:
                elem.append(wrapper)

        # Serialize data_element_ref
        if self.data_element_ref is not None:
            serialized = ARObject._serialize_item(self.data_element_ref, "AutosarDataPrototype")
            if serialized is not None:
                # Wrap with correct tag
                wrapped = ET.Element("DATA-ELEMENT-REF")
                if hasattr(serialized, 'attrib'):
                    wrapped.attrib.update(serialized.attrib)
                    if serialized.text:
                        wrapped.text = serialized.text
                for child in serialized:
                    wrapped.append(child)
                elem.append(wrapped)

        # Serialize handle_out_of_range
        if self.handle_out_of_range is not None:
            serialized = ARObject._serialize_item(self.handle_out_of_range, "Any")
            if serialized is not None:
                # Wrap with correct tag
                wrapped = ET.Element("HANDLE-OUT-OF-RANGE")
                if hasattr(serialized, 'attrib'):
                    wrapped.attrib.update(serialized.attrib)
                    if serialized.text:
                        wrapped.text = serialized.text
                for child in serialized:
                    wrapped.append(child)
                elem.append(wrapped)

        # Serialize network
        if self.network is not None:
            serialized = ARObject._serialize_item(self.network, "SwDataDefProps")
            if serialized is not None:
                # Wrap with correct tag
                wrapped = ET.Element("NETWORK")
                if hasattr(serialized, 'attrib'):
                    wrapped.attrib.update(serialized.attrib)
                    if serialized.text:
                        wrapped.text = serialized.text
                for child in serialized:
                    wrapped.append(child)
                elem.append(wrapped)

        # Serialize transmission
        if self.transmission is not None:
            serialized = ARObject._serialize_item(self.transmission, "Any")
            if serialized is not None:
                # Wrap with correct tag
                wrapped = ET.Element("TRANSMISSION")
                if hasattr(serialized, 'attrib'):
                    wrapped.attrib.update(serialized.attrib)
                    if serialized.text:
                        wrapped.text = serialized.text
                for child in serialized:
                    wrapped.append(child)
                elem.append(wrapped)

        # Serialize transmission_com_spec
        if self.transmission_com_spec is not None:
            serialized = ARObject._serialize_item(self.transmission_com_spec, "TransmissionComSpecProps")
            if serialized is not None:
                # Wrap with correct tag
                wrapped = ET.Element("TRANSMISSION-COM-SPEC")
                if hasattr(serialized, 'attrib'):
                    wrapped.attrib.update(serialized.attrib)
                    if serialized.text:
                        wrapped.text = serialized.text
                for child in serialized:
                    wrapped.append(child)
                elem.append(wrapped)

        # Serialize uses_end_to_end
        if self.uses_end_to_end is not None:
            serialized = ARObject._serialize_item(self.uses_end_to_end, "Boolean")
            if serialized is not None:
                # Wrap with correct tag
                wrapped = ET.Element("USES-END-TO-END")
                if hasattr(serialized, 'attrib'):
                    wrapped.attrib.update(serialized.attrib)
                    if serialized.text:
                        wrapped.text = serialized.text
                for child in serialized:
                    wrapped.append(child)
                elem.append(wrapped)

        return elem

    @classmethod
    def deserialize(cls, element: ET.Element) -> "SenderComSpec":
        """Deserialize XML element to SenderComSpec object.

        Args:
            element: XML element to deserialize from

        Returns:
            Deserialized SenderComSpec object
        """
        # First, call parent's deserialize to handle inherited attributes
        obj = super(SenderComSpec, cls).deserialize(element)

        # Parse composite_networks (list from container "COMPOSITE-NETWORKS")
        obj.composite_networks = []
        container = ARObject._find_child_element(element, "COMPOSITE-NETWORKS")
        if container is not None:
            for child in container:
                # Deserialize each child element dynamically based on its tag
                child_value = ARObject._deserialize_by_tag(child, None)
                if child_value is not None:
                    obj.composite_networks.append(child_value)

        # Parse data_element_ref
        child = ARObject._find_child_element(element, "DATA-ELEMENT-REF")
        if child is not None:
            data_element_ref_value = ARRef.deserialize(child)
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
