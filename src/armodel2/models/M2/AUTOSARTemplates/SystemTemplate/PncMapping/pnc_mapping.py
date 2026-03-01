"""PncMapping AUTOSAR element.

References:
  - AUTOSAR_CP_TPS_SystemTemplate.pdf (page 264)

JSON Source: docs/json/packages/M2_AUTOSARTemplates_SystemTemplate_PncMapping.classes.json"""

from __future__ import annotations
from typing import TYPE_CHECKING, Optional
import xml.etree.ElementTree as ET

from armodel2.models.M2.AUTOSARTemplates.GenericStructure.GeneralTemplateClasses.Identifiable.describable import (
    Describable,
)
from armodel2.models.M2.builder_base import BuilderBase
from armodel2.models.M2.AUTOSARTemplates.GenericStructure.GeneralTemplateClasses.Identifiable.describable import DescribableBuilder
from armodel2.models.M2.AUTOSARTemplates.GenericStructure.GeneralTemplateClasses.ArObject.ar_ref import ARRef
from armodel2.models.M2.AUTOSARTemplates.GenericStructure.GeneralTemplateClasses.PrimitiveTypes import (
    Boolean,
    Identifier,
    PositiveInteger,
)
from armodel2.models.M2.AUTOSARTemplates.SystemTemplate.Fibex.Fibex4Ethernet.ServiceInstances.consumed_provided_service_instance_group import (
    ConsumedProvidedServiceInstanceGroup,
)
from armodel2.models.M2.AUTOSARTemplates.SystemTemplate.Fibex.FibexCore.CoreTopology.ecu_instance import (
    EcuInstance,
)
from armodel2.models.M2.AUTOSARTemplates.SystemTemplate.Fibex.FibexCore.CoreCommunication.frame_triggering import (
    FrameTriggering,
)
from armodel2.models.M2.AUTOSARTemplates.SystemTemplate.Fibex.FibexCore.CoreCommunication.i_signal_i_pdu_group import (
    ISignalIPduGroup,
)
from armodel2.models.M2.AUTOSARTemplates.SystemTemplate.Fibex.FibexCore.CoreCommunication.pdur_i_pdu_group import (
    PdurIPduGroup,
)
from armodel2.models.M2.AUTOSARTemplates.SystemTemplate.Fibex.FibexCore.CoreTopology.physical_channel import (
    PhysicalChannel,
)
from armodel2.models.M2.AUTOSARTemplates.SystemTemplate.PncMapping.pnc_mapping_ident import (
    PncMappingIdent,
)
from armodel2.models.M2.AUTOSARTemplates.SWComponentTemplate.Components.port_group import (
    PortGroup,
)
from armodel2.models.M2.AUTOSARTemplates.GenericStructure.GeneralTemplateClasses.ArObject.ar_object import ARObject
from armodel2.serialization import SerializationHelper


