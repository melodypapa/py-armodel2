"""InfrastructureServices AUTOSAR element.

References:
  - AUTOSAR_CP_TPS_SystemTemplate.pdf (page 469)

JSON Source: docs/json/packages/M2_AUTOSARTemplates_SystemTemplate_Fibex_Fibex4Ethernet_EthernetTopology.classes.json"""

from __future__ import annotations
from typing import TYPE_CHECKING, Optional
import xml.etree.ElementTree as ET

from armodel2.models.M2.builder_base import BuilderBase
from armodel2.models.M2.AUTOSARTemplates.SystemTemplate.Fibex.Fibex4Ethernet.EthernetTopology.do_ip_entity import (
    DoIpEntity,
)
from armodel2.models.M2.AUTOSARTemplates.SystemTemplate.Fibex.Fibex4Ethernet.EthernetTopology.time_synchronization import (
    TimeSynchronization,
)
from armodel2.models.M2.AUTOSARTemplates.GenericStructure.GeneralTemplateClasses.ArObject.ar_object import ARObject
from armodel2.serialization import SerializationHelper


class InfrastructureServices(ARObject):
    """AUTOSAR InfrastructureServices."""

    @property
    def is_abstract(self) -> bool:
        """Check if this class is abstract.

        Returns:
            False for concrete classes
        """
        return False

    _XML_TAG = "INFRASTRUCTURE-SERVICES"


    do_ip_entity: Optional[DoIpEntity]
    time: Optional[TimeSynchronization]
    _DESERIALIZE_DISPATCH = {
        "DO-IP-ENTITY": lambda obj, elem: setattr(obj, "do_ip_entity", SerializationHelper.deserialize_by_tag(elem, "DoIpEntity")),
        "TIME": lambda obj, elem: setattr(obj, "time", SerializationHelper.deserialize_by_tag(elem, "TimeSynchronization")),
    }


    def __init__(self) -> None:
        """Initialize InfrastructureServices."""
        super().__init__()
        self.do_ip_entity: Optional[DoIpEntity] = None
        self.time: Optional[TimeSynchronization] = None

    def serialize(self) -> ET.Element:
        """Serialize InfrastructureServices to XML element.

        Returns:
            xml.etree.ElementTree.Element representing this object
        """
        # Use pre-computed _XML_TAG constant
        elem = ET.Element(self._XML_TAG)

        # First, call parent's serialize to handle inherited attributes
        parent_elem = super(InfrastructureServices, self).serialize()

        # Copy all attributes from parent element
        elem.attrib.update(parent_elem.attrib)

        # Copy text from parent element
        if parent_elem.text:
            elem.text = parent_elem.text

        # Copy all children from parent element
        for child in parent_elem:
            elem.append(child)

        # Serialize do_ip_entity
        if self.do_ip_entity is not None:
            serialized = SerializationHelper.serialize_item(self.do_ip_entity, "DoIpEntity")
            if serialized is not None:
                # Wrap with correct tag
                wrapped = ET.Element("DO-IP-ENTITY")
                if hasattr(serialized, 'attrib'):
                    wrapped.attrib.update(serialized.attrib)
                if serialized.text:
                    wrapped.text = serialized.text
                for child in serialized:
                    wrapped.append(child)
                elem.append(wrapped)

        # Serialize time
        if self.time is not None:
            serialized = SerializationHelper.serialize_item(self.time, "TimeSynchronization")
            if serialized is not None:
                # Wrap with correct tag
                wrapped = ET.Element("TIME")
                if hasattr(serialized, 'attrib'):
                    wrapped.attrib.update(serialized.attrib)
                if serialized.text:
                    wrapped.text = serialized.text
                for child in serialized:
                    wrapped.append(child)
                elem.append(wrapped)

        return elem

    @classmethod
    def deserialize(cls, element: ET.Element) -> "InfrastructureServices":
        """Deserialize XML element to InfrastructureServices object.

        Args:
            element: XML element to deserialize from

        Returns:
            Deserialized InfrastructureServices object
        """
        # First, call parent's deserialize to handle inherited attributes
        obj = super(InfrastructureServices, cls).deserialize(element)

        # Single-pass deserialization with if-elif-else chain
        ns_split = '}'
        for child in element:
            tag = child.tag.split(ns_split, 1)[1] if child.tag.startswith('{') else child.tag
            if tag == "DO-IP-ENTITY":
                setattr(obj, "do_ip_entity", SerializationHelper.deserialize_by_tag(child, "DoIpEntity"))
            elif tag == "TIME":
                setattr(obj, "time", SerializationHelper.deserialize_by_tag(child, "TimeSynchronization"))

        return obj



class InfrastructureServicesBuilder(BuilderBase):
    """Builder for InfrastructureServices with fluent API."""

    def __init__(self) -> None:
        """Initialize builder with defaults."""
        super().__init__()
        self._obj: InfrastructureServices = InfrastructureServices()


    def with_do_ip_entity(self, value: Optional[DoIpEntity]) -> "InfrastructureServicesBuilder":
        """Set do_ip_entity attribute.

        Args:
            value: Value to set

        Returns:
            self for method chaining
        """
        if value is None and not True:
            raise ValueError("Attribute 'do_ip_entity' is required and cannot be None")
        self._obj.do_ip_entity = value
        return self

    def with_time(self, value: Optional[TimeSynchronization]) -> "InfrastructureServicesBuilder":
        """Set time attribute.

        Args:
            value: Value to set

        Returns:
            self for method chaining
        """
        if value is None and not True:
            raise ValueError("Attribute 'time' is required and cannot be None")
        self._obj.time = value
        return self



    # Pre-computed validation constants (generated from JSON schema)
    _OPTIONAL_ATTRIBUTES = {
        "doIpEntity",
        "time",
    }


    def _validate_instance(self) -> None:
        """Validate the built instance based on settings."""
        from armodel2.core import GlobalSettingsManager, BuilderValidationMode

        settings = GlobalSettingsManager()
        mode = settings.builder_validation

        if mode == BuilderValidationMode.DISABLED:
            return

        # No required attributes to validate (all are optional)


    def build(self) -> InfrastructureServices:
        """Build and return the InfrastructureServices instance with validation."""
        self._validate_instance()
        return self._obj