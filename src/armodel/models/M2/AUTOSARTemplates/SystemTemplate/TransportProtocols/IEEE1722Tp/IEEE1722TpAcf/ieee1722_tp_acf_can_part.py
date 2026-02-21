"""IEEE1722TpAcfCanPart AUTOSAR element.

References:
  - AUTOSAR_CP_TPS_SystemTemplate.pdf (page 661)

JSON Source: docs/json/packages/M2_AUTOSARTemplates_SystemTemplate_TransportProtocols_IEEE1722Tp_IEEE1722TpAcf.classes.json"""

from __future__ import annotations
from typing import TYPE_CHECKING, Optional
import xml.etree.ElementTree as ET

from armodel.models.M2.AUTOSARTemplates.SystemTemplate.TransportProtocols.IEEE1722Tp.IEEE1722TpAcf.ieee1722_tp_acf_bus_part import (
    IEEE1722TpAcfBusPart,
)
from armodel.models.M2.AUTOSARTemplates.GenericStructure.GeneralTemplateClasses.ArObject.ar_object import ARObject
from armodel.serialization import SerializationHelper
from armodel.models.M2.AUTOSARTemplates.GenericStructure.GeneralTemplateClasses.ArObject.ar_ref import ARRef
from armodel.models.M2.AUTOSARTemplates.SystemTemplate.Fibex.Fibex4Can.CanCommunication import (
    CanAddressingModeType,
    CanFrameTxBehaviorEnum,
)
from armodel.models.M2.AUTOSARTemplates.GenericStructure.GeneralTemplateClasses.PrimitiveTypes import (
    Boolean,
)
from armodel.models.M2.AUTOSARTemplates.SystemTemplate.Fibex.FibexCore.CoreCommunication.pdu_triggering import (
    PduTriggering,
)
from armodel.models.M2.AUTOSARTemplates.SystemTemplate.Fibex.Fibex4Can.CanCommunication.rx_identifier_range import (
    RxIdentifierRange,
)


