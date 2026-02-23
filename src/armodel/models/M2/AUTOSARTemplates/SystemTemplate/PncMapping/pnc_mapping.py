"""PncMapping AUTOSAR element.

References:
  - AUTOSAR_CP_TPS_SystemTemplate.pdf (page 264)

JSON Source: docs/json/packages/M2_AUTOSARTemplates_SystemTemplate_PncMapping.classes.json"""

from __future__ import annotations
from typing import TYPE_CHECKING, Optional
import xml.etree.ElementTree as ET

from armodel.models.M2.AUTOSARTemplates.GenericStructure.GeneralTemplateClasses.Identifiable.describable import (
    Describable,
)
from armodel.models.M2.AUTOSARTemplates.GenericStructure.GeneralTemplateClasses.ArObject.ar_object import ARObject
from armodel.serialization import SerializationHelper
from armodel.models.M2.AUTOSARTemplates.GenericStructure.GeneralTemplateClasses.ArObject.ar_ref import ARRef
from armodel.models.M2.AUTOSARTemplates.GenericStructure.GeneralTemplateClasses.PrimitiveTypes import (
    Boolean,
    Identifier,
    PositiveInteger,
)
from armodel.models.M2.AUTOSARTemplates.SystemTemplate.Fibex.Fibex4Ethernet.ServiceInstances.consumed_provided_service_instance_group import (
    ConsumedProvidedServiceInstanceGroup,
)
from armodel.models.M2.AUTOSARTemplates.SystemTemplate.Fibex.FibexCore.CoreTopology.ecu_instance import (
    EcuInstance,
)
from armodel.models.M2.AUTOSARTemplates.SystemTemplate.Fibex.FibexCore.CoreCommunication.frame_triggering import (
    FrameTriggering,
)
from armodel.models.M2.AUTOSARTemplates.SystemTemplate.Fibex.FibexCore.CoreCommunication.i_signal_i_pdu_group import (
    ISignalIPduGroup,
)
from armodel.models.M2.AUTOSARTemplates.SystemTemplate.Fibex.FibexCore.CoreCommunication.pdur_i_pdu_group import (
    PdurIPduGroup,
)
from armodel.models.M2.AUTOSARTemplates.SystemTemplate.Fibex.FibexCore.CoreTopology.physical_channel import (
    PhysicalChannel,
)
from armodel.models.M2.AUTOSARTemplates.SystemTemplate.PncMapping.pnc_mapping_ident import (
    PncMappingIdent,
)
from armodel.models.M2.AUTOSARTemplates.SWComponentTemplate.Components.port_group import (
    PortGroup,
)


