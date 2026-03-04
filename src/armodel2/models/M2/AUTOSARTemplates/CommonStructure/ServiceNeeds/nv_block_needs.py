"""NvBlockNeeds AUTOSAR element.

References:
  - AUTOSAR_CP_TPS_BSWModuleDescriptionTemplate.pdf (page 231)
  - AUTOSAR_CP_TPS_SoftwareComponentTemplate.pdf (page 679)

JSON Source: docs/json/packages/M2_AUTOSARTemplates_CommonStructure_ServiceNeeds.classes.json"""

from __future__ import annotations
from typing import TYPE_CHECKING, Optional
import xml.etree.ElementTree as ET

from armodel2.models.M2.AUTOSARTemplates.CommonStructure.ServiceNeeds.service_needs import (
    ServiceNeeds,
)
from armodel2.models.M2.builder_base import BuilderBase
from armodel2.models.M2.AUTOSARTemplates.CommonStructure.ServiceNeeds.service_needs import ServiceNeedsBuilder
from armodel2.models.M2.AUTOSARTemplates.CommonStructure.ServiceNeeds import (
    NvBlockNeedsReliabilityEnum,
    NvBlockNeedsWritingPriorityEnum,
)
from armodel2.models.M2.AUTOSARTemplates.SWComponentTemplate.NvBlockComponent import (
    RamBlockStatusControlEnum,
)
from armodel2.models.M2.AUTOSARTemplates.GenericStructure.GeneralTemplateClasses.PrimitiveTypes import (
    Boolean,
    PositiveInteger,
    TimeValue,
)
from armodel2.models.M2.AUTOSARTemplates.GenericStructure.GeneralTemplateClasses.ArObject.ar_object import ARObject
from armodel2.serialization import SerializationHelper


