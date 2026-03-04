"""DdsCpServiceInstance AUTOSAR element.

References:
  - AUTOSAR_CP_TPS_SystemTemplate.pdf (page 472)

JSON Source: docs/json/packages/M2_AUTOSARTemplates_SystemTemplate_Fibex_Fibex4Ethernet_Dds.classes.json"""

from __future__ import annotations
from typing import TYPE_CHECKING, Optional
import xml.etree.ElementTree as ET

from armodel2.models.M2.AUTOSARTemplates.SystemTemplate.Fibex.Fibex4Ethernet.ServiceInstances.abstract_service_instance import (
    AbstractServiceInstance,
)
from armodel2.models.M2.builder_base import BuilderBase
from armodel2.models.M2.AUTOSARTemplates.SystemTemplate.Fibex.Fibex4Ethernet.ServiceInstances.abstract_service_instance import AbstractServiceInstanceBuilder
from armodel2.models.M2.AUTOSARTemplates.GenericStructure.GeneralTemplateClasses.ArObject.ar_ref import ARRef
from armodel2.models.M2.AUTOSARTemplates.GenericStructure.GeneralTemplateClasses.PrimitiveTypes import (
    PositiveInteger,
    String,
)
from armodel2.models.M2.AUTOSARTemplates.SystemTemplate.Fibex.Fibex4Ethernet.Dds.dds_cp_qos_profile import (
    DdsCpQosProfile,
)
from armodel2.models.M2.AUTOSARTemplates.SystemTemplate.Fibex.Fibex4Ethernet.Dds.dds_cp_topic import (
    DdsCpTopic,
)
from abc import ABC, abstractmethod
from armodel2.models.M2.AUTOSARTemplates.GenericStructure.GeneralTemplateClasses.ArObject.ar_object import ARObject
from armodel2.serialization import SerializationHelper


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
    _DESERIALIZE_DISPATCH = {
        "DDS-FIELD-REPLY-REF": lambda obj, elem: setattr(obj, "dds_field_reply_ref", ARRef.deserialize(elem)),
        "DDS-FIELD-REF": lambda obj, elem: setattr(obj, "dds_field_ref", ARRef.deserialize(elem)),
        "DDS-METHOD-REF": lambda obj, elem: setattr(obj, "dds_method_ref", ARRef.deserialize(elem)),
        "DDS-SERVICE-QOS-REF": lambda obj, elem: setattr(obj, "dds_service_qos_ref", ARRef.deserialize(elem)),
        "SERVICE-INSTANCE": lambda obj, elem: setattr(obj, "service_instance", SerializationHelper.deserialize_by_tag(elem, "PositiveInteger")),
        "SERVICE-INTERFACE": lambda obj, elem: setattr(obj, "service_interface", SerializationHelper.deserialize_by_tag(elem, "String")),
    }


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
        # Use pre-computed _XML_TAG constant
        elem = ET.Element(self._XML_TAG)

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

        # Single-pass deserialization with if-elif-else chain
        ns_split = '}'
        for child in element:
            tag = child.tag.split(ns_split, 1)[1] if child.tag.startswith('{') else child.tag
            if tag == "DDS-FIELD-REPLY-REF":
                setattr(obj, "dds_field_reply_ref", ARRef.deserialize(child))
            elif tag == "DDS-FIELD-REF":
                setattr(obj, "dds_field_ref", ARRef.deserialize(child))
            elif tag == "DDS-METHOD-REF":
                setattr(obj, "dds_method_ref", ARRef.deserialize(child))
            elif tag == "DDS-SERVICE-QOS-REF":
                setattr(obj, "dds_service_qos_ref", ARRef.deserialize(child))
            elif tag == "SERVICE-INSTANCE":
                setattr(obj, "service_instance", SerializationHelper.deserialize_by_tag(child, "PositiveInteger"))
            elif tag == "SERVICE-INTERFACE":
                setattr(obj, "service_interface", SerializationHelper.deserialize_by_tag(child, "String"))

        return obj



class DdsCpServiceInstanceBuilder(AbstractServiceInstanceBuilder):
    """Builder for DdsCpServiceInstance with fluent API."""

    def __init__(self) -> None:
        """Initialize builder with defaults."""
        super().__init__()
        self._obj: DdsCpServiceInstance = DdsCpServiceInstance()


    def with_dds_field_reply(self, value: Optional[DdsCpTopic]) -> "DdsCpServiceInstanceBuilder":
        """Set dds_field_reply attribute.

        Args:
            value: Value to set

        Returns:
            self for method chaining
        """
        if value is None and not True:
            raise ValueError("Attribute '" + snake_attr_name + "' is required and cannot be None")
        self._obj.dds_field_reply = value
        return self

    def with_dds_field(self, value: Optional[DdsCpTopic]) -> "DdsCpServiceInstanceBuilder":
        """Set dds_field attribute.

        Args:
            value: Value to set

        Returns:
            self for method chaining
        """
        if value is None and not True:
            raise ValueError("Attribute '" + snake_attr_name + "' is required and cannot be None")
        self._obj.dds_field = value
        return self

    def with_dds_method(self, value: Optional[DdsCpTopic]) -> "DdsCpServiceInstanceBuilder":
        """Set dds_method attribute.

        Args:
            value: Value to set

        Returns:
            self for method chaining
        """
        if value is None and not True:
            raise ValueError("Attribute '" + snake_attr_name + "' is required and cannot be None")
        self._obj.dds_method = value
        return self

    def with_dds_service_qos(self, value: Optional[DdsCpQosProfile]) -> "DdsCpServiceInstanceBuilder":
        """Set dds_service_qos attribute.

        Args:
            value: Value to set

        Returns:
            self for method chaining
        """
        if value is None and not True:
            raise ValueError("Attribute '" + snake_attr_name + "' is required and cannot be None")
        self._obj.dds_service_qos = value
        return self

    def with_service_instance(self, value: Optional[PositiveInteger]) -> "DdsCpServiceInstanceBuilder":
        """Set service_instance attribute.

        Args:
            value: Value to set

        Returns:
            self for method chaining
        """
        if value is None and not True:
            raise ValueError("Attribute '" + snake_attr_name + "' is required and cannot be None")
        self._obj.service_instance = value
        return self

    def with_service_interface(self, value: Optional[String]) -> "DdsCpServiceInstanceBuilder":
        """Set service_interface attribute.

        Args:
            value: Value to set

        Returns:
            self for method chaining
        """
        if value is None and not True:
            raise ValueError("Attribute '" + snake_attr_name + "' is required and cannot be None")
        self._obj.service_interface = value
        return self



    # Pre-computed validation constants (generated from JSON schema)
    _OPTIONAL_ATTRIBUTES = {
        "ddsField",
        "ddsFieldReply",
        "ddsMethod",
        "ddsServiceQos",
        "serviceInstance",
        "serviceInterface",
    }


    def _validate_instance(self) -> None:
        """Validate the built instance based on settings."""
        from armodel2.core import GlobalSettingsManager, BuilderValidationMode

        settings = GlobalSettingsManager()
        mode = settings.builder_validation

        if mode == BuilderValidationMode.DISABLED:
            return

        # No required attributes to validate (all are optional)


    @abstractmethod
    def build(self) -> DdsCpServiceInstance:
        """Build and return the DdsCpServiceInstance instance (abstract)."""
        raise NotImplementedError