class PncMapping(Describable):
    """AUTOSAR PncMapping."""

    @property
    def is_abstract(self) -> bool:
        """Check if this class is abstract.

        Returns:
            False for concrete classes
        """
        return False

    _XML_TAG = "PNC-MAPPING"


    dynamic_pnc_refs: list[ARRef]
    ident_ref: Optional[ARRef]
    physical_channel_refs: list[ARRef]
    pnc_consumed_refs: list[ARRef]
    pnc_group_refs: list[ARRef]
    pnc_identifier: Optional[PositiveInteger]
    pnc_pdur_group_refs: list[ARRef]
    pnc_wakeup: Optional[Boolean]
    relevant_for_refs: list[ARRef]
    short_label: Optional[Identifier]
    vfc_refs: list[ARRef]
    wakeup_frame_refs: list[ARRef]
    _DESERIALIZE_DISPATCH = {
        "DYNAMIC-PNCS": lambda obj, elem: obj.dynamic_pnc_refs.append(ARRef.deserialize(elem)),
        "IDENT-REF": lambda obj, elem: setattr(obj, "ident_ref", ARRef.deserialize(elem)),
        "PHYSICAL-CHANNELS": ("_POLYMORPHIC_LIST", "physical_channel_refs", ["AbstractCanPhysicalChannel", "EthernetPhysicalChannel", "FlexrayPhysicalChannel", "LinPhysicalChannel"]),
        "PNC-CONSUMEDS": lambda obj, elem: obj.pnc_consumed_refs.append(ARRef.deserialize(elem)),
        "PNC-GROUPS": lambda obj, elem: obj.pnc_group_refs.append(ARRef.deserialize(elem)),
        "PNC-IDENTIFIER": lambda obj, elem: setattr(obj, "pnc_identifier", SerializationHelper.deserialize_by_tag(elem, "PositiveInteger")),
        "PNC-PDUR-GROUPS": lambda obj, elem: obj.pnc_pdur_group_refs.append(ARRef.deserialize(elem)),
        "PNC-WAKEUP": lambda obj, elem: setattr(obj, "pnc_wakeup", SerializationHelper.deserialize_by_tag(elem, "Boolean")),
        "RELEVANT-FORS": lambda obj, elem: obj.relevant_for_refs.append(ARRef.deserialize(elem)),
        "SHORT-LABEL": lambda obj, elem: setattr(obj, "short_label", SerializationHelper.deserialize_by_tag(elem, "Identifier")),
        "VFCS": lambda obj, elem: obj.vfc_refs.append(ARRef.deserialize(elem)),
        "WAKEUP-FRAMES": ("_POLYMORPHIC_LIST", "wakeup_frame_refs", ["CanFrameTriggering", "EthernetFrameTriggering", "FlexrayFrameTriggering", "LinFrameTriggering"]),
    }


    def __init__(self) -> None:
        """Initialize PncMapping."""
        super().__init__()
        self.dynamic_pnc_refs: list[ARRef] = []
        self.ident_ref: Optional[ARRef] = None
        self.physical_channel_refs: list[ARRef] = []
        self.pnc_consumed_refs: list[ARRef] = []
        self.pnc_group_refs: list[ARRef] = []
        self.pnc_identifier: Optional[PositiveInteger] = None
        self.pnc_pdur_group_refs: list[ARRef] = []
        self.pnc_wakeup: Optional[Boolean] = None
        self.relevant_for_refs: list[ARRef] = []
        self.short_label: Optional[Identifier] = None
        self.vfc_refs: list[ARRef] = []
        self.wakeup_frame_refs: list[ARRef] = []

    def serialize(self) -> ET.Element:
        """Serialize PncMapping to XML element.

        Returns:
            xml.etree.ElementTree.Element representing this object
        """
        # Use pre-computed _XML_TAG constant
        elem = ET.Element(self._XML_TAG)

        # First, call parent's serialize to handle inherited attributes
        parent_elem = super(PncMapping, self).serialize()

        # Copy all attributes from parent element
        elem.attrib.update(parent_elem.attrib)

        # Copy text from parent element
        if parent_elem.text:
            elem.text = parent_elem.text

        # Copy all children from parent element
        for child in parent_elem:
            elem.append(child)

        # Serialize dynamic_pnc_refs (list to container "DYNAMIC-PNC-REFS")
        if self.dynamic_pnc_refs:
            wrapper = ET.Element("DYNAMIC-PNC-REFS")
            for item in self.dynamic_pnc_refs:
                serialized = SerializationHelper.serialize_item(item, "ISignalIPduGroup")
                if serialized is not None:
                    child_elem = ET.Element("DYNAMIC-PNC-REF")
                    if hasattr(serialized, 'attrib'):
                        child_elem.attrib.update(serialized.attrib)
                    if serialized.text:
                        child_elem.text = serialized.text
                    for child in serialized:
                        child_elem.append(child)
                    wrapper.append(child_elem)
            if len(wrapper) > 0:
                elem.append(wrapper)

        # Serialize ident_ref
        if self.ident_ref is not None:
            serialized = SerializationHelper.serialize_item(self.ident_ref, "PncMappingIdent")
            if serialized is not None:
                # Wrap with correct tag
                wrapped = ET.Element("IDENT-REF")
                if hasattr(serialized, 'attrib'):
                    wrapped.attrib.update(serialized.attrib)
                if serialized.text:
                    wrapped.text = serialized.text
                for child in serialized:
                    wrapped.append(child)
                elem.append(wrapped)

        # Serialize physical_channel_refs (list to container "PHYSICAL-CHANNEL-REFS")
        if self.physical_channel_refs:
            wrapper = ET.Element("PHYSICAL-CHANNEL-REFS")
            for item in self.physical_channel_refs:
                serialized = SerializationHelper.serialize_item(item, "PhysicalChannel")
                if serialized is not None:
                    child_elem = ET.Element("PHYSICAL-CHANNEL-REF")
                    if hasattr(serialized, 'attrib'):
                        child_elem.attrib.update(serialized.attrib)
                    if serialized.text:
                        child_elem.text = serialized.text
                    for child in serialized:
                        child_elem.append(child)
                    wrapper.append(child_elem)
            if len(wrapper) > 0:
                elem.append(wrapper)

        # Serialize pnc_consumed_refs (list to container "PNC-CONSUMED-REFS")
        if self.pnc_consumed_refs:
            wrapper = ET.Element("PNC-CONSUMED-REFS")
            for item in self.pnc_consumed_refs:
                serialized = SerializationHelper.serialize_item(item, "ConsumedProvidedServiceInstanceGroup")
                if serialized is not None:
                    child_elem = ET.Element("PNC-CONSUMED-REF")
                    if hasattr(serialized, 'attrib'):
                        child_elem.attrib.update(serialized.attrib)
                    if serialized.text:
                        child_elem.text = serialized.text
                    for child in serialized:
                        child_elem.append(child)
                    wrapper.append(child_elem)
            if len(wrapper) > 0:
                elem.append(wrapper)

        # Serialize pnc_group_refs (list to container "PNC-GROUP-REFS")
        if self.pnc_group_refs:
            wrapper = ET.Element("PNC-GROUP-REFS")
            for item in self.pnc_group_refs:
                serialized = SerializationHelper.serialize_item(item, "ISignalIPduGroup")
                if serialized is not None:
                    child_elem = ET.Element("PNC-GROUP-REF")
                    if hasattr(serialized, 'attrib'):
                        child_elem.attrib.update(serialized.attrib)
                    if serialized.text:
                        child_elem.text = serialized.text
                    for child in serialized:
                        child_elem.append(child)
                    wrapper.append(child_elem)
            if len(wrapper) > 0:
                elem.append(wrapper)

        # Serialize pnc_identifier
        if self.pnc_identifier is not None:
            serialized = SerializationHelper.serialize_item(self.pnc_identifier, "PositiveInteger")
            if serialized is not None:
                # Wrap with correct tag
                wrapped = ET.Element("PNC-IDENTIFIER")
                if hasattr(serialized, 'attrib'):
                    wrapped.attrib.update(serialized.attrib)
                if serialized.text:
                    wrapped.text = serialized.text
                for child in serialized:
                    wrapped.append(child)
                elem.append(wrapped)

        # Serialize pnc_pdur_group_refs (list to container "PNC-PDUR-GROUP-REFS")
        if self.pnc_pdur_group_refs:
            wrapper = ET.Element("PNC-PDUR-GROUP-REFS")
            for item in self.pnc_pdur_group_refs:
                serialized = SerializationHelper.serialize_item(item, "PdurIPduGroup")
                if serialized is not None:
                    child_elem = ET.Element("PNC-PDUR-GROUP-REF")
                    if hasattr(serialized, 'attrib'):
                        child_elem.attrib.update(serialized.attrib)
                    if serialized.text:
                        child_elem.text = serialized.text
                    for child in serialized:
                        child_elem.append(child)
                    wrapper.append(child_elem)
            if len(wrapper) > 0:
                elem.append(wrapper)

        # Serialize pnc_wakeup
        if self.pnc_wakeup is not None:
            serialized = SerializationHelper.serialize_item(self.pnc_wakeup, "Boolean")
            if serialized is not None:
                # Wrap with correct tag
                wrapped = ET.Element("PNC-WAKEUP")
                if hasattr(serialized, 'attrib'):
                    wrapped.attrib.update(serialized.attrib)
                if serialized.text:
                    wrapped.text = serialized.text
                for child in serialized:
                    wrapped.append(child)
                elem.append(wrapped)

        # Serialize relevant_for_refs (list to container "RELEVANT-FOR-REFS")
        if self.relevant_for_refs:
            wrapper = ET.Element("RELEVANT-FOR-REFS")
            for item in self.relevant_for_refs:
                serialized = SerializationHelper.serialize_item(item, "EcuInstance")
                if serialized is not None:
                    child_elem = ET.Element("RELEVANT-FOR-REF")
                    if hasattr(serialized, 'attrib'):
                        child_elem.attrib.update(serialized.attrib)
                    if serialized.text:
                        child_elem.text = serialized.text
                    for child in serialized:
                        child_elem.append(child)
                    wrapper.append(child_elem)
            if len(wrapper) > 0:
                elem.append(wrapper)

        # Serialize short_label
        if self.short_label is not None:
            serialized = SerializationHelper.serialize_item(self.short_label, "Identifier")
            if serialized is not None:
                # Wrap with correct tag
                wrapped = ET.Element("SHORT-LABEL")
                if hasattr(serialized, 'attrib'):
                    wrapped.attrib.update(serialized.attrib)
                if serialized.text:
                    wrapped.text = serialized.text
                for child in serialized:
                    wrapped.append(child)
                elem.append(wrapped)

        # Serialize vfc_refs (list to container "VFC-REFS")
        if self.vfc_refs:
            wrapper = ET.Element("VFC-REFS")
            for item in self.vfc_refs:
                serialized = SerializationHelper.serialize_item(item, "PortGroup")
                if serialized is not None:
                    child_elem = ET.Element("VFC-REF")
                    if hasattr(serialized, 'attrib'):
                        child_elem.attrib.update(serialized.attrib)
                    if serialized.text:
                        child_elem.text = serialized.text
                    for child in serialized:
                        child_elem.append(child)
                    wrapper.append(child_elem)
            if len(wrapper) > 0:
                elem.append(wrapper)

        # Serialize wakeup_frame_refs (list to container "WAKEUP-FRAME-REFS")
        if self.wakeup_frame_refs:
            wrapper = ET.Element("WAKEUP-FRAME-REFS")
            for item in self.wakeup_frame_refs:
                serialized = SerializationHelper.serialize_item(item, "FrameTriggering")
                if serialized is not None:
                    child_elem = ET.Element("WAKEUP-FRAME-REF")
                    if hasattr(serialized, 'attrib'):
                        child_elem.attrib.update(serialized.attrib)
                    if serialized.text:
                        child_elem.text = serialized.text
                    for child in serialized:
                        child_elem.append(child)
                    wrapper.append(child_elem)
            if len(wrapper) > 0:
                elem.append(wrapper)

        return elem

    @classmethod
    def deserialize(cls, element: ET.Element) -> "PncMapping":
        """Deserialize XML element to PncMapping object.

        Args:
            element: XML element to deserialize from

        Returns:
            Deserialized PncMapping object
        """
        # First, call parent's deserialize to handle inherited attributes
        obj = super(PncMapping, cls).deserialize(element)

        # Single-pass deserialization with if-elif-else chain
        ns_split = '}'
        for child in element:
            tag = child.tag.split(ns_split, 1)[1] if child.tag.startswith('{') else child.tag
            if tag == "DYNAMIC-PNCS":
                # Iterate through wrapper children
                for item_elem in child:
                    obj.dynamic_pnc_refs.append(SerializationHelper.deserialize_by_tag(item_elem, "ISignalIPduGroup"))
            elif tag == "IDENT-REF":
                setattr(obj, "ident_ref", ARRef.deserialize(child))
            elif tag == "PHYSICAL-CHANNELS":
                # Check first child element for concrete type
                if len(child) > 0:
                    concrete_tag = child[0].tag.split(ns_split, 1)[1] if child[0].tag.startswith("{") else child[0].tag
                    if concrete_tag == "ABSTRACT-CAN-PHYSICAL-CHANNEL":
                        obj.physical_channel_refs.append(SerializationHelper.deserialize_by_tag(child[0], "AbstractCanPhysicalChannel"))
                    elif concrete_tag == "ETHERNET-PHYSICAL-CHANNEL":
                        obj.physical_channel_refs.append(SerializationHelper.deserialize_by_tag(child[0], "EthernetPhysicalChannel"))
                    elif concrete_tag == "FLEXRAY-PHYSICAL-CHANNEL":
                        obj.physical_channel_refs.append(SerializationHelper.deserialize_by_tag(child[0], "FlexrayPhysicalChannel"))
                    elif concrete_tag == "LIN-PHYSICAL-CHANNEL":
                        obj.physical_channel_refs.append(SerializationHelper.deserialize_by_tag(child[0], "LinPhysicalChannel"))
            elif tag == "PNC-CONSUMEDS":
                # Iterate through wrapper children
                for item_elem in child:
                    obj.pnc_consumed_refs.append(SerializationHelper.deserialize_by_tag(item_elem, "ConsumedProvidedServiceInstanceGroup"))
            elif tag == "PNC-GROUPS":
                # Iterate through wrapper children
                for item_elem in child:
                    obj.pnc_group_refs.append(SerializationHelper.deserialize_by_tag(item_elem, "ISignalIPduGroup"))
            elif tag == "PNC-IDENTIFIER":
                setattr(obj, "pnc_identifier", SerializationHelper.deserialize_by_tag(child, "PositiveInteger"))
            elif tag == "PNC-PDUR-GROUPS":
                # Iterate through wrapper children
                for item_elem in child:
                    obj.pnc_pdur_group_refs.append(SerializationHelper.deserialize_by_tag(item_elem, "PdurIPduGroup"))
            elif tag == "PNC-WAKEUP":
                setattr(obj, "pnc_wakeup", SerializationHelper.deserialize_by_tag(child, "Boolean"))
            elif tag == "RELEVANT-FORS":
                # Iterate through wrapper children
                for item_elem in child:
                    obj.relevant_for_refs.append(SerializationHelper.deserialize_by_tag(item_elem, "EcuInstance"))
            elif tag == "SHORT-LABEL":
                setattr(obj, "short_label", SerializationHelper.deserialize_by_tag(child, "Identifier"))
            elif tag == "VFCS":
                # Iterate through wrapper children
                for item_elem in child:
                    obj.vfc_refs.append(SerializationHelper.deserialize_by_tag(item_elem, "PortGroup"))
            elif tag == "WAKEUP-FRAMES":
                # Check first child element for concrete type
                if len(child) > 0:
                    concrete_tag = child[0].tag.split(ns_split, 1)[1] if child[0].tag.startswith("{") else child[0].tag
                    if concrete_tag == "CAN-FRAME-TRIGGERING":
                        obj.wakeup_frame_refs.append(SerializationHelper.deserialize_by_tag(child[0], "CanFrameTriggering"))
                    elif concrete_tag == "ETHERNET-FRAME-TRIGGERING":
                        obj.wakeup_frame_refs.append(SerializationHelper.deserialize_by_tag(child[0], "EthernetFrameTriggering"))
                    elif concrete_tag == "FLEXRAY-FRAME-TRIGGERING":
                        obj.wakeup_frame_refs.append(SerializationHelper.deserialize_by_tag(child[0], "FlexrayFrameTriggering"))
                    elif concrete_tag == "LIN-FRAME-TRIGGERING":
                        obj.wakeup_frame_refs.append(SerializationHelper.deserialize_by_tag(child[0], "LinFrameTriggering"))

        return obj