class IEEE1722TpAcfCanPart(IEEE1722TpAcfBusPart):
    """AUTOSAR IEEE1722TpAcfCanPart."""

    @property
    def is_abstract(self) -> bool:
        """Check if this class is abstract.

        Returns:
            False for concrete classes
        """
        return False

    can_addressing: Optional[CanAddressingModeType]
    can_bit_rate_switch: Optional[Boolean]
    can_frame_tx_behavior: Optional[CanFrameTxBehaviorEnum]
    can_identifier: Optional[RxIdentifierRange]
    sdu_ref: Optional[ARRef]
    def __init__(self) -> None:
        """Initialize IEEE1722TpAcfCanPart."""
        super().__init__()
        self.can_addressing: Optional[CanAddressingModeType] = None
        self.can_bit_rate_switch: Optional[Boolean] = None
        self.can_frame_tx_behavior: Optional[CanFrameTxBehaviorEnum] = None
        self.can_identifier: Optional[RxIdentifierRange] = None
        self.sdu_ref: Optional[ARRef] = None

    def serialize(self) -> ET.Element:
        """Serialize IEEE1722TpAcfCanPart to XML element.

        Returns:
            xml.etree.ElementTree.Element representing this object
        """
        # Get XML tag name for this class
        tag = SerializationHelper.get_xml_tag(self.__class__)
        elem = ET.Element(tag)

        # First, call parent's serialize to handle inherited attributes
        parent_elem = super(IEEE1722TpAcfCanPart, self).serialize()

        # Copy all attributes from parent element
        elem.attrib.update(parent_elem.attrib)

        # Copy text from parent element
        if parent_elem.text:
            elem.text = parent_elem.text

        # Copy all children from parent element
        for child in parent_elem:
            elem.append(child)

        # Serialize can_addressing
        if self.can_addressing is not None:
            serialized = SerializationHelper.serialize_item(self.can_addressing, "CanAddressingModeType")
            if serialized is not None:
                # Wrap with correct tag
                wrapped = ET.Element("CAN-ADDRESSING")
                if hasattr(serialized, 'attrib'):
                    wrapped.attrib.update(serialized.attrib)
                    if serialized.text:
                        wrapped.text = serialized.text
                for child in serialized:
                    wrapped.append(child)
                elem.append(wrapped)

        # Serialize can_bit_rate_switch
        if self.can_bit_rate_switch is not None:
            serialized = SerializationHelper.serialize_item(self.can_bit_rate_switch, "Boolean")
            if serialized is not None:
                # Wrap with correct tag
                wrapped = ET.Element("CAN-BIT-RATE-SWITCH")
                if hasattr(serialized, 'attrib'):
                    wrapped.attrib.update(serialized.attrib)
                    if serialized.text:
                        wrapped.text = serialized.text
                for child in serialized:
                    wrapped.append(child)
                elem.append(wrapped)

        # Serialize can_frame_tx_behavior
        if self.can_frame_tx_behavior is not None:
            serialized = SerializationHelper.serialize_item(self.can_frame_tx_behavior, "CanFrameTxBehaviorEnum")
            if serialized is not None:
                # Wrap with correct tag
                wrapped = ET.Element("CAN-FRAME-TX-BEHAVIOR")
                if hasattr(serialized, 'attrib'):
                    wrapped.attrib.update(serialized.attrib)
                    if serialized.text:
                        wrapped.text = serialized.text
                for child in serialized:
                    wrapped.append(child)
                elem.append(wrapped)

        # Serialize can_identifier
        if self.can_identifier is not None:
            serialized = SerializationHelper.serialize_item(self.can_identifier, "RxIdentifierRange")
            if serialized is not None:
                # Wrap with correct tag
                wrapped = ET.Element("CAN-IDENTIFIER")
                if hasattr(serialized, 'attrib'):
                    wrapped.attrib.update(serialized.attrib)
                    if serialized.text:
                        wrapped.text = serialized.text
                for child in serialized:
                    wrapped.append(child)
                elem.append(wrapped)

        # Serialize sdu_ref
        if self.sdu_ref is not None:
            serialized = SerializationHelper.serialize_item(self.sdu_ref, "PduTriggering")
            if serialized is not None:
                # Wrap with correct tag
                wrapped = ET.Element("SDU-REF")
                if hasattr(serialized, 'attrib'):
                    wrapped.attrib.update(serialized.attrib)
                    if serialized.text:
                        wrapped.text = serialized.text
                for child in serialized:
                    wrapped.append(child)
                elem.append(wrapped)

        return elem

    @classmethod
    def deserialize(cls, element: ET.Element) -> "IEEE1722TpAcfCanPart":
        """Deserialize XML element to IEEE1722TpAcfCanPart object.

        Args:
            element: XML element to deserialize from

        Returns:
            Deserialized IEEE1722TpAcfCanPart object
        """
        # First, call parent's deserialize to handle inherited attributes
        obj = super(IEEE1722TpAcfCanPart, cls).deserialize(element)

        # Parse can_addressing
        child = SerializationHelper.find_child_element(element, "CAN-ADDRESSING")
        if child is not None:
            can_addressing_value = CanAddressingModeType.deserialize(child)
            obj.can_addressing = can_addressing_value

        # Parse can_bit_rate_switch
        child = SerializationHelper.find_child_element(element, "CAN-BIT-RATE-SWITCH")
        if child is not None:
            can_bit_rate_switch_value = child.text
            obj.can_bit_rate_switch = can_bit_rate_switch_value

        # Parse can_frame_tx_behavior
        child = SerializationHelper.find_child_element(element, "CAN-FRAME-TX-BEHAVIOR")
        if child is not None:
            can_frame_tx_behavior_value = CanFrameTxBehaviorEnum.deserialize(child)
            obj.can_frame_tx_behavior = can_frame_tx_behavior_value

        # Parse can_identifier
        child = SerializationHelper.find_child_element(element, "CAN-IDENTIFIER")
        if child is not None:
            can_identifier_value = SerializationHelper.deserialize_by_tag(child, "RxIdentifierRange")
            obj.can_identifier = can_identifier_value

        # Parse sdu_ref
        child = SerializationHelper.find_child_element(element, "SDU-REF")
        if child is not None:
            sdu_ref_value = ARRef.deserialize(child)
            obj.sdu_ref = sdu_ref_value

        return obj



class IEEE1722TpAcfCanPartBuilder:
    """Builder for IEEE1722TpAcfCanPart."""

    def __init__(self) -> None:
        """Initialize builder."""
        self._obj: IEEE1722TpAcfCanPart = IEEE1722TpAcfCanPart()

    def build(self) -> IEEE1722TpAcfCanPart:
        """Build and return IEEE1722TpAcfCanPart object.

        Returns:
            IEEE1722TpAcfCanPart instance
        """
        # TODO: Add validation
        return self._obj