class PncMapping(Describable):
    """AUTOSAR PncMapping."""

    @property
    def is_abstract(self) -> bool:
        """Check if this class is abstract.

        Returns:
            False for concrete classes
        """
        return False

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
        # Get XML tag name for this class
        tag = SerializationHelper.get_xml_tag(self.__class__)
        elem = ET.Element(tag)

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

        # Parse dynamic_pnc_refs (list from container "DYNAMIC-PNC-REFS")
        obj.dynamic_pnc_refs = []
        container = SerializationHelper.find_child_element(element, "DYNAMIC-PNC-REFS")
        if container is not None:
            for child in container:
                # Check if child is a reference element (ends with -REF or -TREF)
                child_element_tag = SerializationHelper.strip_namespace(child.tag)
                if child_element_tag.endswith("-REF") or child_element_tag.endswith("-TREF"):
                    # Use ARRef.deserialize() for reference elements
                    child_value = ARRef.deserialize(child)
                else:
                    # Deserialize each child element dynamically based on its tag
                    child_value = SerializationHelper.deserialize_by_tag(child, None)
                if child_value is not None:
                    obj.dynamic_pnc_refs.append(child_value)

        # Parse ident_ref
        child = SerializationHelper.find_child_element(element, "IDENT-REF")
        if child is not None:
            ident_ref_value = ARRef.deserialize(child)
            obj.ident_ref = ident_ref_value

        # Parse physical_channel_refs (list from container "PHYSICAL-CHANNEL-REFS")
        obj.physical_channel_refs = []
        container = SerializationHelper.find_child_element(element, "PHYSICAL-CHANNEL-REFS")
        if container is not None:
            for child in container:
                # Check if child is a reference element (ends with -REF or -TREF)
                child_element_tag = SerializationHelper.strip_namespace(child.tag)
                if child_element_tag.endswith("-REF") or child_element_tag.endswith("-TREF"):
                    # Use ARRef.deserialize() for reference elements
                    child_value = ARRef.deserialize(child)
                else:
                    # Deserialize each child element dynamically based on its tag
                    child_value = SerializationHelper.deserialize_by_tag(child, None)
                if child_value is not None:
                    obj.physical_channel_refs.append(child_value)

        # Parse pnc_consumed_refs (list from container "PNC-CONSUMED-REFS")
        obj.pnc_consumed_refs = []
        container = SerializationHelper.find_child_element(element, "PNC-CONSUMED-REFS")
        if container is not None:
            for child in container:
                # Check if child is a reference element (ends with -REF or -TREF)
                child_element_tag = SerializationHelper.strip_namespace(child.tag)
                if child_element_tag.endswith("-REF") or child_element_tag.endswith("-TREF"):
                    # Use ARRef.deserialize() for reference elements
                    child_value = ARRef.deserialize(child)
                else:
                    # Deserialize each child element dynamically based on its tag
                    child_value = SerializationHelper.deserialize_by_tag(child, None)
                if child_value is not None:
                    obj.pnc_consumed_refs.append(child_value)

        # Parse pnc_group_refs (list from container "PNC-GROUP-REFS")
        obj.pnc_group_refs = []
        container = SerializationHelper.find_child_element(element, "PNC-GROUP-REFS")
        if container is not None:
            for child in container:
                # Check if child is a reference element (ends with -REF or -TREF)
                child_element_tag = SerializationHelper.strip_namespace(child.tag)
                if child_element_tag.endswith("-REF") or child_element_tag.endswith("-TREF"):
                    # Use ARRef.deserialize() for reference elements
                    child_value = ARRef.deserialize(child)
                else:
                    # Deserialize each child element dynamically based on its tag
                    child_value = SerializationHelper.deserialize_by_tag(child, None)
                if child_value is not None:
                    obj.pnc_group_refs.append(child_value)

        # Parse pnc_identifier
        child = SerializationHelper.find_child_element(element, "PNC-IDENTIFIER")
        if child is not None:
            pnc_identifier_value = child.text
            obj.pnc_identifier = pnc_identifier_value

        # Parse pnc_pdur_group_refs (list from container "PNC-PDUR-GROUP-REFS")
        obj.pnc_pdur_group_refs = []
        container = SerializationHelper.find_child_element(element, "PNC-PDUR-GROUP-REFS")
        if container is not None:
            for child in container:
                # Check if child is a reference element (ends with -REF or -TREF)
                child_element_tag = SerializationHelper.strip_namespace(child.tag)
                if child_element_tag.endswith("-REF") or child_element_tag.endswith("-TREF"):
                    # Use ARRef.deserialize() for reference elements
                    child_value = ARRef.deserialize(child)
                else:
                    # Deserialize each child element dynamically based on its tag
                    child_value = SerializationHelper.deserialize_by_tag(child, None)
                if child_value is not None:
                    obj.pnc_pdur_group_refs.append(child_value)

        # Parse pnc_wakeup
        child = SerializationHelper.find_child_element(element, "PNC-WAKEUP")
        if child is not None:
            pnc_wakeup_value = child.text
            obj.pnc_wakeup = pnc_wakeup_value

        # Parse relevant_for_refs (list from container "RELEVANT-FOR-REFS")
        obj.relevant_for_refs = []
        container = SerializationHelper.find_child_element(element, "RELEVANT-FOR-REFS")
        if container is not None:
            for child in container:
                # Check if child is a reference element (ends with -REF or -TREF)
                child_element_tag = SerializationHelper.strip_namespace(child.tag)
                if child_element_tag.endswith("-REF") or child_element_tag.endswith("-TREF"):
                    # Use ARRef.deserialize() for reference elements
                    child_value = ARRef.deserialize(child)
                else:
                    # Deserialize each child element dynamically based on its tag
                    child_value = SerializationHelper.deserialize_by_tag(child, None)
                if child_value is not None:
                    obj.relevant_for_refs.append(child_value)

        # Parse short_label
        child = SerializationHelper.find_child_element(element, "SHORT-LABEL")
        if child is not None:
            short_label_value = SerializationHelper.deserialize_by_tag(child, "Identifier")
            obj.short_label = short_label_value

        # Parse vfc_refs (list from container "VFC-REFS")
        obj.vfc_refs = []
        container = SerializationHelper.find_child_element(element, "VFC-REFS")
        if container is not None:
            for child in container:
                # Check if child is a reference element (ends with -REF or -TREF)
                child_element_tag = SerializationHelper.strip_namespace(child.tag)
                if child_element_tag.endswith("-REF") or child_element_tag.endswith("-TREF"):
                    # Use ARRef.deserialize() for reference elements
                    child_value = ARRef.deserialize(child)
                else:
                    # Deserialize each child element dynamically based on its tag
                    child_value = SerializationHelper.deserialize_by_tag(child, None)
                if child_value is not None:
                    obj.vfc_refs.append(child_value)

        # Parse wakeup_frame_refs (list from container "WAKEUP-FRAME-REFS")
        obj.wakeup_frame_refs = []
        container = SerializationHelper.find_child_element(element, "WAKEUP-FRAME-REFS")
        if container is not None:
            for child in container:
                # Check if child is a reference element (ends with -REF or -TREF)
                child_element_tag = SerializationHelper.strip_namespace(child.tag)
                if child_element_tag.endswith("-REF") or child_element_tag.endswith("-TREF"):
                    # Use ARRef.deserialize() for reference elements
                    child_value = ARRef.deserialize(child)
                else:
                    # Deserialize each child element dynamically based on its tag
                    child_value = SerializationHelper.deserialize_by_tag(child, None)
                if child_value is not None:
                    obj.wakeup_frame_refs.append(child_value)

        return obj



