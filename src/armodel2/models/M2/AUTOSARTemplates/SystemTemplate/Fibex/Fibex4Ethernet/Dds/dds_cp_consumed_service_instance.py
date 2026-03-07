"""DdsCpConsumedServiceInstance AUTOSAR element.

References:
  - AUTOSAR_CP_TPS_SystemTemplate.pdf (page 474)

JSON Source: docs/json/packages/M2_AUTOSARTemplates_SystemTemplate_Fibex_Fibex4Ethernet_Dds.classes.json"""

from __future__ import annotations
from typing import TYPE_CHECKING, Optional
import xml.etree.ElementTree as ET

from armodel2.models.M2.AUTOSARTemplates.SystemTemplate.Fibex.Fibex4Ethernet.Dds.dds_cp_service_instance import (
    DdsCpServiceInstance,
)
from armodel2.models.M2.builder_base import BuilderBase
from armodel2.models.M2.AUTOSARTemplates.SystemTemplate.Fibex.Fibex4Ethernet.Dds.dds_cp_service_instance import DdsCpServiceInstanceBuilder
from armodel2.models.M2.AUTOSARTemplates.GenericStructure.GeneralTemplateClasses.ArObject.ar_ref import ARRef
from armodel2.models.M2.AUTOSARTemplates.GenericStructure.GeneralTemplateClasses.PrimitiveTypes import (
    AnyVersionString,
)
from armodel2.models.M2.AUTOSARTemplates.SystemTemplate.Fibex.Fibex4Ethernet.EthernetTopology.application_endpoint import (
    ApplicationEndpoint,
)
from armodel2.models.M2.AUTOSARTemplates.GenericStructure.GeneralTemplateClasses.ArObject.ar_object import ARObject
from armodel2.serialization import SerializationHelper


class DdsCpConsumedServiceInstance(DdsCpServiceInstance):
    """AUTOSAR DdsCpConsumedServiceInstance."""

    @property
    def is_abstract(self) -> bool:
        """Check if this class is abstract.

        Returns:
            False for concrete classes
        """
        return False

    _XML_TAG = "DDS-CP-CONSUMED-SERVICE-INSTANCE"


    consumed_ddses: list[DdsCpServiceInstance]
    local_unicast_ref: Optional[ARRef]
    minor_version: Optional[AnyVersionString]
    static_remote_ref: Optional[ARRef]
    _DESERIALIZE_DISPATCH = {
        "CONSUMED-DDSS": ("_POLYMORPHIC_LIST", "consumed_ddses", ["DdsCpConsumedServiceInstance", "DdsCpProvidedServiceInstance"]),
        "LOCAL-UNICAST-REF": lambda obj, elem: setattr(obj, "local_unicast_ref", ARRef.deserialize(elem)),
        "MINOR-VERSION": lambda obj, elem: setattr(obj, "minor_version", SerializationHelper.deserialize_by_tag(elem, "AnyVersionString")),
        "STATIC-REMOTE-REF": lambda obj, elem: setattr(obj, "static_remote_ref", ARRef.deserialize(elem)),
    }


    def __init__(self) -> None:
        """Initialize DdsCpConsumedServiceInstance."""
        super().__init__()
        self.consumed_ddses: list[DdsCpServiceInstance] = []
        self.local_unicast_ref: Optional[ARRef] = None
        self.minor_version: Optional[AnyVersionString] = None
        self.static_remote_ref: Optional[ARRef] = None

    def serialize(self) -> ET.Element:
        """Serialize DdsCpConsumedServiceInstance to XML element.

        Returns:
            xml.etree.ElementTree.Element representing this object
        """
        # Use pre-computed _XML_TAG constant
        elem = ET.Element(self._XML_TAG)

        # First, call parent's serialize to handle inherited attributes
        parent_elem = super(DdsCpConsumedServiceInstance, self).serialize()

        # Copy all attributes from parent element
        elem.attrib.update(parent_elem.attrib)

        # Copy text from parent element
        if parent_elem.text:
            elem.text = parent_elem.text

        # Copy all children from parent element
        for child in parent_elem:
            elem.append(child)

        # Serialize consumed_ddses (list to container "CONSUMED-DDSS")
        if self.consumed_ddses:
            wrapper = ET.Element("CONSUMED-DDSS")
            for item in self.consumed_ddses:
                serialized = SerializationHelper.serialize_item(item, "DdsCpServiceInstance")
                if serialized is not None:
                    wrapper.append(serialized)
            if len(wrapper) > 0:
                elem.append(wrapper)

        # Serialize local_unicast_ref
        if self.local_unicast_ref is not None:
            serialized = SerializationHelper.serialize_item(self.local_unicast_ref, "ApplicationEndpoint")
            if serialized is not None:
                # Wrap with correct tag
                wrapped = ET.Element("LOCAL-UNICAST-REF")
                if hasattr(serialized, 'attrib'):
                    wrapped.attrib.update(serialized.attrib)
                if serialized.text:
                    wrapped.text = serialized.text
                for child in serialized:
                    wrapped.append(child)
                elem.append(wrapped)

        # Serialize minor_version
        if self.minor_version is not None:
            serialized = SerializationHelper.serialize_item(self.minor_version, "AnyVersionString")
            if serialized is not None:
                # Wrap with correct tag
                wrapped = ET.Element("MINOR-VERSION")
                if hasattr(serialized, 'attrib'):
                    wrapped.attrib.update(serialized.attrib)
                if serialized.text:
                    wrapped.text = serialized.text
                for child in serialized:
                    wrapped.append(child)
                elem.append(wrapped)

        # Serialize static_remote_ref
        if self.static_remote_ref is not None:
            serialized = SerializationHelper.serialize_item(self.static_remote_ref, "ApplicationEndpoint")
            if serialized is not None:
                # Wrap with correct tag
                wrapped = ET.Element("STATIC-REMOTE-REF")
                if hasattr(serialized, 'attrib'):
                    wrapped.attrib.update(serialized.attrib)
                if serialized.text:
                    wrapped.text = serialized.text
                for child in serialized:
                    wrapped.append(child)
                elem.append(wrapped)

        return elem

    @classmethod
    def deserialize(cls, element: ET.Element) -> "DdsCpConsumedServiceInstance":
        """Deserialize XML element to DdsCpConsumedServiceInstance object.

        Args:
            element: XML element to deserialize from

        Returns:
            Deserialized DdsCpConsumedServiceInstance object
        """
        # First, call parent's deserialize to handle inherited attributes
        obj = super(DdsCpConsumedServiceInstance, cls).deserialize(element)

        # Single-pass deserialization with if-elif-else chain
        ns_split = '}'
        for child in element:
            tag = child.tag.split(ns_split, 1)[1] if child.tag.startswith('{') else child.tag
            if tag == "CONSUMED-DDSS":
                # Iterate through all child elements and deserialize each based on its concrete type
                for item_elem in child:
                    concrete_tag = item_elem.tag.split(ns_split, 1)[1] if item_elem.tag.startswith("{") else item_elem.tag
                    if concrete_tag == "DDS-CP-CONSUMED-SERVICE-INSTANCE":
                        obj.consumed_ddses.append(SerializationHelper.deserialize_by_tag(item_elem, "DdsCpConsumedServiceInstance"))
                    elif concrete_tag == "DDS-CP-PROVIDED-SERVICE-INSTANCE":
                        obj.consumed_ddses.append(SerializationHelper.deserialize_by_tag(item_elem, "DdsCpProvidedServiceInstance"))
            elif tag == "LOCAL-UNICAST-REF":
                setattr(obj, "local_unicast_ref", ARRef.deserialize(child))
            elif tag == "MINOR-VERSION":
                setattr(obj, "minor_version", SerializationHelper.deserialize_by_tag(child, "AnyVersionString"))
            elif tag == "STATIC-REMOTE-REF":
                setattr(obj, "static_remote_ref", ARRef.deserialize(child))

        return obj



