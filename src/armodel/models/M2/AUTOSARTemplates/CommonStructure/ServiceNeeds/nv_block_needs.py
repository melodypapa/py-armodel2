"""NvBlockNeeds AUTOSAR element.

References:
  - AUTOSAR_CP_TPS_BSWModuleDescriptionTemplate.pdf (page 231)
  - AUTOSAR_CP_TPS_SoftwareComponentTemplate.pdf (page 679)

JSON Source: docs/json/packages/M2_AUTOSARTemplates_CommonStructure_ServiceNeeds.classes.json"""

from __future__ import annotations
from typing import TYPE_CHECKING, Optional
import xml.etree.ElementTree as ET

from armodel.models.M2.AUTOSARTemplates.CommonStructure.ServiceNeeds.service_needs import (
    ServiceNeeds,
)
from armodel.models.M2.builder_base import BuilderBase
from armodel.models.M2.AUTOSARTemplates.CommonStructure.ServiceNeeds.service_needs import ServiceNeedsBuilder
from armodel.models.M2.AUTOSARTemplates.CommonStructure.ServiceNeeds import (
    NvBlockNeedsWritingPriorityEnum,
)
from armodel.models.M2.AUTOSARTemplates.SWComponentTemplate.NvBlockComponent import (
    RamBlockStatusControlEnum,
)
from armodel.models.M2.AUTOSARTemplates.GenericStructure.GeneralTemplateClasses.PrimitiveTypes import (
    Boolean,
    PositiveInteger,
    TimeValue,
)
from armodel.models.M2.AUTOSARTemplates.GenericStructure.GeneralTemplateClasses.ArObject.ar_object import ARObject
from armodel.serialization import SerializationHelper


