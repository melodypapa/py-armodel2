"""FlexrayTpConnectionControl AUTOSAR element."""

from typing import Optional, cast
import xml.etree.ElementTree as ET
from armodel.models.M2.AUTOSARTemplates.GenericStructure.GeneralTemplateClasses.Identifiable.identifiable import (
    Identifiable,
)
from armodel.models.M2.AUTOSARTemplates.GenericStructure.GeneralTemplateClasses.PrimitiveTypes import (
    Integer,
    TimeValue,
)


class FlexrayTpConnectionControl(Identifiable):
    """AUTOSAR FlexrayTpConnectionControl."""

    # XML member definitions for this class only (not inherited from parent classes)
    # Format: (member_name, xml_tag_name, is_attribute, is_list, element_class)
    _xml_members = [
        ("ack_type", None, False, False, FrArTpAckType),  # ackType
        ("max_fc_wait", None, True, False, None),  # maxFcWait
        ("max_number_of", None, True, False, None),  # maxNumberOf
        ("max_retries", None, True, False, None),  # maxRetries
        ("separation_cycle", None, True, False, None),  # separationCycle
        ("time_br", None, True, False, None),  # timeBr
        ("time_buffer", None, True, False, None),  # timeBuffer
        ("time_cs", None, True, False, None),  # timeCs
        ("timeout_ar", None, True, False, None),  # timeoutAr
        ("timeout_as", None, True, False, None),  # timeoutAs
        ("timeout_bs", None, True, False, None),  # timeoutBs
        ("timeout_cr", None, True, False, None),  # timeoutCr
    ]

    def __init__(self) -> None:
        """Initialize FlexrayTpConnectionControl."""
        super().__init__()
        self.ack_type: Optional[FrArTpAckType] = None
        self.max_fc_wait: Optional[Integer] = None
        self.max_number_of: Optional[Integer] = None
        self.max_retries: Optional[Integer] = None
        self.separation_cycle: Optional[Integer] = None
        self.time_br: Optional[TimeValue] = None
        self.time_buffer: Optional[TimeValue] = None
        self.time_cs: Optional[TimeValue] = None
        self.timeout_ar: Optional[TimeValue] = None
        self.timeout_as: Optional[TimeValue] = None
        self.timeout_bs: Optional[TimeValue] = None
        self.timeout_cr: Optional[TimeValue] = None

    def serialize(self, namespace: str, element: Optional[ET.Element] = None) -> ET.Element:
        """Convert FlexrayTpConnectionControl to XML element.

        Args:
            namespace: XML namespace for the element
            element: Optional existing element to add members to (for subclass chaining)

        Returns:
            XML element representing this object
        """
        # ARObject.serialize() handles entire class hierarchy automatically
        return super().serialize(namespace, element)

    @classmethod
    def deserialize(cls, element: ET.Element) -> "FlexrayTpConnectionControl":
        """Create FlexrayTpConnectionControl from XML element.

        Args:
            element: XML element to deserialize from

        Returns:
            FlexrayTpConnectionControl instance
        """
        # ARObject.deserialize() handles entire class hierarchy automatically
        obj = super().deserialize(element)
        # Cast to FlexrayTpConnectionControl since parent returns ARObject
        return cast("FlexrayTpConnectionControl", obj)


class FlexrayTpConnectionControlBuilder:
    """Builder for FlexrayTpConnectionControl."""

    def __init__(self) -> None:
        """Initialize builder."""
        self._obj: FlexrayTpConnectionControl = FlexrayTpConnectionControl()

    def build(self) -> FlexrayTpConnectionControl:
        """Build and return FlexrayTpConnectionControl object.

        Returns:
            FlexrayTpConnectionControl instance
        """
        # TODO: Add validation
        return self._obj