class DdsCpConsumedServiceInstanceBuilder(DdsCpServiceInstanceBuilder):
    """Builder for DdsCpConsumedServiceInstance with fluent API."""

    def __init__(self) -> None:
        """Initialize builder with defaults."""
        super().__init__()
        self._obj: DdsCpConsumedServiceInstance = DdsCpConsumedServiceInstance()


    def with_consumed_ddses(self, items: list[DdsCpServiceInstance]) -> "DdsCpConsumedServiceInstanceBuilder":
        """Set consumed_ddses list attribute.

        Args:
            items: List of items to set

        Returns:
            self for method chaining
        """
        self._obj.consumed_ddses = list(items) if items else []
        return self

    def with_local_unicast(self, value: Optional[ApplicationEndpoint]) -> "DdsCpConsumedServiceInstanceBuilder":
        """Set local_unicast attribute.

        Args:
            value: Value to set

        Returns:
            self for method chaining
        """
        if value is None and not True:
            raise ValueError("Attribute 'local_unicast' is required and cannot be None")
        self._obj.local_unicast = value
        return self

    def with_minor_version(self, value: Optional[AnyVersionString]) -> "DdsCpConsumedServiceInstanceBuilder":
        """Set minor_version attribute.

        Args:
            value: Value to set

        Returns:
            self for method chaining
        """
        if value is None and not True:
            raise ValueError("Attribute 'minor_version' is required and cannot be None")
        self._obj.minor_version = value
        return self

    def with_static_remote(self, value: Optional[ApplicationEndpoint]) -> "DdsCpConsumedServiceInstanceBuilder":
        """Set static_remote attribute.

        Args:
            value: Value to set

        Returns:
            self for method chaining
        """
        if value is None and not True:
            raise ValueError("Attribute 'static_remote' is required and cannot be None")
        self._obj.static_remote = value
        return self


    def add_consumed_dds(self, item: DdsCpServiceInstance) -> "DdsCpConsumedServiceInstanceBuilder":
        """Add a single item to consumed_ddses list.

        Args:
            item: Item to add

        Returns:
            self for method chaining
        """
        self._obj.consumed_ddses.append(item)
        return self

    def clear_consumed_ddses(self) -> "DdsCpConsumedServiceInstanceBuilder":
        """Clear all items from consumed_ddses list.

        Returns:
            self for method chaining
        """
        self._obj.consumed_ddses = []
        return self


    # Pre-computed validation constants (generated from JSON schema)
    _OPTIONAL_ATTRIBUTES = {
        "consumedDds",
        "localUnicast",
        "minorVersion",
        "staticRemote",
    }


    def _validate_instance(self) -> None:
        """Validate the built instance based on settings."""
        from armodel2.core import GlobalSettingsManager, BuilderValidationMode

        settings = GlobalSettingsManager()
        mode = settings.builder_validation

        if mode == BuilderValidationMode.DISABLED:
            return

        # No required attributes to validate (all are optional)


    def build(self) -> DdsCpConsumedServiceInstance:
        """Build and return the DdsCpConsumedServiceInstance instance with validation."""
        self._validate_instance()
        return self._obj