class NvBlockNeeds(ServiceNeeds):
    """AUTOSAR NvBlockNeeds."""

    @property
    def is_abstract(self) -> bool:
        """Check if this class is abstract.

        Returns:
            False for concrete classes
        """
        return False

    _XML_TAG = "NV-BLOCK-NEEDS"


    calc_ram_block_crc: Optional[Boolean]
    check_static_block_id: Optional[Boolean]
    cyclic_writing_period: Optional[TimeValue]
    n_data_sets: Optional[PositiveInteger]
    n_rom_blocks: Optional[PositiveInteger]
    ram_block_status_control: Optional[RamBlockStatusControlEnum]
    readonly: Optional[Boolean]
    reliability: Optional[NvBlockNeedsReliabilityEnum]
    resistant_to_changed_sw: Optional[Boolean]
    restore_at_start: Optional[Boolean]
    select_block_for_first_init_all: Optional[Boolean]
    store_at_shutdown: Optional[Boolean]
    store_cyclic: Optional[Boolean]
    store_emergency: Optional[Boolean]
    store_immediate: Optional[Boolean]
    store_on_change: Optional[Boolean]
    use_auto_validation_at_shut_down: Optional[Boolean]
    use_crc_comp_mechanism: Optional[Boolean]
    write_only_once: Optional[Boolean]
    write_verification: Optional[Boolean]
    writing_frequency: Optional[PositiveInteger]
    writing_priority: Optional[NvBlockNeedsWritingPriorityEnum]
    _DESERIALIZE_DISPATCH = {
        "CALC-RAM-BLOCK-CRC": lambda obj, elem: setattr(obj, "calc_ram_block_crc", SerializationHelper.deserialize_by_tag(elem, "Boolean")),
        "CHECK-STATIC-BLOCK-ID": lambda obj, elem: setattr(obj, "check_static_block_id", SerializationHelper.deserialize_by_tag(elem, "Boolean")),
        "CYCLIC-WRITING-PERIOD": lambda obj, elem: setattr(obj, "cyclic_writing_period", SerializationHelper.deserialize_by_tag(elem, "TimeValue")),
        "N-DATA-SETS": lambda obj, elem: setattr(obj, "n_data_sets", SerializationHelper.deserialize_by_tag(elem, "PositiveInteger")),
        "N-ROM-BLOCKS": lambda obj, elem: setattr(obj, "n_rom_blocks", SerializationHelper.deserialize_by_tag(elem, "PositiveInteger")),
        "RAM-BLOCK-STATUS-CONTROL": lambda obj, elem: setattr(obj, "ram_block_status_control", RamBlockStatusControlEnum.deserialize(elem)),
        "READONLY": lambda obj, elem: setattr(obj, "readonly", SerializationHelper.deserialize_by_tag(elem, "Boolean")),
        "RELIABILITY": lambda obj, elem: setattr(obj, "reliability", NvBlockNeedsReliabilityEnum.deserialize(elem)),
        "RESISTANT-TO-CHANGED-SW": lambda obj, elem: setattr(obj, "resistant_to_changed_sw", SerializationHelper.deserialize_by_tag(elem, "Boolean")),
        "RESTORE-AT-START": lambda obj, elem: setattr(obj, "restore_at_start", SerializationHelper.deserialize_by_tag(elem, "Boolean")),
        "SELECT-BLOCK-FOR-FIRST-INIT-ALL": lambda obj, elem: setattr(obj, "select_block_for_first_init_all", SerializationHelper.deserialize_by_tag(elem, "Boolean")),
        "STORE-AT-SHUTDOWN": lambda obj, elem: setattr(obj, "store_at_shutdown", SerializationHelper.deserialize_by_tag(elem, "Boolean")),
        "STORE-CYCLIC": lambda obj, elem: setattr(obj, "store_cyclic", SerializationHelper.deserialize_by_tag(elem, "Boolean")),
        "STORE-EMERGENCY": lambda obj, elem: setattr(obj, "store_emergency", SerializationHelper.deserialize_by_tag(elem, "Boolean")),
        "STORE-IMMEDIATE": lambda obj, elem: setattr(obj, "store_immediate", SerializationHelper.deserialize_by_tag(elem, "Boolean")),
        "STORE-ON-CHANGE": lambda obj, elem: setattr(obj, "store_on_change", SerializationHelper.deserialize_by_tag(elem, "Boolean")),
        "USE-AUTO-VALIDATION-AT-SHUT-DOWN": lambda obj, elem: setattr(obj, "use_auto_validation_at_shut_down", SerializationHelper.deserialize_by_tag(elem, "Boolean")),
        "USE-CRC-COMP-MECHANISM": lambda obj, elem: setattr(obj, "use_crc_comp_mechanism", SerializationHelper.deserialize_by_tag(elem, "Boolean")),
        "WRITE-ONLY-ONCE": lambda obj, elem: setattr(obj, "write_only_once", SerializationHelper.deserialize_by_tag(elem, "Boolean")),
        "WRITE-VERIFICATION": lambda obj, elem: setattr(obj, "write_verification", SerializationHelper.deserialize_by_tag(elem, "Boolean")),
        "WRITING-FREQUENCY": lambda obj, elem: setattr(obj, "writing_frequency", SerializationHelper.deserialize_by_tag(elem, "PositiveInteger")),
        "WRITING-PRIORITY": lambda obj, elem: setattr(obj, "writing_priority", NvBlockNeedsWritingPriorityEnum.deserialize(elem)),
    }


    def __init__(self) -> None:
        """Initialize NvBlockNeeds."""
        super().__init__()
        self.calc_ram_block_crc: Optional[Boolean] = None
        self.check_static_block_id: Optional[Boolean] = None
        self.cyclic_writing_period: Optional[TimeValue] = None
        self.n_data_sets: Optional[PositiveInteger] = None
        self.n_rom_blocks: Optional[PositiveInteger] = None
        self.ram_block_status_control: Optional[RamBlockStatusControlEnum] = None
        self.readonly: Optional[Boolean] = None
        self.reliability: Optional[NvBlockNeedsReliabilityEnum] = None
        self.resistant_to_changed_sw: Optional[Boolean] = None
        self.restore_at_start: Optional[Boolean] = None
        self.select_block_for_first_init_all: Optional[Boolean] = None
        self.store_at_shutdown: Optional[Boolean] = None
        self.store_cyclic: Optional[Boolean] = None
        self.store_emergency: Optional[Boolean] = None
        self.store_immediate: Optional[Boolean] = None
        self.store_on_change: Optional[Boolean] = None
        self.use_auto_validation_at_shut_down: Optional[Boolean] = None
        self.use_crc_comp_mechanism: Optional[Boolean] = None
        self.write_only_once: Optional[Boolean] = None
        self.write_verification: Optional[Boolean] = None
        self.writing_frequency: Optional[PositiveInteger] = None
        self.writing_priority: Optional[NvBlockNeedsWritingPriorityEnum] = None

    def serialize(self) -> ET.Element:
        """Serialize NvBlockNeeds to XML element.

        Returns:
            xml.etree.ElementTree.Element representing this object
        """
        # Use pre-computed _XML_TAG constant
        elem = ET.Element(self._XML_TAG)

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

        # Serialize calc_ram_block_crc
        if self.calc_ram_block_crc is not None:
            serialized = SerializationHelper.serialize_item(self.calc_ram_block_crc, "Boolean")
            if serialized is not None:
                # Wrap with correct tag
                wrapped = ET.Element("CALC-RAM-BLOCK-CRC")
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

        # Serialize cyclic_writing_period
        if self.cyclic_writing_period is not None:
            serialized = SerializationHelper.serialize_item(self.cyclic_writing_period, "TimeValue")
            if serialized is not None:
                # Wrap with correct tag
                wrapped = ET.Element("CYCLIC-WRITING-PERIOD")
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

        # Serialize reliability
        if self.reliability is not None:
            serialized = SerializationHelper.serialize_item(self.reliability, "NvBlockNeedsReliabilityEnum")
            if serialized is not None:
                # Wrap with correct tag
                wrapped = ET.Element("RELIABILITY")
                if hasattr(serialized, 'attrib'):
                    wrapped.attrib.update(serialized.attrib)
                if serialized.text:
                    wrapped.text = serialized.text
                for child in serialized:
                    wrapped.append(child)
                elem.append(wrapped)

        # Serialize resistant_to_changed_sw
        if self.resistant_to_changed_sw is not None:
            serialized = SerializationHelper.serialize_item(self.resistant_to_changed_sw, "Boolean")
            if serialized is not None:
                # Wrap with correct tag
                wrapped = ET.Element("RESISTANT-TO-CHANGED-SW")
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

        # Serialize select_block_for_first_init_all
        if self.select_block_for_first_init_all is not None:
            serialized = SerializationHelper.serialize_item(self.select_block_for_first_init_all, "Boolean")
            if serialized is not None:
                # Wrap with correct tag
                wrapped = ET.Element("SELECT-BLOCK-FOR-FIRST-INIT-ALL")
                if hasattr(serialized, 'attrib'):
                    wrapped.attrib.update(serialized.attrib)
                if serialized.text:
                    wrapped.text = serialized.text
                for child in serialized:
                    wrapped.append(child)
                elem.append(wrapped)

        # Serialize store_at_shutdown
        if self.store_at_shutdown is not None:
            serialized = SerializationHelper.serialize_item(self.store_at_shutdown, "Boolean")
            if serialized is not None:
                # Wrap with correct tag
                wrapped = ET.Element("STORE-AT-SHUTDOWN")
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

        # Serialize store_emergency
        if self.store_emergency is not None:
            serialized = SerializationHelper.serialize_item(self.store_emergency, "Boolean")
            if serialized is not None:
                # Wrap with correct tag
                wrapped = ET.Element("STORE-EMERGENCY")
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

        # Serialize use_auto_validation_at_shut_down
        if self.use_auto_validation_at_shut_down is not None:
            serialized = SerializationHelper.serialize_item(self.use_auto_validation_at_shut_down, "Boolean")
            if serialized is not None:
                # Wrap with correct tag
                wrapped = ET.Element("USE-AUTO-VALIDATION-AT-SHUT-DOWN")
                if hasattr(serialized, 'attrib'):
                    wrapped.attrib.update(serialized.attrib)
                if serialized.text:
                    wrapped.text = serialized.text
                for child in serialized:
                    wrapped.append(child)
                elem.append(wrapped)

        # Serialize use_crc_comp_mechanism
        if self.use_crc_comp_mechanism is not None:
            serialized = SerializationHelper.serialize_item(self.use_crc_comp_mechanism, "Boolean")
            if serialized is not None:
                # Wrap with correct tag
                wrapped = ET.Element("USE-CRC-COMP-MECHANISM")
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

        # Serialize writing_frequency
        if self.writing_frequency is not None:
            serialized = SerializationHelper.serialize_item(self.writing_frequency, "PositiveInteger")
            if serialized is not None:
                # Wrap with correct tag
                wrapped = ET.Element("WRITING-FREQUENCY")
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

        # Single-pass deserialization with if-elif-else chain
        ns_split = '}'
        for child in element:
            tag = child.tag.split(ns_split, 1)[1] if child.tag.startswith('{') else child.tag
            if tag == "CALC-RAM-BLOCK-CRC":
                setattr(obj, "calc_ram_block_crc", SerializationHelper.deserialize_by_tag(child, "Boolean"))
            elif tag == "CHECK-STATIC-BLOCK-ID":
                setattr(obj, "check_static_block_id", SerializationHelper.deserialize_by_tag(child, "Boolean"))
            elif tag == "CYCLIC-WRITING-PERIOD":
                setattr(obj, "cyclic_writing_period", SerializationHelper.deserialize_by_tag(child, "TimeValue"))
            elif tag == "N-DATA-SETS":
                setattr(obj, "n_data_sets", SerializationHelper.deserialize_by_tag(child, "PositiveInteger"))
            elif tag == "N-ROM-BLOCKS":
                setattr(obj, "n_rom_blocks", SerializationHelper.deserialize_by_tag(child, "PositiveInteger"))
            elif tag == "RAM-BLOCK-STATUS-CONTROL":
                setattr(obj, "ram_block_status_control", RamBlockStatusControlEnum.deserialize(child))
            elif tag == "READONLY":
                setattr(obj, "readonly", SerializationHelper.deserialize_by_tag(child, "Boolean"))
            elif tag == "RELIABILITY":
                setattr(obj, "reliability", NvBlockNeedsReliabilityEnum.deserialize(child))
            elif tag == "RESISTANT-TO-CHANGED-SW":
                setattr(obj, "resistant_to_changed_sw", SerializationHelper.deserialize_by_tag(child, "Boolean"))
            elif tag == "RESTORE-AT-START":
                setattr(obj, "restore_at_start", SerializationHelper.deserialize_by_tag(child, "Boolean"))
            elif tag == "SELECT-BLOCK-FOR-FIRST-INIT-ALL":
                setattr(obj, "select_block_for_first_init_all", SerializationHelper.deserialize_by_tag(child, "Boolean"))
            elif tag == "STORE-AT-SHUTDOWN":
                setattr(obj, "store_at_shutdown", SerializationHelper.deserialize_by_tag(child, "Boolean"))
            elif tag == "STORE-CYCLIC":
                setattr(obj, "store_cyclic", SerializationHelper.deserialize_by_tag(child, "Boolean"))
            elif tag == "STORE-EMERGENCY":
                setattr(obj, "store_emergency", SerializationHelper.deserialize_by_tag(child, "Boolean"))
            elif tag == "STORE-IMMEDIATE":
                setattr(obj, "store_immediate", SerializationHelper.deserialize_by_tag(child, "Boolean"))
            elif tag == "STORE-ON-CHANGE":
                setattr(obj, "store_on_change", SerializationHelper.deserialize_by_tag(child, "Boolean"))
            elif tag == "USE-AUTO-VALIDATION-AT-SHUT-DOWN":
                setattr(obj, "use_auto_validation_at_shut_down", SerializationHelper.deserialize_by_tag(child, "Boolean"))
            elif tag == "USE-CRC-COMP-MECHANISM":
                setattr(obj, "use_crc_comp_mechanism", SerializationHelper.deserialize_by_tag(child, "Boolean"))
            elif tag == "WRITE-ONLY-ONCE":
                setattr(obj, "write_only_once", SerializationHelper.deserialize_by_tag(child, "Boolean"))
            elif tag == "WRITE-VERIFICATION":
                setattr(obj, "write_verification", SerializationHelper.deserialize_by_tag(child, "Boolean"))
            elif tag == "WRITING-FREQUENCY":
                setattr(obj, "writing_frequency", SerializationHelper.deserialize_by_tag(child, "PositiveInteger"))
            elif tag == "WRITING-PRIORITY":
                setattr(obj, "writing_priority", NvBlockNeedsWritingPriorityEnum.deserialize(child))

        return obj



