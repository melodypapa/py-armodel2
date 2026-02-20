"""DdsCpServiceInstance AUTOSAR element.

References:
  - AUTOSAR_CP_TPS_SystemTemplate.pdf (page 472)

JSON Source: docs/json/packages/M2_AUTOSARTemplates_SystemTemplate_Fibex_Fibex4Ethernet_Dds.classes.json"""

from __future__ import annotations
from typing import TYPE_CHECKING, Optional
import xml.etree.ElementTree as ET

from armodel.models.M2.AUTOSARTemplates.SystemTemplate.Fibex.Fibex4Ethernet.ServiceInstances.abstract_service_instance import (
    AbstractServiceInstance,
)
from armodel.models.M2.AUTOSARTemplates.GenericStructure.GeneralTemplateClasses.ArObject.ar_object import ARObject
from armodel.models.M2.AUTOSARTemplates.GenericStructure.GeneralTemplateClasses.PrimitiveTypes import (
    PositiveInteger,
    String,
)
from armodel.models.M2.AUTOSARTemplates.SystemTemplate.Fibex.Fibex4Ethernet.Dds.dds_cp_qos_profile import (
    DdsCpQosProfile,
)
from armodel.models.M2.AUTOSARTemplates.SystemTemplate.Fibex.Fibex4Ethernet.Dds.dds_cp_topic import (
    DdsCpTopic,
)
from abc import ABC, abstractmethod


