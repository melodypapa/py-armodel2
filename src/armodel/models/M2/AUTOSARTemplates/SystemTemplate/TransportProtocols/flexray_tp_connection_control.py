"""FlexrayTpConnectionControl AUTOSAR element.

References:
  - AUTOSAR_CP_TPS_SystemTemplate.pdf (page 593)

JSON Source: docs/json/packages/M2_AUTOSARTemplates_SystemTemplate_TransportProtocols.classes.json"""

from __future__ import annotations
from typing import TYPE_CHECKING, Optional
import xml.etree.ElementTree as ET

from armodel.models.M2.AUTOSARTemplates.GenericStructure.GeneralTemplateClasses.Identifiable.identifiable import (
    Identifiable,
)
from armodel.models.M2.AUTOSARTemplates.GenericStructure.GeneralTemplateClasses.ArObject.ar_object import ARObject
from armodel.models.M2.AUTOSARTemplates.SystemTemplate.TransportProtocols import (
    FrArTpAckType,
)
from armodel.models.M2.AUTOSARTemplates.GenericStructure.GeneralTemplateClasses.PrimitiveTypes import (
    Integer,
    TimeValue,
)


class FlexrayTpConnectionControl(Identifiable):
    """AUTOSAR FlexrayTpConnectionControl."""

    @property
    def is_abstract(self) -> bool:
        """Check if this class is abstract.

        Returns:
            False for concrete classes
        """
        return False

    ack_type: Optional[FrArTpAckType]
    max_fc_wait: Optional[Integer]
    max_number_of: Optional[Integer]
    max_retries: Optional[Integer]
    separation_cycle: Optional[Integer]
    time_br: Optional[TimeValue]
    time_buffer: Optional[TimeValue]
    time_cs: Optional[TimeValue]
    timeout_ar: Optional[TimeValue]
    timeout_as: Optional[TimeValue]
    timeout_bs: Optional[TimeValue]
    timeout_cr: Optional[TimeValue]
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

    def serialize(self) -> ET.Element:
        """Serialize FlexrayTpConnectionControl to XML element.

        Returns:
            xml.etree.ElementTree.Element representing this object
        """
        # Get XML tag name for this class
        tag = self._get_xml_tag()
        elem = ET.Element(tag)

        # First, call parent's serialize to handle inherited attributes
        parent_elem = super(FlexrayTpConnectionControl, self).serialize()

        # Copy all attributes from parent element
        elem.attrib.update(parent_elem.attrib)

        # Copy all children from parent element
        for child in parent_elem:
            elem.append(child)

        # Serialize ack_type
        if self.ack_type is not None:
            serialized = ARObject._serialize_item(self.ack_type, "FrArTpAckType")
            if serialized is not None:
                # Wrap with correct tag
                wrapped = ET.Element("ACK-TYPE")
                if hasattr(serialized, 'attrib'):
                    wrapped.attrib.update(serialized.attrib)
                    if serialized.text:
                        wrapped.text = serialized.text
                for child in serialized:
                    wrapped.append(child)
                elem.append(wrapped)

        # Serialize max_fc_wait
        if self.max_fc_wait is not None:
            serialized = ARObject._serialize_item(self.max_fc_wait, "Integer")
            if serialized is not None:
                # Wrap with correct tag
                wrapped = ET.Element("MAX-FC-WAIT")
                if hasattr(serialized, 'attrib'):
                    wrapped.attrib.update(serialized.attrib)
                    if serialized.text:
                        wrapped.text = serialized.text
                for child in serialized:
                    wrapped.append(child)
                elem.append(wrapped)

        # Serialize max_number_of
        if self.max_number_of is not None:
            serialized = ARObject._serialize_item(self.max_number_of, "Integer")
            if serialized is not None:
                # Wrap with correct tag
                wrapped = ET.Element("MAX-NUMBER-OF")
                if hasattr(serialized, 'attrib'):
                    wrapped.attrib.update(serialized.attrib)
                    if serialized.text:
                        wrapped.text = serialized.text
                for child in serialized:
                    wrapped.append(child)
                elem.append(wrapped)

        # Serialize max_retries
        if self.max_retries is not None:
            serialized = ARObject._serialize_item(self.max_retries, "Integer")
            if serialized is not None:
                # Wrap with correct tag
                wrapped = ET.Element("MAX-RETRIES")
                if hasattr(serialized, 'attrib'):
                    wrapped.attrib.update(serialized.attrib)
                    if serialized.text:
                        wrapped.text = serialized.text
                for child in serialized:
                    wrapped.append(child)
                elem.append(wrapped)

        # Serialize separation_cycle
        if self.separation_cycle is not None:
            serialized = ARObject._serialize_item(self.separation_cycle, "Integer")
            if serialized is not None:
                # Wrap with correct tag
                wrapped = ET.Element("SEPARATION-CYCLE")
                if hasattr(serialized, 'attrib'):
                    wrapped.attrib.update(serialized.attrib)
                    if serialized.text:
                        wrapped.text = serialized.text
                for child in serialized:
                    wrapped.append(child)
                elem.append(wrapped)

        # Serialize time_br
        if self.time_br is not None:
            serialized = ARObject._serialize_item(self.time_br, "TimeValue")
            if serialized is not None:
                # Wrap with correct tag
                wrapped = ET.Element("TIME-BR")
                if hasattr(serialized, 'attrib'):
                    wrapped.attrib.update(serialized.attrib)
                    if serialized.text:
                        wrapped.text = serialized.text
                for child in serialized:
                    wrapped.append(child)
                elem.append(wrapped)

        # Serialize time_buffer
        if self.time_buffer is not None:
            serialized = ARObject._serialize_item(self.time_buffer, "TimeValue")
            if serialized is not None:
                # Wrap with correct tag
                wrapped = ET.Element("TIME-BUFFER")
                if hasattr(serialized, 'attrib'):
                    wrapped.attrib.update(serialized.attrib)
                    if serialized.text:
                        wrapped.text = serialized.text
                for child in serialized:
                    wrapped.append(child)
                elem.append(wrapped)

        # Serialize time_cs
        if self.time_cs is not None:
            serialized = ARObject._serialize_item(self.time_cs, "TimeValue")
            if serialized is not None:
                # Wrap with correct tag
                wrapped = ET.Element("TIME-CS")
                if hasattr(serialized, 'attrib'):
                    wrapped.attrib.update(serialized.attrib)
                    if serialized.text:
                        wrapped.text = serialized.text
                for child in serialized:
                    wrapped.append(child)
                elem.append(wrapped)

        # Serialize timeout_ar
        if self.timeout_ar is not None:
            serialized = ARObject._serialize_item(self.timeout_ar, "TimeValue")
            if serialized is not None:
                # Wrap with correct tag
                wrapped = ET.Element("TIMEOUT-AR")
                if hasattr(serialized, 'attrib'):
                    wrapped.attrib.update(serialized.attrib)
                    if serialized.text:
                        wrapped.text = serialized.text
                for child in serialized:
                    wrapped.append(child)
                elem.append(wrapped)

        # Serialize timeout_as
        if self.timeout_as is not None:
            serialized = ARObject._serialize_item(self.timeout_as, "TimeValue")
            if serialized is not None:
                # Wrap with correct tag
                wrapped = ET.Element("TIMEOUT-AS")
                if hasattr(serialized, 'attrib'):
                    wrapped.attrib.update(serialized.attrib)
                    if serialized.text:
                        wrapped.text = serialized.text
                for child in serialized:
                    wrapped.append(child)
                elem.append(wrapped)

        # Serialize timeout_bs
        if self.timeout_bs is not None:
            serialized = ARObject._serialize_item(self.timeout_bs, "TimeValue")
            if serialized is not None:
                # Wrap with correct tag
                wrapped = ET.Element("TIMEOUT-BS")
                if hasattr(serialized, 'attrib'):
                    wrapped.attrib.update(serialized.attrib)
                    if serialized.text:
                        wrapped.text = serialized.text
                for child in serialized:
                    wrapped.append(child)
                elem.append(wrapped)

        # Serialize timeout_cr
        if self.timeout_cr is not None:
            serialized = ARObject._serialize_item(self.timeout_cr, "TimeValue")
            if serialized is not None:
                # Wrap with correct tag
                wrapped = ET.Element("TIMEOUT-CR")
                if hasattr(serialized, 'attrib'):
                    wrapped.attrib.update(serialized.attrib)
                    if serialized.text:
                        wrapped.text = serialized.text
                for child in serialized:
                    wrapped.append(child)
                elem.append(wrapped)

        return elem

    @classmethod
    def deserialize(cls, element: ET.Element) -> "FlexrayTpConnectionControl":
        """Deserialize XML element to FlexrayTpConnectionControl object.

        Args:
            element: XML element to deserialize from

        Returns:
            Deserialized FlexrayTpConnectionControl object
        """
        # First, call parent's deserialize to handle inherited attributes
        obj = super(FlexrayTpConnectionControl, cls).deserialize(element)

        # Parse ack_type
        child = ARObject._find_child_element(element, "ACK-TYPE")
        if child is not None:
            ack_type_value = FrArTpAckType.deserialize(child)
            obj.ack_type = ack_type_value

        # Parse max_fc_wait
        child = ARObject._find_child_element(element, "MAX-FC-WAIT")
        if child is not None:
            max_fc_wait_value = child.text
            obj.max_fc_wait = max_fc_wait_value

        # Parse max_number_of
        child = ARObject._find_child_element(element, "MAX-NUMBER-OF")
        if child is not None:
            max_number_of_value = child.text
            obj.max_number_of = max_number_of_value

        # Parse max_retries
        child = ARObject._find_child_element(element, "MAX-RETRIES")
        if child is not None:
            max_retries_value = child.text
            obj.max_retries = max_retries_value

        # Parse separation_cycle
        child = ARObject._find_child_element(element, "SEPARATION-CYCLE")
        if child is not None:
            separation_cycle_value = child.text
            obj.separation_cycle = separation_cycle_value

        # Parse time_br
        child = ARObject._find_child_element(element, "TIME-BR")
        if child is not None:
            time_br_value = child.text
            obj.time_br = time_br_value

        # Parse time_buffer
        child = ARObject._find_child_element(element, "TIME-BUFFER")
        if child is not None:
            time_buffer_value = child.text
            obj.time_buffer = time_buffer_value

        # Parse time_cs
        child = ARObject._find_child_element(element, "TIME-CS")
        if child is not None:
            time_cs_value = child.text
            obj.time_cs = time_cs_value

        # Parse timeout_ar
        child = ARObject._find_child_element(element, "TIMEOUT-AR")
        if child is not None:
            timeout_ar_value = child.text
            obj.timeout_ar = timeout_ar_value

        # Parse timeout_as
        child = ARObject._find_child_element(element, "TIMEOUT-AS")
        if child is not None:
            timeout_as_value = child.text
            obj.timeout_as = timeout_as_value

        # Parse timeout_bs
        child = ARObject._find_child_element(element, "TIMEOUT-BS")
        if child is not None:
            timeout_bs_value = child.text
            obj.timeout_bs = timeout_bs_value

        # Parse timeout_cr
        child = ARObject._find_child_element(element, "TIMEOUT-CR")
        if child is not None:
            timeout_cr_value = child.text
            obj.timeout_cr = timeout_cr_value

        return obj



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