class NvBlockNeeds(ServiceNeeds):
    """AUTOSAR NvBlockNeeds."""

    @property
    def is_abstract(self) -> bool:
        """Check if this class is abstract.

        Returns:
            False for concrete classes
        """
        return False

    calc_ram_block: Optional[Boolean]
    check_static_block_id: Optional[Boolean]
    cyclic_writing: Optional[TimeValue]
    n_data_sets: Optional[PositiveInteger]
    n_rom_blocks: Optional[PositiveInteger]
    ram_block_status_control: Optional[RamBlockStatusControlEnum]
    readonly: Optional[Boolean]
    reliability_reliability_enum: Optional[NvBlockNeeds]
    resistant_to: Optional[Boolean]
    restore_at_start: Optional[Boolean]
    select_block_for: Optional[Boolean]
    store_at: Optional[Boolean]
    store_cyclic: Optional[Boolean]
    store: Optional[Boolean]
    store_immediate: Optional[Boolean]
    store_on_change: Optional[Boolean]
    use_auto: Optional[Boolean]
    use_crc_comp: Optional[Boolean]
    write_only_once: Optional[Boolean]
    write_verification: Optional[Boolean]
    writing: Optional[PositiveInteger]
    writing_priority: Optional[NvBlockNeedsWritingPriorityEnum]
    def __init__(self) -> None:
        """Initialize NvBlockNeeds."""
        super().__init__()
        self.calc_ram_block: Optional[Boolean] = None
        self.check_static_block_id: Optional[Boolean] = None
        self.cyclic_writing: Optional[TimeValue] = None
        self.n_data_sets: Optional[PositiveInteger] = None
        self.n_rom_blocks: Optional[PositiveInteger] = None
        self.ram_block_status_control: Optional[RamBlockStatusControlEnum] = None
        self.readonly: Optional[Boolean] = None
        self.reliability_reliability_enum: Optional[NvBlockNeeds] = None
        self.resistant_to: Optional[Boolean] = None
        self.restore_at_start: Optional[Boolean] = None
        self.select_block_for: Optional[Boolean] = None
        self.store_at: Optional[Boolean] = None
        self.store_cyclic: Optional[Boolean] = None
        self.store: Optional[Boolean] = None
        self.store_immediate: Optional[Boolean] = None
        self.store_on_change: Optional[Boolean] = None
        self.use_auto: Optional[Boolean] = None
        self.use_crc_comp: Optional[Boolean] = None
        self.write_only_once: Optional[Boolean] = None
        self.write_verification: Optional[Boolean] = None
        self.writing: Optional[PositiveInteger] = None
        self.writing_priority: Optional[NvBlockNeedsWritingPriorityEnum] = None

    def serialize(self) -> ET.Element:
        """Serialize NvBlockNeeds to XML element.

        Returns:
            xml.etree.ElementTree.Element representing this object
        """
        # Get XML tag name for this class
        tag = SerializationHelper.get_xml_tag(self.__class__)
        elem = ET.Element(tag)

        # First, call parent's serialize to handle inherited attributes
        parent_elem = super(NvBlockNeeds, self).serialize()

        # Copy all attributes from parent element
        elem.attrib.update(parent_elem.attrib)

        # Copy text from parent element
        if parent_elem.text:
            elem.text = parent_elem.text

        # Copy all children from parent element
        for child in parent_elem:
            elem.append(child)

        # Serialize calc_ram_block
        if self.calc_ram_block is not None:
            serialized = SerializationHelper.serialize_item(self.calc_ram_block, "Boolean")
            if serialized is not None:
                # Wrap with correct tag
                wrapped = ET.Element("CALC-RAM-BLOCK")
                if hasattr(serialized, 'attrib'):
                    wrapped.attrib.update(serialized.attrib)
                    if serialized.text:
                        wrapped.text = serialized.text
                for child in serialized:
                    wrapped.append(child)
                elem.append(wrapped)

        # Serialize check_static_block_id
        if self.check_static_block_id is not None:
            serialized = SerializationHelper.serialize_item(self.check_static_block_id, "Boolean")
            if serialized is not None:
                # Wrap with correct tag
                wrapped = ET.Element("CHECK-STATIC-BLOCK-ID")
                if hasattr(serialized, 'attrib'):
                    wrapped.attrib.update(serialized.attrib)
                    if serialized.text:
                        wrapped.text = serialized.text
                for child in serialized:
                    wrapped.append(child)
                elem.append(wrapped)

        # Serialize cyclic_writing
        if self.cyclic_writing is not None:
            serialized = SerializationHelper.serialize_item(self.cyclic_writing, "TimeValue")
            if serialized is not None:
                # Wrap with correct tag
                wrapped = ET.Element("CYCLIC-WRITING")
                if hasattr(serialized, 'attrib'):
                    wrapped.attrib.update(serialized.attrib)
                    if serialized.text:
                        wrapped.text = serialized.text
                for child in serialized:
                    wrapped.append(child)
                elem.append(wrapped)

        # Serialize n_data_sets
        if self.n_data_sets is not None:
            serialized = SerializationHelper.serialize_item(self.n_data_sets, "PositiveInteger")
            if serialized is not None:
                # Wrap with correct tag
                wrapped = ET.Element("N-DATA-SETS")
                if hasattr(serialized, 'attrib'):
                    wrapped.attrib.update(serialized.attrib)
                    if serialized.text:
                        wrapped.text = serialized.text
                for child in serialized:
                    wrapped.append(child)
                elem.append(wrapped)

        # Serialize n_rom_blocks
        if self.n_rom_blocks is not None:
            serialized = SerializationHelper.serialize_item(self.n_rom_blocks, "PositiveInteger")
            if serialized is not None:
                # Wrap with correct tag
                wrapped = ET.Element("N-ROM-BLOCKS")
                if hasattr(serialized, 'attrib'):
                    wrapped.attrib.update(serialized.attrib)
                    if serialized.text:
                        wrapped.text = serialized.text
                for child in serialized:
                    wrapped.append(child)
                elem.append(wrapped)

        # Serialize ram_block_status_control
        if self.ram_block_status_control is not None:
            serialized = SerializationHelper.serialize_item(self.ram_block_status_control, "RamBlockStatusControlEnum")
            if serialized is not None:
                # Wrap with correct tag
                wrapped = ET.Element("RAM-BLOCK-STATUS-CONTROL")
                if hasattr(serialized, 'attrib'):
                    wrapped.attrib.update(serialized.attrib)
                    if serialized.text:
                        wrapped.text = serialized.text
                for child in serialized:
                    wrapped.append(child)
                elem.append(wrapped)

        # Serialize readonly
        if self.readonly is not None:
            serialized = SerializationHelper.serialize_item(self.readonly, "Boolean")
            if serialized is not None:
                # Wrap with correct tag
                wrapped = ET.Element("READONLY")
                if hasattr(serialized, 'attrib'):
                    wrapped.attrib.update(serialized.attrib)
                    if serialized.text:
                        wrapped.text = serialized.text
                for child in serialized:
                    wrapped.append(child)
                elem.append(wrapped)

        # Serialize reliability_reliability_enum
        if self.reliability_reliability_enum is not None:
            serialized = SerializationHelper.serialize_item(self.reliability_reliability_enum, "NvBlockNeeds")
            if serialized is not None:
                # Wrap with correct tag
                wrapped = ET.Element("RELIABILITY-RELIABILITY-ENUM")
                if hasattr(serialized, 'attrib'):
                    wrapped.attrib.update(serialized.attrib)
                    if serialized.text:
                        wrapped.text = serialized.text
                for child in serialized:
                    wrapped.append(child)
                elem.append(wrapped)

        # Serialize resistant_to
        if self.resistant_to is not None:
            serialized = SerializationHelper.serialize_item(self.resistant_to, "Boolean")
            if serialized is not None:
                # Wrap with correct tag
                wrapped = ET.Element("RESISTANT-TO")
                if hasattr(serialized, 'attrib'):
                    wrapped.attrib.update(serialized.attrib)
                    if serialized.text:
                        wrapped.text = serialized.text
                for child in serialized:
                    wrapped.append(child)
                elem.append(wrapped)

        # Serialize restore_at_start
        if self.restore_at_start is not None:
            serialized = SerializationHelper.serialize_item(self.restore_at_start, "Boolean")
            if serialized is not None:
                # Wrap with correct tag
                wrapped = ET.Element("RESTORE-AT-START")
                if hasattr(serialized, 'attrib'):
                    wrapped.attrib.update(serialized.attrib)
                    if serialized.text:
                        wrapped.text = serialized.text
                for child in serialized:
                    wrapped.append(child)
                elem.append(wrapped)

        # Serialize select_block_for
        if self.select_block_for is not None:
            serialized = SerializationHelper.serialize_item(self.select_block_for, "Boolean")
            if serialized is not None:
                # Wrap with correct tag
                wrapped = ET.Element("SELECT-BLOCK-FOR")
                if hasattr(serialized, 'attrib'):
                    wrapped.attrib.update(serialized.attrib)
                    if serialized.text:
                        wrapped.text = serialized.text
                for child in serialized:
                    wrapped.append(child)
                elem.append(wrapped)

        # Serialize store_at
        if self.store_at is not None:
            serialized = SerializationHelper.serialize_item(self.store_at, "Boolean")
            if serialized is not None:
                # Wrap with correct tag
                wrapped = ET.Element("STORE-AT")
                if hasattr(serialized, 'attrib'):
                    wrapped.attrib.update(serialized.attrib)
                    if serialized.text:
                        wrapped.text = serialized.text
                for child in serialized:
                    wrapped.append(child)
                elem.append(wrapped)

        # Serialize store_cyclic
        if self.store_cyclic is not None:
            serialized = SerializationHelper.serialize_item(self.store_cyclic, "Boolean")
            if serialized is not None:
                # Wrap with correct tag
                wrapped = ET.Element("STORE-CYCLIC")
                if hasattr(serialized, 'attrib'):
                    wrapped.attrib.update(serialized.attrib)
                    if serialized.text:
                        wrapped.text = serialized.text
                for child in serialized:
                    wrapped.append(child)
                elem.append(wrapped)

        # Serialize store
        if self.store is not None:
            serialized = SerializationHelper.serialize_item(self.store, "Boolean")
            if serialized is not None:
                # Wrap with correct tag
                wrapped = ET.Element("STORE")
                if hasattr(serialized, 'attrib'):
                    wrapped.attrib.update(serialized.attrib)
                    if serialized.text:
                        wrapped.text = serialized.text
                for child in serialized:
                    wrapped.append(child)
                elem.append(wrapped)

        # Serialize store_immediate
        if self.store_immediate is not None:
            serialized = SerializationHelper.serialize_item(self.store_immediate, "Boolean")
            if serialized is not None:
                # Wrap with correct tag
                wrapped = ET.Element("STORE-IMMEDIATE")
                if hasattr(serialized, 'attrib'):
                    wrapped.attrib.update(serialized.attrib)
                    if serialized.text:
                        wrapped.text = serialized.text
                for child in serialized:
                    wrapped.append(child)
                elem.append(wrapped)

        # Serialize store_on_change
        if self.store_on_change is not None:
            serialized = SerializationHelper.serialize_item(self.store_on_change, "Boolean")
            if serialized is not None:
                # Wrap with correct tag
                wrapped = ET.Element("STORE-ON-CHANGE")
                if hasattr(serialized, 'attrib'):
                    wrapped.attrib.update(serialized.attrib)
                    if serialized.text:
                        wrapped.text = serialized.text
                for child in serialized:
                    wrapped.append(child)
                elem.append(wrapped)

        # Serialize use_auto
        if self.use_auto is not None:
            serialized = SerializationHelper.serialize_item(self.use_auto, "Boolean")
            if serialized is not None:
                # Wrap with correct tag
                wrapped = ET.Element("USE-AUTO")
                if hasattr(serialized, 'attrib'):
                    wrapped.attrib.update(serialized.attrib)
                    if serialized.text:
                        wrapped.text = serialized.text
                for child in serialized:
                    wrapped.append(child)
                elem.append(wrapped)

        # Serialize use_crc_comp
        if self.use_crc_comp is not None:
            serialized = SerializationHelper.serialize_item(self.use_crc_comp, "Boolean")
            if serialized is not None:
                # Wrap with correct tag
                wrapped = ET.Element("USE-CRC-COMP")
                if hasattr(serialized, 'attrib'):
                    wrapped.attrib.update(serialized.attrib)
                    if serialized.text:
                        wrapped.text = serialized.text
                for child in serialized:
                    wrapped.append(child)
                elem.append(wrapped)

        # Serialize write_only_once
        if self.write_only_once is not None:
            serialized = SerializationHelper.serialize_item(self.write_only_once, "Boolean")
            if serialized is not None:
                # Wrap with correct tag
                wrapped = ET.Element("WRITE-ONLY-ONCE")
                if hasattr(serialized, 'attrib'):
                    wrapped.attrib.update(serialized.attrib)
                    if serialized.text:
                        wrapped.text = serialized.text
                for child in serialized:
                    wrapped.append(child)
                elem.append(wrapped)

        # Serialize write_verification
        if self.write_verification is not None:
            serialized = SerializationHelper.serialize_item(self.write_verification, "Boolean")
            if serialized is not None:
                # Wrap with correct tag
                wrapped = ET.Element("WRITE-VERIFICATION")
                if hasattr(serialized, 'attrib'):
                    wrapped.attrib.update(serialized.attrib)
                    if serialized.text:
                        wrapped.text = serialized.text
                for child in serialized:
                    wrapped.append(child)
                elem.append(wrapped)

        # Serialize writing
        if self.writing is not None:
            serialized = SerializationHelper.serialize_item(self.writing, "PositiveInteger")
            if serialized is not None:
                # Wrap with correct tag
                wrapped = ET.Element("WRITING")
                if hasattr(serialized, 'attrib'):
                    wrapped.attrib.update(serialized.attrib)
                    if serialized.text:
                        wrapped.text = serialized.text
                for child in serialized:
                    wrapped.append(child)
                elem.append(wrapped)

        # Serialize writing_priority
        if self.writing_priority is not None:
            serialized = SerializationHelper.serialize_item(self.writing_priority, "NvBlockNeedsWritingPriorityEnum")
            if serialized is not None:
                # Wrap with correct tag
                wrapped = ET.Element("WRITING-PRIORITY")
                if hasattr(serialized, 'attrib'):
                    wrapped.attrib.update(serialized.attrib)
                    if serialized.text:
                        wrapped.text = serialized.text
                for child in serialized:
                    wrapped.append(child)
                elem.append(wrapped)

        return elem

    @classmethod
    def deserialize(cls, element: ET.Element) -> "NvBlockNeeds":
        """Deserialize XML element to NvBlockNeeds object.

        Args:
            element: XML element to deserialize from

        Returns:
            Deserialized NvBlockNeeds object
        """
        # First, call parent's deserialize to handle inherited attributes
        obj = super(NvBlockNeeds, cls).deserialize(element)

        # Parse calc_ram_block
        child = SerializationHelper.find_child_element(element, "CALC-RAM-BLOCK")
        if child is not None:
            calc_ram_block_value = child.text
            obj.calc_ram_block = calc_ram_block_value

        # Parse check_static_block_id
        child = SerializationHelper.find_child_element(element, "CHECK-STATIC-BLOCK-ID")
        if child is not None:
            check_static_block_id_value = child.text
            obj.check_static_block_id = check_static_block_id_value

        # Parse cyclic_writing
        child = SerializationHelper.find_child_element(element, "CYCLIC-WRITING")
        if child is not None:
            cyclic_writing_value = child.text
            obj.cyclic_writing = cyclic_writing_value

        # Parse n_data_sets
        child = SerializationHelper.find_child_element(element, "N-DATA-SETS")
        if child is not None:
            n_data_sets_value = child.text
            obj.n_data_sets = n_data_sets_value

        # Parse n_rom_blocks
        child = SerializationHelper.find_child_element(element, "N-ROM-BLOCKS")
        if child is not None:
            n_rom_blocks_value = child.text
            obj.n_rom_blocks = n_rom_blocks_value

        # Parse ram_block_status_control
        child = SerializationHelper.find_child_element(element, "RAM-BLOCK-STATUS-CONTROL")
        if child is not None:
            ram_block_status_control_value = RamBlockStatusControlEnum.deserialize(child)
            obj.ram_block_status_control = ram_block_status_control_value

        # Parse readonly
        child = SerializationHelper.find_child_element(element, "READONLY")
        if child is not None:
            readonly_value = child.text
            obj.readonly = readonly_value

        # Parse reliability_reliability_enum
        child = SerializationHelper.find_child_element(element, "RELIABILITY-RELIABILITY-ENUM")
        if child is not None:
            reliability_reliability_enum_value = SerializationHelper.deserialize_by_tag(child, "NvBlockNeeds")
            obj.reliability_reliability_enum = reliability_reliability_enum_value

        # Parse resistant_to
        child = SerializationHelper.find_child_element(element, "RESISTANT-TO")
        if child is not None:
            resistant_to_value = child.text
            obj.resistant_to = resistant_to_value

        # Parse restore_at_start
        child = SerializationHelper.find_child_element(element, "RESTORE-AT-START")
        if child is not None:
            restore_at_start_value = child.text
            obj.restore_at_start = restore_at_start_value

        # Parse select_block_for
        child = SerializationHelper.find_child_element(element, "SELECT-BLOCK-FOR")
        if child is not None:
            select_block_for_value = child.text
            obj.select_block_for = select_block_for_value

        # Parse store_at
        child = SerializationHelper.find_child_element(element, "STORE-AT")
        if child is not None:
            store_at_value = child.text
            obj.store_at = store_at_value

        # Parse store_cyclic
        child = SerializationHelper.find_child_element(element, "STORE-CYCLIC")
        if child is not None:
            store_cyclic_value = child.text
            obj.store_cyclic = store_cyclic_value

        # Parse store
        child = SerializationHelper.find_child_element(element, "STORE")
        if child is not None:
            store_value = child.text
            obj.store = store_value

        # Parse store_immediate
        child = SerializationHelper.find_child_element(element, "STORE-IMMEDIATE")
        if child is not None:
            store_immediate_value = child.text
            obj.store_immediate = store_immediate_value

        # Parse store_on_change
        child = SerializationHelper.find_child_element(element, "STORE-ON-CHANGE")
        if child is not None:
            store_on_change_value = child.text
            obj.store_on_change = store_on_change_value

        # Parse use_auto
        child = SerializationHelper.find_child_element(element, "USE-AUTO")
        if child is not None:
            use_auto_value = child.text
            obj.use_auto = use_auto_value

        # Parse use_crc_comp
        child = SerializationHelper.find_child_element(element, "USE-CRC-COMP")
        if child is not None:
            use_crc_comp_value = child.text
            obj.use_crc_comp = use_crc_comp_value

        # Parse write_only_once
        child = SerializationHelper.find_child_element(element, "WRITE-ONLY-ONCE")
        if child is not None:
            write_only_once_value = child.text
            obj.write_only_once = write_only_once_value

        # Parse write_verification
        child = SerializationHelper.find_child_element(element, "WRITE-VERIFICATION")
        if child is not None:
            write_verification_value = child.text
            obj.write_verification = write_verification_value

        # Parse writing
        child = SerializationHelper.find_child_element(element, "WRITING")
        if child is not None:
            writing_value = child.text
            obj.writing = writing_value

        # Parse writing_priority
        child = SerializationHelper.find_child_element(element, "WRITING-PRIORITY")
        if child is not None:
            writing_priority_value = NvBlockNeedsWritingPriorityEnum.deserialize(child)
            obj.writing_priority = writing_priority_value

        return obj



