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
from armodel.serialization import SerializationHelper
from armodel.models.M2.AUTOSARTemplates.GenericStructure.GeneralTemplateClasses.ArObject.ar_ref import ARRef
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

    dds_field_reply_ref: Optional[ARRef]
    dds_field_ref: Optional[ARRef]
    dds_method_ref: Optional[ARRef]
    dds_service_qos_ref: Optional[ARRef]
    service_instance: Optional[PositiveInteger]
    service_interface: Optional[String]
    def __init__(self) -> None:
        """Initialize DdsCpServiceInstance."""
        super().__init__()
        self.dds_field_reply_ref: Optional[ARRef] = None
        self.dds_field_ref: Optional[ARRef] = None
        self.dds_method_ref: Optional[ARRef] = None
        self.dds_service_qos_ref: Optional[ARRef] = None
        self.service_instance: Optional[PositiveInteger] = None
        self.service_interface: Optional[String] = None

    def serialize(self) -> ET.Element:
        """Serialize DdsCpServiceInstance to XML element.

        Returns:
            xml.etree.ElementTree.Element representing this object
        """
        # Get XML tag name for this class
        tag = SerializationHelper.get_xml_tag(self.__class__)
        elem = ET.Element(tag)

        # First, call parent's serialize to handle inherited attributes
        parent_elem = super(DdsCpServiceInstance, self).serialize()

        # Copy all attributes from parent element
        elem.attrib.update(parent_elem.attrib)

        # Copy text from parent element
        if parent_elem.text:
            elem.text = parent_elem.text

        # Copy all children from parent element
        for child in parent_elem:
            elem.append(child)

        # Serialize dds_field_reply_ref
        if self.dds_field_reply_ref is not None:
            serialized = SerializationHelper.serialize_item(self.dds_field_reply_ref, "DdsCpTopic")
            if serialized is not None:
                # Wrap with correct tag
                wrapped = ET.Element("DDS-FIELD-REPLY-REF")
                if hasattr(serialized, 'attrib'):
                    wrapped.attrib.update(serialized.attrib)
                    if serialized.text:
                        wrapped.text = serialized.text
                for child in serialized:
                    wrapped.append(child)
                elem.append(wrapped)

        # Serialize dds_field_ref
        if self.dds_field_ref is not None:
            serialized = SerializationHelper.serialize_item(self.dds_field_ref, "DdsCpTopic")
            if serialized is not None:
                # Wrap with correct tag
                wrapped = ET.Element("DDS-FIELD-REF")
                if hasattr(serialized, 'attrib'):
                    wrapped.attrib.update(serialized.attrib)
                    if serialized.text:
                        wrapped.text = serialized.text
                for child in serialized:
                    wrapped.append(child)
                elem.append(wrapped)

        # Serialize dds_method_ref
        if self.dds_method_ref is not None:
            serialized = SerializationHelper.serialize_item(self.dds_method_ref, "DdsCpTopic")
            if serialized is not None:
                # Wrap with correct tag
                wrapped = ET.Element("DDS-METHOD-REF")
                if hasattr(serialized, 'attrib'):
                    wrapped.attrib.update(serialized.attrib)
                    if serialized.text:
                        wrapped.text = serialized.text
                for child in serialized:
                    wrapped.append(child)
                elem.append(wrapped)

        # Serialize dds_service_qos_ref
        if self.dds_service_qos_ref is not None:
            serialized = SerializationHelper.serialize_item(self.dds_service_qos_ref, "DdsCpQosProfile")
            if serialized is not None:
                # Wrap with correct tag
                wrapped = ET.Element("DDS-SERVICE-QOS-REF")
                if hasattr(serialized, 'attrib'):
                    wrapped.attrib.update(serialized.attrib)
                    if serialized.text:
                        wrapped.text = serialized.text
                for child in serialized:
                    wrapped.append(child)
                elem.append(wrapped)

        # Serialize service_instance
        if self.service_instance is not None:
            serialized = SerializationHelper.serialize_item(self.service_instance, "PositiveInteger")
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
            serialized = SerializationHelper.serialize_item(self.service_interface, "String")
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

        # Parse dds_field_reply_ref
        child = SerializationHelper.find_child_element(element, "DDS-FIELD-REPLY-REF")
        if child is not None:
            dds_field_reply_ref_value = ARRef.deserialize(child)
            obj.dds_field_reply_ref = dds_field_reply_ref_value

        # Parse dds_field_ref
        child = SerializationHelper.find_child_element(element, "DDS-FIELD-REF")
        if child is not None:
            dds_field_ref_value = ARRef.deserialize(child)
            obj.dds_field_ref = dds_field_ref_value

        # Parse dds_method_ref
        child = SerializationHelper.find_child_element(element, "DDS-METHOD-REF")
        if child is not None:
            dds_method_ref_value = ARRef.deserialize(child)
            obj.dds_method_ref = dds_method_ref_value

        # Parse dds_service_qos_ref
        child = SerializationHelper.find_child_element(element, "DDS-SERVICE-QOS-REF")
        if child is not None:
            dds_service_qos_ref_value = ARRef.deserialize(child)
            obj.dds_service_qos_ref = dds_service_qos_ref_value

        # Parse service_instance
        child = SerializationHelper.find_child_element(element, "SERVICE-INSTANCE")
        if child is not None:
            service_instance_value = child.text
            obj.service_instance = service_instance_value

        # Parse service_interface
        child = SerializationHelper.find_child_element(element, "SERVICE-INTERFACE")
        if child is not None:
            service_interface_value = child.text
            obj.service_interface = service_interface_value

        return obj



