"""ReceiverComSpec AUTOSAR element.

References:
  - AUTOSAR_CP_TPS_SoftwareComponentTemplate.pdf (page 170)
  - AUTOSAR_CP_TPS_SystemTemplate.pdf (page 2047)

JSON Source: docs/json/packages/M2_AUTOSARTemplates_SWComponentTemplate_Communication.classes.json"""

from __future__ import annotations
from typing import TYPE_CHECKING, Optional, Any
import xml.etree.ElementTree as ET

from armodel.models.M2.AUTOSARTemplates.SWComponentTemplate.Communication.r_port_com_spec import (
    RPortComSpec,
)
from armodel.models.M2.AUTOSARTemplates.GenericStructure.GeneralTemplateClasses.ArObject.ar_object import ARObject
from armodel.models.M2.AUTOSARTemplates.GenericStructure.GeneralTemplateClasses.ArObject.ar_ref import ARRef
from armodel.models.M2.AUTOSARTemplates.GenericStructure.GeneralTemplateClasses.PrimitiveTypes import (
    Boolean,
    PositiveInteger,
)
from armodel.models.M2.AUTOSARTemplates.SWComponentTemplate.Datatype.DataPrototypes.autosar_data_prototype import (
    AutosarDataPrototype,
)
from armodel.models.M2.AUTOSARTemplates.SWComponentTemplate.Communication.composite_network_representation import (
    CompositeNetworkRepresentation,
)
from abc import ABC, abstractmethod


class ReceiverComSpec(RPortComSpec, ABC):
    """AUTOSAR ReceiverComSpec."""

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
    max_delta: Optional[PositiveInteger]
    sync_counter_init: Optional[PositiveInteger]
    transformation_coms: list[Any]
    uses_end_to_end: Optional[Boolean]
    def __init__(self) -> None:
        """Initialize ReceiverComSpec."""
        super().__init__()
        self.composite_networks: list[CompositeNetworkRepresentation] = []
        self.data_element_ref: Optional[ARRef] = None
        self.handle_out_of_range: Optional[Any] = None
        self.max_delta: Optional[PositiveInteger] = None
        self.sync_counter_init: Optional[PositiveInteger] = None
        self.transformation_coms: list[Any] = []
        self.uses_end_to_end: Optional[Boolean] = None
    def serialize(self) -> ET.Element:
        """Serialize ReceiverComSpec to XML element.

        Returns:
            xml.etree.ElementTree.Element representing this object
        """
        # Get XML tag name for this class
        tag = self._get_xml_tag()
        elem = ET.Element(tag)

        # First, call parent's serialize to handle inherited attributes
        parent_elem = super(ReceiverComSpec, self).serialize()

        # Copy all attributes from parent element
        elem.attrib.update(parent_elem.attrib)

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

        # Serialize max_delta
        if self.max_delta is not None:
            serialized = ARObject._serialize_item(self.max_delta, "PositiveInteger")
            if serialized is not None:
                # Wrap with correct tag
                wrapped = ET.Element("MAX-DELTA")
                if hasattr(serialized, 'attrib'):
                    wrapped.attrib.update(serialized.attrib)
                    if serialized.text:
                        wrapped.text = serialized.text
                for child in serialized:
                    wrapped.append(child)
                elem.append(wrapped)

        # Serialize sync_counter_init
        if self.sync_counter_init is not None:
            serialized = ARObject._serialize_item(self.sync_counter_init, "PositiveInteger")
            if serialized is not None:
                # Wrap with correct tag
                wrapped = ET.Element("SYNC-COUNTER-INIT")
                if hasattr(serialized, 'attrib'):
                    wrapped.attrib.update(serialized.attrib)
                    if serialized.text:
                        wrapped.text = serialized.text
                for child in serialized:
                    wrapped.append(child)
                elem.append(wrapped)

        # Serialize transformation_coms (list to container "TRANSFORMATION-COMS")
        if self.transformation_coms:
            wrapper = ET.Element("TRANSFORMATION-COMS")
            for item in self.transformation_coms:
                serialized = ARObject._serialize_item(item, "Any")
                if serialized is not None:
                    wrapper.append(serialized)
            if len(wrapper) > 0:
                elem.append(wrapper)

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
    def deserialize(cls, element: ET.Element) -> "ReceiverComSpec":
        """Deserialize XML element to ReceiverComSpec object.

        Args:
            element: XML element to deserialize from

        Returns:
            Deserialized ReceiverComSpec object
        """
        # First, call parent's deserialize to handle inherited attributes
        obj = super(ReceiverComSpec, cls).deserialize(element)

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

        # Parse max_delta
        child = ARObject._find_child_element(element, "MAX-DELTA")
        if child is not None:
            max_delta_value = child.text
            obj.max_delta = max_delta_value

        # Parse sync_counter_init
        child = ARObject._find_child_element(element, "SYNC-COUNTER-INIT")
        if child is not None:
            sync_counter_init_value = child.text
            obj.sync_counter_init = sync_counter_init_value

        # Parse transformation_coms (list from container "TRANSFORMATION-COMS")
        obj.transformation_coms = []
        container = ARObject._find_child_element(element, "TRANSFORMATION-COMS")
        if container is not None:
            for child in container:
                # Deserialize each child element dynamically based on its tag
                child_value = ARObject._deserialize_by_tag(child, None)
                if child_value is not None:
                    obj.transformation_coms.append(child_value)

        # Parse uses_end_to_end
        child = ARObject._find_child_element(element, "USES-END-TO-END")
        if child is not None:
            uses_end_to_end_value = child.text
            obj.uses_end_to_end = uses_end_to_end_value

        return obj



class ReceiverComSpecBuilder:
    """Builder for ReceiverComSpec."""

    def __init__(self) -> None:
        """Initialize builder."""
        self._obj: ReceiverComSpec = ReceiverComSpec()

    def build(self) -> ReceiverComSpec:
        """Build and return ReceiverComSpec object.

        Returns:
            ReceiverComSpec instance
        """
        # TODO: Add validation
        return self._obj