class DdsCpServiceInstance(AbstractServiceInstance, ABC):
    """AUTOSAR DdsCpServiceInstance."""

    @property
    def is_abstract(self) -> bool:
        """Check if this class is abstract.

        Returns:
            True for abstract classes
        """
        return True

    dds_field_reply: Optional[DdsCpTopic]
    dds_field: Optional[DdsCpTopic]
    dds_method: Optional[DdsCpTopic]
    dds_service_qos: Optional[DdsCpQosProfile]
    service_instance: Optional[PositiveInteger]
    service_interface: Optional[String]
    def __init__(self) -> None:
        """Initialize DdsCpServiceInstance."""
        super().__init__()
        self.dds_field_reply: Optional[DdsCpTopic] = None
        self.dds_field: Optional[DdsCpTopic] = None
        self.dds_method: Optional[DdsCpTopic] = None
        self.dds_service_qos: Optional[DdsCpQosProfile] = None
        self.service_instance: Optional[PositiveInteger] = None
        self.service_interface: Optional[String] = None

    def serialize(self) -> ET.Element:
        """Serialize DdsCpServiceInstance to XML element.

        Returns:
            xml.etree.ElementTree.Element representing this object
        """
        # Get XML tag name for this class
        tag = self._get_xml_tag()
        elem = ET.Element(tag)

        # First, call parent's serialize to handle inherited attributes
        parent_elem = super(DdsCpServiceInstance, self).serialize()

        # Copy all attributes from parent element
        elem.attrib.update(parent_elem.attrib)

        # Copy all children from parent element
        for child in parent_elem:
            elem.append(child)

        # Serialize dds_field_reply
        if self.dds_field_reply is not None:
            serialized = ARObject._serialize_item(self.dds_field_reply, "DdsCpTopic")
            if serialized is not None:
                # Wrap with correct tag
                wrapped = ET.Element("DDS-FIELD-REPLY")
                if hasattr(serialized, 'attrib'):
                    wrapped.attrib.update(serialized.attrib)
                    if serialized.text:
                        wrapped.text = serialized.text
                for child in serialized:
                    wrapped.append(child)
                elem.append(wrapped)

        # Serialize dds_field
        if self.dds_field is not None:
            serialized = ARObject._serialize_item(self.dds_field, "DdsCpTopic")
            if serialized is not None:
                # Wrap with correct tag
                wrapped = ET.Element("DDS-FIELD")
                if hasattr(serialized, 'attrib'):
                    wrapped.attrib.update(serialized.attrib)
                    if serialized.text:
                        wrapped.text = serialized.text
                for child in serialized:
                    wrapped.append(child)
                elem.append(wrapped)

        # Serialize dds_method
        if self.dds_method is not None:
            serialized = ARObject._serialize_item(self.dds_method, "DdsCpTopic")
            if serialized is not None:
                # Wrap with correct tag
                wrapped = ET.Element("DDS-METHOD")
                if hasattr(serialized, 'attrib'):
                    wrapped.attrib.update(serialized.attrib)
                    if serialized.text:
                        wrapped.text = serialized.text
                for child in serialized:
                    wrapped.append(child)
                elem.append(wrapped)

        # Serialize dds_service_qos
        if self.dds_service_qos is not None:
            serialized = ARObject._serialize_item(self.dds_service_qos, "DdsCpQosProfile")
            if serialized is not None:
                # Wrap with correct tag
                wrapped = ET.Element("DDS-SERVICE-QOS")
                if hasattr(serialized, 'attrib'):
                    wrapped.attrib.update(serialized.attrib)
                    if serialized.text:
                        wrapped.text = serialized.text
                for child in serialized:
                    wrapped.append(child)
                elem.append(wrapped)

        # Serialize service_instance
        if self.service_instance is not None:
            serialized = ARObject._serialize_item(self.service_instance, "PositiveInteger")
            if serialized is not None:
                # Wrap with correct tag
                wrapped = ET.Element("SERVICE-INSTANCE")
                if hasattr(serialized, 'attrib'):
                    wrapped.attrib.update(serialized.attrib)
                    if serialized.text:
                        wrapped.text = serialized.text
                for child in serialized:
                    wrapped.append(child)
                elem.append(wrapped)

        # Serialize service_interface
        if self.service_interface is not None:
            serialized = ARObject._serialize_item(self.service_interface, "String")
            if serialized is not None:
                # Wrap with correct tag
                wrapped = ET.Element("SERVICE-INTERFACE")
                if hasattr(serialized, 'attrib'):
                    wrapped.attrib.update(serialized.attrib)
                    if serialized.text:
                        wrapped.text = serialized.text
                for child in serialized:
                    wrapped.append(child)
                elem.append(wrapped)

        return elem

    @classmethod
    def deserialize(cls, element: ET.Element) -> "DdsCpServiceInstance":
        """Deserialize XML element to DdsCpServiceInstance object.

        Args:
            element: XML element to deserialize from

        Returns:
            Deserialized DdsCpServiceInstance object
        """
        # First, call parent's deserialize to handle inherited attributes
        obj = super(DdsCpServiceInstance, cls).deserialize(element)

        # Parse dds_field_reply
        child = ARObject._find_child_element(element, "DDS-FIELD-REPLY")
        if child is not None:
            dds_field_reply_value = ARObject._deserialize_by_tag(child, "DdsCpTopic")
            obj.dds_field_reply = dds_field_reply_value

        # Parse dds_field
        child = ARObject._find_child_element(element, "DDS-FIELD")
        if child is not None:
            dds_field_value = ARObject._deserialize_by_tag(child, "DdsCpTopic")
            obj.dds_field = dds_field_value

        # Parse dds_method
        child = ARObject._find_child_element(element, "DDS-METHOD")
        if child is not None:
            dds_method_value = ARObject._deserialize_by_tag(child, "DdsCpTopic")
            obj.dds_method = dds_method_value

        # Parse dds_service_qos
        child = ARObject._find_child_element(element, "DDS-SERVICE-QOS")
        if child is not None:
            dds_service_qos_value = ARObject._deserialize_by_tag(child, "DdsCpQosProfile")
            obj.dds_service_qos = dds_service_qos_value

        # Parse service_instance
        child = ARObject._find_child_element(element, "SERVICE-INSTANCE")
        if child is not None:
            service_instance_value = child.text
            obj.service_instance = service_instance_value

        # Parse service_interface
        child = ARObject._find_child_element(element, "SERVICE-INTERFACE")
        if child is not None:
            service_interface_value = child.text
            obj.service_interface = service_interface_value

        return obj



class DdsCpServiceInstanceBuilder:
    """Builder for DdsCpServiceInstance."""

    def __init__(self) -> None:
        """Initialize builder."""
        self._obj: DdsCpServiceInstance = DdsCpServiceInstance()

    def build(self) -> DdsCpServiceInstance:
        """Build and return DdsCpServiceInstance object.

        Returns:
            DdsCpServiceInstance instance
        """
        # TODO: Add validation
        return self._obj
