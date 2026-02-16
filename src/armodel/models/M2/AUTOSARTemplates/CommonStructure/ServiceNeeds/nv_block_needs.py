"""NvBlockNeeds AUTOSAR element."""

from typing import Optional, cast
import xml.etree.ElementTree as ET
from armodel.models.M2.AUTOSARTemplates.CommonStructure.ServiceNeeds.service_needs import (
    ServiceNeeds,
)
from armodel.models.M2.AUTOSARTemplates.GenericStructure.GeneralTemplateClasses.PrimitiveTypes import (
    Boolean,
    PositiveInteger,
    TimeValue,
)
from armodel.models.M2.AUTOSARTemplates.CommonStructure.ServiceNeeds.nv_block_needs import (
    NvBlockNeeds,
)


class NvBlockNeeds(ServiceNeeds):
    """AUTOSAR NvBlockNeeds."""

    # XML member definitions for this class only (not inherited from parent classes)
    # Format: (member_name, xml_tag_name, is_attribute, is_list, element_class)
    _xml_members = [
        ("calc_ram_block", None, True, False, None),  # calcRamBlock
        ("check_static_block_id", None, True, False, None),  # checkStaticBlockId
        ("cyclic_writing", None, True, False, None),  # cyclicWriting
        ("n_data_sets", None, True, False, None),  # nDataSets
        ("n_rom_blocks", None, True, False, None),  # nRomBlocks
        ("ram_block_status_control", None, False, False, RamBlockStatusControlEnum),  # ramBlockStatusControl
        ("readonly", None, True, False, None),  # readonly
        ("reliability_reliability_enum", None, False, False, NvBlockNeeds),  # reliabilityReliabilityEnum
        ("resistant_to", None, True, False, None),  # resistantTo
        ("restore_at_start", None, True, False, None),  # restoreAtStart
        ("select_block_for", None, True, False, None),  # selectBlockFor
        ("store_at", None, True, False, None),  # storeAt
        ("store_cyclic", None, True, False, None),  # storeCyclic
        ("store", None, True, False, None),  # store
        ("store_immediate", None, True, False, None),  # storeImmediate
        ("store_on_change", None, True, False, None),  # storeOnChange
        ("use_auto", None, True, False, None),  # useAuto
        ("use_crc_comp", None, True, False, None),  # useCRCComp
        ("write_only_once", None, True, False, None),  # writeOnlyOnce
        ("write_verification", None, True, False, None),  # writeVerification
        ("writing", None, True, False, None),  # writing
        ("writing_priority", None, False, False, NvBlockNeedsWritingPriorityEnum),  # writingPriority
    ]

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

    def serialize(self, namespace: str, element: Optional[ET.Element] = None) -> ET.Element:
        """Convert NvBlockNeeds to XML element.

        Args:
            namespace: XML namespace for the element
            element: Optional existing element to add members to (for subclass chaining)

        Returns:
            XML element representing this object
        """
        # ARObject.serialize() handles entire class hierarchy automatically
        return super().serialize(namespace, element)

    @classmethod
    def deserialize(cls, element: ET.Element) -> "NvBlockNeeds":
        """Create NvBlockNeeds from XML element.

        Args:
            element: XML element to deserialize from

        Returns:
            NvBlockNeeds instance
        """
        # ARObject.deserialize() handles entire class hierarchy automatically
        obj = super().deserialize(element)
        # Cast to NvBlockNeeds since parent returns ARObject
        return cast("NvBlockNeeds", obj)


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
