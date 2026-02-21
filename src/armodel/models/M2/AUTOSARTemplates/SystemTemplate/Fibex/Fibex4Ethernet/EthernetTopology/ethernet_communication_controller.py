"""EthernetCommunicationController AUTOSAR element.

References:
  - AUTOSAR_CP_TPS_SystemTemplate.pdf (page 115)

JSON Source: docs/json/packages/M2_AUTOSARTemplates_SystemTemplate_Fibex_Fibex4Ethernet_EthernetTopology.classes.json"""

from __future__ import annotations
from typing import TYPE_CHECKING, Optional, Any
import xml.etree.ElementTree as ET
from armodel.serialization.decorators import atp_variant

from armodel.models.M2.AUTOSARTemplates.GenericStructure.GeneralTemplateClasses.ArObject.ar_object import ARObject
from armodel.serialization import SerializationHelper
from armodel.models.M2.AUTOSARTemplates.GenericStructure.GeneralTemplateClasses.ArObject.ar_ref import ARRef
from armodel.models.M2.AUTOSARTemplates.SystemTemplate.Fibex.Fibex4Ethernet.EthernetTopology import (
    EthernetMacLayerTypeEnum,
)
from armodel.models.M2.AUTOSARTemplates.GenericStructure.GeneralTemplateClasses.PrimitiveTypes import (
    Boolean,
    Integer,
    MacAddressString,
    TimeValue,
)
from armodel.models.M2.AUTOSARTemplates.SystemTemplate.Fibex.Fibex4Ethernet.EthernetTopology.coupling_port import (
    CouplingPort,
)


@atp_variant()

