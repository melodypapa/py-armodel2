"""CanClusterBusOffRecovery AUTOSAR element."""

from typing import Optional, cast
import xml.etree.ElementTree as ET
from armodel.models.M2.AUTOSARTemplates.GenericStructure.GeneralTemplateClasses.ar_object import ARObject
from armodel.models.M2.AUTOSARTemplates.GenericStructure.GeneralTemplateClasses.PrimitiveTypes import (
    PositiveInteger,
    TimeValue,
)


class CanClusterBusOffRecovery(ARObject):
    """AUTOSAR CanClusterBusOffRecovery."""

    # XML member definitions for this class only (not inherited from parent classes)
    # Format: (member_name, xml_tag_name, is_attribute, is_list, element_class)
    _xml_members = [
        ("bor_counter_l1_to", None, True, False, None),  # borCounterL1To
        ("bor_time_l1", None, True, False, None),  # borTimeL1
        ("bor_time_l2", None, True, False, None),  # borTimeL2
        ("bor_time_tx", None, True, False, None),  # borTimeTx
        ("main_function", None, True, False, None),  # mainFunction
    ]

    def __init__(self) -> None:
        """Initialize CanClusterBusOffRecovery."""
        super().__init__()
        self.bor_counter_l1_to: Optional[PositiveInteger] = None
        self.bor_time_l1: Optional[TimeValue] = None
        self.bor_time_l2: Optional[TimeValue] = None
        self.bor_time_tx: Optional[TimeValue] = None
        self.main_function: Optional[TimeValue] = None

    def serialize(self, namespace: str, element: Optional[ET.Element] = None) -> ET.Element:
        """Convert CanClusterBusOffRecovery to XML element.

        Args:
            namespace: XML namespace for the element
            element: Optional existing element to add members to (for subclass chaining)

        Returns:
            XML element representing this object
        """
        # ARObject.serialize() handles entire class hierarchy automatically
        return super().serialize(namespace, element)

    @classmethod
    def deserialize(cls, element: ET.Element) -> "CanClusterBusOffRecovery":
        """Create CanClusterBusOffRecovery from XML element.

        Args:
            element: XML element to deserialize from

        Returns:
            CanClusterBusOffRecovery instance
        """
        # ARObject.deserialize() handles entire class hierarchy automatically
        obj = super().deserialize(element)
        # Cast to CanClusterBusOffRecovery since parent returns ARObject
        return cast("CanClusterBusOffRecovery", obj)


class CanClusterBusOffRecoveryBuilder:
    """Builder for CanClusterBusOffRecovery."""

    def __init__(self) -> None:
        """Initialize builder."""
        self._obj: CanClusterBusOffRecovery = CanClusterBusOffRecovery()

    def build(self) -> CanClusterBusOffRecovery:
        """Build and return CanClusterBusOffRecovery object.

        Returns:
            CanClusterBusOffRecovery instance
        """
        # TODO: Add validation
        return self._obj