class PncMappingBuilder(DescribableBuilder):
    """Builder for PncMapping with fluent API."""

    def __init__(self) -> None:
        """Initialize builder with defaults."""
        super().__init__()
        self._obj: PncMapping = PncMapping()


    def with_dynamic_pncs(self, items: list[ISignalIPduGroup]) -> "PncMappingBuilder":
        """Set dynamic_pncs list attribute.

        Args:
            items: List of items to set

        Returns:
            self for method chaining
        """
        self._obj.dynamic_pncs = list(items) if items else []
        return self

    def with_ident(self, value: Optional[PncMappingIdent]) -> "PncMappingBuilder":
        """Set ident attribute.

        Args:
            value: Value to set

        Returns:
            self for method chaining
        """
        if value is None and not True:
            raise ValueError("Attribute '" + snake_attr_name + "' is required and cannot be None")
        self._obj.ident = value
        return self

    def with_physical_channels(self, items: list[PhysicalChannel]) -> "PncMappingBuilder":
        """Set physical_channels list attribute.

        Args:
            items: List of items to set

        Returns:
            self for method chaining
        """
        self._obj.physical_channels = list(items) if items else []
        return self

    def with_pnc_consumeds(self, items: list[ConsumedProvidedServiceInstanceGroup]) -> "PncMappingBuilder":
        """Set pnc_consumeds list attribute.

        Args:
            items: List of items to set

        Returns:
            self for method chaining
        """
        self._obj.pnc_consumeds = list(items) if items else []
        return self

    def with_pnc_groups(self, items: list[ISignalIPduGroup]) -> "PncMappingBuilder":
        """Set pnc_groups list attribute.

        Args:
            items: List of items to set

        Returns:
            self for method chaining
        """
        self._obj.pnc_groups = list(items) if items else []
        return self

    def with_pnc_identifier(self, value: Optional[PositiveInteger]) -> "PncMappingBuilder":
        """Set pnc_identifier attribute.

        Args:
            value: Value to set

        Returns:
            self for method chaining
        """
        if value is None and not True:
            raise ValueError("Attribute '" + snake_attr_name + "' is required and cannot be None")
        self._obj.pnc_identifier = value
        return self

    def with_pnc_pdur_groups(self, items: list[PdurIPduGroup]) -> "PncMappingBuilder":
        """Set pnc_pdur_groups list attribute.

        Args:
            items: List of items to set

        Returns:
            self for method chaining
        """
        self._obj.pnc_pdur_groups = list(items) if items else []
        return self

    def with_pnc_wakeup(self, value: Optional[Boolean]) -> "PncMappingBuilder":
        """Set pnc_wakeup attribute.

        Args:
            value: Value to set

        Returns:
            self for method chaining
        """
        if value is None and not True:
            raise ValueError("Attribute '" + snake_attr_name + "' is required and cannot be None")
        self._obj.pnc_wakeup = value
        return self

    def with_relevant_fors(self, items: list[EcuInstance]) -> "PncMappingBuilder":
        """Set relevant_fors list attribute.

        Args:
            items: List of items to set

        Returns:
            self for method chaining
        """
        self._obj.relevant_fors = list(items) if items else []
        return self

    def with_short_label(self, value: Optional[Identifier]) -> "PncMappingBuilder":
        """Set short_label attribute.

        Args:
            value: Value to set

        Returns:
            self for method chaining
        """
        if value is None and not True:
            raise ValueError("Attribute '" + snake_attr_name + "' is required and cannot be None")
        self._obj.short_label = value
        return self

    def with_vfcs(self, items: list[PortGroup]) -> "PncMappingBuilder":
        """Set vfcs list attribute.

        Args:
            items: List of items to set

        Returns:
            self for method chaining
        """
        self._obj.vfcs = list(items) if items else []
        return self

    def with_wakeup_frames(self, items: list[FrameTriggering]) -> "PncMappingBuilder":
        """Set wakeup_frames list attribute.

        Args:
            items: List of items to set

        Returns:
            self for method chaining
        """
        self._obj.wakeup_frames = list(items) if items else []
        return self


    def add_dynamic_pnc(self, item: ISignalIPduGroup) -> "PncMappingBuilder":
        """Add a single item to dynamic_pncs list.

        Args:
            item: Item to add

        Returns:
            self for method chaining
        """
        self._obj.dynamic_pncs.append(item)
        return self

    def clear_dynamic_pncs(self) -> "PncMappingBuilder":
        """Clear all items from dynamic_pncs list.

        Returns:
            self for method chaining
        """
        self._obj.dynamic_pncs = []
        return self

    def add_physical_channel(self, item: PhysicalChannel) -> "PncMappingBuilder":
        """Add a single item to physical_channels list.

        Args:
            item: Item to add

        Returns:
            self for method chaining
        """
        self._obj.physical_channels.append(item)
        return self

    def clear_physical_channels(self) -> "PncMappingBuilder":
        """Clear all items from physical_channels list.

        Returns:
            self for method chaining
        """
        self._obj.physical_channels = []
        return self

    def add_pnc_consumed(self, item: ConsumedProvidedServiceInstanceGroup) -> "PncMappingBuilder":
        """Add a single item to pnc_consumeds list.

        Args:
            item: Item to add

        Returns:
            self for method chaining
        """
        self._obj.pnc_consumeds.append(item)
        return self

    def clear_pnc_consumeds(self) -> "PncMappingBuilder":
        """Clear all items from pnc_consumeds list.

        Returns:
            self for method chaining
        """
        self._obj.pnc_consumeds = []
        return self

    def add_pnc_group(self, item: ISignalIPduGroup) -> "PncMappingBuilder":
        """Add a single item to pnc_groups list.

        Args:
            item: Item to add

        Returns:
            self for method chaining
        """
        self._obj.pnc_groups.append(item)
        return self

    def clear_pnc_groups(self) -> "PncMappingBuilder":
        """Clear all items from pnc_groups list.

        Returns:
            self for method chaining
        """
        self._obj.pnc_groups = []
        return self

    def add_pnc_pdur_group(self, item: PdurIPduGroup) -> "PncMappingBuilder":
        """Add a single item to pnc_pdur_groups list.

        Args:
            item: Item to add

        Returns:
            self for method chaining
        """
        self._obj.pnc_pdur_groups.append(item)
        return self

    def clear_pnc_pdur_groups(self) -> "PncMappingBuilder":
        """Clear all items from pnc_pdur_groups list.

        Returns:
            self for method chaining
        """
        self._obj.pnc_pdur_groups = []
        return self

    def add_relevant_for(self, item: EcuInstance) -> "PncMappingBuilder":
        """Add a single item to relevant_fors list.

        Args:
            item: Item to add

        Returns:
            self for method chaining
        """
        self._obj.relevant_fors.append(item)
        return self

    def clear_relevant_fors(self) -> "PncMappingBuilder":
        """Clear all items from relevant_fors list.

        Returns:
            self for method chaining
        """
        self._obj.relevant_fors = []
        return self

    def add_vfc(self, item: PortGroup) -> "PncMappingBuilder":
        """Add a single item to vfcs list.

        Args:
            item: Item to add

        Returns:
            self for method chaining
        """
        self._obj.vfcs.append(item)
        return self

    def clear_vfcs(self) -> "PncMappingBuilder":
        """Clear all items from vfcs list.

        Returns:
            self for method chaining
        """
        self._obj.vfcs = []
        return self

    def add_wakeup_frame(self, item: FrameTriggering) -> "PncMappingBuilder":
        """Add a single item to wakeup_frames list.

        Args:
            item: Item to add

        Returns:
            self for method chaining
        """
        self._obj.wakeup_frames.append(item)
        return self

    def clear_wakeup_frames(self) -> "PncMappingBuilder":
        """Clear all items from wakeup_frames list.

        Returns:
            self for method chaining
        """
        self._obj.wakeup_frames = []
        return self



    def _validate_instance(self) -> None:
        """Validate the built instance based on settings."""
        from typing import get_type_hints
        from armodel2.core import GlobalSettingsManager, BuilderValidationMode

        settings = GlobalSettingsManager()
        mode = settings.builder_validation

        if mode == BuilderValidationMode.DISABLED:
            return

        # Get type hints for the class
        try:
            type_hints_dict = get_type_hints(type(self._obj))
        except Exception:
            # Cannot resolve type hints (e.g., forward references), skip validation
            return

        for attr_name, attr_type in type_hints_dict.items():
            if attr_name.startswith("_"):
                continue

            value = getattr(self._obj, attr_name)

            # Check required fields (not Optional)
            if value is None and not self._is_optional_type(attr_type):
                if mode == BuilderValidationMode.STRICT:
                    raise ValueError(
                        f"Required attribute '{attr_name}' is None"
                    )
                elif mode == BuilderValidationMode.LENIENT:
                    import warnings
                    warnings.warn(
                        f"Required attribute '{attr_name}' is None",
                        UserWarning
                    )

    @staticmethod
    def _is_optional_type(type_hint: Any) -> bool:
        """Check if a type hint is Optional.

        Args:
            type_hint: Type hint to check

        Returns:
            True if type is Optional, False otherwise
        """
        origin = getattr(type_hint, "__origin__", None)
        return origin is Union

    @staticmethod
    def _get_expected_type(type_hint: Any) -> type:
        """Extract expected type from type hint.

        Args:
            type_hint: Type hint to extract from

        Returns:
            Expected type
        """
        if isinstance(type_hint, str):
            return object
        origin = getattr(type_hint, "__origin__", None)
        if origin is Union:
            args = getattr(type_hint, "__args__", [])
            for arg in args:
                if arg is not type(None):
                    return arg
        elif origin is list:
            args = getattr(type_hint, "__args__", [object])
            return args[0] if args else object
        return type_hint if isinstance(type_hint, type) else object


    def build(self) -> PncMapping:
        """Build and return the PncMapping instance with validation."""
        self._validate_instance()
        pass
        return self._obj