class EthernetCommunicationController(ARObject):
    """AUTOSAR EthernetCommunicationController."""

    @property
    def is_abstract(self) -> bool:
        """Check if this class is abstract.

        Returns:
            False for concrete classes
        """
        return False

    can_xl_config_ref: Optional[Any]
    coupling_ports: list[CouplingPort]
    mac_layer_type: Optional[EthernetMacLayerTypeEnum]
    mac_unicast: Optional[MacAddressString]
    maximum: Optional[Integer]
    slave_act_as: Optional[Boolean]
    slave_qualified: Optional[TimeValue]
    def __init__(self) -> None:
        """Initialize EthernetCommunicationController."""
        super().__init__()
        self.can_xl_config_ref: Optional[Any] = None
        self.coupling_ports: list[CouplingPort] = []
        self.mac_layer_type: Optional[EthernetMacLayerTypeEnum] = None
        self.mac_unicast: Optional[MacAddressString] = None
        self.maximum: Optional[Integer] = None
        self.slave_act_as: Optional[Boolean] = None
        self.slave_qualified: Optional[TimeValue] = None

    def serialize(self) -> ET.Element:
        """Serialize EthernetCommunicationController to XML element with atp_variant wrapper.

        Returns:
            xml.etree.ElementTree.Element representing this object
        """
        # Get XML tag name for this class
        tag = SerializationHelper.get_xml_tag(self.__class__)
        elem = ET.Element(tag)

        # Create inner element to hold attributes before wrapping
        inner_elem = ET.Element("INNER")

        # Serialize can_xl_config_ref
        if self.can_xl_config_ref is not None:
            serialized = SerializationHelper.serialize_item(self.can_xl_config_ref, "Any")
            if serialized is not None:
                wrapped = ET.Element("CAN-XL-CONFIG-REF")
                if hasattr(serialized, 'attrib'):
                    wrapped.attrib.update(serialized.attrib)
                    if serialized.text:
                        wrapped.text = serialized.text
                for child in serialized:
                    wrapped.append(child)
                inner_elem.append(wrapped)

        # Serialize coupling_ports (list from container "COUPLING-PORTS")
        if self.coupling_ports:
            container = ET.Element("COUPLING-PORTS")
            for item in self.coupling_ports:
                if is_ref:
                    # For reference lists, serialize as reference
                    if hasattr(item, "serialize"):
                        container.append(item.serialize())
                elif is_primitive_type("CouplingPort", package_data):
                    # Simple primitive type
                    child = ET.Element("COUPLING-PORT")
                    child.text = str(item)
                    container.append(child)
                elif is_enum_type("CouplingPort", package_data):
                    # Enum type - use serialize method
                    if hasattr(item, "serialize"):
                        container.append(item.serialize())
                else:
                    # Complex object type
                    if hasattr(item, "serialize"):
                        container.append(item.serialize())
            inner_elem.append(container)

        # Serialize mac_layer_type
        if self.mac_layer_type is not None:
            serialized = SerializationHelper.serialize_item(self.mac_layer_type, "EthernetMacLayerTypeEnum")
            if serialized is not None:
                wrapped = ET.Element("MAC-LAYER-TYPE")
                if hasattr(serialized, 'attrib'):
                    wrapped.attrib.update(serialized.attrib)
                    if serialized.text:
                        wrapped.text = serialized.text
                for child in serialized:
                    wrapped.append(child)
                inner_elem.append(wrapped)

        # Serialize mac_unicast
        if self.mac_unicast is not None:
            serialized = SerializationHelper.serialize_item(self.mac_unicast, "MacAddressString")
            if serialized is not None:
                wrapped = ET.Element("MAC-UNICAST")
                if hasattr(serialized, 'attrib'):
                    wrapped.attrib.update(serialized.attrib)
                    if serialized.text:
                        wrapped.text = serialized.text
                for child in serialized:
                    wrapped.append(child)
                inner_elem.append(wrapped)

        # Serialize maximum
        if self.maximum is not None:
            serialized = SerializationHelper.serialize_item(self.maximum, "Integer")
            if serialized is not None:
                wrapped = ET.Element("MAXIMUM")
                if hasattr(serialized, 'attrib'):
                    wrapped.attrib.update(serialized.attrib)
                    if serialized.text:
                        wrapped.text = serialized.text
                for child in serialized:
                    wrapped.append(child)
                inner_elem.append(wrapped)

        # Serialize slave_act_as
        if self.slave_act_as is not None:
            serialized = SerializationHelper.serialize_item(self.slave_act_as, "Boolean")
            if serialized is not None:
                wrapped = ET.Element("SLAVE-ACT-AS")
                if hasattr(serialized, 'attrib'):
                    wrapped.attrib.update(serialized.attrib)
                    if serialized.text:
                        wrapped.text = serialized.text
                for child in serialized:
                    wrapped.append(child)
                inner_elem.append(wrapped)

        # Serialize slave_qualified
        if self.slave_qualified is not None:
            serialized = SerializationHelper.serialize_item(self.slave_qualified, "TimeValue")
            if serialized is not None:
                wrapped = ET.Element("SLAVE-QUALIFIED")
                if hasattr(serialized, 'attrib'):
                    wrapped.attrib.update(serialized.attrib)
                    if serialized.text:
                        wrapped.text = serialized.text
                for child in serialized:
                    wrapped.append(child)
                inner_elem.append(wrapped)

        # Wrap inner element in atp_variant VARIANTS/CONDITIONAL structure
        wrapped = SerializationHelper.serialize_with_atp_variant(inner_elem, "EthernetCommunicationController")
        elem.append(wrapped)

        return elem

    @classmethod
    def deserialize(cls, element: ET.Element) -> "EthernetCommunicationController":
        """Deserialize XML element to EthernetCommunicationController object with atp_variant unwrapping.

        Args:
            element: XML element to deserialize from

        Returns:
            Deserialized EthernetCommunicationController object
        """
        # Create instance and initialize with default values
        obj = cls.__new__(cls)
        obj.__init__()

        # Handle ARObject inherited attributes (checksum and timestamp)
        # Parse timestamp (XML attribute 'T')
        timestamp_value = element.get("T")
        if timestamp_value is not None:
            obj.timestamp = timestamp_value

        # Parse checksum (child element)
        checksum_elem = SerializationHelper.find_child_element(element, "CHECKSUM")
        if checksum_elem is not None:
            checksum_value = checksum_elem.text
            if checksum_value is not None:
                obj.checksum = checksum_value

        # Unwrap atp_variant VARIANTS/CONDITIONAL structure
        inner_elem = SerializationHelper.deserialize_from_atp_variant(element, "EthernetCommunicationController")
        if inner_elem is None:
            # No wrapper structure found, return object with default values
            return obj

        # Parse can_xl_config_ref
        child = SerializationHelper.find_child_element(inner_elem, "CAN-XL-CONFIG-REF")
        if child is not None:
            can_xl_config_ref_value = ARRef.deserialize(child)
            obj.can_xl_config_ref = can_xl_config_ref_value

        # Parse coupling_ports (list from container "COUPLING-PORTS")
        obj.coupling_ports = []
        container = SerializationHelper.find_child_element(inner_elem, "COUPLING-PORTS")
        if container is not None:
            for child in container:
                if is_ref:
                    child_tag = SerializationHelper.strip_namespace(child.tag)
                    if child_tag.endswith("-REF") or child_tag.endswith("-TREF"):
                        child_value = ARRef.deserialize(child)
                    else:
                        child_value = SerializationHelper.deserialize_by_tag(child, None)
                elif is_primitive_type("CouplingPort", package_data):
                    child_value = child.text
                elif is_enum_type("CouplingPort", package_data):
                    child_value = CouplingPort.deserialize(child)
                else:
                    child_value = SerializationHelper.deserialize_by_tag(child, None)
                if child_value is not None:
                    obj.coupling_ports.append(child_value)

        # Parse mac_layer_type
        child = SerializationHelper.find_child_element(inner_elem, "MAC-LAYER-TYPE")
        if child is not None:
            mac_layer_type_value = EthernetMacLayerTypeEnum.deserialize(child)
            obj.mac_layer_type = mac_layer_type_value

        # Parse mac_unicast
        child = SerializationHelper.find_child_element(inner_elem, "MAC-UNICAST")
        if child is not None:
            mac_unicast_value = child.text
            obj.mac_unicast = mac_unicast_value

        # Parse maximum
        child = SerializationHelper.find_child_element(inner_elem, "MAXIMUM")
        if child is not None:
            maximum_value = child.text
            obj.maximum = maximum_value

        # Parse slave_act_as
        child = SerializationHelper.find_child_element(inner_elem, "SLAVE-ACT-AS")
        if child is not None:
            slave_act_as_value = child.text
            obj.slave_act_as = slave_act_as_value

        # Parse slave_qualified
        child = SerializationHelper.find_child_element(inner_elem, "SLAVE-QUALIFIED")
        if child is not None:
            slave_qualified_value = child.text
            obj.slave_qualified = slave_qualified_value

        return obj



class EthernetCommunicationControllerBuilder:
    """Builder for EthernetCommunicationController."""

    def __init__(self) -> None:
        """Initialize builder."""
        self._obj: EthernetCommunicationController = EthernetCommunicationController()

    def build(self) -> EthernetCommunicationController:
        """Build and return EthernetCommunicationController object.

        Returns:
            EthernetCommunicationController instance
        """
        # TODO: Add validation
        return self._obj