class NvBlockNeedsBuilder(ServiceNeedsBuilder):
    """Builder for NvBlockNeeds with fluent API."""

    def __init__(self) -> None:
        """Initialize builder with defaults."""
        super().__init__()
        self._obj: NvBlockNeeds = NvBlockNeeds()


    def with_calc_ram_block_crc(self, value: Optional[Boolean]) -> "NvBlockNeedsBuilder":
        """Set calc_ram_block_crc attribute.

        Args:
            value: Value to set

        Returns:
            self for method chaining
        """
        if value is None and not True:
            raise ValueError("Attribute '" + snake_attr_name + "' is required and cannot be None")
        self._obj.calc_ram_block_crc = value
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

    def with_cyclic_writing_period(self, value: Optional[TimeValue]) -> "NvBlockNeedsBuilder":
        """Set cyclic_writing_period attribute.

        Args:
            value: Value to set

        Returns:
            self for method chaining
        """
        if value is None and not True:
            raise ValueError("Attribute '" + snake_attr_name + "' is required and cannot be None")
        self._obj.cyclic_writing_period = value
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

    def with_reliability(self, value: Optional[NvBlockNeedsReliabilityEnum]) -> "NvBlockNeedsBuilder":
        """Set reliability attribute.

        Args:
            value: Value to set

        Returns:
            self for method chaining
        """
        if value is None and not True:
            raise ValueError("Attribute '" + snake_attr_name + "' is required and cannot be None")
        self._obj.reliability = value
        return self

    def with_resistant_to_changed_sw(self, value: Optional[Boolean]) -> "NvBlockNeedsBuilder":
        """Set resistant_to_changed_sw attribute.

        Args:
            value: Value to set

        Returns:
            self for method chaining
        """
        if value is None and not True:
            raise ValueError("Attribute '" + snake_attr_name + "' is required and cannot be None")
        self._obj.resistant_to_changed_sw = value
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

    def with_select_block_for_first_init_all(self, value: Optional[Boolean]) -> "NvBlockNeedsBuilder":
        """Set select_block_for_first_init_all attribute.

        Args:
            value: Value to set

        Returns:
            self for method chaining
        """
        if value is None and not True:
            raise ValueError("Attribute '" + snake_attr_name + "' is required and cannot be None")
        self._obj.select_block_for_first_init_all = value
        return self

    def with_store_at_shutdown(self, value: Optional[Boolean]) -> "NvBlockNeedsBuilder":
        """Set store_at_shutdown attribute.

        Args:
            value: Value to set

        Returns:
            self for method chaining
        """
        if value is None and not True:
            raise ValueError("Attribute '" + snake_attr_name + "' is required and cannot be None")
        self._obj.store_at_shutdown = value
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

    def with_store_emergency(self, value: Optional[Boolean]) -> "NvBlockNeedsBuilder":
        """Set store_emergency attribute.

        Args:
            value: Value to set

        Returns:
            self for method chaining
        """
        if value is None and not True:
            raise ValueError("Attribute '" + snake_attr_name + "' is required and cannot be None")
        self._obj.store_emergency = value
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

    def with_use_auto_validation_at_shut_down(self, value: Optional[Boolean]) -> "NvBlockNeedsBuilder":
        """Set use_auto_validation_at_shut_down attribute.

        Args:
            value: Value to set

        Returns:
            self for method chaining
        """
        if value is None and not True:
            raise ValueError("Attribute '" + snake_attr_name + "' is required and cannot be None")
        self._obj.use_auto_validation_at_shut_down = value
        return self

    def with_use_crc_comp_mechanism(self, value: Optional[Boolean]) -> "NvBlockNeedsBuilder":
        """Set use_crc_comp_mechanism attribute.

        Args:
            value: Value to set

        Returns:
            self for method chaining
        """
        if value is None and not True:
            raise ValueError("Attribute '" + snake_attr_name + "' is required and cannot be None")
        self._obj.use_crc_comp_mechanism = value
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

    def with_writing_frequency(self, value: Optional[PositiveInteger]) -> "NvBlockNeedsBuilder":
        """Set writing_frequency attribute.

        Args:
            value: Value to set

        Returns:
            self for method chaining
        """
        if value is None and not True:
            raise ValueError("Attribute '" + snake_attr_name + "' is required and cannot be None")
        self._obj.writing_frequency = value
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



    # Pre-computed validation constants (generated from JSON schema)
    _OPTIONAL_ATTRIBUTES = {
        "calcRamBlockCrc",
        "checkStaticBlockId",
        "cyclicWritingPeriod",
        "nDataSets",
        "nRomBlocks",
        "ramBlockStatusControl",
        "readonly",
        "reliability",
        "resistantToChangedSw",
        "restoreAtStart",
        "selectBlockForFirstInitAll",
        "storeAtShutdown",
        "storeCyclic",
        "storeEmergency",
        "storeImmediate",
        "storeOnChange",
        "useAutoValidationAtShutDown",
        "useCRCCompMechanism",
        "writeOnlyOnce",
        "writeVerification",
        "writingFrequency",
        "writingPriority",
    }


    def _validate_instance(self) -> None:
        """Validate the built instance based on settings."""
        from armodel2.core import GlobalSettingsManager, BuilderValidationMode

        settings = GlobalSettingsManager()
        mode = settings.builder_validation

        if mode == BuilderValidationMode.DISABLED:
            return

        # No required attributes to validate (all are optional)


    def build(self) -> NvBlockNeeds:
        """Build and return the NvBlockNeeds instance with validation."""
        self._validate_instance()
        return self._obj