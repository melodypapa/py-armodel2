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
from armodel.models.M2.AUTOSARTemplates.GenericStructure.GeneralTemplateClasses.ArObject.ar_object import ARObject
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
        child = ARObject._find_child_element(element, "CALC-RAM-BLOCK")
        if child is not None:
            calc_ram_block_value = child.text
            obj.calc_ram_block = calc_ram_block_value

        # Parse check_static_block_id
        child = ARObject._find_child_element(element, "CHECK-STATIC-BLOCK-ID")
        if child is not None:
            check_static_block_id_value = child.text
            obj.check_static_block_id = check_static_block_id_value

        # Parse cyclic_writing
        child = ARObject._find_child_element(element, "CYCLIC-WRITING")
        if child is not None:
            cyclic_writing_value = child.text
            obj.cyclic_writing = cyclic_writing_value

        # Parse n_data_sets
        child = ARObject._find_child_element(element, "N-DATA-SETS")
        if child is not None:
            n_data_sets_value = child.text
            obj.n_data_sets = n_data_sets_value

        # Parse n_rom_blocks
        child = ARObject._find_child_element(element, "N-ROM-BLOCKS")
        if child is not None:
            n_rom_blocks_value = child.text
            obj.n_rom_blocks = n_rom_blocks_value

        # Parse ram_block_status_control
        child = ARObject._find_child_element(element, "RAM-BLOCK-STATUS-CONTROL")
        if child is not None:
            ram_block_status_control_value = RamBlockStatusControlEnum.deserialize(child)
            obj.ram_block_status_control = ram_block_status_control_value

        # Parse readonly
        child = ARObject._find_child_element(element, "READONLY")
        if child is not None:
            readonly_value = child.text
            obj.readonly = readonly_value

        # Parse reliability_reliability_enum
        child = ARObject._find_child_element(element, "RELIABILITY-RELIABILITY-ENUM")
        if child is not None:
            reliability_reliability_enum_value = ARObject._deserialize_by_tag(child, "NvBlockNeeds")
            obj.reliability_reliability_enum = reliability_reliability_enum_value

        # Parse resistant_to
        child = ARObject._find_child_element(element, "RESISTANT-TO")
        if child is not None:
            resistant_to_value = child.text
            obj.resistant_to = resistant_to_value

        # Parse restore_at_start
        child = ARObject._find_child_element(element, "RESTORE-AT-START")
        if child is not None:
            restore_at_start_value = child.text
            obj.restore_at_start = restore_at_start_value

        # Parse select_block_for
        child = ARObject._find_child_element(element, "SELECT-BLOCK-FOR")
        if child is not None:
            select_block_for_value = child.text
            obj.select_block_for = select_block_for_value

        # Parse store_at
        child = ARObject._find_child_element(element, "STORE-AT")
        if child is not None:
            store_at_value = child.text
            obj.store_at = store_at_value

        # Parse store_cyclic
        child = ARObject._find_child_element(element, "STORE-CYCLIC")
        if child is not None:
            store_cyclic_value = child.text
            obj.store_cyclic = store_cyclic_value

        # Parse store
        child = ARObject._find_child_element(element, "STORE")
        if child is not None:
            store_value = child.text
            obj.store = store_value

        # Parse store_immediate
        child = ARObject._find_child_element(element, "STORE-IMMEDIATE")
        if child is not None:
            store_immediate_value = child.text
            obj.store_immediate = store_immediate_value

        # Parse store_on_change
        child = ARObject._find_child_element(element, "STORE-ON-CHANGE")
        if child is not None:
            store_on_change_value = child.text
            obj.store_on_change = store_on_change_value

        # Parse use_auto
        child = ARObject._find_child_element(element, "USE-AUTO")
        if child is not None:
            use_auto_value = child.text
            obj.use_auto = use_auto_value

        # Parse use_crc_comp
        child = ARObject._find_child_element(element, "USE-CRC-COMP")
        if child is not None:
            use_crc_comp_value = child.text
            obj.use_crc_comp = use_crc_comp_value

        # Parse write_only_once
        child = ARObject._find_child_element(element, "WRITE-ONLY-ONCE")
        if child is not None:
            write_only_once_value = child.text
            obj.write_only_once = write_only_once_value

        # Parse write_verification
        child = ARObject._find_child_element(element, "WRITE-VERIFICATION")
        if child is not None:
            write_verification_value = child.text
            obj.write_verification = write_verification_value

        # Parse writing
        child = ARObject._find_child_element(element, "WRITING")
        if child is not None:
            writing_value = child.text
            obj.writing = writing_value

        # Parse writing_priority
        child = ARObject._find_child_element(element, "WRITING-PRIORITY")
        if child is not None:
            writing_priority_value = NvBlockNeedsWritingPriorityEnum.deserialize(child)
            obj.writing_priority = writing_priority_value

        return obj



class NvBlockNeedsBuilder:
    """Builder for NvBlockNeeds."""

    def __init__(self) -> None:
        """Initialize builder."""
        self._obj: NvBlockNeeds = NvBlockNeeds()

    def build(self) -> NvBlockNeeds:
        """Build and return NvBlockNeeds object.

        Returns:
            NvBlockNeeds instance
        """
        # TODO: Add validation
        return self._obj
