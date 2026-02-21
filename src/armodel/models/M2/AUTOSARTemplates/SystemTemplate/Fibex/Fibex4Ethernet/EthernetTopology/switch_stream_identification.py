"""SwitchStreamIdentification AUTOSAR element.

References:
  - AUTOSAR_CP_TPS_SystemTemplate.pdf (page 135)

JSON Source: docs/json/packages/M2_AUTOSARTemplates_SystemTemplate_Fibex_Fibex4Ethernet_EthernetTopology.classes.json"""

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
    PositiveInteger,
)
from armodel.models.M2.AUTOSARTemplates.SystemTemplate.Fibex.Fibex4Ethernet.EthernetTopology.coupling_port import (
    CouplingPort,
)
from armodel.models.M2.AUTOSARTemplates.SystemTemplate.Fibex.Fibex4Ethernet.EthernetTopology.switch_stream_filter_rule import (
    SwitchStreamFilterRule,
)


class SwitchStreamIdentification(Identifiable):
    """AUTOSAR SwitchStreamIdentification."""

    @property
    def is_abstract(self) -> bool:
        """Check if this class is abstract.

        Returns:
            False for concrete classes
        """
        return False

    egress_port_refs: list[ARRef]
    filter_action_block: Optional[Boolean]
    filter_action_dest: Optional[Any]
    filter_action_drop: Optional[Boolean]
    filter_action_vlan: Optional[PositiveInteger]
    ingress_port_refs: list[ARRef]
    stream_filter: Optional[SwitchStreamFilterRule]
    def __init__(self) -> None:
        """Initialize SwitchStreamIdentification."""
        super().__init__()
        self.egress_port_refs: list[ARRef] = []
        self.filter_action_block: Optional[Boolean] = None
        self.filter_action_dest: Optional[Any] = None
        self.filter_action_drop: Optional[Boolean] = None
        self.filter_action_vlan: Optional[PositiveInteger] = None
        self.ingress_port_refs: list[ARRef] = []
        self.stream_filter: Optional[SwitchStreamFilterRule] = None

    def serialize(self) -> ET.Element:
        """Serialize SwitchStreamIdentification to XML element.

        Returns:
            xml.etree.ElementTree.Element representing this object
        """
        # Get XML tag name for this class
        tag = self._get_xml_tag()
        elem = ET.Element(tag)

        # First, call parent's serialize to handle inherited attributes
        parent_elem = super(SwitchStreamIdentification, self).serialize()

        # Copy all attributes from parent element
        elem.attrib.update(parent_elem.attrib)

        # Copy text from parent element
        if parent_elem.text:
            elem.text = parent_elem.text

        # Copy all children from parent element
        for child in parent_elem:
            elem.append(child)

        # Serialize egress_port_refs (list to container "EGRESS-PORT-REFS")
        if self.egress_port_refs:
            wrapper = ET.Element("EGRESS-PORT-REFS")
            for item in self.egress_port_refs:
                serialized = ARObject._serialize_item(item, "CouplingPort")
                if serialized is not None:
                    child_elem = ET.Element("EGRESS-PORT-REF")
                    if hasattr(serialized, 'attrib'):
                        child_elem.attrib.update(serialized.attrib)
                    if serialized.text:
                        child_elem.text = serialized.text
                    for child in serialized:
                        child_elem.append(child)
                    wrapper.append(child_elem)
            if len(wrapper) > 0:
                elem.append(wrapper)

        # Serialize filter_action_block
        if self.filter_action_block is not None:
            serialized = ARObject._serialize_item(self.filter_action_block, "Boolean")
            if serialized is not None:
                # Wrap with correct tag
                wrapped = ET.Element("FILTER-ACTION-BLOCK")
                if hasattr(serialized, 'attrib'):
                    wrapped.attrib.update(serialized.attrib)
                    if serialized.text:
                        wrapped.text = serialized.text
                for child in serialized:
                    wrapped.append(child)
                elem.append(wrapped)

        # Serialize filter_action_dest
        if self.filter_action_dest is not None:
            serialized = ARObject._serialize_item(self.filter_action_dest, "Any")
            if serialized is not None:
                # Wrap with correct tag
                wrapped = ET.Element("FILTER-ACTION-DEST")
                if hasattr(serialized, 'attrib'):
                    wrapped.attrib.update(serialized.attrib)
                    if serialized.text:
                        wrapped.text = serialized.text
                for child in serialized:
                    wrapped.append(child)
                elem.append(wrapped)

        # Serialize filter_action_drop
        if self.filter_action_drop is not None:
            serialized = ARObject._serialize_item(self.filter_action_drop, "Boolean")
            if serialized is not None:
                # Wrap with correct tag
                wrapped = ET.Element("FILTER-ACTION-DROP")
                if hasattr(serialized, 'attrib'):
                    wrapped.attrib.update(serialized.attrib)
                    if serialized.text:
                        wrapped.text = serialized.text
                for child in serialized:
                    wrapped.append(child)
                elem.append(wrapped)

        # Serialize filter_action_vlan
        if self.filter_action_vlan is not None:
            serialized = ARObject._serialize_item(self.filter_action_vlan, "PositiveInteger")
            if serialized is not None:
                # Wrap with correct tag
                wrapped = ET.Element("FILTER-ACTION-VLAN")
                if hasattr(serialized, 'attrib'):
                    wrapped.attrib.update(serialized.attrib)
                    if serialized.text:
                        wrapped.text = serialized.text
                for child in serialized:
                    wrapped.append(child)
                elem.append(wrapped)

        # Serialize ingress_port_refs (list to container "INGRESS-PORT-REFS")
        if self.ingress_port_refs:
            wrapper = ET.Element("INGRESS-PORT-REFS")
            for item in self.ingress_port_refs:
                serialized = ARObject._serialize_item(item, "CouplingPort")
                if serialized is not None:
                    child_elem = ET.Element("INGRESS-PORT-REF")
                    if hasattr(serialized, 'attrib'):
                        child_elem.attrib.update(serialized.attrib)
                    if serialized.text:
                        child_elem.text = serialized.text
                    for child in serialized:
                        child_elem.append(child)
                    wrapper.append(child_elem)
            if len(wrapper) > 0:
                elem.append(wrapper)

        # Serialize stream_filter
        if self.stream_filter is not None:
            serialized = ARObject._serialize_item(self.stream_filter, "SwitchStreamFilterRule")
            if serialized is not None:
                # Wrap with correct tag
                wrapped = ET.Element("STREAM-FILTER")
                if hasattr(serialized, 'attrib'):
                    wrapped.attrib.update(serialized.attrib)
                    if serialized.text:
                        wrapped.text = serialized.text
                for child in serialized:
                    wrapped.append(child)
                elem.append(wrapped)

        return elem

    @classmethod
    def deserialize(cls, element: ET.Element) -> "SwitchStreamIdentification":
        """Deserialize XML element to SwitchStreamIdentification object.

        Args:
            element: XML element to deserialize from

        Returns:
            Deserialized SwitchStreamIdentification object
        """
        # First, call parent's deserialize to handle inherited attributes
        obj = super(SwitchStreamIdentification, cls).deserialize(element)

        # Parse egress_port_refs (list from container "EGRESS-PORT-REFS")
        obj.egress_port_refs = []
        container = ARObject._find_child_element(element, "EGRESS-PORT-REFS")
        if container is not None:
            for child in container:
                # Check if child is a reference element (ends with -REF or -TREF)
                child_tag = ARObject._strip_namespace(child.tag)
                if child_tag.endswith("-REF") or child_tag.endswith("-TREF"):
                    # Use ARRef.deserialize() for reference elements
                    child_value = ARRef.deserialize(child)
                else:
                    # Deserialize each child element dynamically based on its tag
                    child_value = ARObject._deserialize_by_tag(child, None)
                if child_value is not None:
                    obj.egress_port_refs.append(child_value)

        # Parse filter_action_block
        child = ARObject._find_child_element(element, "FILTER-ACTION-BLOCK")
        if child is not None:
            filter_action_block_value = child.text
            obj.filter_action_block = filter_action_block_value

        # Parse filter_action_dest
        child = ARObject._find_child_element(element, "FILTER-ACTION-DEST")
        if child is not None:
            filter_action_dest_value = child.text
            obj.filter_action_dest = filter_action_dest_value

        # Parse filter_action_drop
        child = ARObject._find_child_element(element, "FILTER-ACTION-DROP")
        if child is not None:
            filter_action_drop_value = child.text
            obj.filter_action_drop = filter_action_drop_value

        # Parse filter_action_vlan
        child = ARObject._find_child_element(element, "FILTER-ACTION-VLAN")
        if child is not None:
            filter_action_vlan_value = child.text
            obj.filter_action_vlan = filter_action_vlan_value

        # Parse ingress_port_refs (list from container "INGRESS-PORT-REFS")
        obj.ingress_port_refs = []
        container = ARObject._find_child_element(element, "INGRESS-PORT-REFS")
        if container is not None:
            for child in container:
                # Check if child is a reference element (ends with -REF or -TREF)
                child_tag = ARObject._strip_namespace(child.tag)
                if child_tag.endswith("-REF") or child_tag.endswith("-TREF"):
                    # Use ARRef.deserialize() for reference elements
                    child_value = ARRef.deserialize(child)
                else:
                    # Deserialize each child element dynamically based on its tag
                    child_value = ARObject._deserialize_by_tag(child, None)
                if child_value is not None:
                    obj.ingress_port_refs.append(child_value)

        # Parse stream_filter
        child = ARObject._find_child_element(element, "STREAM-FILTER")
        if child is not None:
            stream_filter_value = ARObject._deserialize_by_tag(child, "SwitchStreamFilterRule")
            obj.stream_filter = stream_filter_value

        return obj



class SwitchStreamIdentificationBuilder:
    """Builder for SwitchStreamIdentification."""

    def __init__(self) -> None:
        """Initialize builder."""
        self._obj: SwitchStreamIdentification = SwitchStreamIdentification()

    def build(self) -> SwitchStreamIdentification:
        """Build and return SwitchStreamIdentification object.

        Returns:
            SwitchStreamIdentification instance
        """
        # TODO: Add validation
        return self._obj