class NvBlockNeedsBuilder(ServiceNeedsBuilder):
    """Builder for NvBlockNeeds with fluent API."""

    def __init__(self) -> None:
        """Initialize builder with defaults."""
        super().__init__()
        self._obj: NvBlockNeeds = NvBlockNeeds()


    def with_calc_ram_block(self, value: Optional[Boolean]) -> "NvBlockNeedsBuilder":
        """Set calc_ram_block attribute.

        Args:
            value: Value to set

        Returns:
            self for method chaining
        """
        if value is None and not True:
            raise ValueError("Attribute '" + snake_attr_name + "' is required and cannot be None")
        self._obj.calc_ram_block = value
        return self

    def with_check_static_block_id(self, value: Optional[Boolean]) -> "NvBlockNeedsBuilder":
        """Set check_static_block_id attribute.

        Args:
            value: Value to set

        Returns:
            self for method chaining
        """
        if value is None and not True:
            raise ValueError("Attribute '" + snake_attr_name + "' is required and cannot be None")
        self._obj.check_static_block_id = value
        return self

    def with_cyclic_writing(self, value: Optional[TimeValue]) -> "NvBlockNeedsBuilder":
        """Set cyclic_writing attribute.

        Args:
            value: Value to set

        Returns:
            self for method chaining
        """
        if value is None and not True:
            raise ValueError("Attribute '" + snake_attr_name + "' is required and cannot be None")
        self._obj.cyclic_writing = value
        return self

    def with_n_data_sets(self, value: Optional[PositiveInteger]) -> "NvBlockNeedsBuilder":
        """Set n_data_sets attribute.

        Args:
            value: Value to set

        Returns:
            self for method chaining
        """
        if value is None and not True:
            raise ValueError("Attribute '" + snake_attr_name + "' is required and cannot be None")
        self._obj.n_data_sets = value
        return self

    def with_n_rom_blocks(self, value: Optional[PositiveInteger]) -> "NvBlockNeedsBuilder":
        """Set n_rom_blocks attribute.

        Args:
            value: Value to set

        Returns:
            self for method chaining
        """
        if value is None and not True:
            raise ValueError("Attribute '" + snake_attr_name + "' is required and cannot be None")
        self._obj.n_rom_blocks = value
        return self

    def with_ram_block_status_control(self, value: Optional[RamBlockStatusControlEnum]) -> "NvBlockNeedsBuilder":
        """Set ram_block_status_control attribute.

        Args:
            value: Value to set

        Returns:
            self for method chaining
        """
        if value is None and not True:
            raise ValueError("Attribute '" + snake_attr_name + "' is required and cannot be None")
        self._obj.ram_block_status_control = value
        return self

    def with_readonly(self, value: Optional[Boolean]) -> "NvBlockNeedsBuilder":
        """Set readonly attribute.

        Args:
            value: Value to set

        Returns:
            self for method chaining
        """
        if value is None and not True:
            raise ValueError("Attribute '" + snake_attr_name + "' is required and cannot be None")
        self._obj.readonly = value
        return self

    def with_reliability_reliability_enum(self, value: Optional[NvBlockNeeds]) -> "NvBlockNeedsBuilder":
        """Set reliability_reliability_enum attribute.

        Args:
            value: Value to set

        Returns:
            self for method chaining
        """
        if value is None and not True:
            raise ValueError("Attribute '" + snake_attr_name + "' is required and cannot be None")
        self._obj.reliability_reliability_enum = value
        return self

    def with_resistant_to(self, value: Optional[Boolean]) -> "NvBlockNeedsBuilder":
        """Set resistant_to attribute.

        Args:
            value: Value to set

        Returns:
            self for method chaining
        """
        if value is None and not True:
            raise ValueError("Attribute '" + snake_attr_name + "' is required and cannot be None")
        self._obj.resistant_to = value
        return self

    def with_restore_at_start(self, value: Optional[Boolean]) -> "NvBlockNeedsBuilder":
        """Set restore_at_start attribute.

        Args:
            value: Value to set

        Returns:
            self for method chaining
        """
        if value is None and not True:
            raise ValueError("Attribute '" + snake_attr_name + "' is required and cannot be None")
        self._obj.restore_at_start = value
        return self

    def with_select_block_for(self, value: Optional[Boolean]) -> "NvBlockNeedsBuilder":
        """Set select_block_for attribute.

        Args:
            value: Value to set

        Returns:
            self for method chaining
        """
        if value is None and not True:
            raise ValueError("Attribute '" + snake_attr_name + "' is required and cannot be None")
        self._obj.select_block_for = value
        return self

    def with_store_at(self, value: Optional[Boolean]) -> "NvBlockNeedsBuilder":
        """Set store_at attribute.

        Args:
            value: Value to set

        Returns:
            self for method chaining
        """
        if value is None and not True:
            raise ValueError("Attribute '" + snake_attr_name + "' is required and cannot be None")
        self._obj.store_at = value
        return self

    def with_store_cyclic(self, value: Optional[Boolean]) -> "NvBlockNeedsBuilder":
        """Set store_cyclic attribute.

        Args:
            value: Value to set

        Returns:
            self for method chaining
        """
        if value is None and not True:
            raise ValueError("Attribute '" + snake_attr_name + "' is required and cannot be None")
        self._obj.store_cyclic = value
        return self

    def with_store(self, value: Optional[Boolean]) -> "NvBlockNeedsBuilder":
        """Set store attribute.

        Args:
            value: Value to set

        Returns:
            self for method chaining
        """
        if value is None and not True:
            raise ValueError("Attribute '" + snake_attr_name + "' is required and cannot be None")
        self._obj.store = value
        return self

    def with_store_immediate(self, value: Optional[Boolean]) -> "NvBlockNeedsBuilder":
        """Set store_immediate attribute.

        Args:
            value: Value to set

        Returns:
            self for method chaining
        """
        if value is None and not True:
            raise ValueError("Attribute '" + snake_attr_name + "' is required and cannot be None")
        self._obj.store_immediate = value
        return self

    def with_store_on_change(self, value: Optional[Boolean]) -> "NvBlockNeedsBuilder":
        """Set store_on_change attribute.

        Args:
            value: Value to set

        Returns:
            self for method chaining
        """
        if value is None and not True:
            raise ValueError("Attribute '" + snake_attr_name + "' is required and cannot be None")
        self._obj.store_on_change = value
        return self

    def with_use_auto(self, value: Optional[Boolean]) -> "NvBlockNeedsBuilder":
        """Set use_auto attribute.

        Args:
            value: Value to set

        Returns:
            self for method chaining
        """
        if value is None and not True:
            raise ValueError("Attribute '" + snake_attr_name + "' is required and cannot be None")
        self._obj.use_auto = value
        return self

    def with_use_crc_comp(self, value: Optional[Boolean]) -> "NvBlockNeedsBuilder":
        """Set use_crc_comp attribute.

        Args:
            value: Value to set

        Returns:
            self for method chaining
        """
        if value is None and not True:
            raise ValueError("Attribute '" + snake_attr_name + "' is required and cannot be None")
        self._obj.use_crc_comp = value
        return self

    def with_write_only_once(self, value: Optional[Boolean]) -> "NvBlockNeedsBuilder":
        """Set write_only_once attribute.

        Args:
            value: Value to set

        Returns:
            self for method chaining
        """
        if value is None and not True:
            raise ValueError("Attribute '" + snake_attr_name + "' is required and cannot be None")
        self._obj.write_only_once = value
        return self

    def with_write_verification(self, value: Optional[Boolean]) -> "NvBlockNeedsBuilder":
        """Set write_verification attribute.

        Args:
            value: Value to set

        Returns:
            self for method chaining
        """
        if value is None and not True:
            raise ValueError("Attribute '" + snake_attr_name + "' is required and cannot be None")
        self._obj.write_verification = value
        return self

    def with_writing(self, value: Optional[PositiveInteger]) -> "NvBlockNeedsBuilder":
        """Set writing attribute.

        Args:
            value: Value to set

        Returns:
            self for method chaining
        """
        if value is None and not True:
            raise ValueError("Attribute '" + snake_attr_name + "' is required and cannot be None")
        self._obj.writing = value
        return self

    def with_writing_priority(self, value: Optional[NvBlockNeedsWritingPriorityEnum]) -> "NvBlockNeedsBuilder":
        """Set writing_priority attribute.

        Args:
            value: Value to set

        Returns:
            self for method chaining
        """
        if value is None and not True:
            raise ValueError("Attribute '" + snake_attr_name + "' is required and cannot be None")
        self._obj.writing_priority = value
        return self




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


    def build(self) -> NvBlockNeeds:
        """Build and return the NvBlockNeeds instance with validation."""
        self._validate_instance()
        pass
        return self._obj