class PncMappingBuilder:
    """Builder for PncMapping with fluent API."""

    def __init__(self) -> None:
        """Initialize builder with defaults."""
        pass
        self._obj: PncMapping = PncMapping()


    def with_admin_data(self, value: Optional[AdminData]) -> "PncMappingBuilder":
        """Set admin_data attribute.

        Args:
            value: Value to set

        Returns:
            self for method chaining
        """
        if value is None and not True:
            raise ValueError("Attribute '" + snake_attr_name + "' is required and cannot be None")
        self._obj.admin_data = value
        return self

    def with_category(self, value: Optional[CategoryString]) -> "PncMappingBuilder":
        """Set category attribute.

        Args:
            value: Value to set

        Returns:
            self for method chaining
        """
        if value is None and not True:
            raise ValueError("Attribute '" + snake_attr_name + "' is required and cannot be None")
        self._obj.category = value
        return self

    def with_desc(self, value: Optional[MultiLanguageOverviewParagraph]) -> "PncMappingBuilder":
        """Set desc attribute.

        Args:
            value: Value to set

        Returns:
            self for method chaining
        """
        if value is None and not True:
            raise ValueError("Attribute '" + snake_attr_name + "' is required and cannot be None")
        self._obj.desc = value
        return self

    def with_introduction(self, value: Optional[DocumentationBlock]) -> "PncMappingBuilder":
        """Set introduction attribute.

        Args:
            value: Value to set

        Returns:
            self for method chaining
        """
        if value is None and not True:
            raise ValueError("Attribute '" + snake_attr_name + "' is required and cannot be None")
        self._obj.introduction = value
        return self

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


    @staticmethod
    def _coerce_to_int(value: Any) -> int:
        """Coerce value to int.

        Args:
            value: Value to coerce

        Returns:
            Integer value

        Raises:
            ValueError: If value cannot be coerced to int
        """
        if isinstance(value, int):
            return value
        if isinstance(value, str) and value.isdigit():
            return int(value)
        if isinstance(value, float):
            return int(value)
        if isinstance(value, bool):
            return int(value)
        raise ValueError(f"Cannot coerce {type(value).__name__} to int: {value}")

    @staticmethod
    def _coerce_to_float(value: Any) -> float:
        """Coerce value to float.

        Args:
            value: Value to coerce

        Returns:
            Float value

        Raises:
            ValueError: If value cannot be coerced to float
        """
        if isinstance(value, float):
            return value
        if isinstance(value, int):
            return float(value)
        if isinstance(value, str):
            try:
                return float(value)
            except ValueError:
                pass
        raise ValueError(f"Cannot coerce {type(value).__name__} to float: {value}")

    @staticmethod
    def _coerce_to_bool(value: Any) -> bool:
        """Coerce value to bool.

        Args:
            value: Value to coerce

        Returns:
            Boolean value

        Raises:
            ValueError: If value cannot be coerced to bool
        """
        if isinstance(value, bool):
            return value
        if isinstance(value, int):
            return bool(value)
        if isinstance(value, str):
            if value.lower() in ("true", "1", "yes"):
                return True
            if value.lower() in ("false", "0", "no"):
                return False
        raise ValueError(f"Cannot coerce {type(value).__name__} to bool: {value}")

    @staticmethod
    def _coerce_to_str(value: Any) -> str:
        """Coerce value to str.

        Args:
            value: Value to coerce

        Returns:
            String value
        """
        return str(value)


    @staticmethod
    def _coerce_to_list(value: Any, item_type: str) -> list:
        """Coerce value to list.

        Args:
            value: Value to coerce
            item_type: Expected item type (for error messages)

        Returns:
            List value

        Raises:
            ValueError: If value cannot be coerced to list
        """
        if isinstance(value, list):
            return value
        if isinstance(value, tuple):
            return list(value)
        raise ValueError(f"Cannot coerce {type(value).__name__} to list[{item_type}]: {value}")


    def _validate_instance(self) -> None:
        """Validate the built instance based on settings."""
        from typing import get_type_hints
        from armodel.core import GlobalSettingsManager, BuilderValidationMode

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